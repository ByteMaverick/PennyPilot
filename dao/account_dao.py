from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker
from models.account import Account

class AccountDAO:
    """
    Account Data Access Object to manipulate account data in SQLite database.
    """
    def __init__(self, db_url="sqlite:///../pennypilot.db"):
        self.engine = create_engine(db_url)

       # Call session() when needed
        self.session = sessionmaker(bind=self.engine)

    def add_account(self, name, email, password, overrideKey):
        """
        Add a new account to the database.
        :param name: Name of user.
        :param email: Email of user.
        :param password: Password of user.
        :param overrideKey: Override key of user.
        :return: True if account was added.
        """
        session = self.session()
        try:
            new_account = Account(name=name, email=email, password=password, overrideKey =overrideKey)
            session.add(new_account)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()


    def get_all_accounts(self):
        """
        Get all accounts.
        :return: All accounts from database.
        """
        session = self.session()
        try:
            accounts = session.query(Account).all()
            return accounts
        except Exception as e:
            session.rollback()
            raise e
        finally: session.close()



    def get_account(self, username):
        """
        Get account by username.
        :param username: Username of user.
        :return: Account if found, otherwise "notfound".
        """
        session = self.session()
        try:
            account = session.query(Account).filter_by(email=username).one()
            return account
        except NoResultFound:
            return "notfound"
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()


    def get_account_by_username(self, username):
        """
        Get account password by username.
        :param username: Username of user.
        :return: Password if found, otherwise "notfound".
        """
        session = self.session()

        try:
            account = session.query(Account).filter_by(email=username).one()
            return account.password
        except NoResultFound:
            return "notfound"
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_account_by_password(self, overrideKey):
        """
        Get account password using overrideKey.
        :param overrideKey: Override key of user.
        :return: Password if found, otherwise "notfound".
        """
        session = self.session()
        try:
            account = session.query(Account).filter_by(overrideKey=overrideKey).one()
            return account.password
        except NoResultFound:
            return "notfound"
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()


    def get_name_by_email(self, username):
        """
        Get name of user by email.
        :param username: Email of user.
        :return: Name of user if found, otherwise "notfound".
        """
        session = self.session()

        try:
            account = session.query(Account).filter_by(email=username).one()
            return account.name
        except NoResultFound:
            return "notfound"
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()


