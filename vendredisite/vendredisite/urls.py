"""vendredisite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.conf.urls import *
from django.template.response import TemplateResponse

from django.http import HttpResponse, Http404


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^uneApp/', include('uneApp.urls')),


]

def handler500(request):
    """500 error handler which includes ``request`` in the context.

    Templates: `500.html`
    Context: None
    """

    context = {'request': request}
    template_name = '500.html'  # You need to create a 500.html template.
    return TemplateResponse(request, template_name, context, status=500)


def handler404(request):

    context = {'request': request}
    template_name = '404.html'
    return TemplateResponse(request, template_name, context, status=500)


from django.core.signals import got_request_exception

class MyMiddleware(object):
    def process_exception(self, request, exception):
        # Make sure the exception signal is fired for Sentry
        got_request_exception.send(sender=self, request=request)
        return HttpResponse('foo')

