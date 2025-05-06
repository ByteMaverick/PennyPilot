from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.balance import Balance

class BalanceDAO:
    def __init__(self, db_url="sqlite:///../pennypilot.db"):
        self.engine = create_engine(db_url)

       # Call session() when needed
        self.session = sessionmaker(bind=self.engine)

    # Add updated balance for a user
    def add_balance(self, account_id, date, amount):
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

    # Retrieve balance history for a user
    def get_balance_history(self, account_id):
        session = self.session()
        try:
            balance_history = session.query(Balance).filter_by(account_id = account_id).all()
            return balance_history
        except Exception as e:
            session.rollback()
            raise e
        finally: session.close()

    def delete_all(self):
        session = self.session()
        try:
            session.query(Balance).delete()
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()