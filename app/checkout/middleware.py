from django.urls import resolve

def disable_csrf_for_notification(get_response):
    def middleware(request):
        if resolve(request.path_info).view_name == 'notification':
            setattr(request, '_dont_enforce_csrf_checks', True)
        return get_response(request)
    return middleware