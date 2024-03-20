# day 83 main File
import win32com.client 
  

speaker = win32com.client.Dispatch("SAPI.SpVoice") 
name = ['ram',"mishl","omg","dhruvish","lathiya"]  
t ="shout out , to , "
for s in name:
    speaker.Speak(t+s) 
