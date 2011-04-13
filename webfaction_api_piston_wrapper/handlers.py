from piston.handler import BaseHandler
from piston.utils import throttle, validate, rc
from models import Domain
from helper import api
#from piston.utils import throttle, validate, rc

 

class EmailHandler(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'POST', 'DELETE')
    exclude = ()
    def read(self, request):
      return None

class WebsiteHandler(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'POST', 'DELETE')
    exclude = ()
    def read(self, request):
        return None

class DomainHandler(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'POST', 'DELETE')
    exclude = ()
    def read(self, request):
        domains = api.list_domains()
        return domains

    #@validate(DomainForm, 'POST')
    def create(self, request):
        domain = request.POST.get('domain')
        subdomains = request.POST.getlist('subdomains')
        return api.create_domain(domain, *subdomains)

    def delete(self, request, domain, subdomain=None):
        if subdomain:
            api.delete_domain(domain, subdomain)          
        else:
            api.delete_domain(domain)
        return rc.DELETED

class ApplicationHandler(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'POST', 'DELETE')
    exclude = ()
    def read(self, request):
        return None

class CronHandler(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'POST', 'DELETE')
    exclude = ()
    def read(self, request):
        return None

class DNSHandler(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'POST', 'DELETE')
    exclude = ()
    def read(self, request):
        return None

class DatabaseHandler(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'POST', 'DELETE')
    exclude = ()
    def read(self, request):
        return None

class FileHandler(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'POST', 'DELETE')
    exclude = ()
    def read(self, request):
        return None

class ShellUserHandler(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'POST', 'DELETE')
    exclude = ()
    def read(self, request):
        return None

class ServerHandler(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'POST', 'DELETE')
    exclude = ()
    def read(self, request):
        return None
