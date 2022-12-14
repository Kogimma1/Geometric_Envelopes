import turtle as tat
import numpy as np

ecran=tat.Screen()
#ecran.screensize(2000,2000)
ecran.bgcolor("black")

tat = tat.Turtle()
tat.color("white")
tat.speed(0)
tat.pensize(1)

rad_theta = np.linspace(-2*np.pi, 2*np.pi, 360)
deg_theta = np.degrees(rad_theta)

val1 = np.cos(rad_theta)
val2 = np.sin(rad_theta)

radius = 300

ls1 = []
ls2 = []
ls3 = []

for i in val1:
	d1 = radius * i
	print(int(d1))
	ls1.append(int(d1))
	
for j in val2:
	d2 = radius * j
	print(int(d2))
	ls2.append(int(d2))

print(ls1)
print(ls2)

for l in range(len(ls1)):
	ls3.append([ ls1[l], ls2[l] ])
	
print(ls3)

for i in range(len(ls3)):
	k = i*2
	q = k%360
	tat.penup()
	tat.goto(ls3[i%360])
	tat.pendown()
	tat.goto(ls3[q])
	tat.penup()
