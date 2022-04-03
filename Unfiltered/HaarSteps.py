#===========================================================================================
#Handy cmds
pwd --> to display cirrent dir
rm -r folder_path--> to delete a folder and its contents
rm file_path--> to delete a file
mkdir folder_name--> create a directory
mkdir info{1..n} --> to create n directories
cp -r source_path dest_path --> to copy a folder and its contents
ls --> list content of current directory
ls -l --> detailed list
ls -a --> list including hiddent files
ls -1 | wc -l --> counts the content of current folder.
#-------------------------------------------------------------------------------------------
Step#1: Setting up your machine
#-------------------------------------------------------------------------------------------
#Upgrad your Linux server
alem@alem-Satellite-S40-A:~$ sudo -i
[sudo] password for alem:*********
root@alem-Satellite-S40-A:~#

#Update and upgrade your environment
root@alem-Satellite-S40-A:~# sudo apt-get update
root@alem-Satellite-S40-A:~# sudo apt-get upgrade

#Create a working Directory named opencv_workspace
root@alem-Satellite-S40-A:~# mkdir opencv_workspace
root@alem-Satellite-S40-A:~# cd opencv_workspace
root@alem-Satellite-S40-A:~/opencv_workspace#  #use ls, ls -l, or ls -a to see details

# Grab and install an opencv from a github
root@alem-Satellite-S40-A:~/opencv_workspace# sudo apt-get install git
root@alem-Satellite-S40-A:~/opencv_workspace# git clone https://github.com/Itseez/opencv.git

#Install the compiler
root@alem-Satellite-S40-A:~/opencv_workspace# sudo apt-get install build-essential

#Libraries
root@alem-Satellite-S40-A:~/opencv_workspace# sudo apt-get install cmake git libgtk2.0-dev 
                            pkg-config libavcodec-dev libavformat-dev libswscale-dev

#Python bindings 
root@alem-Satellite-S40-A:~/opencv_workspace# sudo apt-get install python-dev python-numpy 
                            libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev 
                            libjasper-dev libdc1394-22-dev

#At last grab and install the OpenCV development library:
root@alem-Satellite-S40-A:~/opencv_workspace# sudo apt-get install libopencv-dev 
#-------------------------------------------------------------------------------------------
#===========================================================================================
#-------------------------------------------------------------------------------------------
Step#2: Creating the Dataset --> Walls/Negative/Background images + positive/windows images
#-------------------------------------------------------------------------------------------
==> I collected 580 different window images --> some are captured by my mobile cameras and 
    some are downloaded from the Internet. No previously publicly available created dataset 
    for windows.
==> Win images were resized to 64x64 and then converted to grayscales
==> 11600 samples of Wall or wall like images were created. I collected 1048 wall images
    from image-net.org, and the rest were created from a video captured around 
    Binghamton University scenes. They are the backgorund or negative images.
==> The 1048 images were downloaded & filtered using a python script -- downloading.py
    #https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/
==> They were resized to 128x128, and then converted to grayscales
#Organize folders and files as follows
root@alem-Satellite-S40-A:~/opencv_workspace# mkdir walls  --> for negative images
root@alem-Satellite-S40-A:~/opencv_workspace# mkdir info   --> for positive images
root@alem-Satellite-S40-A:~/opencv_workspace# mkdir data   --> for output
root@alem-Satellite-S40-A:~/opencv_workspace# cp -r /home/alem/Desktop/privacy/test/wins/*.jpg 
                                                    /root/opencv_workspace/
root@alem-Satellite-S40-A:~/opencv_workspace# ls  alem.sh  bg.txt  data  opencv  positives.vec  walls
        --data
        --info
        --opencv
        --walls
        ---wall_1.jpg ... --- wall_11600
        --winImg_1 ... --winImg_580
#Create the file descriptor
# Create a  bg.txt file that contains the list of paths of every negative/wall image
#Here is the python method used to create the bg.text file that contains something like (11600 entries):
       walls/wall_8795.jpg
       walls/wall_2761.jpg
       ...
       walls/wall_9052.jpg
       walls/wall_706.jpg
 
import os

def create_descriptor():
    for file_type in ['walls']:        
        for img in os.listdir(file_type):
            if file_type == 'walls':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f: #appends every line
                    f.write(line)

create_descriptor()

# Break the bg.txt files into 580 subsets (one for each win image)
    bg_1.txt (contains 20 random walls/wall_8795.jpg ...)
    ...
    bg_11600.txt
#Break bg.txt into 580 sets           
lines=[]            
def break_descriptor():  
    with open("bg.txt", "r") as ins:
        lines = []
        for line in ins:
            lines.append(line)
    k=0
    for i in range(1,581):	
        name='bg_'+str(i)+'.txt' #bg_1, ..., bg_11600
        for j in range(20):
            line2 = lines[k]		
            with open(name,'a') as f:
                f.write(line2)            
            k+=1
            print("k=",k)

break_descriptor()

#Create 580 info1 to info580 folders in the workspace
root@alem-Satellite-S40-A:~/opencv_workspace# mkdir info{1..580}

#Created the set of positive samples totalling 11600=580x20
 That is, every winImg is expanded to 20 images by sumperimposing it onto 20 different
 wall images through position and color transformations. Then, 580 window images multiplied
 by 20 becomes 11600 positive images. The 580 window images are dirrent in shape, appearance, 
 color, style, size, etc!

# A python and bash shell scripts were employed to create samples for the 580win objects
#Python script
--> The opencv_createsamples creates positive samples for obe window image only
opencv_createsamples -img winImg_1.jpg -bg bg.txt -info info/info.lst -pngoutput info 
   -maxxangle 0.3 -maxyangle 0.3 -maxzangle 0.3 -num 11600
--> Then, a python script was used to create 580 such lines cos I have 580 different win images

import os
def create_positives(): 
    for file_type in ['wins']:
        k=1	
        for img in os.listdir(file_type):
            if file_type == 'wins':
                line ='\topencv_createsamples -img '+img+' -bg '+'bg_'+str(k)+'.txt -info 
                       info'+str(k)+'/info'+str(k)+'.lst -pngoutput info -maxxangle 0.3 
                       -maxyangle 0.3 -maxzangle 0.3 -num 20 \\n'+'\n' 
                #print()
                with open('cmd.txt','a') as f:
                    f.write(line)
            k+=1

create_positives()

# Sample out ...
 opencv_createsamples -img WinImg_579.jpg -bg bg_1.txt -info info1/info1.lst -pngoutput info 
     -maxxangle 0.3 -maxyangle 0.3 -maxzangle 0.3 -num 20 \n
 opencv_createsamples -img WinImg_508.jpg -bg bg_2.txt -info info2/info2.lst -pngoutput info 
     -maxxangle 0.3 -maxyangle 0.3 -maxzangle 0.3 -num 20 \n
 opencv_createsamples -img WinImg_507.jpg -bg bg_3.txt -info info3/info3.lst -pngoutput info 
     -maxxangle 0.3 -maxyangle 0.3 -maxzangle 0.3 -num 20 \n
	...
#To create the samples, use a shell script or simply copy the 580 lines and paste them on 
# root terminal being in the opencv_workspace
root@alem-Satellite-S40-A:~/opencv_workspace#  opencv_createsamples ..(all 580 full lines)
#Bash shell script --> alem.sh
#!/bin/bash

for ((n=0;n<5;n++))
do
  opencv_createsamples -img WinImg_579.jpg -bg bg_1.txt -info info1/info1.lst -pngoutput info 
     -maxxangle 0.3 -maxyangle 0.3 -maxzangle 0.3 -num 20 \n
 opencv_createsamples -img WinImg_508.jpg -bg bg_2.txt -info info2/info2.lst -pngoutput info 
     -maxxangle 0.3 -maxyangle 0.3 -maxzangle 0.3 -num 20 \n
 opencv_createsamples -img WinImg_507.jpg -bg bg_3.txt -info info3/info3.lst -pngoutput info 
     -maxxangle 0.3 -maxyangle 0.3 -maxzangle 0.3 -num 20 \n
	...

done
root@alem-Satellite-S40-A:~/opencv_workspace# chmod u+x alem.sh
root@alem-Satellite-S40-A:~/opencv_workspace# ./alemsh
#At the end of this stage your working directory should look like the following:
root@alem-Satellite-S40-A:~/opencv_workspace#
        --alem.sh
        --bg.txt
        --bg_1.txt
           ...
        --bg_580.txt
        --data
        --info
        --info1
        ---0001_0024_0034_0053_0053.jpg
                ...
        ---0020_0038_0011_0054_0054.jpg
        ---info1.lst
            ...
        --info580
        ---0001_0016_0010_0038_0038.jpg
                ...
        ---0020_0036_0014_0036_0036.jpg
        ---info580.lst
        --opencv
        --walls
        ---wall_1.jpg ... --- wall_11600
        --winImg_1 
            ... 
        --winImg_580
#After creating 20 positive samples images for every window image, 580 sets each containing
#20 samples, they are merged into a single info folder and info.lst using a python script.
#There are 580 info1 to info580 folders, each containing 20 created sample.Positives and the 
#corresponding lists (info1.lst to info580.lst)       
root@alem-Satellite-S40-A:~/opencv_workspace/info#ls -1 | wc -l //count files in info=11601
#Remember to use cd and cd .. to navigate downward & upward (or back and forth)
# Now the workspace looks as ensues:
root@alem-Satellite-S40-A:~/opencv_workspace# ls alem.sh  bg.txt  data  info  opencv  walls
        --alem.sh
        --bg.txt        
        --data
        --info
        ---00001_0024_0034_0053_0053.jpg
                ...        
                ...
        ---11600_0036_0014_0036_0036.jpg
        ---info.lst
        --opencv
        --walls
        ---wall_1.jpg 
             ... 
             ...
        ---wall_11600.jpg
        --winImg_1 
            ... 
            ...
        --winImg_580
#The content of the info.lst looks like
  Img #  X    Y   X-Dis Y-Dis   #  X Y  X  Y
  00001_0024_0034_0053_0053.jpg 1 24 34 53 53
  00002_0084_0074_0027_0027.jpg 1 84 74 27 27
  00003_0024_0056_0030_0030.jpg 1 24 56 30 30
       ...
       ...
  11599_0026_0032_0065_0065.jpg 1 26 32 65 65
  11600_0036_0014_0036_0036.jpg 1 36 14 36 36
#-------------------------------------------------------------------------------------------
#===========================================================================================
#-------------------------------------------------------------------------------------------
Step#3: Creating the required one vector file for the positive images
#-------------------------------------------------------------------------------------------
# We have already created the sample positive images. Now, we have to create the corresponding
# vector file. All names and psoitions of the positive images are stitched together in this
# vector file, which is once again cretaed as ensues using the opencv_createsamples command.
root@alem-Satellite-S40-A:~/opencv_workspace# opencv_createsamples -info info/info.lst -num 
                                              11600 -w 64 -h 64 -vec positives.vec
# Results
root@alem-Satellite-S40-A:~/opencv_workspace# opencv_createsamples -info info/info.lst -num 11600 
                                            # -w 64 -h 64 -vec positives.vec
Info file name: info/info.lst
Img file name: (NULL)
Vec file name: positives.vec
BG  file name: (NULL)
Num: 11600
BG color: 0
BG threshold: 80
Invert: FALSE
Max intensity deviation: 40
Max x angle: 1.1
Max y angle: 1.1
Max z angle: 0.5
Show samples: FALSE
Width: 64
Height: 64
Create training samples from images collection...
Done. Created 11600 samples

root@alem-Satellite-S40-A:~/opencv_workspace# ls 
#alem.py alem.sh  bg.txt  data  info  opencv  positives.vec  walls
        --alem.py
        --alem.sh
        --bg.txt        
        --data
        --info
        ---00001_0024_0034_0053_0053.jpg
                ...        
                ...
        ---11600_0036_0014_0036_0036.jpg
        ---info.lst
        --opencv
        --positives.vec 
        --walls
        ---wall_1.jpg 
             ... 
             ...
        ---wall_11600.jpg
        --winImg_1 
            ... 
            ...
        --winImg_580
#-------------------------------------------------------------------------------------------
#===========================================================================================
#-------------------------------------------------------------------------------------------
Step#4: Training the samples
#opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 10000 -numNeg 5800 -numStages 20 -w 64 -h 64
#-------------------------------------------------------------------------------------------
root@alem-Satellite-S40-A:~/opencv_workspace# opencv_traincascade -data data -vec positives.vec 
                           -bg bg.txt -numPos 11600 -numNeg 5800 -numStages 20 -w 64 -h 64
# The vector file is preced by a data folder where we want the output to be saved.
# The background file (bg.txt) gives info about the paths of negative images.
# -numPos tells how many positive images are needed to be trained --> use less than max#
# -numNeg tells the number negative images to be considered for the training 
# -numSatges refers to the cascade stages. Employ significantly less numPos than you have to
# make room for the stages.
# -w & -h are width and height.
# This allows the command to continue running, even after the terminal has been closed. 
 root@alem-Satellite-S40-A:~/opencv_workspace# nohup opencv_traincascade -data data -vec 
                                              positives.vec -bg bg.txt -numPos 11600 -numNeg 900 
                                              -numStages 25 -w 64 -h 64 &

#-------------------------------------------------------------------------------------------
#===========================================================================================
#References
#https://stackoverflow.com/questions/16058080/how-to-train-cascade-properly
#https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/

#===========================================================================================
#===========================================================================================
#===========================================================================================
#===========================================================================================
#===========================================================================================
