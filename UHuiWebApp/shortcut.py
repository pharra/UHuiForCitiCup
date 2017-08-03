from django.template import loader
import django.http


class render(django.http.HttpResponse):
    def __init__(self, request, template_name, context={}, content_type=None, status=None, using=None):
        content = loader.render_to_string(template_name, context, request, using=using)
        self.contentlist = [template_name, context, request, using]
        super(render, self).__init__(content, content_type, status)
        self.type = "render"

    def addContent(self, context):
        for key in context:
            self.contentlist[1][key] = context[key]
        self.content = loader.render_to_string(self.contentlist[0], self.contentlist[1], self.contentlist[2],
                                               using=self.contentlist[3])


class JsonResponse(django.http.JsonResponse):
    def __init__(self, content):
        super(JsonResponse, self).__init__(data=content)
        self.type = "JsonResponse"
