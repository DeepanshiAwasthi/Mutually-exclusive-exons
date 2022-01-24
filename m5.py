import os 
import re
from collections import defaultdict
path='/home/deepanshi/projects/mxe5/gex'
files = os.listdir(path)
names=[]
for f in files:
    ff='/home/deepanshi/projects/mxe5/gex/'+f
    count = 0
    print(ff)
    for line in open(ff): count += 1
    print(count,f)
    if int(count)>1:
        with open (ff,'r') as f1:       
            d1={}
            d2={}
            d3={}
            elen=0
            l=0
            list1=[]
            for line in f1:
                line=line.strip('\n')
                el=re.split('\t',line)
                t_id=el[0]
                l=el[1]
                ex=re.split(',',el[2])
                elen=len(ex)
                d1.update({t_id:int(l)})
                d2.update({t_id:int(elen)})
                d3.update({t_id:el[2]})
            for i in d1:
                l1=set()
                llist1=[]
                llist1=re.split(',',d3[i])
                for j in d1:
                    l2=set()
                    llist2=[]
                    list1.append(i)
                    if j not in list1:
                        if d1[i]-d1[j]>-11 and d1[i]-d1[j]<11:
                            llist2=re.split(',',d3[j])
                            #print(llist2)
                            with open('/home/deepanshi/projects/mxe5/gex4/'+f,'a') as f2: 
                                llen1=len(llist1)
                                llen2=len(llist2)  
                                f2.write("{}\t{}\t{}\t{}\n".format(i,d1[i],d3[i],llen1-llen2))                
                                f2.write("{}\t{}\t{}\t{}\n\n".format(j,d1[j],d3[j],llen2-llen1))
                            
                          
    else:
        exit                                
                                    
                                

                                            


                                        
