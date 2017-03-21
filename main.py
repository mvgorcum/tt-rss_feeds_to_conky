import json
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("feed_name")
parser.add_argument("maxarticles")
args = parser.parse_args()

feedname=args.feed_name
maxarticles=int(args.maxarticles)
username='username'
password='supersecretpassword'
url='https://example.com/tt-rss/api/'


sendlogin='{"op":"login","user":"'+ username +'","password":"'+password +'"}'
response=requests.post(url,data=sendlogin)
sid=json.loads(response.content.decode('utf-8'))['content']['session_id']

getfeeds='{"sid":"'+sid+'","op":"getFeeds","cat_id":"-3"}'
feedresponse=requests.post(url,data=getfeeds)
feedlist=json.loads(feedresponse.content.decode('utf-8'))

for feed in feedlist['content']:
    if feed['title'] == feedname:
        feedid=feed['id']
        unreadcount=int(feed['unread'])
        #print(unreadcount)


getheadlines='{"sid":"'+sid+'","op":"getHeadlines","feed_id":"'+str(feedid)+'"}'
headlinesresp=requests.post(url,data=getheadlines)
headlines=json.loads(headlinesresp.content.decode('utf-8'))

for artnr,article in enumerate(headlines['content']):
    if artnr >= min(maxarticles,int(unreadcount)):
        break
    print(article['title'])
