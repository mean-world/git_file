import pandas as pd

df=pd.read_csv("SDSC-SP2-1998-4.2-cln.csv")
print(df)

run_queue=list()
wait_queue=list()
#0-1 start time 
#0-2 finsh time
for i in range(len(df)):
    wait_queue.append([df["Submit Time"][i],0,df["Run Time"][i],df["Requested Number of Processors"][i],0])
    
#print(wait_queue)
wait_queue=wait_queue[0:20]
cpu=128
time=0
while len(wait_queue)!=0:
    if wait_queue[0][3]<cpu:
        wait_queue[0][1]=time
        cpu=cpu- wait_queue[0][3]
        
        for i in range(1,len(wait_queue)-1):
            if wait_queue[0][1]+wait_queue[0][2]>wait_queue[i][0]:
                time=wait_queue[i][0]
                
                if wait_queue[i][3]<cpu:
                    wait_queue[i][1]=time
                    cpu=cpu- wait_queue[i][3]
                    time=time+wait_queue[i][2]
                    cpu=cpu+ wait_queue[i][3]
            time=time+wait_queue[i][2]
            cpu=cpu+ wait_queue[i][3]
        run_queue.append(wait_queue[0])
        wait_queue.pop(0)
        
print(len(run_queue))
        

    

        
            