from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QFormLayout, QFrame
)
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtCore import Qt, pyqtSignal
import sys


import  controllers.ui_controller as ui_controller
from controllers.ui_controller import authenticate_user
from create_account_view import CreateAccountWindow
from forgot_password_view import ForgotPasswordWindow
from dashboard_view import Dashboard
from profile_view import ProfileWindow




#  Custom Clickable QLabel
class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
class LoginWindow(QWidget):
    """
    QWidget for Login View.
    """
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

        # Login Label
        login_label = QLabel("Login")
        login_label.setAlignment(Qt.AlignCenter)
        login_label.setStyleSheet("""
                color: #000;
                text-align: center;
                font-family: Inter;
                font-size: 24px;
                font-style: normal;
                font-weight: 600;
                line-height: 150%; /* 36px */
                letter-spacing: -0.24px;""")

        # Subtext
        subtext = QLabel("Enter your email and password to sign in")
        subtext.setAlignment(Qt.AlignCenter)
        subtext.setStyleSheet("""
                color: #000;
                text-align: center;
                font-family: Inter;
                font-size: 16px;
                font-style: normal;
                font-weight: 400;
                margin-top: 0px;
                line-height: 150%; /* 24px */""")

        # Username Input
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Email")
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


        # Sign in Button
        sign_in_button = QPushButton("Sign in")
        sign_in_button.setCursor(QCursor(Qt.PointingHandCursor))
        sign_in_button.setFixedSize(250, 40)
        sign_in_button.setStyleSheet("""
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
        sign_in_button.clicked.connect(self.login)

        sign_in_layout = QHBoxLayout()
        sign_in_layout.addStretch()
        sign_in_layout.addWidget(sign_in_button)
        sign_in_layout.addStretch()



        # Forgot my password
        forgot_my_password_label = ClickableLabel("Forgot my password?")
        forgot_my_password_label.setAlignment(Qt.AlignCenter)
        forgot_my_password_label.setStyleSheet("""
                        color: #5293d9;
                        text-align: center;
                        font-family: Inter;
                        font-size: 16px;
                        font-style: normal;
                        font-weight: 400;
                        line-height: 150%; /* 24px */""")
        forgot_my_password_label.setCursor(QCursor(Qt.PointingHandCursor))
        forgot_my_password_label.clicked.connect(self.open_forgot_password_window)


        # Maybe a layout
        forgot_layout = QHBoxLayout()
        forgot_layout.addStretch()
        forgot_layout.addWidget(forgot_my_password_label)
        forgot_layout.addStretch()

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




        # Create account button
        create_button = QPushButton("Create Account")
        create_button.setCursor(QCursor(Qt.PointingHandCursor))
        create_button.setFixedSize(250,40)
        create_button.setStyleSheet("""
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
        create_button.clicked.connect(self.open_create_account_window)

        create_button_layout = QHBoxLayout()
        create_button_layout.addStretch()
        create_button_layout.addWidget(create_button)
        create_button_layout.addStretch()

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
        main_layout.addWidget(login_label)
        main_layout.addSpacing(1)
        main_layout.addWidget(subtext)
        main_layout.addSpacing(10)
        main_layout.addLayout(username_layout)
        main_layout.addLayout(password_layout)
        main_layout.addLayout(sign_in_layout)
        main_layout.addWidget(forgot_my_password_label)
        main_layout.addLayout(forgot_layout)
        main_layout.addLayout(line_layout)
        main_layout.addLayout(create_button_layout)
        main_layout.addWidget(
            terms_label)

        self.setLayout(main_layout)




    def login(self):
        """
        Log in user.
        :return: None.
        """
        username = self.username_input.text()
        password = self.password_input.text()

        # If username and password are empty
        if not  username.strip() or not password.strip():
            msg = QMessageBox(self)
            msg.setWindowTitle("Missing Fields")
            msg.setText("Username and Password are required.")
            msg.setIcon(QMessageBox.Warning)

            # Custom styling
            msg.setStyleSheet("""
                        QMessageBox {
                            background-color: #white;
                            font-family: Inter;
                            font-size: 12pt;
                        }
                        QLabel {
                            color: black;
                        }
                        QPushButton {
                            background-color: #White;
                            border: 1px solid #ccc;
                            padding: 6px 12px;
                            border-radius: 6px;
                            min-width: 80px;
                        }
                        QPushButton:hover {
                            background-color: #e0e0e0;
                        }
                    """)

            msg.exec_()
            return

        self.auth(password,username)



    def auth(self,password,username):
        """
        Authenticate user using username and password.
        :param password: password input.
        :param username: username input.
        :return: None.
        """
        loading = ui_controller.show_loading_message()
        QApplication.processEvents()
        username = self.username_input.text()
        password = self.password_input.text()

        auth = authenticate_user(username, password)
        print(auth)
        # Password matches
        if auth == "True":

            try:
                self.open_profile_window = ProfileWindow(email=username)
                self.open_profile_window.show()
                # self.open_dashboard_window = Dashboard()
                # self.open_dashboard_window.showFullScreen()
            except Exception as e:
                # print(f"Error while opening dashboard: {e}")
                print(f"Error while opening profiles: {e}")
            finally:
                loading.close()
                self.close()

        # Password does not match
        elif auth == "False":
            ui_controller.show_popup("Password is incorrect")
        # Account not found in database
        else:
            ui_controller.show_popup("Account Not Found, Please Create New Account")


    def open_create_account_window(self):
        """
        Open create account window.
        :return: None.
        """
        self.create_window = CreateAccountWindow()
        self.create_window.show()
        self.close()

    def open_forgot_password_window(self):
        """
        Open forgot password window.
        :return: None.
        """
        self.forgot_window = ForgotPasswordWindow()
        self.forgot_window.show()
        self.close()




# Run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
