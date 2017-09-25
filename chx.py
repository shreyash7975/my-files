# importing the module
import tweepy
 
# personal information
consumer_key ="FfqzyAvxeBbxqFZRndF3XH09G"
consumer_secret ="k9HSs6R1YES9oqDckXuPfS52AtKIBxFfQz7FvrnjDDsFExRFW8"
access_token ="912244949390733312-J7mCs4rFe0ZPgdCyfM4HagcaPLjOsty"
access_token_secret ="SRNTmSyFnFRUIo6GiH4x2z5utkuKd1WqREvbt85XXkU4Z"
 
# authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
  
api = tweepy.API(auth)
tweet ="hallaluya" 
image_path ="/home/pi/Desktop/charya1.jpg" 
 

status = api.update_with_media(image_path, tweet) 
api.update_status(status = tweet)
