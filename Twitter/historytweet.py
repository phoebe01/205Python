#modules being imported
import twitter
import datetime
import urllib2

#find web history file and read
file = open("/Users/phamilton/Library/Application Support/Google/Chrome/Default/Current Session")
data = file.read()

#find the beginning and end of the url
urlStart = str(data).rfind("http")
urlEnd = str(data).find(chr(0), urlStart)
url = data[urlStart:urlEnd]

#open the webpage
response = urllib2.urlopen(url)
web = response.read() #looks at the data
print (web) #prints the website data

#find the title page from start to end
findPageTitle = web.find("<title>")
findPageTitleEnd = web.find("</title>")

title = web [findPageTitle:findPageTitleEnd]
title = title.replace("<title>","") #replace title with new word
print(title) #print new title

#twitter credentials
api = twitter.Api(consumer_key="r2yXR6nO6clnZe01dkk8ALmsD",consumer_secret="0uBDfIxMo2a1Z2aLaZxqzK9LNalkS8XSns31RHMUQTIeQGmhUZ",

#receives the time
timestamp = datetime.datetime.utcnow()

#posts tweet to twitter
response = api.PostUpdate("The last thing I viewed " + title + url + str(timestamp)) #updated status

print("Update: " + response.text) #shows twitter has been updated
