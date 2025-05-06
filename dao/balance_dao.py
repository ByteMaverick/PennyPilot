from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.balance import Balance

class BalanceDAO:
    """
    Balance Data Access Object to manipulate balance data in SQLite database.
    """
    def __init__(self, db_url="sqlite:///../pennypilot.db"):
        self.engine = create_engine(db_url)

       # Call session() when needed
        self.session = sessionmaker(bind=self.engine)


    def add_balance(self, account_id, date, amount):
        """
        Add balance for a user to the database.
        :param account_id: ID of the user's account.
        :param date: Date of balance.
        :param amount: Amount of balance.
        :return: None.
        """
        session = self.session()
        try:
            new_balance = Balance(account_id = account_id, date = date, amount = amount)
            session.add(new_balance)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()



    def get_balance_history(self, account_id):
        """
        Get balance history for a user,
        :param account_id: ID of user's account.
        :return: Balance history of a user.
        """
        session = self.session()
        try:
            balance_history = session.query(Balance).filter_by(account_id = account_id).all()
            return balance_history
        except Exception as e:
            session.rollback()
            raise e
        finally: session.close()


    def delete_all(self):
        """
        Delete all balances.
        :return: None.
        """
        session = self.session()
        try:
            session.query(Balance).delete()
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()