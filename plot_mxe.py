import matplotlib.pyplot as plt
import re
import numpy as np
N=15
ind=np.arange(N)
width = 0.4
plt.rcParams.update({'font.size':14})
xvals=[]
yvals=[]
zvals=[]

with open('/home/deepanshi/projects/mxe5/m6.txt','r') as f1:
    a=0
    for line in f1:
        a=a+1
        if a>1:
            el=re.split('\t',line)
            xvals.append(int(el[0]))
            yvals.append(int(el[1]))
            zvals.append(int(el[2]))

fig, ax = plt.subplots()            
bar1 = ax.bar(ind-width/2, yvals, width, color = 'magenta')
bar2 =ax.bar(ind+width/2, zvals, width, color='cyan')

ax.set_xlabel('Difference in number of coding exons')
ax.set_ylabel('Frequency')
ax.set_xticks(ind) 
ax.set_xticklabels(xvals)
ax.set_title('Variation in the coding exon count among transcript pairs of approximate similar length (+/- 10 a.a.)')
ax.legend( (bar1, bar2), ('Number of genes','Number of transcript pairs') )
ax.bar_label(bar1, padding=3,fontsize=10) 
ax.bar_label(bar2, padding=3,fontsize=10) 
plt.show()
