from noti import notiyi
import os 
import time

NowTime = int(time.strftime("%H"))
print(NowTime,type(NowTime))

def MyWork():
    if NowTime == 7:
        notiyi(NowTime,"Good MOring")
    if NowTime == 8 or NowTime==10 or NowTime==12 or NowTime==14 or NowTime==16 or NowTime==18 or NowTime==20 :
        notiyi(NowTime,"Dring a Woter")

    if NowTime==8 or NowTime==12 or NowTime==19:
        notiyi(NowTime,"Eating")

    if NowTime== 22:
        notiyi(NowTime,"Good Ninght")

MyWork()
# notiyi(NowTime,MyWork)