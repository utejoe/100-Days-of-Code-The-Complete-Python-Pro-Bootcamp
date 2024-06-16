import tkinter as tk
from math import floor

# Constants
YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
PINK = "#e2979c"
RED = "#e7305b"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Global variable to keep track of repetitions
reps = 0
timer = None

# Function to reset the timer
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    global reps
    reps = 0

# Function to start the timer
def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# Function to handle the countdown mechanism
def count_down(count):
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 != 0:
            marks = ""
            work_sessions = floor(reps / 2)
            for _ in range(work_sessions):
                marks += "✓"
            check_marks.config(text=marks)

# Set up the user interface
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Title Label
title_label = tk.Label(window, text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# Canvas for the timer
canvas = tk.Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start Button
start_button = tk.Button(window, text="Start", command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = tk.Button(window, text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

# Checkmarks Label
check_marks = tk.Label(window, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24))
check_marks.grid(column=1, row=3)

window.mainloop()
