from tkinter import *
from PIL import ImageTk, Image
import math
# timings for work and break
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ------------------TIMER RESET------------------#

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(title_label, text= "00:00")
    label.config(text= "Timer",)
    check_mark.config(text = " ")

# -------------------TIMER MECHANISM--------------#

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # if reps modulo 8 is equals 0
    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Break", fill="red")
    # if it's 2nd/4th/6th rep)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Break", fg="blue")
    # if no one in above
    else:
        count_down(work_sec)
        label.config(text="Work", fg="black")

# ----------------------TIME COUNTDOWN--------------#

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = int((count % 60))
    # if time is less than 9 then add zero before the time
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    # to configure the above code
    canvas.itemconfig(title_label, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        # for in the range of work_session
        for i in range(work_sessions):
            marks += "✅"
        check_mark.config(text = marks)

# ---------------------UI MAKER----------------------#

window = Tk()
window.config(padx=50, pady=50, background="yellow")

# to show the text of label

label = Label(text="Timer", fg="red", bg="yellow", font=("Courier", 50))
label.grid(column=1, row=0)
# to import the image
canvas = Canvas(width=200, height=195, bg="yellow")
img = ImageTk.PhotoImage(Image.open("images.jpg"))
canvas.create_image(2, 0, anchor=NW, image=img)
title_label = canvas.create_text(100, 100, text="00:00", fill="white", font=("Courier", 33, "bold"))
canvas.grid(column=1, row=1)
# to print the start button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
# to print the reset button
reset_button = Button(text="Reset", highlightthickness=0, command= reset_timer)
reset_button.grid(column=2, row=2)
# to print the check mark button
check_mark = Button(text="✅")
check_mark.grid(column=1, row=3)

window.mainloop()