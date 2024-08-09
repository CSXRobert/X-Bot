# Created by @CSXRobert

import time
import tweepy
import random

# Twitter API keys (replace with your own keys)
API_KEY = 'YOUR_TWITTER_API_KEY'
API_SECRET_KEY = 'YOUR_TWITTER_API_SECRET_KEY'
ACCESS_TOKEN = 'YOUR_TWITTER_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR_TWITTER_ACCESS_TOKEN_SECRET'
BEARER_TOKEN = 'YOUR_TWITTER_BEARER_TOKEN'

# Set up the connection to Twitter using API V2
client = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=API_KEY, consumer_secret=API_SECRET_KEY,
                       access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)

# Function to read the text file
def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.readlines()
    return [line.strip() for line in content]

# Function to post a tweet every 35 minutes
def daily_tweet():
    tweets = read_file('tweets.txt')
    phrases = read_file('phrases.txt')
    total_tweets = len(tweets)
    total_phrases = len(phrases)

    while True:
        used_tweets = set()
        used_phrases = set()

        while len(used_tweets) < total_tweets and len(used_phrases) < total_phrases:
            if len(used_tweets) == total_tweets:
                used_tweets.clear()  # Reset the list of used tweets when all have been posted
            if len(used_phrases) == total_phrases:
                used_phrases.clear()  # Reset the list of used phrases when all have been used

            # Select a random tweet and phrase that haven't been used yet
            tweet_index = random.choice([i for i in range(total_tweets) if i not in used_tweets])
            phrase_index = random.choice([i for i in range(total_phrases) if i not in used_phrases])

            used_tweets.add(tweet_index)
            used_phrases.add(phrase_index)

            tweet = f"{phrases[phrase_index]}\n{tweets[tweet_index]}"

            try:
                client.create_tweet(text=tweet)
                print(f'Tweet posted: {tweet}')
            except tweepy.TweepyException as e:
                print(f'Error posting the tweet: {e}')

            time.sleep(35 * 60)  # Wait 35 minutes (35 * 60 seconds)

if __name__ == "__main__":
    daily_tweet()
