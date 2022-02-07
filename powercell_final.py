#
#	This python script reads the output of powercell Arduino
#	Timing is determined by the Arduino code. Currently the output has about 3 points every second
#	Current scetch name is "powercell_final.ino"
#	Python script plots the data as a bar graph as well as stores a screen capture of the plot
#	Arduino will send string QQQ to indicate that the stop button 
#	has been pushed at the weight cell. After receipt of this string,
#	the reading is terminated, maximum reading is printed out and the files closed. 
#	
#

import tkinter as tk
import serial
from pynput.keyboard import Key, Controller
from PIL import Image, ImageTk
from datetime import datetime
 
#----- Environment variables 
yDiv = 45	# Pixels per kilogram (default unit of force), used for the plot
factor = 80930   # raw reading per kg. Calibrated on Nov 19 2019 (should be stored in file in the future)
styles = ["Free", "Breast", "Fly", "Back"]				# For button menu texts
stylex = ["freestyle", "breaststroke", "butterfly", "backstroke"]	# for header text
plot_color = "#ff5085"
date_form = "%d.%m.%Y, %H:%M"
swimmers = list()
maxPower = list()
start = False	# If looping is implemented, this needs to be inside the loop
finish = False

#----- Functions

def graduate(axis):  # Draws the y axis scale. 475 px equals the value of yScale
    a = 0
    yDiv = 475 / axis	# pixels per unit of force
    step_size = int(axis / 4)	# graduation step size here
    while (a < axis):
        yCoor = 475 - a*yDiv
        # draw scale value
        screen.create_text(25, yCoor, font=("arial",14), text=str(a))
        # draw the tick mark
        screen.create_line(45, yCoor, 50, yCoor)
        a += step_size	

def getZero():      # Two zero readings are averaged
    z1 = float(ser.readline())
    z2 = float(ser.readline())
    return (z1+ z2) / 2

def getRead():      # Read data from serial port
    aData = zData
    try:
        aData = float(ser.readline())
    except:
        global finish
        finish = True
    netData = (aData - zData) / factor  # as long as valid data is read	     
    return netData
    
def plot(xCoor):    # Draws a vertical line, height equal to the serial input value
    reading = getRead()
    if finish == True:
        return
    height = int(reading * yDiv +0.5) # scaling and rounding to the nearest pixel value
    screen.create_line(xCoor, 475-height, xCoor, 474, width=2, fill=plot_color)  #"#ff5085")
    return reading
def ReadDisc():
    disc = open("C:\\Users\\user\\Desktop\\teamcsv.txt", "r") # Desktop file containing the names and power levels
    for x in disc:
        n = x.partition(",")	# strip the comma
        swimmers.append(n[0])
        maxPower.append(n[2])
    disc.close()

def starting():
    global start
    start = True
    
def maxRead():
    leng = int((maxval * yDiv) + 0.5)
    ycoor = 475 - leng - 16		# 16 pixels above the plot peak
    maxtime = int((maxcoo - 54) / 4 * 0.363) # Amend if graphics window is different
    screen.create_text(maxcoo+15, ycoor, font=("Arial",12), text=('%.2f' % maxval)+" kp @ "+str(maxtime)+" sec.")
    screen.create_line(maxcoo, ycoor+10, maxcoo, ycoor+15, width=2, fill="#000")
    plotw.update()
     
# Main
ser = serial.Serial('COM3',baudrate = 38400, timeout=3) # Open serial port
finish = False   # Turns True when serial input string 'QQQ' is read
start = False
WinSmall = tk.Tk()
WinSmall.title("Power swimmer select")
WinSmall.geometry("300x500+150+150")
load = Image.open("vetodelf.jpg")
render = ImageTk.PhotoImage(load)
logo = tk.Label(WinSmall, image=render)
logo.pack()
event = ""
swimmers = list()
ReadDisc()

# Create a Tkinter variable
Swimmer = tk.StringVar()
SwimmerSel = tk.OptionMenu(WinSmall, Swimmer, *swimmers)
SwimmerSel.config(width=16, bg="#ebfb45", font=("Arial",15)) # set the button font
menu = WinSmall.nametowidget(SwimmerSel.menuname)
menu.config(font=("Arial",15)) # set the drop down menu font
SwimmerSel.pack()
space = tk.Label(WinSmall, text=" ")
space.pack()

v = tk.IntVar()
v.set(0)

for val, style in enumerate(styles):
    radiot = tk.Radiobutton(WinSmall, # radio buttons formatted as square buttons
                  text=style,
                  indicatoron = 0,
                  width = 10,
                  bg="#db83bb",          
                  variable=v, 
                  value=val).pack()
start = False
space = tk.Label(WinSmall, text=" ")
space.pack()  #--- create a small space
Butn1 = tk.Button(WinSmall,
                   text="Start!",
                   bg="#73f27b",
                   width=18,	# large butten is easy to handle
                   height=3,
                   font=(15),
                   command=starting)
Butn1.pack()
while (start == False):
    WinSmall.update()
yAxis = int(maxPower[swimmers.index(Swimmer.get())])	# individual y-axis scale
yDiv = int(450 / yAxis)
ser.reset_input_buffer()    #  After "Start" is pressed, purge all sh#t from serial buffer
zeroData = getZero()        # Fetch a zero reading - NOTE: the power cell unit must be unloaded at this stage  
header = Swimmer.get()+"_"
header = header + stylex[v.get()] + "_" +datetime.now().strftime(date_form)
plotw = tk.Tk()
plotw.title("Forward power plot")
plotw.geometry("850x500+460+150")
screen = tk.Canvas(plotw, width=850, height=500, relief='sunken', bd=5, bg = "#fbfcff")
screen.pack()
screen.create_line(50, 0, 50, 475)       # Y axis
screen.create_line(50, 475, 850, 475)    # X axis
graduate(yAxis)      # draw the y axis values and marks
screen.create_text(200, 20, text=header, font=("Times", 15))
zData = getZero()
xCoor = 52
reading = 0
maxval = 0
maxcoo = 0
plotw.update()

while reading < 0.1:     # Plotting starts when input value exceeds 100 g
    reading = getRead()
luku = plot(xCoor)
while finish == False:
    if luku > maxval:	# keep track of the highest value and its x position
        maxval=luku
        maxcoo = xCoor
    xCoor += 4
    luku = plot(xCoor)
    plotw.update()
					# Final step after receiving the QQQ string
plotw.focus_force()	# activate the plotting window to enable screen capture
keyb = Controller()
maxRead()
keyb.press(Key.alt)	# create a Print Active Window command (Alt+PrtSc = screen capture)
keyb.press(Key.print_screen)
keyb.release(Key.print_screen)
keyb.release(Key.alt)
start = False
# WinSmall.mainloop()  # 
