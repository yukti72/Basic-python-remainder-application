#start by importing modules
import time
import webbrowser
from playsound import playsound

#now, set the remainder for required website
Set_alarm=input('Set Remainder at HH:MM:SS: ')
url=input('Enter the link to your website: ')


#referring it to the selected time
actual_time=time.strftime('%I:%M:%S')

while(actual_time!=Set_alarm):
    print('The time is:'+ actual_time)
    actual_time=time.strftime('%I:%M:%S')
    time.sleep(1)

if(actual_time==Set_alarm):
    print("Your time you visit website is up!")
    playsound('C:/Users/yukti singh/Documents/attendance project using ml/beep-09.mp3')


    webbrowser.open(url)
    


