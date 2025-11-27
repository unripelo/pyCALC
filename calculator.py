import tkinter 
import math

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

# Calculator state
current_value = None
operator = None
clear_next = False

def format_number(n):
    # Format numbers to avoid unnecessary .0
    if isinstance(n, str):
        return n
    if n is None:
        return "0"
    if math.isinf(n) or math.isnan(n):
        return "Error"
    if abs(n - int(n)) < 1e-12:
        return str(int(n))
    return str(n)

def get_display_value():
    text = label.cget("text")
    if text == "Error":
        return text
    try:
        return float(text)
    except Exception:
        return 0.0

def set_display(value):
    if isinstance(value, str):
        label.config(text=value)
    else:
        label.config(text=format_number(value))

def perform_operation(a, op, b):
    try:
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "×":
            return a * b
        if op == "÷":
            if b == 0:
                return "Error"
            return a / b
    except Exception:
        return "Error"

def button_clicked(value):
    global current_value, operator, clear_next

    disp = label.cget("text")

    # If currently showing Error, any non-AC input resets
    if disp == "Error" and value != "AC":
        return

    # Digits
    if value.isdigit():
        if clear_next or disp == "0":
            set_display(int(value))
            clear_next = False
        else:
            # append digit
            set_display(disp + value)
        return

    # Decimal point
    if value == ".":
        if clear_next:
            set_display("0.")
            clear_next = False
            return
        if "." not in disp:
            set_display(disp + ".")
        return

    # All Clear
    if value == "AC":
        current_value = None
        operator = None
        clear_next = False
        set_display(0)
        return

    # Toggle sign
    if value == "+/-":
        try:
            num = float(disp)
            num = -num
            set_display(num)
        except Exception:
            set_display("Error")
        return

    # Percent
    if value == "%":
        try:
            num = float(disp) / 100.0
            set_display(num)
        except Exception:
            set_display("Error")
        return

    # Square root
    if value == "√":
        try:
            num = float(disp)
            if num < 0:
                set_display("Error")
            else:
                set_display(math.sqrt(num))
        except Exception:
            set_display("Error")
        clear_next = True
        return

    # Operators (+, -, ×, ÷)
    if value in ["+", "-", "×", "÷"]:
        try:
            num = float(disp)
        except Exception:
            set_display("Error")
            return

        if current_value is None:
            current_value = num
        else:
            # If chaining operations, compute previous first
            if not clear_next:
                result = perform_operation(current_value, operator, num)
                if result == "Error":
                    set_display("Error")
                    current_value = None
                    operator = None
                    clear_next = True
                    return
                current_value = result
                set_display(current_value)

        operator = value
        clear_next = True
        return

    # Equals
    if value == "=":
        if operator is None or current_value is None:
            return
        try:
            num = float(disp)
        except Exception:
            set_display("Error")
            return

        result = perform_operation(current_value, operator, num)
        if result == "Error":
            set_display("Error")
        else:
            set_display(result)
        # reset state
        current_value = None
        operator = None
        clear_next = True
        return

    # Fallback
    return

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

# Center the window on the screen
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
pos_x = (screen_width // 2) - (width // 2)
pos_y = (screen_height // 2) - (height // 2)
window.geometry(f"{width}x{height}+{pos_x}+{pos_y}")

window.mainloop()
