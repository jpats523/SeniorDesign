#!/bin/bash

#this script will create a copy a zip of the image for distrobution
#must run with sudo

#removing the zipped image if there is one
rm -r /home/Jeremy/CustomImage/WearableHeadset.zip

#create a copy to the right location
echo "Creating a copy of the image on the SD card [1/5]"
dd if=/dev/sdd of =/home/Jeremy/CustomImage/clone.img

wait(2000) #wait for 2 seconds

#shrinks the file down - renames it
echo "Shrinking the image on the SD card [2/5]"
pishrink.sh /home/Jeremy/CustomImage/clone.img /home/Jeremy/CustomImage/WearableHeadset.img

wait(2000) #wait for 2 seconds

#remove clone.img
echo "Removing unshrunk image of SD card [3/5]"
rm /home/Jeremy/CustomImage/clone.img

wait(2000) #wait for 2 seconds

#then we are going to zip up the file
echo "Zipping custom image [4/5]"
gzip -9 /home/Jeremy/CustomImage/WearableHeadset.img

wait(2000) #wait for 2 seconds

#remove the unzipped image
echo "Removing unzipped image [5/5]"
rm /home/Jeremy/CustomImage/WearableHeadset.img

wait(2000) #wait for 2 seconds
