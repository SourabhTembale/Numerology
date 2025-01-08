from tkinter import *

alphabet_values = {
    'A': 1, 'B': 2, 'C': 3, 'D': 8, 'E': 5, 
    'F': 8, 'G': 3, 'H': 5, 'I': 1, 'J': 1, 
    'K': 2, 'L': 1, 'M': 4, 'N': 5, 'O': 7, 
    'P': 8, 'Q': 1, 'R': 2, 'S': 3, 'T': 4, 
    'U': 6, 'V': 6, 'W': 6, 'X': 5, 'Y': 1, 'Z': 7
}

def calculate_string_value(string):
    total = 0
    for char in string.upper():
        if char.isalpha():
            total += alphabet_values.get(char, 0)  
    while total > 9:
        total = sum(int(digit) for digit in str(total))
    return total

def on_enter_press(event):
    count_length()

def count_length():
    text = entry.get().upper()
    result = calculate_string_value(text)
    result_label.config(text=f" Value: {result}", font=("Arial", 25))  

window = Tk()
window.title("Alphabet Value Calculator")

window_width = 500
window_height = 500 
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

title_label = Label(window, text="Numerology Calculator", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

label = Label(window, text="Enter Name:", font=("Arial", 14))
label.pack(pady=15)

entry = Entry(window, width=50, font=("Arial", 12))
entry.pack()
entry.bind('<Return>', on_enter_press) 

button = Button(window, text="Calculate", font=("Arial", 12), bg="#4CAF50", fg="white", padx=20, pady=10)
button.pack(pady=15)

result_label = Label(window, text="", font=("Arial", 50))  
result_label.pack(pady=15)

window.configure(bg="#f0f0f0") 

window.mainloop()