import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QMessageBox, QCheckBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class LoginApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Login App')
        self.setGeometry(100, 100, 400, 300)

        # Pusatkan jendela
        self.center()

        # Set up the central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)

        # Sub-layout for email and password inputs
        input_layout = QVBoxLayout()
        input_layout.setSpacing(5)

        # Email input
        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText('Enter your email')
        self.email_input.setFixedWidth(300)

        input_layout.addWidget(self.email_input, alignment=Qt.AlignCenter)

        # Password input
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText('Enter your password')
        self.password_input.setFixedWidth(300)

        input_layout.addWidget(self.password_input, alignment=Qt.AlignCenter)

        main_layout.addLayout(input_layout)

        # Sub-layout for Show Password checkbox and Login button
        button_layout = QVBoxLayout()
        button_layout.setSpacing(10)

        # Show password checkbox
        self.show_password_checkbox = QCheckBox('Show Password', self)
        self.show_password_checkbox.stateChanged.connect(self.toggle_password_visibility)

        button_layout.addWidget(self.show_password_checkbox, alignment=Qt.AlignCenter)

        # Login button
        login_button = QPushButton('Login', self)
        login_button.setStyleSheet("background-color: blue; color: white;")
        login_button.setFont(QFont('Arial', 12))
        login_button.clicked.connect(self.handle_login)

        button_layout.addWidget(login_button, alignment=Qt.AlignCenter)

        main_layout.addLayout(button_layout)

        central_widget.setLayout(main_layout)

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def handle_login(self):
        email = self.email_input.text()
        password = self.password_input.text()

        # Simple validation for demonstration purposes
        if email == "user@example.com" and password == "password":
            QMessageBox.information(self, 'Success', 'Login Successful!')
        else:
            QMessageBox.warning(self, 'Error', 'Invalid email or password')

    def toggle_password_visibility(self):
        if self.show_password_checkbox.isChecked():
            self.password_input.setEchoMode(QLineEdit.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.Password)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec_())
