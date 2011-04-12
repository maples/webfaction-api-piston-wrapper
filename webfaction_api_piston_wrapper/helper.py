import xmlrpclib

class Webfaction:

    def __init__(self, user_name, passwd):
          self.__missing_method_name = None
          self.server = None
          self.session_id = None
          self.account = None
          self.login(user_name, passwd)

    def login(self, user_name, passwd ):
        print user_name
        print passwd
        self.server = xmlrpclib.ServerProxy('https://api.webfaction.com/')
        self.session_id, self.account = self.server.login(user_name, passwd)

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def __getattr__(self, name):
        self.__missing_method_name = name
        return getattr(self, '__methodmissing__')

    def __methodmissing__(self, *args, **kwargs):
        try:
            return getattr(self.server, self.__missing_method_name)(self.session_id, *args, **kwargs)
        except AttributeError, e:
            #TODO: add APIException
            raise e
        except xmlrpclib.ProtocolError, e:
            #TODO: add APIException
            raise e

api = Webfaction('maples', '')


