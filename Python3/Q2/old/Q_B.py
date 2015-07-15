def allMinusInt(num_lst, sub):
    for i in range(0,len(num_lst)):
        num_lst[i] -= sub
        if(num_lst[i] <=0):
            num_lst[i] = 0
    clearZero(num_lst)

def clearZero(num_lst):
    while 0 in num_lst:
        num_lst.remove(0)

def clearOneAndTwo(num_lst):
    temp_minutes = 0
    while (num_lst.count(1)>0) | (num_lst.count(2)>0):
        if(num_lst.count(2) >0):
            allMinusInt(num_penks,2)
            temp_minutes +=2
        elif(num_lst.count(1)>0):
            allMinusInt(num_penks,1)
            temp_minutes +=1
    return temp_minutes

def procEachCase(num_penks):
    minutes = 0
    num_penks.sort()
    #print(num_penks)
    while(num_penks):
        minutes += clearOneAndTwo(num_penks)
        
        if(num_penks):
            print(num_penks)
            # if the largest is odd, all eat one
            if(num_penks[-1]%2 == 1):
                allMinusInt(num_penks,1)
                minutes +=1
                minutes += clearOneAndTwo(num_penks)
                if(not num_penks):
                    return minutes
            
            # if the largest is even, break it even 
            
        
    return 0


#---- main code here
filepath = "example"
anspath = "answer"

file = open(filepath,'r')
ans_file = open(anspath,'w')

str_T = file.readline()
T = int(str_T)
print(T)
for i in range(1,T+1):
    #print(i)
    str_diners = file.readline()
    num_diners = int(str_diners)
    print(num_diners)
    
    str_penks = file.readline()
    penks_pars = str_penks.split(" ")
    num_penks = []
    for i in range(0,num_diners):
        num_penks.append(int(penks_pars[i]))
        #print(penks_pars[i])
    answer = procEachCase(num_penks)
    
    #ans_file.write("Case #%d: %d\n" %(i,answer))
    #ans_file.write("%d,%d,%d, Case #%d: %s\n" %(X,R,C,i,answer))

ans_file.close()
file.close()

#print(procEachCase(3,1,3))

