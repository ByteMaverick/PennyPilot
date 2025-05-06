from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.expense import Expense

class ExpenseDAO:
    """
    Expense Data Access Object to manipulate expense data in the SQLite database.
    """
    def __init__(self, db_url="sqlite:///../pennypilot.db"):
        self.engine = create_engine(db_url)

       # Call session() when needed
        self.session = sessionmaker(bind=self.engine)


    def add_expense(self, account_id, amount, date, category):
        """
        Add expense for a user to the database.
        :param account_id: ID of user's account.
        :param amount: Amount of expense.
        :param date: Data of expense.
        :param category: Category of expense.
        :return: None.
        """
        session = self.session()
        try:
            new_expense = Expense(account_id = account_id, amount = amount, date = date, category = category)
            session.add(new_expense)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()


    def get_user_expenses(self, account_id):
        """
        Get all expenses of a user.
        :param account_id: ID of user's account.
        :return: Expenses of a user.
        """
        session = self.session()
        try:
            user_expenses = session.query(Expense).filter_by(account_id = account_id).all()
            return user_expenses
        except Exception as e:
            session.rollback()
            raise e
        finally: session.close()


    # Retrieve all expenses
    def get_all(self):
        """
        Get all expenses in the database.
        :return: All expenses.
        """
        session = self.session()
        try:
            expenses = session.query(Expense).all()
            return expenses
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()


    def delete_all(self):
        """
        Delete all expenses in the database.
        :return: None.
        """
        session = self.session()
        try:
            session.query(Expense).delete()
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()