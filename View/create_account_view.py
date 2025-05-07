from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QFormLayout, QFrame
)
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtCore import Qt
import sys

import utils.extractor
from dao.account_dao import AccountDAO
import  controllers.ui_controller as ui_controller


class CreateAccountWindow(QWidget):
    """
    QWidget for Create Account View.
    """
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PennyPilot")
        self.resize(900, 700)
        self.move(QApplication.primaryScreen().availableGeometry().center() - self.rect().center())
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

        # Name Input
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Full Name")
        self.name_input.setFixedSize(250, 40)
        self.name_input.setStyleSheet("""
                           QLineEdit {
                               border: 1px solid #ccc;
                               border-radius: 8px;
                               padding: 8px;
                               font-size: 12pt;
                               color: black;
                           }
                       """)

        name_layout = QHBoxLayout()
        name_layout.addStretch()
        name_layout.addWidget(self.name_input)
        name_layout.addStretch()


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
        self.password_input.setEchoMode(QLineEdit.Password)
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
        self.retype_password_input.setEchoMode(QLineEdit.Password)
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


        create_account_button.clicked.connect(self.createAccount)


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
            'PennyPilot — Track your income, expenses, and spending habits.\n© 2025 Mohammed & Alex. \nAll rights reserved'
        )


        # Add widgets in correct order
        main_layout.setSpacing(6)
        main_layout.addWidget(title)
        main_layout.addWidget(signup_label)
        main_layout.addSpacing(10)
        main_layout.addLayout(name_layout)
        main_layout.addLayout(username_layout)
        main_layout.addLayout(password_layout)
        main_layout.addLayout(retype_password_layout)
        main_layout.addLayout(create_account_layout)

        main_layout.addLayout(line_layout)
        main_layout.addSpacing(20)
        main_layout.addLayout(back_to_login_layout)

        main_layout.addWidget(
            terms_label)

        self.setLayout(main_layout)



    def open_login_window(self):
        """
        Return to login window.
        :return: None.
        """
        from View.login_view import LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()

    def createAccount(self):
        """
        Create account.
        :return: None.
        """
        if not self.name_input.text() or not self.username_input.text() or not self.password_input.text() or not self.retype_password_input.text():
            ui_controller.show_popup("Please fill in all fields")
            return

        if  not utils.extractor.is_email(self.username_input.text()):
            ui_controller.show_popup("Enter a valid email address")
            return


        name = self.name_input.text()
        email = self.username_input.text()
        password = self.password_input.text()
        new_account = AccountDAO()

        if new_account.get_account(email) != "notfound":
            ui_controller.show_popup("Account already exists, please try to sign in.")
            self.open_login_window()
            return


        if self.password_input.text() != self.retype_password_input.text():
            ui_controller.show_popup("Passwords didn't match, Try again.")
            return

        key =utils.extractor.generate_key()
        accountCreated =new_account.add_account(name, email, password,key)
        if accountCreated:
            ui_controller.show_popup(f"Account created successfully.\n  Key: {key} (Use Key to retrieve password, Incase you lose your password)")
            self.open_login_window()


        else:
            ui_controller.show_popup("Failed to create account.")










# Run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateAccountWindow()
    window.show()
    sys.exit(app.exec_())
