from dao.account_dao import AccountDAO


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
