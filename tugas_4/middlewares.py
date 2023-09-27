from datetime import datetime

class LastLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Cek jika user telah login dan tidak memiliki cookie last_login
        if request.user.is_authenticated and 'last_login' not in request.COOKIES:
            response.set_cookie('last_login', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        
        return response
