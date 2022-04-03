#https://www.instructables.com/id/Create-OpenCV-Image-Classifiers-Using-Python/
#opencv_createsamples -img watch5050.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1950
#opencv_createsamples -img watch5050.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 20

import os
#Create the file descriptor
def create_descriptor():
    for file_type in ['wall_gray']:        
        for img in os.listdir(file_type):
            if file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat','a') as f:
                    f.write(line)
            elif file_type == 'wall_gray':
                line = file_type+'/'+img+'\n'
                with open('wg.txt','a') as f:
                    f.write(line)

create_descriptor()
#Break bg.txt into 580 sets           
lines=[]            
def break_descriptor():  
    with open("wg.txt", "r") as ins:
        lines = []
        for line in ins:
            lines.append(line)
    k=0
    for i in range(1,581):	
        name='wg_'+str(i)
        for j in range(20):
            line2 = lines[k]		
            with open(name,'a') as f:
                f.write(line2)		
            k+=1
            print("k=",k)

break_descriptor()
#create the 
def create_positives(): 
    for file_type in ['wins_gray']:
        k=1	
        for img in os.listdir(file_type):
            if file_type == 'wins_gray':
                line = 'opencv_createsamples -img '+img+' -bg '+'wg_'+str(k)+'.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 20\n'
                with open('cmd.txt','a') as f:
                    f.write(line)
            k+=1

create_positives()