# Run the app
import sys

from PyQt5.QtWidgets import QApplication

from View.login_view import LoginWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()

    window.show()
    sys.exit(app.exec_())
