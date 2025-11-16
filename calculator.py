import tkinter 

buttons = [
     ["AC", "+/-", "%", "÷"],
     ["7", "8", "9", "×"],
     ["4", "5", "6", "-"],
     ["1", "2", "3", "+"],
     ["0", ".", "√", "="]
]

right_symbols = ["+", "-", "×", "÷", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(buttons) #5
column_count = len(buttons[0]) #4

color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "#FFFFFF"

window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)
window.mainloop()


    