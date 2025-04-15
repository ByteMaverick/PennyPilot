from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QFormLayout, QFrame
)
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtCore import Qt
import sys



class CreateAccountWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PennyPilot")
        self.setGeometry(720, 450, 900, 700)
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
        signup_label = QLabel("Sign Up with PennyPilot")
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



        # Password Input
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setFixedSize(250, 40)
        self.password_input.setStyleSheet("""
                          QLineEdit {
                              border: 1px solid #ccc;
                              border-radius: 8px;
                              padding: 8px;
                              font-size: 12pt;
                              color: black;
                          }
                      """)

        password_layout = QHBoxLayout()
        password_layout.addStretch()
        password_layout.addWidget(self.password_input)
        password_layout.addStretch()

        # Password Input
        self.retype_password_input = QLineEdit(self)
        self.retype_password_input.setPlaceholderText("Re-Type Password")
        self.retype_password_input.setFixedSize(250, 40)
        self.retype_password_input.setStyleSheet("""
                                  QLineEdit {
                                      border: 1px solid #ccc;
                                      border-radius: 8px;
                                      padding: 8px;
                                      font-size: 12pt;
                                      color: black;
                                  }
                              """)

        retype_password_layout = QHBoxLayout()
        retype_password_layout.addStretch()
        retype_password_layout.addWidget(self.retype_password_input)
        retype_password_layout.addStretch()



        # Create Account Button
        create_account_button = QPushButton("Create Account")
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

        # Line
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("background-color: #ccc;")
        line.setFixedHeight(1)
        line.setFixedWidth(200)  # Fixed width to match your inputs/buttons

        # Center it using a layout
        line_layout = QHBoxLayout()
        line_layout.addStretch()
        line_layout.addWidget(line)
        line_layout.addStretch()

        # Footer
        # Terms and Conditions
        terms_label = QLabel("By clicking continue, you agree to our Terms of Service and Privacy Policy")
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
            'By clicking continue, you agree to our <a href="#">Terms of Service</a> and <a href="#">Privacy Policy</a>.'
        )
        terms_label.setOpenExternalLinks(True)

        # Add widgets in correct order
        main_layout.setSpacing(6)
        main_layout.addWidget(title)
        main_layout.addWidget(signup_label)
        main_layout.addSpacing(10)
        main_layout.addLayout(username_layout)
        main_layout.addLayout(password_layout)
        main_layout.addLayout(retype_password_layout)
        main_layout.addLayout(create_account_layout)

        main_layout.addLayout(line_layout)

        main_layout.addWidget(
            terms_label)

        self.setLayout(main_layout)


    def login(self):
        pass
# Run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateAccountWindow()
    window.show()
    sys.exit(app.exec_())
