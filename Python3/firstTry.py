

#import demjson
import re

# extract the twitter text from a csv line. by using the regular expression
# return a list - matchObj, and the text is matchObj(2).
# matchObj(1) and (3) store the string before and after the twitter text.
def extractText( csvLine ):
   reFlags = re.M|re.I|re.U
   pattern = "\d+,\d+,\d+,\d+,(.*)text\"\":\"\"(.*)\"\",\"\"in_reply_to_status_id\"\":(.*)"
   #pattern = "\d+,\d+,\d+,\d+,(.*)"
   matchObj = re.match(pattern, csvLine, reFlags)
   return matchObj

def countPerLine(target,twit):
    i = 0
    words = ''.join(c if c.isalnum() else ' ' for c in twit.lower()).split()
    #print(words)
    for word in words:
        if(word == target):
            i = i+1
    return i


# open the csv file.
miniTwit = open("miniTwitter.csv",'r')


#skip the firs line of the file
miniTwit.readline()
# default target is "ash"
target = "ash"
index = 0
targetCount = 0

for csvline in miniTwit :
   twitText = extractText(csvline)
   targetCount = targetCount + countPerLine(target,twitText.group(2))
   index = index+1
   print(index, " : ", targetCount)
   



