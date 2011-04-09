from piston.handler import BaseHandler
from models import Domain
#from piston.utils import throttle, validate, rc

class EmailHandler(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'POST', 'DELETE')
    #model = Email
    exclude = ()
    def read(self, request):
      return None

class Website(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'POST', 'DELETE')
    #model = Email
    exclude = ()
    def read(self, request):
        return None

class Domain(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'POST', 'DELETE')
    #model = Domain
    exclude = ()
    def read(self, request):
        return None

class Application(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'POST', 'DELETE')
    #model = Email
    exclude = ()
    def read(self, request):
        return None

class Cron(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'POST', 'DELETE')
    #model = Email
    exclude = ()
    def read(self, request):
        return None

class DNS(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'POST', 'DELETE')
    #model = DNS
    exclude = ()
    def read(self, request):
        return None

class Database(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'POST', 'DELETE')
    #model = Database
    exclude = ()
    def read(self, request):
        return None

class File(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'POST', 'DELETE')
    #model = File
    exclude = ()
    def read(self, request):
        return None

class ShellUser(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'POST', 'DELETE')
    #model = ShellUser
    exclude = ()
    def read(self, request):
        return None

class Server(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'POST', 'DELETE')
    #model = ShellUser
    exclude = ()
    def read(self, request):
        return None
