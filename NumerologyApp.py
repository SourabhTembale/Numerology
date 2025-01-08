from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

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


class NumerologyApp(App):
    def build(self):
        layout = GridLayout(cols=1, padding=50, spacing=20)

        # Create labels and input field with desired font sizes
        self.input_label = Label(text="Enter Name:", font_size=20,color=(1, 1, 1, 1))
        layout.add_widget(self.input_label)

        # Set input text size (width and height)
        self.input_text = TextInput(multiline=False, font_size=18, size_hint=(0.8, 0.5))  # Adjust width and height as needed

        layout.add_widget(self.input_text)

        # Create a green button with smaller size and white text
        self.calculate_button = Button(
            text="Calculate",
            font_size=18,
            background_color=(0.4, 0.8, 0.4, 1),  # Green color
            color=(1, 1, 1, 1),  # White text color
            size_hint=(0.5, 0.5)  # Set button width and height
        )
        self.calculate_button.bind(on_press=self.calculate)
        layout.add_widget(self.calculate_button)

        # Create result label
        self.result_label = Label(text="", font_size=24,)
        layout.add_widget(self.result_label)

        return layout

    def calculate(self, instance):
        name = self.input_text.text.upper()
        result = calculate_string_value(name)
        self.result_label.text = f"Value: {result}"


if __name__ == '__main__':
    NumerologyApp().run()