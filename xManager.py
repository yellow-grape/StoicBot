import os
import requests
from requests_oauthlib import OAuth1
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Method to get Twitter API credentials from environment variables
def get_twitter_credentials():
    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
    return consumer_key, consumer_secret, access_token, access_token_secret

# Method to send a tweet
def send_tweet(text):
    # Retrieve credentials
    consumer_key, consumer_secret, access_token, access_token_secret = get_twitter_credentials()

    auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)

    tweet_data = {'text': text}

    # Make the POST request to send the tweet
    response = requests.post('https://api.twitter.com/2/tweets', auth=auth, json=tweet_data)

    # Print the status code and response from the API
    if response.status_code == 201:
        print("Tweet sent successfully!")
    else:
        print(f"Failed to send tweet. Status code: {response.status_code}")
        print(response.json())

