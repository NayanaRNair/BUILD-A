from re import I

from tweepy import API
import tweepy
from tweepy import cursor
id=input("enter user name")

consumer_key='zJkas3FrAWaKR85xDkzIc5BoD'

consumer_secret='7Y595SHWNTrDkLNZFpj8unG7QVEOrTIj7ilKn4Cd2eXhZ6A5tl'

access_token='1390673212212613127-wuWEc5GEg3zlTzbMWQ5T4OTBjXNWYX'

access_token_secret='VfKfhtx20hYhv96VEDN3jkCNk3lFGeGAPrdrCjHdC3New'


auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

screen_name="Sahaay3"

user=api.get_user(screen_name)

CD=user.id_str
print('ID is' + CD)

cursor=tweepy.Cursor(api.user_timeline,id,tweet_mode='extended').items(1)


for i in cursor:
    print(i.full_text)
    text=i.full_text

direct_message = api.send_direct_message(CD,text)

print(direct_message.message_create["message_data"]["text"])

stream = tweepy.Stream(consumer_key,consumer_secret,access_token,access_token_secret)
stream.fliter(track=["Tweepy"])