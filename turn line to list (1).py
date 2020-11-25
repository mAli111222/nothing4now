import random
import datetime
import time
import pyttsx3
list1 = []
engine = pyttsx3.init()

#first I need to open nounslist
#then I need to split it
#then I need to put it in an array
#then I need to loop the array to print out random lines
file = open('nounslist.txt', 'r')

reading = file.read()

splitlines = reading.split('\n')

print(splitlines)

random.shuffle(splitlines)

print(splitlines)

#num = random.randint(0,len(splitlines))

#print(num)

#print(splitlines[num])
istrue = True





hour = input('what hour : ')
minute = input('what minute : ')
while istrue:
    
    timenow = datetime.datetime.now()

    nowHour = timenow.strftime("%H")
    nowMin = timenow.strftime("%M")

    print(nowHour)
    print(nowMin)

        
    num = random.randint(0,len(splitlines)-1)
    print(splitlines[num])
    word = str(splitlines[num])
    engine.say('yab likes' + word)
    engine.runAndWait()
    time.sleep(5)
    if minute == nowMin and hour == nowHour :
        istrue = False












