#####################################
# SayCow Quotations App For Jasmine #
#####################################

import json
import re
import random
import environment
import interaction


####################
# Public Functions #
####################

#Identifies the app in a unique id.
app_id = "saycow"

#In any lib_* file, "check" function checks if the post/news item is of the app's corresponding post
def check(post):
	matchObj = re.search(r"^(?:think\s*!*|quote|wassup|howdy|sup|what\'?s\s*up|say\s*what)\s*[\?!]*\s*",post['message'])
	if matchObj:
		return True
	return False

#After confirming that the message/status corresponds to the current app using the "check" function above, "execute" function
#is called to do the actual work

def execute(post):
	quote = return_random_quote()#calling an internal function
	return quote
		
	
######################
# Internal Functions #
######################

#Returns a random quotation everytime it's called
def return_random_quote():
	f = open(environment.directory['apps']+"quotations.json",'r')
	quote_dict = json.loads(f.read())
	f.close()
	author = quote_dict.keys()[random.randint(0,len(quote_dict.keys())-1)]
	quote = random.choice(quote_dict[author])
	
	return quote+"\n-"+author
	
