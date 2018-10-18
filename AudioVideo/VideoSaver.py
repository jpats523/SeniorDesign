#written by Jeremy Patterson
#this program will record the video, audio, and then put them together as one file

import numpy as np
import cv2
from time import strftime, gmtime
import time
import datetime
import pyaudio
import threading
import subprocess
import os

class VideoRecorder(): #can we start the filming at a certain seconds?

    def __init__(self,camera_number, fps):

        self.open = True
        self.fps = fps #sets the fps of the video (use this for the delays later)
        self.frameSize = (640,480) #size
        time = (strftime("%a_%d_%b_%Y_%H_%M_%S", gmtime())) #reads in the time to save
        self.name = time
        self.video_filename = time + ".avi" #file name (I want this to have the date)
        self.video_cap = cv2.VideoCapture(camera_number) #reads in the capture
        self.video_writer = cv2.VideoWriter_fourcc(*'XVID') #set the writer
        self.video_out = cv2.VideoWriter(self.video_filename, self.video_writer, self.fps, self.frameSize)
        

    def record(self): #opens up the video and starts recording. I could split this up
        self.starttime = int(time.time())
        self.framenumber = 0
        while(self.open == True): #makes sure that the recording has started
            ret, frame = self.video_cap.read()
            if ret == True:
                self.video_out.write(frame) #reads in the frame and saves it
                self.framenumber += 1#could put something here to print each time
                print(self.framenumber)
                cv2.imshow('frame',frame)# i want to make this a def later on
                if cv2.waitKey(1) & 0xFF == ord('q'): # if you push q then it stops
                    self.stop()
                #here i think we do the manual delay
                time.sleep(1/self.fps)
            else:
                break
    
    def stop(self): #this will do all the breaks/releases
        if self.open == True: #you can only close it if it it's open
            self.open = False #this closes the video stream
            self.endtime =  int(time.time())
            self.totalseconds = self.endtime - self.starttime
            self.video_out.release() # realeases the opening of a video stream
            self.video_cap.release() # releases something else???
            self.timer()
            self.information()
            cv2.destroyAllWindows() # closes out the window
        else: # I think this is here just incase it never opened?
            pass

    def start(self):
        #this create the video recording function using a thread
        video_thread = threading.Thread(target = self.record)
        video_thread.start()

    def peak(self): #this is where you would "stream" the video to the computer
        print("peaking into the video")
    
    def timer(self): #pass the duration - may have to do this a different way? the self part really isn't that important because the calculations are done after the recording
        seconds = self.totalseconds
        self.hours = int(seconds/3600)
        seconds = seconds - (self.hours *3600)
        self.minutes = int(seconds/60)
        self.seconds = seconds - (60*self.minutes)
        
        if self.minutes > 0: # there are minutes
            if self.hours > 0: #hours, minutes, seconds
                self.duration = ('Hours:' + str(hours) + ' Minutes:' + str(minutes)+ ' Seconds:' + str(seconds))
            else: #minutes, seconds
                self.duration = ('Minutes:' + str(minutes)+ ' Seconds:' + str(seconds))
        else: # only seconds
            self.duration = ('Seconds: ' + str(seconds))

    def information(self): #this just prints the properties of the video that we care about
        print(self.name)    #print the name of the video
        print(self.duration)    #print the length of the video
        stinfo = os.stat(self.video_filename)
        statinfo = stinfo.st_size
        if statinfo > 1024**3:
            statinfo = statinfo / (1024**3)
            print(str(round(statinfo,2)) + "GB")
        elif statinfo > 1024**2:
            statinfo = statinfo / (1024**2)
            print(str(round(statinfo,2)) + "MB")
        else:
            statinfo = statinfo / (1024)
            print(str(round(statinfo,2)) + "KB")

              
    
    
class AudioRecorder():
    #this will be reading from the microphone and will save the audio

    def __init__(self):

        self.open = True # used for the loop later on 
        self.rate = 44100 # not sure what this is for(sample rate?)
        self.frames_per_buffer = 1024 # 8 bit audio?
        self.channels = 2 # 2 channels for sterio?
        self.format = pyaudio.paInt16
        self.audio_filename = "temp_audio.wav" #this will be changed later
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=self.format,
                                      channels=self.channels,
                                      rate=self.rate,
                                      input=True,
                                      frames_per_buffer = self.frames_per_buffer)
        self.audio_frames = [] # not sure what this is needed for
        

    def record(self):
        #for mysself
        print("Recording.....")
        
        #this is where the audio recording gets started
        while(self.open == True): #this makes sure that the intialized open happend
            data = self.stream.read(self.frames_per_buffer) #reads in the data
            self.audio_frames.append(data) #this was the list we created
            print(data) # I want to see what is happening/ what it is reading


            if self.open == False: #not sure why they have it like this
                break

    def stop(self):
        #the stop stops, and then it writes all the data out

        if self.open == True: #can't close it if it's open
            self.open = False #closes it
            self.stream.stop_stream() #this calls itself?
            self.stream.close() #closes the stream
            self.audio.terminate() #i believe this is like destroy all windows

            waveFile = wave.open(self.audio_filename, 'wb') # this is where we are starting to write
            waveFile = setnchannels(self.channels) #this is 2 for us becuase of sterio
            waveFile.setsampwidth(self.audio.get_sample_size(self.format))
            waveFile.setframerate(self.rate)
            waveFile.writeframes(b''.join(self.audio_frames))
            waveFile.close()

        pass #why can't we do this for other parts of the code
    
    def start(self):
        #this creates the thread for the audio portion of the recording
        audio_thread = threading.Thread(target = self.record)
        audio_thread.start() # starts the thread

#def start_AVrecording(filename):
#def stop_AVrecording(filename):

            
def message(filename):
    msg = 'A new recording has finished'
    date = 'Date of the recording: ' + str(filename.name)
    name = 'The name of the of the recording: ' + str(filename.video_filename)
    duration = 'Duration of the recording: ' + str(filename.duration)
    size = 'Size of the recording: ' +str(filename.memorysize) #need to figure out what i want to call this
#USED MEMORY/ TOTAL USEABLE MEMORY (AND A PERCENTAGE)

capture = VideoRecorder(1,24)
capture.record() #this is stopped by pressing q - this should also stop the audio
#print(time + ".avi")
#noise = AudioRecorder()
#noise.record()
print("I ran")



        
