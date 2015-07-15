

#import demjson
import re
import sys
from collections import Counter

# extract the twitter text from a csv line. by using the regular expression
# return a list - matchObj, and the text is matchObj(2).
# matchObj(1) and (3) store the string before and after the twitter text.
def extractText( csvLine ):
   reFlags = re.M|re.I|re.U
   pattern = "\d+,\d+,\d+,\d+,(.*)text\"\":\"\"(.*)\"\",\"\"in_reply_to_status_id\"\":(.*)"
   #pattern = "\d+,\d+,\d+,\d+,(.*)"
   matchObj = re.match(pattern, csvLine, reFlags)
   return matchObj

# count the frequence of target word in each line
# and return number.
def countPerLine(target,twit):
    i = 0
    words = ''.join(c if c.isalnum() else ' ' for c in twit.lower()).split()

   # !!!!!!!!!1for test!!!!!!!!!!!!!1
   # print(words)

    for word in words:
        if(word == target):
            i = i+1
    return i

# find the @username in each line and return them as a list
def findUserPerLine(twit):
   users = re.findall(r"(?<=@)\w+",twit.lower())
   return users

# find the #topic in each line and return them as a list
def findTopicPerLine(twit):
   topics = re.findall(r"(?<=#)\w+",twit.lower())
   return topics

# add a list of terms to the Counter()
def appendTermsToDict(term_dict,terms):
   line_count = Counter(terms)

   #!!!!!!!!for test!!!!!!!!!!!!!!!!!!!!!!!!
   #print line_count

   term_dict = term_dict + line_count
   return term_dict

#-----------------------------
# one way to get the user input
print sys.argv


# initialize the paras.
index = 0
target_word_count = 0

user_dict = Counter()
print user_dict

topic_dict = Counter()
print topic_dict

# get the word searching for from user input
# if user do not enter anything, just press enter
# Then the default target is "ash"
target_word = "ash"
input_target = raw_input\
              ("Please input the word that you want count \
               \n(or just press \"Enter\" using default)\n: ")
if input_target :
    target_word = input_target

print "Will count the word :\"",target_word, "\""


# ------------------------

# open the csv file.
miniTwit = open("Data/miniTwitter.csv",'r')

#skip the firs line of the file
miniTwit.readline()

for csvline in miniTwit :
   # read each line and increment index each line
   index = index+1
   twitText = extractText(csvline)

   #!!!!! for test!!!!!!!!!!!!!!!!!
   #print twitText.group(2)

   
   # count the number of target term.
   target_word_count = target_word_count + countPerLine(target_word,twitText.group(2))

   # count @users frequencies
   users = findUserPerLine(twitText.group(2))
   user_dict = appendTermsToDict(user_dict,users)

   # count #topic frequencies
   topics = findTopicPerLine(twitText.group(2))
   topic_dict = appendTermsToDict(topic_dict,topics)
   
   #print index,':',target_word_count
   
print "The word \"", target_word, "\" appeared ", target_word_count, "time(s) in the file"
print "users: ",user_dict.most_common(10)
print "topics: ",topic_dict.most_common(10)
