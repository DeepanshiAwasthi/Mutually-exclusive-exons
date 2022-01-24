import re
import os 
from collections import defaultdict
path='/home/deepanshi/projects/mxe5/gex'
files = os.listdir(path)
count=0
for f in files:
    ff='/home/deepanshi/projects/mxe5/uniq/'+f
    with open (ff,'w') as f1: 
        count=count+1
        with open('/home/deepanshi/projects/mxe5/gex/'+f,'r') as f:
            d=defaultdict(list)
            ex_str=''
            for line in f:
                line=line.strip('\n')
                el=re.split('\t',line)
                tid=el[0]
                pl=el[1]
                ex_str=''
                exlist=re.split(",",el[2])
                for i in range(0,len(exlist)):
                    if i==len(exlist)-1:
                        if ex_str:
                            ex_str=ex_str+','+exlist[i][2:-2]
                        else:
                            ex_str=exlist[i][2:-2]  
                    else:
                        if ex_str:
                            ex_str=ex_str+','+exlist[i][2:-1]    
                        else:
                            ex_str=exlist[i][2:-1]    
                d[ex_str].append(tid)
        d1=dict(d)
        for i in d1:
            f1.write("{}\t{}\n".format(i,d1[i]))
        print(count)       