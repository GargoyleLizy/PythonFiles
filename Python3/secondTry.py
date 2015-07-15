
import re
import sys
from collections import Counter
import datetime

# extract the twitter text from a csv line. by using the regular expression
# return a list - matchObj, and the text is matchObj(2).
def extractText( csvLine ):
   reFlags = re.M|re.I|re.U
   pattern = "\d+,\d+,\d+,\d+,(.*)text\"\":\"\"(.*)\"\",\"\"in_reply_to_status_id\"\":(.*)"
   matchObj = re.match(pattern, csvLine, reFlags)
   return matchObj

# count the frequence of target word in each line
# and return number.
def countTargetPerLine(target,twit):
    i = 0
    words = ''.join(c if c.isalnum() else ' ' for c in twit.lower()).split()

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
   term_dict = term_dict + line_count
   return term_dict

# aggrate the functions above.
def countAll(query, twit_list):
   query_count = 0
   user_dict = Counter()
   topic_dict = Counter()
   
   for twit in twit_list:
      
      query_count += countTargetPerLine(query,twit)

      users = findUserPerLine(twit)
      user_dict = appendTermsToDict(user_dict,users)
   
      topics = findTopicPerLine(twit)
      topic_dict = appendTermsToDict(topic_dict,topics)
   
   return [query_count, user_dict, topic_dict]

#--- main code start here --------
#-----------------------------
# if there is an command argument, take it as query word
# and the default query word is ash
query_word = "ash" 
if(len(sys.argv)>=2):
    if(sys.argv[1]):
        query_word = sys.argv[1]

print("Will count the word :\"",query_word, "\"")


# ------------------------
start_time = datetime.datetime.now()
# TIME RECODING
print("start_time: ",start_time)


# open the csv file.
twits = open("data/Twitter.csv",'r')

data = twits.readlines() 

IO_end_time = datetime.datetime.now()
# TIME RECODING
print("IO_end_time: ", IO_end_time)
      

result = countAll(query_word,twit_list)

#---- get the result ------ 
print("The word \"", query_word, "\" appeared ", result[0], "time(s) in the file")
print("top 10 users: ",result[1].most_common(10) )
print("top 10 topics: ",result[2].most_common(10) )
end_time = datetime.datetime.now()
print("end_time: ", end_time)
IO_time = IO_end_time - start_time
print("IO_time: ", IO_time)
total_time = end_time - start_time
print("total_time: ", total_time)
