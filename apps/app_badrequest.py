########################################
# Bad Request Handling App For Jasmine #
########################################

import random
import environment
import interaction


####################
# Public Functions #
####################

#Identifies the app in a unique id.
app_id = "badrequest"

#In any lib_* file, "check" function checks if the post/news item is of the app's corresponding post
def check(post):
	return True

#After confirming that the message/status corresponds to the current app using the "check" function above, "execute" function
#is called to do the actual work

def execute(post):
	message = return_random_negative_answer()
	return message
		
	
######################
# Internal Functions #
######################

#Returns a random quotation everytime it's called
def return_random_negative_answer():
	negative = ['what ?', "eh ?", "what was that ?", "Din't quite get you. Sorry!", "What's that supposed to mean ?", "Cool Story! But I din't understand what you meant :P", "blahblahblahblah -> that's what it sounded like :P", ":poop:", "Roses are red, Skies are blue, Your post gives me no clue :P", "umm.. nope.. I don't understand your post","o.O ?", "What if I told you, I don't understand what you meant ?"]
	return random.choice(negative)
