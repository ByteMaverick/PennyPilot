
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from dao.account_dao import AccountDAO


def authenticate_user(username, password):

    actual_password = AccountDAO().get_account_by_username(username)

    if actual_password == password:

        return "True"
    elif actual_password == "notfound":
        return "notfound"
    else:
        return "False"



def show_popup(message):
    msg = QMessageBox()
    msg.setWindowTitle("Pop-up Title")
    msg.setText(message)
    msg.setIcon(QMessageBox.Information)
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    result = msg.exec_()

    if result == QMessageBox.Ok:
        print("OK clicked")
    elif result == QMessageBox.Cancel:
        print("Cancel clicked")


