from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

x = 0
y = 0
c = 0
v = 0
b = 0
n = 0
def pix():
	sense.clear()
	sense.set_pixel(x,y,0,0,255)
	sense.set_pixel(c,v,255,0,0)
	sense.set_pixel(b,n,0,255,0)
	print(str(x) + ","+ str(y)+ ", "+str(c)+", "+str(v))
def setcv():
	c=x
	v=y
pix()
while True:
	for event in sense.stick.get_events():
    # Check if the joystick was pressed
		if event.action == "pressed":
      # Check which direction
			if event.direction == "up":
				if y>0:
					sleep(1)
					#setcv()
					b=c
					n=v
					c=x
					v=y
					y=y-1
					pix()
			elif event.direction == "down":
				if y<7:
					sleep(1)
					#setcv()
					b=c
					n=v
					c=x
					v=y
					y=y+1
					pix()
			elif event.direction == "left":
				if x>0:
					sleep(1)
					#setcv()
					b=c
					n=v
					c=x
					v=y
					x=x-1
					pix()
			elif event.direction == "right":
				if x<7:
					sleep(1)
					#setcv()
					b=c
					n=v
					c=x
					v=y
					x=x+1
					pix()
			elif event.direction == "middle":
				#setcv()
				x = x-x
				y = y-y
				pix()
