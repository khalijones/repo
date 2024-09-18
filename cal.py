import tkinter as tk
from tkinter import messagebox

# Function to calculate the sum
def calculate_sum():
    try:
        number1 = float(entry1.get())
        number2 = float(entry2.get())
        total = number1 + number2
        result_label.config(text=f"The sum is: {total}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create the input fields and labels
label1 = tk.Label(window, text="Enter first number:")
label1.pack(pady=5)
entry1 = tk.Entry(window)
entry1.pack(pady=5)

label2 = tk.Label(window, text="Enter second number:")
label2.pack(pady=5)
entry2 = tk.Entry(window)
entry2.pack(pady=5)

# Create the calculate button
calculate_button = tk.Button(window, text="Calculate Sum", command=calculate_sum)
calculate_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Run the application
window.mainloop()
