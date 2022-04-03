#https://www.instructables.com/id/Create-OpenCV-Image-Classifiers-Using-Python/
#opencv_createsamples -img watch5050.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1950
#opencv_createsamples -img watch5050.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 20

import os
#Create the file descriptor
def create_descriptor():
    for file_type in ['walls']:        
        for img in os.listdir(file_type):
            if file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat','a') as f:
                    f.write(line)
            elif file_type == 'walls':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)

create_descriptor()
#Break bg.txt into 580 sets           
lines=[]            
def break_descriptor():  
    with open("bg.txt", "r") as ins:
        lines = []
        for line in ins:
            lines.append(line)
    k=0
    for i in range(1,581):	
        name='bg_'+str(i)+'.txt'
        for j in range(20):
            line2 = lines[k]		
            with open(name,'a') as f:
                f.write(line2)            
            k+=1
            print("k=",k)

break_descriptor()
#create the import os
def create_positives(): 
    for file_type in ['wins']:
        k=1	
        for img in os.listdir(file_type):
            if file_type == 'wins':
                line ='\topencv_createsamples -img '+img+' -bg '+'bg_'+str(k)+'.txt -info info'+str(k)+'/info'+str(k)+'.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 20 \\n'+'\n' 
                #print()
                with open('cmd.txt','a') as f:
                    f.write(line)
            k+=1

create_positives()


#create the import os
def create_sudos(): 
    k=1
    for i in range(1,581):
        #line='sudo chmod 777 /home/alem/Desktop/privacy/test/allinfo/info'+str(k)+'/*.jpg'+'\n'
        line='sudo chmod 777 /home/alem/Desktop/privacy/test/allinfo/info'+str(k)+'/*.lst'+'\n'
        with open('lst.txt','a') as f:
            f.write(line)
        k+=1

create_sudos()



#create the import os
def create_sn(): 
    k=1
    for i in range(1,11601):
        #line='sudo chmod 777 /home/alem/Desktop/privacy/test/allinfo/info'+str(k)+'/*.jpg'+'\n'
        if k<10:
            line='0000'+ str(k)+'\n'
        elif k>=10 and k<100:
            line='000'+ str(k)+'\n'
        elif k>=100 and k<1000:
            line='00'+ str(k)+'\n'
        elif k>=1000 and k<10000:
            line='0'+ str(k)+'\n'
        else:
            line=str(k)+'\n'
        with open('sn.txt','a') as f:
            f.write(line)
        k+=1

create_sn()

f"{1:02d}
a='Hello\\tWorld\\nHello World\n'
print(repr(a))