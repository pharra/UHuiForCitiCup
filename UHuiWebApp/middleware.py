#coding=utf-8
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
        UA = request.META['HTTP_USER_AGENT']
        if uid is False:
            response = HttpResponseRedirect('/login')
            response.delete_cookie('uhui')
            return response
        request.uid = None

        if url == '/' and ('Android' in UA or 'Mobile Safari' in UA):
            if uid:
                request.uid = uid
            response = HttpResponseRedirect('/mobile_index')
            return response

        if uid:
            request.uid = uid
        elif url.startswith("/manage") or url.startswith('/user') or url.startswith('/mobile_sell_final'):
            return HttpResponseRedirect("/login")
        elif url.startswith('/mobile_my') or url.startswith('/mobile_user_'):
            return HttpResponseRedirect("/mobile_login")
        elif url.startswith('/post_dislike') or url.startswith('/post_like'):
            return JsonResponse({'errno': '5', 'message': '您未登录'})

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
        response.charset = 'UTF-8'
        return response
