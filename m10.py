import os 
import re
from collections import defaultdict
def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i in li1 and i not in li2]
    return li_dif
path='/home/deepanshi/projects/mxe5/gex'
files = os.listdir(path)
names=[]
d={}
for f in files:
    ff='/home/deepanshi/projects/mxe5/gex/'+f
    with open (ff,'r') as f1: 
        for line in f1:
            line=line.strip('\n')
            a=re.search("^\w",line)
            if a:
                el=re.split('\t',line)
                tid=el[0]
                ex=el[2] 
                d.update({tid:ex})

path1='/home/deepanshi/projects/mxe5/gex6'
files1 = os.listdir(path1)
for f11 in files1:
    ff1='/home/deepanshi/projects/mxe5/gex6/'+f11
    with open (ff1,'r') as f2: 
        with open('/home/deepanshi/projects/mxe5/gex7/'+f11,'w') as f3:
            for line1 in f2:
                line1=line1.strip('\n')
                a1=re.search("^\w",line1)
                if a1:
                    list1=[]
                    list2=[]
                    el1=re.split('\t',line1)
                    tid1=el1[0]
                    #print(tid1)
                    l=el1[1]
                    diff=el1[2]
                    tel=re.split(":",tid1)
                    print(tel[0],tel[1])
                    k1=re.split(',',d[tel[0]])
                    for i in range(0,len(k1)):
                        if i==len(k1)-1:
                            list1.append(k1[i][2:-2])
                        else:
                            list1.append(k1[i][2:-1])    
                    k2=re.split(',',d[tel[1]])
                    for j in range(0,len(k2)):
                        if j==len(k2)-1:
                            list2.append(k2[j][2:-2])
                        else:
                            list2.append(k2[j][2:-1])  
                    tw1=Diff(list1,list2)  
                    tw2=Diff(list2,list1)   
                    if len(tw1)==0 and len(tw2)!=0:
                        tw1=0 
                        f3.write("{}\t{}\t{}\t{}:{}\t{}\n".format(tid1,l,diff,tw1,tw2,tw1+len(tw2))) 
                    elif len(tw2)==0 and len(tw1)!=0:
                        tw2=0
                        f3.write("{}\t{}\t{}\t{}:{}\t{}\n".format(tid1,l,diff,tw1,tw2,len(tw1)+tw2))  
                    elif len(tw1)==0 and len(tw2)==0:  
                        f3.write("{}\t{}\t{}\t{}:{}\t{}\n".format(tid1,l,diff,tw1,tw2,0))  
                    else:    
                        f3.write("{}\t{}\t{}\t{}:{}\t{}\n".format(tid1,l,diff,tw1,tw2,len(tw1)+len(tw2)))          
                


               