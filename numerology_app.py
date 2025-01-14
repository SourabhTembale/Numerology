from tkinter import *

# Define alphabet values with corresponding names (based on the provided image)
alphabet_values = {
    'A': 1, 'B': 2, 'C': 3, 'D': 8, 'E': 5,
    'F': 8, 'G': 3, 'H': 5, 'I': 1, 'J': 1,
    'K': 2, 'L': 1, 'M': 4, 'N': 5, 'O': 7,
    'P': 8, 'Q': 1, 'R': 2, 'S': 3, 'T': 4,
    'U': 6, 'V': 6, 'W': 6, 'X': 5, 'Y': 1, 'Z': 7
}

planet_names = {
    1: "रवि",
    2: "चंद्र",
    3: "गुरु",
    4: "राहु",
    5: "बुध",
    6: "शुक्र",
    7: "नेपच्यून",
    8: "शनि",
    9: "मंगल",
    0: "प्लूटो"
}

def calculate_string_value(string):
    """Calculates the sum of alphabet values in a string."""
    total = 0
    for char in string.upper():
        if char.isalpha():
            total += alphabet_values.get(char, 0)

    while total > 9:
        total = sum(int(digit) for digit in str(total))

    return total

def get_planet_name(number):
    """Returns the planet name corresponding to the given number."""
    return planet_names.get(number, "Unknown")

def on_enter_press(event):
    """Handles Enter key press to calculate and display the result."""
    count_length()

def count_length():
    """Calculates and displays the sum of alphabet values and the corresponding planet name."""
    text = entry.get().upper()
    result_number = calculate_string_value(text)
    result_planet = get_planet_name(result_number)
    result_label.config(text=f"Value: {result_number} ({result_planet})")

# Create the main window
window = Tk()
window.title("Numerology Calculator")

# Center the window on the screen
window_width = 400
window_height = 200
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Create a label for input
label = Label(window, text="Enter Name:", font=("Arial", 14))
label.pack(pady=15)

# Create an input field
entry = Entry(window, width=50, font=("Arial", 12))
entry.pack()
entry.bind('<Return>', on_enter_press)

# Create a button to trigger the calculation
button = Button(window, text="Calculate", font=("Arial", 12), bg="#4CAF50", fg="white", padx=20, pady=10)
button.pack(pady=15)

# Create a label to display the result
result_label = Label(window, text="", font=("Arial", 14))
result_label.pack(pady=15)

# Start the GUI event loop
window.mainloop()