import re
from collections import defaultdict
d={}
with open('/home/deepanshi/projects/fasta_files.txt','r') as f1:
    for line in f1:
        line=line.strip('\n')
        el=re.split('\t',line)
        tid=el[0][1:]
        #print(el[1])
        d.update({tid:el[1]})
l1=[0]    
for i in l1:
    ll={}
    with open('c_'+str(i)+'_var','w') as f2: 
        with open('c_'+str(i)+'_tra','r') as f3:  
            for line in f3:
                res=[]
                count=0
                line=line.strip('\n')
                el=re.split('[;:]',line)
                tr1=el[1]
                tr2=el[2]
                seq1=d[tr1]
                seq2=d[tr2]
                for i1, j1 in zip(range(0,len(seq1)), range(0,len(seq2))):
                    #print(seq1[i1],seq2[j1])
                    if seq1[i1]==seq2[j1]:
                        count=count
                    else:
                        count=count+1
                        res.append(str(i1)+";"+seq1[i1]+':'+seq2[j1])  
                if res:    
                    ll.update({line:res})            
        for jk in ll:
            f2.write("{}\t{}\t{}\n".format(jk,ll[jk],len(ll[jk])))
    print (i)        

      