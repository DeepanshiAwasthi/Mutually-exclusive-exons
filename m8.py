import os 
import re
from collections import defaultdict
path='/home/deepanshi/projects/mxe5/gex5'
files = os.listdir(path)
names=[]
d1=[]
d2=[]

count=0
for f in files:
    ff='/home/deepanshi/projects/mxe5/gex5/'+f
    with open (ff,'r') as f1: 
        with open('/home/deepanshi/projects/mxe5/gex6/'+f,'w') as f2:  
            for line in f1:
                line=line.strip('\n')
                a=re.search("^\w",line)
                if a:
                    el=re.split('\t',line)
                    tid=el[0]
                    l=el[1]
                    var=int(el[2])
                    el2=re.split(':',l)
                    if el2[0]==el2[1]:
                        print(line)
                        f2.write("{}\t{}\t{}\n".format(tid,l,var))

          



