from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    pass

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer")
timer_label.config(bg=YELLOW, fg= GREEN,font=(FONT_NAME, 40))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
bg_image = PhotoImage(file="tomato.png")  # convert image to canvas image format
canvas.create_image(100, 112, image=bg_image) 
canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", highlightbackground=YELLOW,command = start)
start_button.grid(column=0, row=2)


reset_button = Button(text="Reset", highlightbackground=YELLOW,command = reset)
reset_button.grid(column=2, row=2)

check_box_label = Label(text="✅")
check_box_label.config(bg=YELLOW, fg= GREEN,font=(FONT_NAME, 15))
check_box_label.grid(column=1, row=3)














window.mainloop()