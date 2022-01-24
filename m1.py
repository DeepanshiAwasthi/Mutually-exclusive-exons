import re
import os
from collections import defaultdict
d1={}
with open('/home/deepanshi/projects/fasta_files.txt','r') as f1:
    for line in f1:
        line=line.strip('\n')
        el=re.split('[\t]',line)
        tlen=len(el[1])
        tid=el[0][1:]
        d1.update({tid:tlen})

path='/home/deepanshi/projects/gene_data/deepanshi_dir'
files = os.listdir(path)
names=[]
for f in files:
    ff='/home/deepanshi/projects/gene_data/deepanshi_dir/'+f
    exid=defaultdict(list)
    with open (ff,'r') as f2:
        with open('/home/deepanshi/projects/mxe5/gex/'+f,'w') as f3:
            for line in f2:
                line=line.strip('\n')
                el=re.split('[,\t\s]',line)
                a=re.search('^#',el[0])
                if a:
                    id=re.split('[:]',el[0])
                    t_id=id[1]
                b=re.search("^\w",line)  
                if b:
                    if len(el)>2:
                        eid=re.split("[.:]",el[0])
                        if eid[1]!='-2':    
                            exid[t_id].append(el[0])
            d2=dict(exid)

            for i in d2:  
                f3.write("{}\t{}\t{}\n".format(i,d1[i],d2[i]))

                            
                



