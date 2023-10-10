import os
import pyfiglet
import time

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print centered text
def print_centered(text):
    terminal_width = os.get_terminal_size().columns
    padding = (terminal_width - len(text)) // 2
    centered_text = ' ' * padding + text
    return centered_text

# Function to print text with a radio style effect
def print_radio_style(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)  # Adjust the delay as needed
    print()

# Clear the screen
clear_screen()

# Create a Figlet font with a specified size and set the color to red
custom_font = pyfiglet.Figlet(font='big', width=200)

# Generate the "Boost Mode" text using the custom font in red
boost_mode_text = custom_font.renderText("\033[31mBoost Mode\033[0m")  # Set text color to red

# Calculate the number of spaces needed for centering
terminal_width = os.get_terminal_size().columns
padding = (terminal_width - len(boost_mode_text.splitlines()[0])) // 2

# Display the "Boost Mode" text in the center
for line in boost_mode_text.splitlines():
    print(' ' * padding + line)

# Lines to display in radio style
lines = [
    "Optimization done",
    "Low Input delay Done",
    "Textures Fixed"
]

# Display each line in a radio style
for line in lines:
    print_radio_style(line)

# Display "Boost mode Successfully Enabled" in the center in green
centered_message = print_centered("\033[32mBoost mode Successfully Enabled\033[0m")  # Set text color to green
print(centered_message)

# Keep the script running until Enter is pressed
input()
