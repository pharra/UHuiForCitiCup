from django.template import loader
import django.http


class render(django.http.HttpResponse):
    def __init__(self, request, template_name, context=None, content_type=None, status=None, using=None):
        content = loader.render_to_string(template_name, context, request, using=using)
        self.contentlist = [template_name, context, request, using]
        super(render, self).__init__(content, content_type, status)
        self.type = "render"

    def addContent(self, context):
        for key in context:
            self.contentlist[1][key] = context[key]
        self.content = loader.render_to_string(self.contentlist[0], self.contentlist[1], self.contentlist[2],
                                               using=self.contentlist[3])


        # def __call__(self, request, template_name, content_type=None, context=None, status=None, using=None):
        #     return drender(request=request, template_name=template_name, content_type=content_type, context=context, status=status,
        #             using=using)
        #
        # def render(request, template_name, context=None, content_type=None, status=None, using=None):
        #     """
        #     Returns a HttpResponse whose content is filled with the result of calling
        #     django.template.loader.render_to_string() with the passed arguments.
        #     """
        #     content = loader.render_to_string(template_name, context, request, using=using)
        #     return HttpResponse(content, content_type, status)


class JsonResponse(django.http.JsonResponse):
    def __init__(self, content):
        super(JsonResponse, self).__init__(data=content)
        self.type = "JsonResponse"
