from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.expense import Expense

class ExpenseDAO:
    def __init__(self, db_url="sqlite:///../pennypilot.db"):
        self.engine = create_engine(db_url)

       # Call session() when needed
        self.session = sessionmaker(bind=self.engine)

    # Add new expense for a user
    def add_expense(self, account_id, amount, date, category):
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

    # Retrieve all expenses of a user
    def get_user_expenses(self, account_id):
        session = self.session()
        try:
            user_expenses = session.query(Expense).filter_by(account_id = account_id).all()
            return user_expenses
        except Exception as e:
            session.rollback()
            raise e
        finally: session.close()

    def delete_all(self):
        session = self.session()
        try:
            session.query(Expense).delete()
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()