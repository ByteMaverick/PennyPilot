from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtWidgets import QMessageBox, QFileDialog

from dao.account_dao import AccountDAO
from dao.profile_dao import ProfileDAO


def authenticate_user(username, password):
    """
    Authenticates a user in login view by checking the username and password
    :param username: Username of user.
    :param password: Password of user.
    :return: "True" if authenticated, "False" if not authenticated, "notfound" if account does not exist
    """

    # Get actual password from database
    actual_password = AccountDAO().get_account_by_username(username)

    # Check if password matches
    if actual_password == password:
        return "True"
    # Account doesn't exist
    elif actual_password == "notfound":
        return "notfound"
    # Password is wrong
    else:
        return "False"

def retrieve_password(overrideKey):
    """
    Retrieves password for a specific user by getting their overrideKey.
    :param overrideKey: User's key to override their password.
    :return: "True" if account exists, "False" if account doesn't exist
    """
    response = AccountDAO().get_account_by_password(overrideKey)

    if response != "notfound":
        show_popup(f" Your password is: {response}\n")
        return "True"
    else:
        show_popup("No account connected to the override key")
        return "False"



def retrieve_name(email):
    """
    Retrieves name for a specific user by getting their email.
    :param email: Email of a user.
    :return: Name of the user.
    """
    response = AccountDAO().get_name_by_email(email)
    return response


def retrieve_profile(email, number):
    """
    Retrieves profile for a specific user by getting their email.
    :param email: Email of a user.
    :param number: Profile number specified by user.
    :return: String to be used in the corresponding profile button.
    """
    response = ProfileDAO().get_profile(email, number)
    if (response != "notfound"):
        return f"Profile {number}: {response}"
    else:
        return f"Create New Profile {number}"



def show_popup(message):
    """
    Shows a popup upon user input depending on message.
    :param message: Message to be displayed in popup.
    :return: None
    """
    msg = QMessageBox()
    msg.setWindowTitle("Pop-up Title")
    msg.setText(message)
    msg.setIcon(QMessageBox.Information)
    msg.setStandardButtons(QMessageBox.Ok)
    result = msg.exec_()





from PyQt5.QtWidgets import QMessageBox

def show_loading_message():
    """
    Shows loading message to the user.
    :return: QMessageBox containing the loading message.
    """
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