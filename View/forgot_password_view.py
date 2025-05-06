from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QFormLayout, QFrame
)
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtCore import Qt
import sys

from controllers import ui_controller


class ForgotPasswordWindow(QWidget):
    """
    QWidget for Forgot Password View.
    """
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PennyPilot")
        self.setGeometry(700, 500, 900, 700)
        self.setStyleSheet("background-color: white;")


        main_layout = QVBoxLayout()

        # Title
        title = QLabel("PennyPilot")

        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet(
            """
            color: #000;
            text-align: center;
            font-family: Inter;
            font-size: 32px;
            font-style: normal; 
            font-weight: 600;
            line-height: 150%; /* 48px */
            letter-spacing: -0.32px;
            """)

        # Sign Up Label
        signup_label = QLabel("Forgot Password")
        signup_label.setAlignment(Qt.AlignCenter)
        signup_label.setStyleSheet("""
                color: #000;
                text-align: center;
                font-family: Inter;
                font-size: 24px;
                font-style: normal;
                font-weight: 600;
                line-height: 150%; /* 36px */
                letter-spacing: -0.24px;""")


        # Username Input
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("email@domain.com")
        self.username_input.setFixedSize(250, 40)
        self.username_input.setStyleSheet("""
                   QLineEdit {
                       border: 1px solid #ccc;
                       border-radius: 8px;
                       padding: 8px;
                       font-size: 12pt;
                       color: black;
                   }
               """)

        username_layout = QHBoxLayout()
        username_layout.addStretch()
        username_layout.addWidget(self.username_input)
        username_layout.addStretch()

        # Password Override Key
        self.key_input = QLineEdit(self)
        self.key_input.setPlaceholderText("Override Key")
        self.key_input.setFixedSize(250, 40)
        self.key_input.setStyleSheet(""" QLineEdit {
                       border: 1px solid #ccc;
                       border-radius: 8px;
                       padding: 8px;
                       font-size: 12pt;
                       color: black;
                   }""")

        key_layout = QHBoxLayout()
        key_layout.addStretch()
        key_layout.addWidget(self.key_input)
        key_layout.addStretch()






        # Retrieve Password Button
        retrieve_password_button = QPushButton("Retrieve Password")
        retrieve_password_button.setCursor(QCursor(Qt.PointingHandCursor))
        retrieve_password_button.setFixedSize(250, 40)
        retrieve_password_button.setStyleSheet("""
                            QPushButton {
                                background-color: black;
                                color: white;
                                border: none;
                                border-radius: 8px;
                                font-weight: bold;
                                font-size: 11pt;
                            }
                            QPushButton:hover {
                                background-color: #333;
                            }
                        """)

        retrieve_password_layout = QHBoxLayout()
        retrieve_password_layout.addStretch()
        retrieve_password_layout.addWidget(retrieve_password_button)
        retrieve_password_layout.addStretch()

        retrieve_password_button.clicked.connect(self.AuthKey)
        # Line
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("background-color: #ccc;")
        line.setFixedHeight(1)
        line.setFixedWidth(200)

        # Center it using a layout
        line_layout = QHBoxLayout()
        line_layout.addStretch()
        line_layout.addWidget(line)
        line_layout.addStretch()


        # Button to return to Login view
        back_to_login_button = QPushButton("Back to Login")
        back_to_login_button.setCursor(QCursor(Qt.PointingHandCursor))
        back_to_login_button.setFixedSize(250, 40)
        back_to_login_button.setStyleSheet("""
                                            QPushButton {
                                                background-color: #f0f0f0;
                                                color: black;
                                                border: none;
                                                border-radius: 8px;
                                                font-weight: bold;
                                                font-size: 11pt;
                                            }
                                            QPushButton:hover {
                                                background-color: #e0e0e0;
                                            }
                                        """)
        back_to_login_button.clicked.connect(self.open_login_window)

        back_to_login_layout = QHBoxLayout()
        back_to_login_layout.addStretch()
        back_to_login_layout.addWidget(back_to_login_button)
        back_to_login_layout.addStretch()


        # Footer
        # Terms and Conditions
        terms_label = QLabel("Trade marker")
        terms_label.setWordWrap(True)
        terms_label.setAlignment(Qt.AlignCenter)
        terms_label.setStyleSheet("""
            color: gray;
            font-family: Inter;
            font-size: 10px;
            font-style: normal;
            font-weight: 400;
            line-height: 150%;
        """)
        terms_label.setText(
            'PennyPilot — Track your income, expenses, and spending habits.\n© 2025 Mohammed & Alex. \nAll rights reserved.'
        )
        terms_label.setOpenExternalLinks(True)

        # Add widgets in correct order
        main_layout.setSpacing(6)
        main_layout.addWidget(title)
        main_layout.addWidget(signup_label)
        main_layout.addSpacing(10)
        main_layout.addLayout(username_layout)
        main_layout.addLayout(key_layout)
        main_layout.addLayout(retrieve_password_layout)

        main_layout.addLayout(line_layout)
        main_layout.addSpacing(20)
        main_layout.addLayout(back_to_login_layout)

        main_layout.addWidget(
            terms_label)

        self.setLayout(main_layout)


    def open_login_window(self):
        """
        Open Login Window.
        :return: None.
        """
        from View.login_view import LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()


    def AuthKey(self):
        """
        Check if key is valid.
        :return: None.
        """
        key = self.key_input.text()
        valid = ui_controller.retrieve_password(key)
        # Go back to login window after user retrieves password
        if (valid == "True") :
            self.open_login_window()


# Run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ForgotPasswordWindow()
    window.show()
    sys.exit(app.exec_())
