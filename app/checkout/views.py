import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http import JsonResponse

@api_view(['POST'])
def create_payment(request):
    access_token = 'TEST-335553357611407-080122-942398a1221823ef28e369332a6ddffe-628278408'

    url = 'https://api.mercadopago.com/checkout/preferences'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access_token
    }

    # notification_url = request.build_absolute_uri('/api/notification/')


    data = {
        "items": [
            {
                "title": request.data["title"],
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": request.data["value"]
            }
        ],
        # "payer": {
        #     "email": request.data["email"]
        # },
        "back_urls": {
            "success": "http://localhost:5173/dashboard",
            "failure": "http://localhost:5173/shop",
            "pending": "http://localhost:5173/shop"
        },
        "auto_return": "approved",
        "notification_url": "https://2c8b-2804-1b3-a3c1-1111-987b-ad20-d492-ce35.ngrok-free.app/api/notification/"
    }

    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()

    payment_link = response_data.get('init_point')

    return Response({'payment_link': payment_link})


@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def notification(request):
    if request.method == 'POST':
        data = request.data
        print(data)
        if data.get('topic') == 'merchant_order':
            # Notificação de atualização da ordem de compra
            resource_url = data.get('resource')
            if resource_url:
                order_id = resource_url.split('/')[-1]
                print('Ordem de Compra Atualizada - ID:', order_id)

        elif data.get('type') == 'payment':
            # Notificação de criação de pagamento

            action = data.get('action')
            if action and action == 'payment.created':
                payment_id = data.get('data', {}).get('id')
                status = data.get('data', {}).get('status')
                title = data.get('data', {}).get('transaction_details', {}).get('item', {}).get('title')

                print(payment_id)
                print(status)
                print(title)
                if payment_id and status == 'approved' and title:
                    print('Pagamento Aprovado - ID:', payment_id)
                    print('Título do Produto:', title)

        return HttpResponse(status=200)

    return HttpResponse(status=400)

@permission_classes([AllowAny])
@csrf_exempt
def get_payment(request):
    access_token = 'TEST-335553357611407-080122-942398a1221823ef28e369332a6ddffe-628278408'  # Substitua pelo seu access token do Mercado Pago

    url = f'https://api.mercadopago.com/v1/payments/1315314079'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        payment_data = response.json()
        title = payment_data["additional_info"]["items"][0]["title"]
        price = payment_data["additional_info"]["items"][0]["unit_price"]
        return JsonResponse(payment_data)  # Retorna os dados do pagamento como uma resposta JSON
    else:
        return JsonResponse({'error': 'Falha ao obter pagamento'}, status=500)  # Retorna uma resposta JSON com erro




