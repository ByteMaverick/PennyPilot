from dao.account_dao import AccountDAO


def authenticate_user(username, password):

    actual_password = AccountDAO().get_account_by_username(username)

    if actual_password == password:

        return "True"
    elif actual_password == "notfound":
        return "notfound"
    else:
        return "False"
