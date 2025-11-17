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

row_count = len(button_values) #5
column_count = len(button_values[0]) #4

color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "#FFFFFF"

window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial", 40), bg=color_black, fg=color_white, width=14, height=2, anchor="e")


label.grid(row=0, column=0)

for row in range(row_count):
    for column in range(row_count):
        value = button_values[row][column]
        button_= tkinter.Button(frame, text=value, font=("Arial", 24), width=column_count-1, height=1, command=lambda v=value: print(v))
frame.pack()
window.mainloop()




    