# importing the module
import tweepy
 
# personal information
consumer_key ="FfqzyAvxeBbxqFZRndF3XH09G"
consumer_secret ="k9HSs6R1YES9oqDckXuPfS52AtKIBxFfQz7FvrnjDDsFExRFW8"
access_token ="912244949390733312-J7mCs4rFe0ZPgdCyfM4HagcaPLjOsty"
access_token_secret ="SRNTmSyFnFRUIo6GiH4x2z5utkuKd1WqREvbt85XXkU4Z"
#from line 5 to 8 all the tokens are to be created in the "createapplication in the twitter official page" 
 
# authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
  
api = tweepy.API(auth)
tweet ="hallaluya"
#tweet is the text message that has to be comented on command
image_path ="/home/pi/Desktop/charya1.jpg" 
#is the image path
 

status = api.update_with_media(image_path, tweet) 
api.update_status(status = tweet)
