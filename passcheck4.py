import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QToolButton, QHBoxLayout
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtCore import Qt

class PasswordStrengthChecker(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Set window properties
        self.setWindowTitle('Password Strength Checker')
        self.setGeometry(100, 100, 400, 200)
        self.setWindowIcon(QIcon('C:/Users/MC Don Juan/Desktop/passcheck.png'))  # Replace with the actual path to your window icon

        # Set dark mode style
        self.set_style_dark_mode()

        # Create layout
        layout = QVBoxLayout()

        # Create widgets
        self.label = QLabel('Enter a password:', self)
        self.label.setAlignment(Qt.AlignHCenter)  # Center align horizontally

        # Create a horizontal layout for the password input and show/hide button
        password_layout = QHBoxLayout()

        self.password_input = QLineEdit(self)
        self.password_input.setAlignment(Qt.AlignCenter)  # Center align the entered text
        self.password_input.setEchoMode(QLineEdit.Password)  # Set initial echo mode to Password
        self.password_input.setStyleSheet('border-radius: 10px; padding: 5px;')  # Set border-radius for curved corners

        # Create show/hide password button
        self.show_hide_button = QToolButton(self)
        self.show_hide_button.setIcon(QIcon('C:/Users/MC Don Juan/Desktop/eye.png'))  # Replace with the actual path to your eye icon
        self.show_hide_button.setCheckable(True)
        self.show_hide_button.clicked.connect(self.toggle_password_visibility)

        # Add widgets to the password layout
        password_layout.addWidget(self.password_input)
        password_layout.addWidget(self.show_hide_button)

        # Add password layout to the main layout
        layout.addWidget(self.label)
        layout.addLayout(password_layout)

        # Create and connect the "Check Password" button
        check_button = QPushButton('Check Password', self)
        check_button.clicked.connect(self.check_password)

        # Add widgets to the main layout
        layout.addWidget(check_button)

        self.result_label = QLabel(self)
        self.result_label.setStyleSheet('font-family: Arial; font-size: 16px;')  # Set default font style

        # Center align the result_label
        result_label_container = QWidget(self)
        result_layout = QVBoxLayout(result_label_container)
        result_layout.addWidget(self.result_label)
        result_layout.setAlignment(self.result_label, Qt.AlignCenter)  # Center align horizontally and vertically
        layout.addWidget(result_label_container)

        # Set the layout for the main window
        self.setLayout(layout)

    def check_password(self):
        # Get the entered password
        password = self.password_input.text()

        # Check password strength and update the result label
        result, text_color = self.check_password_strength(password)
        self.result_label.setText(result)
        self.result_label.setStyleSheet(f'color: {text_color}; font-family: Arial; font-size: 16px; font-weight: bold;')

    def check_password_strength(self, password):
        # Password strength checking logic
        if len(password) >= 8:
            has_uppercase = any(char.isupper() for char in password)
            has_lowercase = any(char.islower() for char in password)
            has_digit = any(char.isdigit() for char in password)
            has_special_char = any(char in '!@#$%^&*()_+{}[]:;<>,.?~/-' for char in password)

            # Check if all conditions are met
            if all([has_uppercase, has_lowercase, has_digit, has_special_char]):
                return "Strong Password!", 'darkgreen'  # Set text color to dark green for strong password
            else:
                return "Weak Password!", 'darkred'  # Set text color to dark red for weak password
        else:
            return "Weak Password!", 'darkred'  # Set text color to dark red for weak password

    def toggle_password_visibility(self):
        # Toggle password visibility when the show/hide button is clicked
        if self.show_hide_button.isChecked():
            self.password_input.setEchoMode(QLineEdit.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.Password)

    def set_style_dark_mode(self):
        app.setStyle('Fusion')

        # Create dark color palette
        dark_palette = app.palette()
        dark_palette.setColor(QPalette.Window, QColor(21, 24, 25))
        dark_palette.setColor(QPalette.WindowText, Qt.white)
        dark_palette.setColor(QPalette.Base, QColor(6, 42, 73))
        dark_palette.setColor(QPalette.AlternateBase, QColor(39, 23, 60))
        dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
        dark_palette.setColor(QPalette.ToolTipText, Qt.white)
        dark_palette.setColor(QPalette.Text, Qt.white)
        dark_palette.setColor(QPalette.Button, QColor(39, 23, 60))
        dark_palette.setColor(QPalette.ButtonText, Qt.white)
        dark_palette.setColor(QPalette.BrightText, Qt.red)
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, Qt.black)

        # Set the dark color palette
        app.setPalette(dark_palette)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = PasswordStrengthChecker()
    main_window.show()
    sys.exit(app.exec_())
