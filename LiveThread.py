import praw  # Wrapper for the Reddit API.
import time
import traceback
 
"""CONFIGURATION DATA"""
BOT_DESCRIPTION = "LiveThread Helper"
VERSION = '0.1.0'
USER_AGENT = "{} v{}, to help remove all live discussion posts.".format(BOT_DESCRIPTION, VERSION)
WAIT = 60
 
reddit = praw.Reddit(client_id="",
                     client_secret="", password='',
                     user_agent=USER_AGENT, username='')
 
 
def main_runtime():
   
    for submission in reddit.subreddit('SubredditName').new(limit=100):
   
        submission_type = submission.discussion_type
        if submission.saved:
            continue
       
        if submission_type == "CHAT":
            submission.save()
            print("Post '{}' is a live chat post. Removing...".format(submission.title))
            submission.mod.remove()
            submission.reply("Hey, it looks like you submitted a Live Discussion post. Please submit a regular text-only post instead. Thank you.")
 
    return
 
 
while True:
    try:
        main_runtime()
    except:  # The bot encountered an error/exception.
        print(traceback.format_exc())  # Display the exception.
    time.sleep(WAIT)
