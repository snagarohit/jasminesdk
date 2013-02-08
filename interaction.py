#This file provides functions for interacting with posts.

import environment
import time


#Function that handles comment feature
def comment(object_id,msg,tok):
	print "+--------------+"
	print "|Comment Posted|"
	print "+--------------+"
	print msg

#Fuction that handles "liking" an object	
def like(object_id,tok):
	print "+-----+"
	print "|Liked|"
	print "+-----+"
	
#Update the status or post a message on a friend's wall	
def update(msg,tok,profile_id="me"):
	print "+-------------+"
	print "|Status Posted|"
	print "+-------------+"
	print msg
	
#Extend Access Token
def refresh_token():
	f = open(environment.directory['core']+"token.data",'r')
	tok = f.read()
	return tok

#Get News Feed	
def get_feed(tok):

	print "\n\n\n+-------+"
	print "|Message|"
	print "+-------+"
	
	message = raw_input('>>')
	
	#Final return object is a list of dicts
	final_feed = []

	job = {}
	job['from'] = '123412341234' #Userid of status poster
	job['message'] = message     #Message of the status
	
	job['time'] = time.strftime("%Y-%m-%dT%H:%M:%S+0000",time.gmtime()) #Ex: '2013-01-06T20:40:36+0000'
	#NOTE: the returned time string is in UTC time zone and not IST
	
	job['id'] = '789078080_987987890' #Object Id of the status object of facebook
	final_feed.append(job)
	
	return final_feed
	
	
	
	
	
	
	
	
