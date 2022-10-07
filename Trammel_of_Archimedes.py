import tkinter as tk
import turtle as tat
from PIL import Image
from PIL import ImageTk
import tkinter.font as font

web = tk.Tk()

can1=tk.Canvas(web,bg="black",width = 720, height = 1500)
can1.grid(ipadx=0, ipady=0, rowspan=1, columnspan=1)

ecran=tat.TurtleScreen(can1)
#ecran.screensize(2000,2000)
#The line above is responsible for controlling screen size
ecran.bgcolor("black")

tat = tat.RawTurtle(can1)
tat.color("white")
tat.speed(0)
tat.pensize(1.5)

for i in range(0,30000):
	def goto(x,y,m,u,e):
		tat.penup()
		if y > 0:
			tat.goto(x*e,y-i*m)
		if y < 0:
			tat.goto(x*e,y+i*m)
		tat.pendown()
		#tat.rt(3)
		#tat.fd(10)
		n=1000-i
		tat.goto(x+u*m,x*e+200)
	if i <= 14:
		tat.color("white")
		u=i
		e=1
		goto(-30,450,20,-u,e)
		tat.color("#0000ff")
		goto(-30,450,20,u,e)
		tat.color("#00ff00")
		goto(-30,-110,20,-u,e)
		tat.color("#ff0000")
		goto(-30,-110,20,u,e)
	if 14 < i <= 17:
		tat.penup()
		tat.color("white")
		tat.goto(250,170)
		tat.goto(-300,170)

a =Image.open("Path/to/image/to/use/as/watermark/though/not/necessary")
mag1=a.resize((250,600),Image.ANTIALIAS)
ppp1 = ImageTk.PhotoImage(mag1)
can1.create_image(180,-50,anchor="n",image=ppp1)

web.mainloop()	
