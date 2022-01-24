import os 
import re
from collections import defaultdict
path='/home/deepanshi/projects/mxe5/gex5'
files = os.listdir(path)
names=[]
d1=defaultdict(set)
d2=defaultdict(set)
for f in files:
    ff='/home/deepanshi/projects/mxe5/gex5/'+f
    with open (ff,'r') as f1: 
        for line in f1:
            line=line.strip('\n')
            el=re.split('\t',line)
            print(el)
            var=el[2]
            tid=el[0]
            d1[var].add(el[0])
            d2[var].add(f)
dic1=dict(d1)
dic2=dict(d2)            
with open('m6.txt','w') as f2:
    f2.write("{}\t{}\t{}\n".format('Varying coding exons','Genes','Transcript pairs'))
    for i in dic1:
        f2.write('{}\t{}\t{}\n'.format(i,len(dic2[i]),len(dic1[i]))) 
        with open('m6genes_'+i,'w') as f3: 
            for i1 in dic2[i]:
                f3.write('{}\n'.format(i1))   
        with open('m6pairs_'+i,'w') as f4: 
            for j1 in dic1[i]:
                f4.write('{}\n'.format(j1))            