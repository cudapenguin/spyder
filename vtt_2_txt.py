# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 00:03:26 2022

@author: Chris Liu
"""

f=open('C:/Users/Chris Liu/spyder/partC.vtt')
lines=f.readlines()
print(lines[2:10])
f.close()

header=lines[:2]

vtt_lines=lines[2:]

timestamps=[]
subtitles=[]
isTime=True
line_labels=[]
line_count=0
for l in vtt_lines:   
    line=l.strip('\n')
    if (line_count%4==0):
        line_labels.append(l)
    if (line_count%4==1):
        timestamps.append(l)
    if (line_count%4==2):
        subtitles.append(l)
    line_count+=1


outf=open('C:/Users/Chris Liu/spyder/output.txt','w')

for sub in subtitles:
    outf.write(sub+'\n')
     
outf.close()