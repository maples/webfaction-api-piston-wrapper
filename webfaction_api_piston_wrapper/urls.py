from django.conf.urls.defaults import *
from piston.resource import Resource
from handlers import EmailHandler

email_handler = Resource(EmailHandler)
#TODO: how to use the same pattern for optional params?
urlpatterns = patterns('',
    url(r'^email/$', email_handler, {'emitter_format' : 'json'}),
    url(r'^email/(?P<email>\w+)$', email_handler, {'emitter_format' : 'json'}),
)
