def checkImp(N,K,B,T,chick_Xs,chick_Vs):
    reachable = 0
    for i in range(0,N):
        if (B - chick_Xs[i])/chick_Vs[i] <= T:
            reachable += 1
    if reachable < K:
        return True

def procEachCase(N,K,B,T,chick_Xs,chick_Vs):
    if checkImp(N,K,B,T,chick_Xs,chick_Vs):
        return "IMPOSSIBLE"
    
    return "possible"


#---- main code here
filepath = "example"
anspath = "answer"

file = open(filepath,'r')
ans_file = open(anspath,'w')

str_T = file.readline()
T = int(str_T)
print(T)
for i in range(1,T+1):
    print("case",i)
    str_case = file.readline()
    case_pars = str_case.split(" ")
    N = int(case_pars[0])
    K = int(case_pars[1])
    B = int(case_pars[2])
    T = int(case_pars[3])

    str_chick_Xs = file.readline()
    chick_Xs_vars = str_chick_Xs.split(" ")
    chick_Xs = []
    for j in range(0,N):
        chick_Xs.append(int(chick_Xs_vars[j]))
        print(chick_Xs[j])
    

    str_chick_Vs = file.readline()
    chick_Vs_vars = str_chick_Vs.split(" ")
    chick_Vs = []
    for j in range(0,N):
        chick_Vs.append(int(chick_Vs_vars[j]))
        print(chick_Vs[j])


    answer = procEachCase(N,K,B,T,chick_Xs,chick_Vs)
    print(answer)
    #ans_file.write("Case #%d: %s\n" %(i,answer))
    #ans_file.write("%d,%d,%d, Case #%d: %s\n" %(X,R,C,i,answer))

ans_file.close()
file.close()

#print(procEachCase(3,1,3))

