from tkinter import *
from pytube import YouTube
import os

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("DataFlair-youtube video downloader")


Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()




##enter link
link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)



#function to download video


def Downloader():
     
    url =YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210) 

    #fuction to download mp3 audio

#def MP3():

    #url = YouTube(str(link.get()))
    #MP3 = url.streams.get_audio_only()
    #MP3.download()
    
    #Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)


Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)
Button(root,text = 'MP3', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 200)


root.mainloop()
