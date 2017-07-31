from . import views
from .shortcut import render, JsonResponse
from django.http import HttpResponseRedirect
import json


class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        self.process_request = self.process_request
        # One-time configuration and initialization.

    def process_request(self, request):
        url = request.path
        uid = views.get_uid(request)
        if uid is False:
            response = HttpResponseRedirect('/login')
            response.delete_cookie('uhui')
            return response
        request.uid = None
        if uid:
            request.uid = uid
        elif url.startswith("/manage") or url.startswith('/user') or url.startswith('/mobile_sell_final'):
            return HttpResponseRedirect("/login")
        elif url.startswith('/post_dislike') or url.startswith('/post_like'):
            return JsonResponse({'errno': '5', 'message': '��δ��¼'})

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.process_request(request)
        if not response:
            response = self.get_response(request)
            if isinstance(response, dict):
                response = JsonResponse(response)
            elif request.uid is not None and response.type == "JsonResponse":
                print(response.content)
                content = json.loads(bytes.decode(response.content))
                userinfo = views.post_userInfo(request.uid)
                for key in userinfo:
                    content[key] = userinfo[key]
                response.content = json.dumps(content)
            elif request.uid is not None and response.type == "render":
                response.addContent(views.post_userInfo(request.uid))

        # Code to be executed for each request/response after
        # the view is called.

        return response
