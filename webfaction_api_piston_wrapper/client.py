from helper import Webfaction
from django.conf import settings

webfaction = Webfaction(settings.API_WEBFACTION_USER, settings.API_WEBFACTION_PASSWD)

def domain_exists(domain):
    domains = webfaction.list_domains()
    return bool([ d for d in domains if d['domain'] == domain])

def subdomain_exists(domain, subdomain):
    domains = webfaction.list_domains()
    return bool([ d for d in domains if d['domain'] == domain and subdomain in d['subdomains']])

def create_subdomain(domain, subdomain):
    subdomain = (subdomain, ) if type(subdomain) == str or type(subdomain) else subdomain
    if subdomain_exists(domain, subdomain): raise WebFactionAPIException('SUBDOMAIN_EXISTS')
    return webfaction.create_domain(domain, *subdomain)

def create_domain(domain):
    if domain_exists(domain): raise WebFactionAPIException('DOMAIN_EXISTS')
    return webfaction.create_domain(domain)

def app_exists(name):
    apps = webfaction.list_apps()
    return bool([ d for d in apps if d['name'] == name])
    
def create_app(name, type, extra_info=None, autostart=False):
    if  app_exists(name): raise WebFactionAPIException('APPLICATION_EXISTS')
    return webfaction.create_app(name, type, autostart, extra_info)

def website_exists(website_name):
    websites = webfaction.list_websites()
    return bool([ d for d in websites if d['name'] == website_name])
    
def create_website(website_name, ip, https=False, subdomains, site_apps):
    if  website_exists(website_name): raise WebFactionAPIException('WEBSITE_EXISTS')
    return webfaction.create_website(website_name, ip, https=False, subdomains, site_apps)
    
