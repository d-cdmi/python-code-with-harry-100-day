from moviepy.editor import *

# s = int(input("Enter of Start on Minuts :\n"))
# sf = float(input("Enter of Start Second :\n"))
# e = int(input("Enter of end  Minuts :\n"))
# ef = float(input("Enter of end  Second :\n"))


s  = 0
sf = 0
e  =5
ef =52




clip = VideoFileClip('Test_video.mp4')
clip1 = clip.subclip((s,sf),(e,ef))
clip1.write_videofile('1.mp4',codec='libx264')