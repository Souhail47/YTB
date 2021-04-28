from tkinter import *
#standard GUI(graphical user interface library).
from pytube import YouTube
#used to download videos from youtube
root = Tk()
#setting the name for the window
root.geometry("1300x1050")
#set a fixed size for the window
root.title("Youtube Video Downloader")
#gives a title de the window
Label(root,text = 'Youtube Video Downloader', font =('Times New Roman',20)).pack()
#displays a text
link = StringVar()
#stores the video link
Label(root, text = 'Paste Link Here:', font = ('Times New Roman',15)).place(x= 560 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 370, y = 90)
#entry is used to create an input text field
def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = ('Times New Roman',15),bg='green').place(x= 770 , y = 150)  
Button(root,text = 'DOWNLOAD', font = ('Times New Roman',15) ,bg = 'red',  command = Downloader).place(x=565 ,y = 150)
root.mainloop()
#a method to excute the program