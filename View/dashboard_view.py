from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QFormLayout, QFrame
)
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtCore import Qt
import sys



class Dashboard(QWidget):
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
        signup_label = QLabel("Dashboard")
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








        main_layout.addWidget(title)
        main_layout.addWidget(signup_label)
        self.setLayout(main_layout)


    def login(self):
        pass
# Run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dashboard()
    window.showFullScreen()
    sys.exit(app.exec_())
