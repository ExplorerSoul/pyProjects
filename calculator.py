import tkinter as tk


def on_click(btn_val):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + btn_val)


def on_clear():
    display.delete(0, tk.END)


def on_equal():
    try:
        # Split the display content by space to get numbers and operator
        content = display.get()
        if len(content) == 3:
            n1, operator, n2 = float(content[0]), content[1], float(content[2])  # Convert to float
            result = "Invalid operator!"
            if operator == "+":
                result = n1 + n2
            elif operator == "-":
                result = n1 - n2
            elif operator == "*":
                result = n1 * n2
            elif operator == "/":
                if n2 != 0:  # Check for division by zero
                    result = n1 / n2
                else:
                    result = "Error: Division by zero"
            display.delete(0, tk.END)
            display.insert(0, str(result))
        else:
            display.delete(0, tk.END)
            display.insert(0, "Error: Invalid input")
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# Create the main window
root = tk.Tk()
root.title("Simple Calculator")


# Fix the window size
root.configure(bg='light pink')
root.geometry('301x404')  # Width x Height
root.resizable(False, False)  # Disable resizing in the x and y direction


# Define the calculator's buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]
# Create and place the buttons with custom colors
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=15, pady=15, bg='light yellow', fg='black',
                       command=lambda val=text: on_click(val), font=('Helvetica', 12))
    button.grid(row=row, column=col, pady=5)

# Add clear button
clear_button = tk.Button(root, bg='orange', text='CE', padx=60, pady=15, command=on_clear, font=('Helvetica', 12))
clear_button.grid(row=5, column=0, columnspan=2)

# Add equal button
equal_button = tk.Button(root, bg='light blue', text='=', padx=60, pady=15, command=on_equal, font=('Helvetica', 12))
equal_button.grid(row=5, column=2, columnspan=2)

# Create the display with a custom background and foreground color
display = tk.Entry(root, width=25, borderwidth=5, bg='light grey', fg='black', font=('Helvetica', 14))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

# Run the application
root.mainloop()
