import random
import string
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit, QPushButton, QCheckBox, QSlider
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QFont, QClipboard, QGuiApplication, QRegExpValidator


def generate_password(strength, start_with, num_digits, num_special_chars):
    characters = string.ascii_letters + string.digits + string.punctuation

    if strength == "Weak":
        length = 8
    elif strength == "Strong":
        length = 10
    elif strength == "Very Strong":
        length = 12
    else:
        return "Invalid strength input."

    # Ensure start_with is a valid character
    if start_with and start_with[0] not in string.ascii_letters:
        start_with = ""

    password = ""

    # Generate the password
    while len(password) < length:
        if start_with and len(password) == 0:
            password += start_with
        elif len(password) < length - num_digits - num_special_chars:
            password += random.choice(characters)
        elif num_digits > 0:
            password += random.choice(string.digits)
            num_digits -= 1
        elif num_special_chars > 0:
            password += random.choice(string.punctuation)
            num_special_chars -= 1

    return password

def generate_and_display_password():
    strength = strength_combo.currentText()
    start_with = start_with_edit.text()
    num_digits = digits_slider.value()
    num_special_chars = special_chars_slider.value()

    generated_password = generate_password(strength, start_with, num_digits, num_special_chars)
    password_label.setText("Generated password: " + generated_password)

    # Copy password to clipboard
    clipboard = QGuiApplication.clipboard()
    clipboard.setText(generated_password)

app = QApplication(sys.argv)

# Create main window
window = QWidget()
window.setWindowTitle("Password Generator")
window.setGeometry(100, 100, 400, 200)

# Create layout
layout = QVBoxLayout()

# Strength combo box
strength_label = QLabel("Password Strength:")
strength_combo = QComboBox()
strength_combo.addItems(["Weak", "Strong", "Very Strong"])

# Start with
start_with_label = QLabel("Start with:")
start_with_edit = QLineEdit()
start_with_pattern = QRegExp("[a-zA-Z]")
start_with_validator = QRegExpValidator(start_with_pattern)
start_with_edit.setValidator(start_with_validator)


# Number of digits slider
digits_label = QLabel("Number of digits:")
digits_slider = QSlider(Qt.Horizontal)
digits_slider.setMinimum(0)
digits_slider.setMaximum(10)

# Number of special characters slider
special_chars_label = QLabel("Number of special characters:")
special_chars_slider = QSlider(Qt.Horizontal)
special_chars_slider.setMinimum(0)
special_chars_slider.setMaximum(10)

# Generate button
generate_button = QPushButton("Generate Password")
generate_button.clicked.connect(generate_and_display_password)

# Password label
password_label = QLabel("Generated password: ")

# Add widgets to layout
layout.addWidget(strength_label)
layout.addWidget(strength_combo)
layout.addWidget(start_with_label)
layout.addWidget(start_with_edit)
layout.addWidget(digits_label)
layout.addWidget(digits_slider)
layout.addWidget(special_chars_label)
layout.addWidget(special_chars_slider)
layout.addWidget(generate_button)
layout.addWidget(password_label)

# Set layout for the window
window.setLayout(layout)

# Show the window
window.show()

sys.exit(app.exec_())
