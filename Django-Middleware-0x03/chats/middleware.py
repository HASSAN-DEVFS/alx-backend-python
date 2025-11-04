<<<<<<< HEAD


import logging
from datetime import datetime

class RequestLoggingMiddleware:
    def __init__(self, get_response):
       
        self.get_response = get_response

       
        logging.basicConfig(
            filename='requests.log',
            level=logging.INFO,
            format='%(message)s'
        )

    def __call__(self, request):
       
        user = request.user if request.user.is_authenticated else 'Anonymous'

        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}"
        logging.info(log_message)

=======
# chats/middleware.py
from datetime import datetime
from django.http import HttpResponse

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
      
        current_hour = datetime.now().hour

      
        if current_hour >= 22 or current_hour < 6:
            return HttpResponse("Access restricted: The site is closed at this time.", status=403)

     
>>>>>>> cce28c8 (Regler un erreur de middelware)
        response = self.get_response(request)
        return response
