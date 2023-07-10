import time
import mercadopago

def payment_status_check_job():
    access_token = 'TEST-335553357611407-080122-942398a1221823ef28e369332a6ddffe-628278408'

    # Configurar a biblioteca do Mercado Pago
    mp = mercadopago.MP(access_token)

    # Obter os pagamentos pendentes no seu sistema
    pagamentos_pendentes = [1, 2, 3]  # Substitua pelo código para obter os pagamentos pendentes
    print('lindo')
    for pagamento in pagamentos_pendentes:
        preference_id = pagamento.preference_id

        # Consultar o status do pagamento
        payment_info = mp.get_payment_info(preference_id)

        # Verificar se o pagamento foi aprovado
        if payment_info['status'] == 'approved':
            print(f"Um pagamento via boleto foi aprovado: {preference_id}")

        # Aguardar alguns segundos antes de fazer a próxima verificação
        time.sleep(1)