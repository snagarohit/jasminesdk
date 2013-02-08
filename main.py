import urllib2,urllib
import time
import json
import sys
import random
import environment
import os
import imp
import re

#Checking if proxy server is required and installing appropriate handler for proxy
import network
network.proxy_init()

#Get the feed
import interaction
token = interaction.refresh_token()

while True:
	feed = interaction.get_feed(token)

	for item in feed:
	
		#Dynamic Application Checking & Loading
		files_in_apps = os.listdir(environment.directory['apps'])
		refined_files = [] #Ignoring .pyc and other non-app files
		for filename in files_in_apps:
			if re.search(r'^app_.*?\.py$',filename) and not filename=="app_badrequest.py":
				refined_files.append(filename)
			
		is_app_found = False #Used to know if we need to execute the default app if all remaining apps don't claim the input message	
		for filename in refined_files:
			app_file = environment.directory['apps']+filename
			module_handle = imp.load_source(filename[:-3],app_file)
			if module_handle.check(item):
				print "App Id: "+module_handle.app_id
				interaction.comment(item['id'],module_handle.execute(item),token)
				is_app_found = True
				break;
	
		if not is_app_found:
			app_file = environment.directory['apps']+"app_badrequest.py"
			module_handle = imp.load_source('app_badrequest',app_file)
			print "App Id: "+module_handle.app_id
			interaction.comment(item['id'],module_handle.execute(item),token)
	
		continue
