import os 
import re
from collections import defaultdict
tcount=[]
gcount=[]
path='/home/deepanshi/projects/mxe5/gex7'
files = os.listdir(path)
names=[]
d={}
d1=defaultdict(list)
kc=0
for f in files:
    ff='/home/deepanshi/projects/mxe5/gex7/'+f
    with open (ff,'r') as f1: 
        d={}
        
        kc=0
        for line in f1:
            line=line.strip('\n')
            a=re.search("^\w",line)
            if a:
                kc=9
                el=re.split('\t',line)
                tid=el[0]
                ex=el[3] 
                dex=el[2]
            
                if dex=='0':
                    num=int(el[4])
                    #print(num)
                    d1[int(num/2)].append(f+";"+tid+";"+ex)
                    print(int(num/2),f+";"+tid+";"+ex)
                    if num==2:
                        #print(tid,ex)
                        
                        d.update({f+';'+tid:ex})
        if kc==9:                
            with open('/home/deepanshi/projects/mxe5/gex8/'+f,'w') as f2:
                for j in d:
                    f2.write('{}\t{}\n'.format(j,d[j]))  
                    tcount.append(j)
                    gcount.append(f)           

with open('cg_9','w') as f3:
    for k in gcount:
        f3.write("{}\n".format(k))

with open('ct_9','w') as f3:
    for ik in tcount:
        f3.write("{}\n".format(ik))    
d2=dict(d1)
for il in d2:
    with open('c_'+str(il)+'_tra','w') as ffl:
        for jl in d2[il]:
            ffl.write("{}\n".format(jl))   
    with open('c_'+str(il)+'_genes','w') as ffl2:
        g=[]
        for jl in d2[il]:
            a=re.split(';',jl)
            g.append(a[0])
        for gl in g:
            ffl2.write("{}\n".format(gl)) 