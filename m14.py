import re
from collections import defaultdict
ll=[1,2,3,4,5,6,7,8,10]
d={}
with open('/home/deepanshi/projects/fasta_files.txt','r') as f1:
    for line in f1:
        line=line.strip('\n')
        el=re.split('\t',line)
        tid=el[0][1:]
        #print(el[1])
        d.update({tid:el[1]})
for i in ll:
    with open('var_fre_'+str(i),'w') as f3:
        with open('var_count_'+str(i),'w') as f2:
            with open('var_fcount_'+str(i),'w') as f4:
                d1=defaultdict(list)
                dd1=defaultdict(list)
                d2={}
                dd2={}
                with open ('c_'+str(i)+'_var','r') as f1:
                    for line in f1:
                        line=line.strip('\n')
                        el=re.split('\t',line)
                        c=el[2]
                        #print(c)
                        el1=re.split('[:;]',el[0])
                        tid=el1[1]
                        l=len(d[tid])
                        #print(tid,l)
                        f3.write("{}\t{}\t{}\n".format(line,l,round(int(c)/l,2)))
                        d1[int(c)].append(1)
                        gp=round(int(c)/l,1)
                        dd1[round(gp*100,0)].append(1)
                d2=dict(d1)
                dd2=dict(dd1)
                for ii in sorted(d2.keys()):
                    f2.write("{}\t{}\n".format(ii,len(d2[ii])))    
                for iii in sorted(dd2.keys()):
                    f4.write("{}\t{}\n".format(int(iii),len(dd2[iii])))        
