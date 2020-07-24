import GetOldTweets3 as got
from datetime import date
import time

# The word to search for
word = 'hi'
# The file to write to
f = open("usernameTest.txt", "a+")
# today's date
today = date.today()
# today's date as a string
since = today.strftime("%Y-%m-%d")
# The script will go until stopped
functioning = True
# A counter
round = 1

print('ROUND 1')

# The criteria for tweets that appear
tweetCriteria = got.manager.TweetCriteria().setQuerySearch(word).setSince(since).setMaxTweets(5)
# The tweets that last appeared
lastTweets = got.manager.TweetManager.getTweets(tweetCriteria)
# Loops through tweets and uses them
for tweet in lastTweets:
    print("here is the tweet id: " + tweet.id)
    print(tweet.text + ' BY: ' + tweet.username + '\n')
    if word in tweet.text.lower():
        # if it has the word, it writes it to the file
        f.write(tweet.username + '\n')
        print('username added\n')

round+=1
time.sleep(5)

#Go until not functioning
while functioning:

    print('ROUND ' + str(round) + '\n')
    repeat = False
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    lastIDs = [len(lastTweets)]
    for i in range(len(lastTweets)):
        lastIDs.append(lastTweets[i].id)

    for tweet in tweets:
    #Check if Tweet has already been tracked
        if tweet.id in lastIDs:
            print("This is a repeat")
            tweets.remove(tweet)

    # Loop through with new tweets list
    for tweet in tweets:
        # if len(tweets) == 0:
        #     print("All repeats")
        #     break
        print(tweet.text + ' BY: ' + tweet.username + '\n')
        # Check if it has the word in it
        f.write(tweet.username + '\n')
        print('username added\n')
    lastTweets = tweets
    time.sleep(30)
    round+=1
    if round == 5:
        functioning = False
    
f.close()
