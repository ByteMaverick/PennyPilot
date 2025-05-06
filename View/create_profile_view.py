from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QFormLayout, QFrame
)
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtCore import Qt
import sys

from dao.profile_dao import ProfileDAO
import  controllers.ui_controller as ui_controller


class CreateProfileWindow(QWidget):
    """
    QWidget for Create Profile View.
    """
    def __init__(self, email, number):
        super().__init__()
        self.email = email
        self.number = number

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

        # Create Profile Label
        create_profile_label = QLabel(f"Enter name for new Profile {number}")
        create_profile_label.setAlignment(Qt.AlignCenter)
        create_profile_label.setStyleSheet("""
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
        self.name_input.setPlaceholderText(f"Profile {number} Name")
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


        # Create Profile Button
        create_profile_button = QPushButton(f"Create Profile {number}")
        create_profile_button.setCursor(QCursor(Qt.PointingHandCursor))
        create_profile_button.setFixedSize(250, 40)
        create_profile_button.setStyleSheet("""
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


        create_profile_button.clicked.connect(self.createProfile)


        create_profile_layout = QHBoxLayout()
        create_profile_layout.addStretch()
        create_profile_layout.addWidget(create_profile_button)
        create_profile_layout.addStretch()

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


        # Button to return to Profile view
        back_to_profile_button = QPushButton("Back to Profiles")
        back_to_profile_button.setCursor(QCursor(Qt.PointingHandCursor))
        back_to_profile_button.setFixedSize(250, 40)
        back_to_profile_button.setStyleSheet("""
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
        back_to_profile_button.clicked.connect(self.open_profile_window)

        back_to_profile_layout = QHBoxLayout()
        back_to_profile_layout.addStretch()
        back_to_profile_layout.addWidget(back_to_profile_button)
        back_to_profile_layout.addStretch()


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
        main_layout.addWidget(create_profile_label)
        main_layout.addSpacing(10)
        main_layout.addLayout(name_layout)
        main_layout.addLayout(create_profile_layout)

        main_layout.addLayout(line_layout)
        main_layout.addSpacing(20)
        main_layout.addLayout(back_to_profile_layout)

        main_layout.addWidget(
            terms_label)

        self.setLayout(main_layout)



    def open_profile_window(self):
        """
        Open Profile Window.
        :return: None.
        """
        from View.profile_view import ProfileWindow
        self.profile_window = ProfileWindow(email=self.email)
        self.profile_window.show()
        self.close()



    def createProfile(self):
        """
        Create profile.
        :return: None.
        """
        if not self.name_input.text():
            ui_controller.show_popup(f"Please enter name of new profile {self.number}")
            return


        name = self.name_input.text()

        new_profile = ProfileDAO()

        profileCreated = new_profile.add_profile(self.email, self.number, name)
        if profileCreated:
            ui_controller.show_popup(f"New Profile {self.number} called {name} created successfully.")
            self.open_profile_window()

        else:
            ui_controller.show_popup(f"Failed to create profile {self.number}.")






# Run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateProfileWindow()
    window.show()
    sys.exit(app.exec_())
