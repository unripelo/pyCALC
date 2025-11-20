import tkinter 

button_values = [
     ["AC", "+/-", "%", "÷"],
     ["7", "8", "9", "×"],
     ["4", "5", "6", "-"],
     ["1", "2", "3", "+"],
     ["0", ".", "√", "="]
]

right_symbols = ["+", "-", "×", "÷", "="]
top_symbols = ["AC", "+/-", "%"]

color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "#FFFFFF"

window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window, bg=color_black)
frame.pack(fill="both", expand=True)

# Display Label
label = tkinter.Label(
    frame,
    text="0",
    font=("Arial", 40),
    bg=color_black,
    fg=color_white,
    anchor="e",
    padx=20,
    pady=20
)
label.grid(row=0, column=0, columnspan=4, sticky="nsew")

def button_clicked(value):
    pass

# Create buttons
for row in range(len(button_values)):
    for column in range(len(button_values[row])):
        value = button_values[row][column]

        # Color logic
        if value in top_symbols:
            bg = color_light_gray
            fg = color_black
        elif value in right_symbols:
            bg = color_orange
            fg = color_white
        else:
            bg = color_dark_gray
            fg = color_white

        button = tkinter.Button(
            frame,
            text=value,
            font=("Arial", 26),
            bg=bg,
            fg=fg,
            bd=0,
            activebackground=bg,
            activeforeground=fg,
            command=lambda v=value: button_clicked(v)
        )

        # Make 0 button wider (like real calculators)
        if value == "0":
            button.grid(row=row+1, column=column, columnspan=2, sticky="nsew")
        else:
            button.grid(row=row+1, column=column, sticky="nsew")

# Grid stretching for equal button sizes
for i in range(4):
    frame.columnconfigure(i, weight=1)

for i in range(len(button_values) + 1):
    frame.rowconfigure(i, weight=1)

window.mainloop()
