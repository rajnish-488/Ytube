from pytube import YouTube
from playsound import playsound
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import io
import os


class youtube:

    def __init__(self,root):
        self.root = root
        self.root.geometry("655x450")
        self.root.title("YOUTUBE VIDEO DOWNLOADER")
        self.root.configure(bg = "lightyellow")
        self.root.resizable(False, False) 

        self.l1=Label(self.root, text = "    YOUTUBE VIDEO DOWNLOADER | BY R.S JANWER     ", font = "Verdana 15 bold" ,bg = "black",foreground = "white" )
        self.l1.place(x=10, y=0)
        self.l2=Label(self.root, text = "   DOWNLOAD LINK   ", font = "Verdana 15 bold" ,bg = "red",foreground = "blue" )
        self.l2.place(x=10, y = 35)
        self.l3=Label(self.root, text = "  CHANGE FILE NAME ", font = "Verdana 15 bold" ,bg = "red",foreground = "blue" )
        self.l3.place(x=10, y = 70)

        self.link = Entry(master = self.root, width = 60 ,bd = "5 pixels")
        self.link.place(x=270, y = 35)
        self.name = Entry(master = self.root, width = 60 ,bd = "5 pixels")
        self.name.place(x=270, y = 70)

# 1 for 720p, 2 for 360p and , 3 for 240p 
        self.var = IntVar()   #variable for radio button
        self.R1 = Radiobutton(self.root, text="720p", variable=self.var, value=1).place(x=20,y=110)

        self.R2 = Radiobutton(self.root, text="360p", variable=self.var, value=2).place(x=100,y=110)

        self.R3 = Radiobutton(self.root, text="240p", variable=self.var, value=3).place(x=180,y=110)


        self.serch = Button(self.root, text="SERCH VIDEO" ,command = self.serch, bg = "blue",height = 1,fg='yellow',width = 20).place(x=400,y=110)

        self.frame1 = Frame(self.root, bd =2,relief = RIDGE, bg="lightyellow" )
        self.frame1.place(x =10 , y=140,height = 200, width = 637)

        self.f1=Label(self.frame1, text = " YOUTUBE VIDEO TITLE  ", font = "Verdana 15 bold" ,bg = "black",foreground = "white" )
        self.f1.place(x=0, y=0 ,width = 635)

        self.f2=Label(self.frame1, text = " VIDEO  \nIMAGE  ", font = "Verdana 15 bold" , bg = "white", foreground = "black")
        self.f2.place(x=5, y=35 ,width = 300,height=157)

        self.f3=Text(self.frame1, font = "Verdana 8 bold" ,bg = "green",foreground = "black" ) 
        self.f3.place(x=310, y=65 ,width = 317,height=127)

        self.f4=Label(self.frame1, text = " DESCRIPTION  ", font = "Verdana 15 bold" ,bg = "yellow",foreground = "green" )
        self.f4.place(x=310, y=35 ,width = 317,height=25)

        self.size=Label(self.root, text = "SIZE: 00mb", font = "Verdana 15 bold" ,bg = "lightyellow",foreground = "black" )
        self.size.place(x=10, y=350)

        self.down=Label(self.root, text = "DOWNLOADED 00%", font = "Verdana 15 bold" ,bg = "lightyellow",foreground = "black" )
        self.down.place(x=180, y=350)

        self.download = Button(self.root, text="DOWNLOAD" ,command = self.download, bg = "blue",height = 1,fg='yellow',width = 20).place(x=495,y=350,height = 30,width = 150)
        self.clear = Button(self.root, text="CLEAR" ,command = self.clearall, bg = "grey",height = 1,fg='black',width = 20).place(x=433,y=350,height = 30,width = 60)

        self.prog = ttk.Progressbar(self.root, orient = HORIZONTAL, length = 637, mode = 'determinate')
        self.prog.place(x=10, y =390)

        self.error=Label(self.root, text ="  MESSEAGE  ", font = "Verdana 15 bold" ,bg = "black",foreground = "white" )
        self.error.place(x=10, y=415,width = 527)
        
        self.images=Image.open('p.png')
        self.images = self.images.resize((102 ,31), Image.ANTIALIAS)
        self.images = ImageTk.PhotoImage(self.images)

        self.logo=Label(self.root, bg = "blue", image = self.images).place(x=545, y=415,width = 102, height = 31)
  
        
       


        self.root.mainloop()

    def serch(self):
        playsound('click.mp3')
        try:
            y = YouTube(self.link.get())
        except:
            messagebox.showerror("ERROR", "VIDEO NOT AVALABLE")
    #video720p = y.streams.filter(progressive = True, file_extension = "mp4", res = "720p").first()
    #video360p = y.streams.filter(progressive = True, file_extension = "mp4", res = "360p").first()
    #video240p = y.streams.filter(progressive = True, file_extension = "mp4", res = "240p").first()  
        self.f1.config(text = y.title, font = "Verdana 8 bold" )  #give title
    # chage image 
        response = requests.get(y.thumbnail_url)
        img_byte = io.BytesIO(response.content)
        img=Image.open(img_byte)
        img1 = img.resize((300 ,157), Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(img1)
        self.f2.config(image = img2)
        print("done")
    # description
        self.f3.delete('1.0',END)
        self.f3.insert(END,y.description[:2000])
    # size of data
        if self.var.get()== 1:
            select = y.streams.filter(progressive = True, file_extension = "mp4", res = "720p").first()
        if self.var.get()== 2:
            select = y.streams.filter(progressive = True, file_extension = "mp4", res = "360p").first()
        if self.var.get()== 3:
            select = y.streams.filter(progressive = True, file_extension = "mp4", res = "240p").first()
        if select is not None:
            self.size_inBytes = select.filesize
            max_size=self.size_inBytes/1024000
            mb = str(round(max_size,1)) + 'MB'
            self.size.config( text = "SIZE: " + mb)
            messagebox.showinfo("showinfo", "VIDEO IS PRESENT")
        else:
            messagebox.showerror("ERROR", "CHOISE OTHER RESOLUTION")
        

    def progress(self,streams,chunk,bytes_remaining):
        percentage = (float(abs(bytes_remaining-self.size_inBytes)/self.size_inBytes))*float(100)
        self.prog['value'] = percentage
        self.prog.update()
        self.down.config( text = "DOWNLOADED "+str(round(percentage,1))+"%")
        #if round(percentage,1) == 100:
          #  self.download.config(state = DISABLED)

    def clearall(self):
        playsound('click.mp3')
        self.var.set(0)
        self.prog['value']=0
        self.error.config(text = "MESSEAGE")
        self.link.config(text ="")
        #self.link.set('')
        self.name.config(text ="")
        #self.name.set('')
        self.f1.config(text=' YOUTUBE VIDEO TITLE  ', font = "Verdana 15 bold")
        self.f2.config(image='')
        self.f3.delete('1.0',END)
        self.size.config(text = "SIZE: 00mb")
        self.down.config(text = "DOWNLOADED 00%")
        
        
    def download(self):
        playsound('click.mp3')
        try:
            y = YouTube(self.link.get(), on_progress_callback = self.progress)
        except:
            messagebox.showerror("ERROR", "VIDEO NOT AVALABLE")
        if self.var.get()== 1:
            select = y.streams.filter(progressive = True, file_extension = "mp4", res = "720p").first()
        if self.var.get()== 2:
            select = y.streams.filter(progressive = True, file_extension = "mp4", res = "360p").first()
        if self.var.get()== 3:
            select = y.streams.filter(progressive = True, file_extension = "mp4", res = "240p").first()
        if select is not None:
            select.download(filename = self.name.get(),output_path="Videos")
            self.error.config(text="   DOWNLOAD COMPLETED  ")
        else:
            messagebox.showerror("ERROR", "PLOBLEM IN DOWNLOAD")


root = Tk()
yo = youtube(root)
root.mainloop()

    
    
