"""
This script is counting how many times a stopWord is used in each tweet W(tweets) by reading the file('tweets2009-06.txt')where the information of T=time,U=user,W=tweets of each user is. 


PLEASE REVISE
-this program is just comparing "drunk"= "drunk" but not "#drunk" in other words I am not removing all non-alphanumerical characters (except # to detect hashtags)#tweet = re.sub(r'[^a-zA-Z0-9#]', '',tweet)

"""
import operator, re
# Load stop worda into a stopWords dictionary
stopWords = {}
fileOfStopWords = open('stopWords.txt')#file where all the stopWords are
while fileOfStopWords:
    #Read next line
    line = fileOfStopWords.readline()
    #Stop if line is empty
    if len(line) == 0:
        break
    #Add word to the stopWords hashtable
    stopWords[line.strip()] = 1
#Display stop words
#print stopWords.keys()



## Construct wordCount dictionary to stores the number of times each word appears
wordCount = {}
fileOfTweets = open('tweets2009-06.txt')#file where the T=time,U=user and W=tweets are


lineNum = 0
#Read file line by line
while fileOfTweets and lineNum < 1000000:
    lineNum += 1
    #Print number of lines processed every 1 Million lines
    if operator.mod(lineNum,1000000) == 0:
        print lineNum, " lines processed"
    #Read next line
    line = fileOfTweets.readline()
    #Stop if line is empty
    if len(line) == 0:
        break
    #Split line by tabs
    line = line.split('\t')
    # For this we don't care about the URL or the time stamp so we only process the line if it is a tweet
    if line[0] == 'W':
        #Make tweet into lower case
        tweet = line[1].lower()
        #Remove all non-alphanumerical characters (except # to detect hashtags)
        #tweet = re.sub(r'[^a-zA-Z0-9#]', '',tweet)
        #Split tweet by spaces so we can go through each word
        tweet = tweet.split()
        #Go through each word w in tweet
        for w in tweet:
            #If word w is a stop word continue to next word
            if w in stopWords:
            	if (w in wordCount) == False:
                    wordCount[w] = 0
                # Add one to the count of word w in the hashbale wordCount
             	wordCount[w] += 1
             	
            else:
                #If word w is not in the hashtable wordCount yet, add it and initiate its count with 0
                continue         
                
#Display tweets split 
   
#print wordCount# to see the wordCount dictionary in the console
 
fileOfStopWords.close()




# Sort the hashtable in reverse order. This returns an array of pairs (word, frequency) sorted (in reverse) by frequency
word_count_sorted = sorted(wordCount.iteritems(), key=operator.itemgetter(1), reverse = True)

#Set a minimum number of mentions to print the word. We don't want to print all the words that were only mentioned very few times. I picked 1000 for now. 
MinMention = 1
#We will write in a file called wordFrequency_minMentions_1000
wfile = open('output10.txt', 'w')
wordNum = 0
#Go through the sorted array
for wordFreq in word_count_sorted:
	wordNum += 1
 	#print the word and count if the count is larger than MinMention
	if wordFreq[1] >= MinMention:
		wfile.write(wordFreq[0]+" "+str(wordFreq[1])+'\n')

wfile.close()