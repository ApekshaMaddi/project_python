import tkinter as ui #tkinter is refered as ui in this pgm  
import time
import math
window = ui.Tk() #instance of a window
window.geometry("400x400")#to set the size of the window

def update_clock():
    hours = int(time.strftime("%I")) #current hour is extracted using I
    minutes = int(time.strftime("%M")) #current mintue is extracted using M
    seconds = int(time.strftime("%S")) #current sec is extracted using S

    #updating sec hands per sec
    seconds_x = seconds_hand_len * math.sin(math.radians(seconds * 6)) + center_x #x=r*sin(t)
    seconds_y = -1 * seconds_hand_len * math.cos(math.radians(seconds * 6))+center_y #y=-r*cos(t) 360/60=6 ie t=6(angle to be moved by the hands)
    canvas.coords(seconds_hand, center_x, center_y, seconds_x, seconds_y)

    #updating sec hands per sec
    minutes_x = minutes_hand_len * math.sin(math.radians(minutes * 6)) + center_x #360/60=6 ie t=6
    minutes_y = -1 * minutes_hand_len * math.cos(math.radians(minutes * 6))+center_y
    canvas.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)

    #updating sec hands per sec
    hours_x = hours_hand_len * math.sin(math.radians(hours * 30)) + center_x #360/12=30 ie t=30
    hours_y = -1 * hours_hand_len * math.cos(math.radians(hours * 30))+center_y
    canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)

    window.after(1000, update_clock)
    

canvas = ui.Canvas(window, width=400, height=400, bg="black")#to draw things use canvas
canvas.pack(expand=True, fill="both")

#create background
bg=ui.PhotoImage(file="clock.png")
canvas.create_image(200,200,image=bg)#midpoint

#create hands
center_x = 200
center_y = 200
seconds_hand_len = 60
minutes_hand_len = 50
hours_hand_len = 30

#drawing clock hands
seconds_hand = canvas.create_line(200,200,200+seconds_hand_len, 200+seconds_hand_len, width=1.2, fill="red")#line connects two end points 1st two arguments
                                                                                                             # are 1st end points, 2nd argu 2nd end point 
minutes_hand = canvas.create_line(200,200,200+minutes_hand_len, 200+minutes_hand_len, width=2, fill="red")
hours_hand = canvas.create_line(200,200,200+hours_hand_len, 200+hours_hand_len, width=4, fill="red")
                                                                                      
update_clock()
window.mainloop() #creation of window or display 



