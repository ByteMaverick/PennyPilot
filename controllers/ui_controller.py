from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtWidgets import QMessageBox, QFileDialog

from dao.account_dao import AccountDAO
from dao.profile_dao import ProfileDAO


def authenticate_user(username, password):

    actual_password = AccountDAO().get_account_by_username(username)

    if actual_password == password:

        return "True"
    elif actual_password == "notfound":
        return "notfound"
    else:
        return "False"

def retrieve_password(overrideKey):
    response = AccountDAO().get_account_by_password(overrideKey)

    if response != "notfound":
        show_popup(f" Your password is: {response}\n")
        return "True"
    else:
        show_popup("No account connected to the override key")
        return "False"


def retrieve_name(email):
    response = AccountDAO().get_name_by_email(email)
    return response


def retrieve_profile(email, number):
    response = ProfileDAO().get_profile(email, number)
    if (response != "notfound"):
        return f"Profile {number}: {response}"
    else:
        return f"Create New Profile {number}"


def show_popup(message):
    msg = QMessageBox()
    msg.setWindowTitle("Pop-up Title")
    msg.setText(message)
    msg.setIcon(QMessageBox.Information)
    msg.setStandardButtons(QMessageBox.Ok)
    result = msg.exec_()





from PyQt5.QtWidgets import QMessageBox

def show_loading_message():
    msg = QMessageBox()
    msg.setText("Loading, please wait...")
    msg.setWindowTitle("Loading")
    msg.setStandardButtons(QMessageBox.NoButton)

    msg.setStyleSheet("""
        QMessageBox {
            background-color: white;
            border: 1px solid #ccc;
            font-family: 'Segoe UI', sans-serif;
            font-size: 14px;
        }
        QLabel {
            color: #333;
        }
        QMessageBox QPushButton {
            background-color: #f0f0f0;
            border: 1px solid #aaa;
            padding: 5px 10px;
            border-radius: 4px;
            font-size: 13px;
        }
    """)
    msg.setIconPixmap(QPixmap("assets/Modern Typography Electronic Logo.png").scaled(32,32))

    msg.show()
    return msg