import pandas as pd

a2=list()
a4=list()
a8=list()


with open('SDSC-SP2-1998-4.2-cln.swf', 'r') as f:
    s= f.readlines()

for i in  s:
    i=i.strip() 
    i=i.replace("      ",",",100)
    i=i.replace("     ",",",100)
    i=i.replace("    ",",",100)
    i=i.replace("   ",",",100)
    i=i.replace("  ",",",100)
    i=i.replace(" ",",",100)
    #print(i)
    i=i.split(",")
    for x in range(len(i)):
        if len(i[x])==0:
            i.pop(x)
    #print(i)
    
    if int(i[3])>0:
        if int(i[10])==1:
            a2.append(int(i[1])-566290)
            a4.append(int(i[3]))
            a8.append(int(i[7]))
    

#print(a4)
dic={
    "Submit Time": a2,
    "Run Time": a4,
    "Requested Number of Processors": a8
     }

df=pd.DataFrame(dic)

print(df.head(10))
#print(len(df))

#df.to_csv("SDSC-SP2-1998-4.2-cln.csv")

original_q=list()

for i in range(len(a2)):
    original_q.append([a2[i],a4[i],a8[i]])
    

original_q=original_q[0:10]

cpu_n=128
sd=0
run_q=[]
wait_q=list()
while(len(original_q)!=0):
    if len(wait_q)!=0:
        for i in range(len(wait_q)):
            if wait_q[i][2]<cpu_n:
                run_q.append(wait_q[i])
                cpu_n=cpu_n-wait_q[i][2]
                wait_q.pop(i)
            else:
                break
    else:
        for i in original_q:
            if i[2]<cpu_n:
                run_q.append(i)
                cpu_n=cpu_n-i[2]
                original_q.pop(0)
            else:
                break
                
    for i in range(len(run_q)):
        sd=sd+run_q[i][0]
        sd=sd+run_q[i][0]+run_q[i][1]
        print("submit time:",run_q[i][0],"run time:",run_q[i][1],"finsh time:",run_q[i][0]+run_q[i][1])
        cpu_n=cpu_n+run_q[i][2]
        run_q.pop(0)
        if len(wait_q)!=0:
            for i in range(len(wait_q)):
                if wait_q[i][2]<cpu_n:
                    run_q.append(wait_q[i])
                    cpu_n=cpu_n-wait_q[i][2]
                    wait_q.pop(i)
                else:
                    break
        else:
            for i in original_q:
                if i[2]<cpu_n:
                    run_q.append(i)
                    cpu_n=cpu_n-i[2]
                    original_q.pop(0)
                else:
                    break
        
        
                
    
            
    
            