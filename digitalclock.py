import tkinter as ui #tkinter is refered as ui in this pgm  
import time
window = ui.Tk() #instance of a window

def update_clock():
    hours = time.strftime("%I") #current hour is extracted using I
    minutes = time.strftime("%M") #current mintue is extracted using M
    seconds = time.strftime("%S") #current sec is extracted using S
    am_or_pm = time.strftime("%p") #current am or pm is extracted using p
    time_text =  hours + ":" +minutes+":"+seconds+" "+am_or_pm #min,hr,sec,am or pm is concatenated
    digital_clock_lbl.config(text=time_text) #update digital clock system label with time_text constructed
    digital_clock_lbl.after(1000, update_clock) #to update the clock every sec, here 1000 refers to 1000ms i.e 1sec
    

digital_clock_lbl = ui.Label(window, text="00:00:00", font="Calibir 75 bold") #label of the window and text font
digital_clock_lbl.pack()#label of the window is displayed 
update_clock()
window.mainloop() #creation of window or display 
