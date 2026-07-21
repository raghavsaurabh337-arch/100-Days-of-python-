import time
t=time.strftime('%H:%M:%S')

hour=int(time.strftime('%H'))
if(hour>=0 and hour<12):
     print("Good Morning!")
elif(hour>=12 and 17>hour):
     print("Good Afternoon!")
elif(hour>=17 and 21>hour):
     print("Good Evening!")
else:
     print("Good Night!")
