def procEachCase():
    return


#---- main code here
filepath = "example"
anspath = "answer"

file = open(filepath,'r')
ans_file = open(anspath,'w')

T = file.readInt()
 
print(T)
for i in range(1,T+1):
    print i

#ans_file.close()
file.close()

#print(procEachCase(3,1,3))

