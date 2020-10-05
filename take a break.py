#---------------------------------Take A Break----------------------
import webbrowser
import time
i=0
print("this program started " +time.ctime())#current time
while(i<3):
    time.sleep(10)#for program to wait
    webbrowser.open("https://www.youtube.com/watch?v=pv6W3RJB918")#open webbrowser to play video
    i+=1
#press ctrl+c to stop it



#webbrowser documentation link ----https://docs.python.org/3/library/webbrowser.html
#time documentation link ----- https://docs.python.org/3/library/time.html   
