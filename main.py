#import os
#import time
#import playsound

import GMMTesting
import GMMTraining
import sounddevice
from scipy.io.wavfile import write
from commands import getoutput as gt
import recognition
import preprocessing
import time

threshold =  0.63
def record(Name, Range, Path,second) :
    sr =44100
    if Range == 10 :
        record_voice=sounddevice.rec(int(second * sr),samplerate=sr,channels=2)
        sounddevice.wait()
        fname=Name
        write(fname,sr,record_voice)
        return
    
    for i in range(Range) : 
		record_voice=sounddevice.rec(int(second * sr),samplerate=sr,channels=2)
		sounddevice.wait()
		fname=Name+str(i+1)+".wav"
        
		write(fname,sr,record_voice)

if __name__ == "__main__":
    
    print("Select Option:\n1. Sign In\n2. Sign Up\n3. Change Password")
    a=int(input())
    if(a == 1) :
        print "press 1 to give passcode"
        input()
        record("temp" , 1 , "",8)
        print("Recording Done")
        name = GMMTesting.testSingleaudio("temp1.wav")
        preprocessing.start("temp1.wav")

        corr1   = recognition.start('temp1.wav'  , "PasswordData/"+name+"/"+name+"1.wav")
        corr2   = recognition.start('temp1.wav'  , "PasswordData/"+name+"/"+name+"2.wav")
        corr3   = recognition.start('temp1.wav'  , "PasswordData/"+name+"/"+name+"3.wav")
        corr4   = recognition.start('temp1.wav'  , "PasswordData/"+name+"/"+name+"4.wav")
        corr5   = recognition.start('temp1.wav'  , "PasswordData/"+name+"/"+name+"5.wav")
        
        confirm=0
        confirm=corr1+corr2+corr3+corr4+corr5
        if confirm > 2 :
            print "Hello " + name+ ", you are successfully authenticated."
        else :
            print ("Hello "+ name + ", your audio password does not match with the database.")
            
        gt("rm temp1.wav")
        
        
    elif (a == 2) :
        print("Enter your Name : ")
        name = raw_input()
        path = "TrainingData/" + name
        gt("mkdir %s" %(path))
        
        print("We will take 5 sample. Press 1 to start recording")
        input()
        
        record(name , 5 , path,6)
        
        for i in range(5) :
            fname=name+str(i+1)+".wav"
            gt("mv %s %s" %(fname , path))        
        # GMMTraining.GMMModels('TrainingData/' , 'GMMModels')
        GMMTraining.singleModelTraining(path,'GMMModels')
        print "press 1 to give passcode"
        input()
        passpath = "PasswordData/"+name
        gt("mkdir %s" %(passpath))
        
        #saving passcord after preprocessing
        print "give pass duration:"
        dur = int(input())
        
        time.sleep(1)
        print "Go"
        record(name + '1.wav',10,passpath,dur)
        preprocessing.start(name+"1.wav")
        gt("mv %s %s" %(name+"1.wav" , passpath))
        
        print "Done"
        time.sleep(1)
        print "Go"
        record(name + '2.wav',10,passpath,dur)
        preprocessing.start(name+"2.wav")
        gt("mv %s %s" %(name+"2.wav" , passpath))
        
        print "Done"
        time.sleep(1)
        print "Go"
        record(name + '3.wav',10,passpath,dur)
        preprocessing.start(name+"3.wav")
        gt("mv %s %s" %(name+"3.wav" , passpath))
        print "Done"

        time.sleep(1)
        print "Go"
        record(name + '4.wav',10,passpath,dur)
        preprocessing.start(name+"4.wav")
        gt("mv %s %s" %(name+"4.wav" , passpath))
        
        print "Done"
        time.sleep(1)
        print "Go"
        record(name + '5.wav',10,passpath,dur)
        preprocessing.start(name+"5.wav")
        gt("mv %s %s" %(name+"5.wav" , passpath))  

    elif a==3:
        print("Enter your Name : ")
        name = raw_input()
        passpath = "PasswordData/"+name
        print "give pass duration:"
        dur = int(input())
        
        time.sleep(1)
        print "Go"
        record(name + '1.wav',10,passpath,dur)
        preprocessing.start(name+"1.wav")
        gt("mv %s %s" %(name+"1.wav" , passpath))
        
        print "Done"
        time.sleep(1)
        print "Go"
        record(name + '2.wav',10,passpath,dur)
        preprocessing.start(name+"2.wav")
        gt("mv %s %s" %(name+"2.wav" , passpath))
        
        print "Done"
        time.sleep(1)
        print "Go"
        record(name + '3.wav',10,passpath,dur)
        preprocessing.start(name+"3.wav")
        gt("mv %s %s" %(name+"3.wav" , passpath))
        print "Done"

        time.sleep(1)
        print "Go"
        record(name + '4.wav',10,passpath,dur)
        preprocessing.start(name+"4.wav")
        gt("mv %s %s" %(name+"4.wav" , passpath))
        
        print "Done"
        time.sleep(1)
        print "Go"
        record(name + '5.wav',10,passpath,dur)
        preprocessing.start(name+"5.wav")
        gt("mv %s %s" %(name+"5.wav" , passpath))



