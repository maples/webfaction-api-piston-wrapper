from django.conf.urls.defaults import *
from piston.resource import Resource
import handlers

email_handler = Resource(handlers.EmailHandler)
domain_handler =Resource(handlers.DomainHandler)
#TODO: how to use the same pattern for optional params?
urlpatterns = patterns('',
    url(r'^email/$', email_handler, {'emitter_format' : 'json'}),
    url(r'^email/(?P<email>\w+)$', email_handler, {'emitter_format' : 'json'}),

    url(r'^website/$', email_handler, {'emitter_format' : 'json'}),
    url(r'^website/(?P<website>\w+)$', email_handler, {'emitter_format' : 'json'}),

    url(r'^domain/$', domain_handler, {'emitter_format' : 'json'}),
    url(r'^domain/(?P<domain>.+)$', domain_handler, {'emitter_format' : 'json'}),

    url(r'^application/$', email_handler, {'emitter_format' : 'json'}),
    url(r'^application/(?P<application>\w+)$', email_handler, {'emitter_format' : 'json'}),

    url(r'^cron/$', email_handler, {'emitter_format' : 'json'}),
    url(r'^cron/(?P<cron>\w+)$', email_handler, {'emitter_format' : 'json'}),

    url(r'^dns/$', email_handler, {'emitter_format' : 'json'}),
    url(r'^dns/(?P<dns>\w+)$', email_handler, {'emitter_format' : 'json'}),

    url(r'^database/$', email_handler, {'emitter_format' : 'json'}),
    url(r'^database/(?P<database>\w+)$', email_handler, {'emitter_format' : 'json'}),

    url(r'^file/$', email_handler, {'emitter_format' : 'json'}),
    url(r'^file/(?P<file>\w+)$', email_handler, {'emitter_format' : 'json'}),
    
    url(r'^shelluser/$', email_handler, {'emitter_format' : 'json'}),
    url(r'^shelluser/(?P<shelluser>\w+)$', email_handler, {'emitter_format' : 'json'}),

    url(r'^server/$', email_handler, {'emitter_format' : 'json'}),
    url(r'^server/(?P<server>\w+)$', email_handler, {'emitter_format' : 'json'}),
)
