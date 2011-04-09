from piston.handler import BaseHandler
#from piston.utils import throttle, validate, rc

class EmailHandler(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'POST', 'DELETE')
    #model = Email
    exclude = ()

    def read(self, request):
        return None
