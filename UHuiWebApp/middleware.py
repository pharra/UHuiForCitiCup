from . import views
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        self.process_request = self.process_request
        # One-time configuration and initialization.

    def process_request(self, request):
        url = request.path
        uid = views.get_uid(request)

        if uid:
            request.uid = uid
        elif url.startswith("/manage"):
            return HttpResponseRedirect("/login")

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.process_request(request)
        if not response:
            response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

