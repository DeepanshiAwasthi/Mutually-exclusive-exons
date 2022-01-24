import re
import os 
from collections import defaultdict
path='/home/deepanshi/projects/mxe5/uniq'
files = os.listdir(path)
count=0

for f in files:
    ff='/home/deepanshi/projects/mxe5/uniq_2/'+f
    with open (ff,'w') as f1: 
        count=count+1
        d={}
        t_str=''
        with open('/home/deepanshi/projects/mxe5/uniq/'+f,'r') as f:
            for line in f:
                t_str=''
                ex=[]
                line=line.strip('\n')
                el=re.split('\t',line)
                eid=el[0]
                tlist=re.split(",",el[1])
                for i in range(0,len(tlist)):
                    if i==len(tlist)-1:
                        if t_str:
                            t_str=t_str+','+tlist[i][2:-2]
                            ex.append(tlist[i][2:-2])
                            #d.update({tlist[i][2:-2]:t_str})
                        else:
                            t_str=tlist[i][2:-2]
                            #d.update({tlist[i][2:-2]:t_str})
                            ex.append(tlist[i][2:-2])
                    else:
                        if t_str:
                            t_str=t_str+','+tlist[i][2:-1]
                            ex.append(tlist[i][2:-1])
                            #d.update({tlist[i][2:-1]:t_str})    
                        else:
                            t_str=tlist[i][2:-1] 
                            ex.append(tlist[i][2:-1])
                            #d.update({tlist[i][2:-1]:t_str})
                for j in ex:
                    d.update({j:t_str})              
        for i in d:
            f1.write("{}\t{}\n".format(i,d[i]))
        print(count)       