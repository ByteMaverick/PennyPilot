from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QFormLayout, QFrame
)
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtCore import Qt
import sys

from controllers import ui_controller


class ForgotPasswordWindow(QWidget):
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






        # Create Account Button
        create_account_button = QPushButton("Retrieve Password")
        create_account_button.setCursor(QCursor(Qt.PointingHandCursor))
        create_account_button.setFixedSize(250, 40)
        create_account_button.setStyleSheet("""
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

        create_account_layout = QHBoxLayout()
        create_account_layout.addStretch()
        create_account_layout.addWidget(create_account_button)
        create_account_layout.addStretch()

        create_account_button.clicked.connect(self.AuthKey)
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
        main_layout.addLayout(create_account_layout)

        main_layout.addLayout(line_layout)

        main_layout.addWidget(
            terms_label)

        self.setLayout(main_layout)


    def AuthKey(self):
        key = self.key_input.text()
        return ui_controller.retrieve_password(key)


# Run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ForgotPasswordWindow()
    window.show()
    sys.exit(app.exec_())
