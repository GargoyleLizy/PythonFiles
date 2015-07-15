# -*- coding: utf-8 -*-



import demjson
import re

# extract the twitter text from a csv line. by using the regular expression
# return a list - matchObj, and the text is matchObj(2).
# matchObj(1) and (3) store the string before and after the twitter text.
def extractText( csvLine ):
   reFlags = re.M|re.I|re.U
   pattern = "\d+,\d+,\d+,\d+,(.*)text\"\":\"(.*)\"\",\"\"in_reply_to_status_id\"\":(.*)"
   #pattern = "\d+,\d+,\d+,\d+,(.*)"
   matchObj = re.match(pattern, csvLine, re.UNICODE)
   return matchObj

# open the csv file.
miniTwit = open("miniTwitter.csv",'r')


#skip the firs line of the file
miniTwit.readline()


i = 0
while(i < 7):
   csvline = miniTwit.readline()
   twitJson = extractText(csvline)
   print twitJson.group(2)
   i= i+1



# start processing the csv file line by line.
#for csvLine in miniTwit :
#   matchObj = extractText(csvLine)
#   i=i+1   
#   if matchObj:
#      
#      print i," : matchObj.group(2) : ",matchObj.group(2)
#   else:
#      print "No match!!"



