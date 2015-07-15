def getrank(score):
    rank = 0
    while(score):
        score /= 10
        rank +=1
    return rank

def getAll9(rank):
    if(rank == 1):
        return 9
    if(rank > 1):
        return 10**rank-1
    
def cleanFirst(N,rank):
    first = N/(10**(rank-1))
    return first

def procEachCase(N):
    rank = getrank(N)
    if(rank == 1):
        return N
    if(rank > 1):
        first = cleanFirst(N,rank)
        rest = N-first*(10**(rank-1))
        print(first, rest)
        if(rest ==0):
            return N
        elif(first == 1):
            return rest+1 + procEachCase(getAll9(rank-1))
        elif(first >1):
            return first+rest+1+procEachCase(getAll9(rank-1))


#---- main code here
filepath = "A-small-attempt2.in"
#filepath = "example"
tt = "A-small-attempt1.in"
anspath = "answer"

file = open(filepath,'r')
ans_file = open(anspath,'w')

str_T = file.readline()
T = int(str_T)
print(T)
for i in range(1,T+1):
    print("case",i)
    str_N = file.readline()
    N = int(str_N)
    print(N)
    answer = procEachCase(N)
    print(answer)
    #print(answer)
    ans_file.write("Case #%d: %d\n" %(i,answer))
    #ans_file.write("%d,%d,%d, Case #%d: %s\n" %(X,R,C,i,answer))

ans_file.close()
file.close()

