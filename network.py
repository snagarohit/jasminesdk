#This module is used for initializing network settings like installing appropriate proxy handlers. 
#This module was separated from "main.py" so as to modularize the network code from the source and 
#this file can be distributed directly as a binary instead of a source file

import urllib
import urllib2
import environment

#initializes proxy server settings if required from environment settings file.
#does nothing if proxy is not required.
def proxy_init():
	if environment.is_proxy:
		proxy = None
		opener = None
		if environment.proxy_authentication:
			proxy = urllib2.ProxyHandler({'https':'https://'+environment.proxy_username+':'+environment.proxy_password+'@'+environment.proxy_server+':'+str(environment.proxy_server_port),'http':'http://'+environment.proxy_username+':'+environment.proxy_password+'@'+environment.proxy_server+':'+str(environment.proxy_server_port)})
			pro_auth = urllib2.ProxyBasicAuthHandler()
			opener = urllib2.build_opener(proxy,pro_auth,urllib2.HTTPSHandler,urllib2.HTTPHandler)
		#Proxy authorization handler is not necessry if authoization for proxy is not required
		else:
			proxy = urllib2.ProxyHandler({'https':'https://'+environment.proxy_server+':'+str(environment.proxy_server_port),'http':'http://'+environment.proxy_server+':'+str(environment.proxy_server_port)})
			opener = urllib2.build_opener(proxy,urllib2.HTTPSHandler,urllib2.HTTPHandler)	
		urllib2.install_opener(opener)
