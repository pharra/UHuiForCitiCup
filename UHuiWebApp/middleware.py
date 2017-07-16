from . import views
from django.http import HttpRequest,HttpResponse, HttpResponseRedirect, JsonResponse

class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        self.process_request = self.process_request
        # One-time configuration and initialization.

    def process_request(self, request):
        cookie_content = request.COOKIES['uhui']
        url = request.path
        if cookie_content:
            pass
        elif url.startwith("/manage"):
            return HttpResponseRedirect("/login")
    def __call__(self, request):

        # Code to be executed for each request before
        # the view (and later middleware) are called.
        self.process_request(request)
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response