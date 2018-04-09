from tkinter import *
from bs4 import BeautifulSoup
import requests
import urllib
from PIL import ImageTk,Image
url_array=[]
a=[]
root=Tk()
root.title("Image Scrapper")
sizex = 800
sizey = 600
posx  = 100
posy  = 100
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
frame1=Frame(root,height=100,width=100,bd=1,relief=GROOVE)
frame1.place(x=250,y=10)
Label(frame1,text="Enter the URL").grid(row=0,column=2)
url=StringVar()
entry=Entry(frame1,textvariable=url).grid(row=1,column=2)
def click():
	print("GH")
	response=requests.get(url.get())
	page=response.text
	soup=BeautifulSoup(page,"html.parser")
	for i in soup.find_all("img"):
		if i.get("src"):
			url_array.append("http:"+i.get("src"))
	for i,e in enumerate(url_array[0:10]):
		k=str("img"+str(i)+".jpg")
		a.append(k)
		urllib.request.urlretrieve(e,k)

	for i,e in enumerate(a):
		im = Image.open(e)
		resized = im.resize((100, 100), Image.ANTIALIAS)
		image=ImageTk.PhotoImage(resized)
		myvar = Label(innerframe, image=image)
		myvar.image = image
		myvar.grid(row=2+i, column=0)



def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=200,height=200)

button=Button(frame1,text="Ise dabaye",command=click).grid(row=3,column=2)
mainframe=Frame(root,height=100,width=100,relief=GROOVE,bd=1)
mainframe.place(x=100,y=100)
canvas=Canvas(mainframe)
innerframe=Frame(canvas)
myscrollbar=Scrollbar(mainframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left")
canvas.create_window((0,0),window=innerframe,anchor='nw')
innerframe.bind("<Configure>",myfunction)
root.mainloop()
