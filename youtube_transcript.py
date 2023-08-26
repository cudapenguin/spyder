# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 23:49:15 2022

@author: Chris Liu
"""

#f=open('C:/Users/Chris Liu/spyder/rain.txt')
f=open('C:/Users/Chris Liu/spyder/transcript.txt')
lines=f.readlines()
print(lines[:10])
f.close()

lines_to_include=lines[1:]

timestamps=[]
subtitles=[]
isTime=True
for l in lines_to_include:
    line=l.strip('\n')
    #print(line)
    if (isTime):
        timestamps.append(line)
        isTime=False
    else:
        subtitles.append(line)
        isTime=True

timestrings=[]
for i in range(len(timestamps)):
    t=timestamps[i]
    m,s=t.split(':')
    if len(m)==1:m='0'+m
    startt=f"00:{m}:{s}"
        
    nexti=i+1
    if (nexti==len(timestamps)):
        continue
    else:
        nextt=timestamps[nexti]
#        print(nextt)
        m,s=nextt.split(':')
        if len(m)==1:m='0'+m
        endt=f"00:{m}:{s}"  
    timestrings.append(f"{startt},000 --> {endt},000")
   

srtf=open('C:/Users/Chris Liu/spyder/video.srt','w')

linum=1
for sub,time in zip(subtitles,timestrings):
    srtf.write(str(linum)+'\n')
    srtf.write(time+'\n')
    srtf.write(sub+'\n')
    srtf.write('\n')
    linum+=1

srtf.close()