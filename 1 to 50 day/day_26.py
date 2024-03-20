import time
# h=int(time.strftime('%H'))
m=int(time.strftime('%M'))
h=18


if h>2 and h<12:
    print("Good moring")
elif h>12 and h<17:
    print("Good After")
else:
    print("Good Night .....!")
