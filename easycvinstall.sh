#this should pip install opencv
#https://www.pyimagesearch.com/2018/09/19/pip-install-opencv/

#dependencies
sudo apt-get install libhdf5-dev libhdf5-serial-dev -y 
sudo apt-get install libqtwebkit4 libqt4-test -y

#this gets us pip
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py -y

#this installs opencv
sudo pip install opencv-contrib-python

#this brings in the picamera function
pip install "picamera[array]"
