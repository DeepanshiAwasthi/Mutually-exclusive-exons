import os 
import re
from collections import defaultdict
path='/home/deepanshi/projects/mxe5/gex4'
files = os.listdir(path)
names=[]
d1=[]
d2=[]

count=0
for f in files:
    ff='/home/deepanshi/projects/mxe5/gex4/'+f
    with open (ff,'r') as f1: 
        with open('/home/deepanshi/projects/mxe5/gex5/'+f,'w') as f2:  
            for line in f1:
                line=line.strip('\n')
                a=re.search("^\w",line)
                if a:
                    count=count+1
                    el=re.split('\t',line)
                    tid=el[0]
                    l=el[1]
                    var=int(el[3])
                    d1.append(tid)
                    d2.append(l)
                   
                    if count==2:
                        f2.write("{}:{}\t{}:{}\t{}\n".format(d1[0],d1[1],d2[0],d2[1],abs(var)))


                else:
                    count=0
                    d1=[]
                    d2=[]
                  
                

