import tweepy
import csv
from datetime import timedelta
from textblob import TextBlob
subList = {}
polList = {}
tweets = {}
with open('tweets.csv', newline='') as csvfile:
	read = csv.reader(csvfile)
	i = 0
	for row in read:
		analysis = TextBlob(row[0])
		subList[i] = analysis.sentiment.subjectivity
		polList[i] = analysis.sentiment.polarity
		tweets[i] = row[0]
		print(i)
		i = i+1

with open('results.csv','w') as f:
	for b in tweets:
		strin = tweets[b]+ ","+str(subList[b])+","+str(polList[b])+'\n'
		f.write(strin)

pass