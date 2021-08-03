from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
pomodoro = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    global pomodoro
    pomodoro = 0
    label.config(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global pomodoro
    pomodoro += 1

    if pomodoro % 8 == 0:
        label.config(text="Rest", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif pomodoro % 2 == 0:
        label.config(text="Rest", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    global pomodoro

    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"

    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        if pomodoro % 2 == 0:
            pomodoro_checks = ""
            for _ in range(0, pomodoro, 2):
                pomodoro_checks += "✔"
            check_marks.config(text=pomodoro_checks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
label.grid(row=1, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="resources/images/tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 129, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=1)

start_button = Button(text="start", bg="white", highlightthickness=0, command=start_timer)
start_button.grid(row=3, column=0)
reset_button = Button(text="reset", bg="white", highlightthickness=0, command=reset_timer)
reset_button.grid(row=3, column=2)

check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(row=4, column=1)

window.mainloop()
