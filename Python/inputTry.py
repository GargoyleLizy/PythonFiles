import re
from collections import Counter
import sys

print sys.argv

target_word = "ash"
user_target = raw_input\
              ("Please input the word that you want count \n(or just press \"Enter\" using default)\n: ")
if user_target :
    target_word = user_target

print target_word



def appendUsersToDict(user_dict, users):
   for user in users:
      if user in user_dict:
         user_dict[user] += 1
      else:
         user_dict[user] = 1
   return user_dict

def append2(user_dict,users):
    line_counter = Counter(users)
    print line_counter
    user_dict = user_dict + line_counter
    print line_counter
    return user_dict

user_dict = Counter()

string = "@Dasweo @dasweo @hasdf wWere you at?"
words = re.findall("@\w+",string.lower() )
user_dict= append2(user_dict, words)


print user_dict
