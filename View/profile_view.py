from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QFormLayout, QFrame
)
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtCore import Qt, pyqtSignal
import sys


import  controllers.ui_controller as ui_controller
from controllers.ui_controller import authenticate_user, retrieve_name, retrieve_profile



#  Custom Clickable QLabel
class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()

class ProfileWindow(QWidget):

    def __init__(self, email=None):
        super().__init__()

        self.email = email

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

        # Profile Label
        login_label = QLabel("Profiles")
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

        # Greeting
        greeting = QLabel(f"Hello, {retrieve_name(email)}. Create a new profile or choose an existing one.")
        greeting.setAlignment(Qt.AlignCenter)
        greeting.setStyleSheet("""
                color: #000;
                text-align: center;
                font-family: Inter;
                font-size: 16px;
                font-style: normal;
                font-weight: 400;
                margin-top: 0px;
                line-height: 150%; /* 24px */""")


        # Profile One Button
        # profile_one_button = QPushButton("Create New Profile 1")
        profile_one_button = QPushButton(retrieve_profile(email, 1))
        profile_one_button.setCursor(QCursor(Qt.PointingHandCursor))
        profile_one_button.setFixedSize(250, 40)
        profile_one_button.setStyleSheet("""
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
        profile_one_button.clicked.connect(self.openProfileOne)

        profile_one_layout = QHBoxLayout()
        profile_one_layout.addStretch()
        profile_one_layout.addWidget(profile_one_button)
        profile_one_layout.addStretch()


        # Profile Two Button
        # profile_two_button = QPushButton("Create New Profile 2")
        profile_two_button = QPushButton(retrieve_profile(email, 2))
        profile_two_button.setCursor(QCursor(Qt.PointingHandCursor))
        profile_two_button.setFixedSize(250, 40)
        profile_two_button.setStyleSheet("""
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
        profile_two_button.clicked.connect(self.openProfileTwo)

        profile_two_layout = QHBoxLayout()
        profile_two_layout.addStretch()
        profile_two_layout.addWidget(profile_two_button)
        profile_two_layout.addStretch()


        # Profile Three Button
        # profile_three_button = QPushButton("Create New Profile 3")
        profile_three_button = QPushButton(retrieve_profile(email, 3))
        profile_three_button.setCursor(QCursor(Qt.PointingHandCursor))
        profile_three_button.setFixedSize(250, 40)
        profile_three_button.setStyleSheet("""
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
        profile_three_button.clicked.connect(self.openProfileThree)

        profile_three_layout = QHBoxLayout()
        profile_three_layout.addStretch()
        profile_three_layout.addWidget(profile_three_button)
        profile_three_layout.addStretch()





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


        # Button to Log Out
        log_out_button = QPushButton("Log Out")
        log_out_button.setCursor(QCursor(Qt.PointingHandCursor))
        log_out_button.setFixedSize(250, 40)
        log_out_button.setStyleSheet("""
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
        log_out_button.clicked.connect(self.login_window)

        log_out_layout = QHBoxLayout()
        log_out_layout.addStretch()
        log_out_layout.addWidget(log_out_button)
        log_out_layout.addStretch()


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
        main_layout.addWidget(greeting)
        main_layout.addSpacing(10)
        main_layout.addLayout(profile_one_layout)
        main_layout.addLayout(profile_two_layout)
        main_layout.addLayout(profile_three_layout)

        main_layout.addLayout(line_layout)
        main_layout.addSpacing(20)
        main_layout.addLayout(log_out_layout)

        main_layout.addWidget(
            terms_label)

        self.setLayout(main_layout)


    def create_profile_window(self, number):
        from View.create_profile_view import CreateProfileWindow
        self.create_profile_window = CreateProfileWindow(self.email, number)
        self.create_profile_window.show()
        self.close()


    def openProfileOne(self):
        if retrieve_profile(self.email, 1) == "Create New Profile 1":
            self.create_profile_window(1)

        else:
            loading = ui_controller.show_loading_message()
            QApplication.processEvents()
            try:
                from View.dashboard_view import Dashboard
                # Opens Dashboard for Profile 1
                self.open_dashboard_window = Dashboard(self.email, 1)
                self.open_dashboard_window.showFullScreen()
            except Exception as e:
                print(f"Error while opening dashboard: {e}")
            finally:
                loading.close()
                self.close()



    def openProfileTwo(self):
        if retrieve_profile(self.email, 2) == "Create New Profile 2":
            self.create_profile_window(2)

        else:
            loading = ui_controller.show_loading_message()
            QApplication.processEvents()
            try:
                from View.dashboard_view import Dashboard
                # Opens Dashboard for Profile 2
                self.open_dashboard_window = Dashboard(self.email, 2)
                self.open_dashboard_window.showFullScreen()
            except Exception as e:
                print(f"Error while opening dashboard: {e}")
            finally:
                loading.close()
                self.close()


    def openProfileThree(self):
        if retrieve_profile(self.email, 3) == "Create New Profile 3":
            self.create_profile_window(3)

        else:
            loading = ui_controller.show_loading_message()
            QApplication.processEvents()
            try:
                from View.dashboard_view import Dashboard
                # Opens Dashboard for Profile 3
                self.open_dashboard_window = Dashboard(self.email, 3)
                self.open_dashboard_window.showFullScreen()
            except Exception as e:
                print(f"Error while opening dashboard: {e}")
            finally:
                loading.close()
                self.close()


    def login_window(self):
        from View.login_view import LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()



# Run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProfileWindow()
    window.show()
    sys.exit(app.exec_())
