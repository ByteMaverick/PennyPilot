from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.account import Account

class AccountDAO:
    def __init__(self, db_url="sqlite:///../pennypilot.db"):
        self.engine = create_engine(db_url)

       # Call session() when needed
        self.session = sessionmaker(bind=self.engine)

    # Add new user account to database
    def add_account(self, name, email, password):
        session = self.session()
        try:
            new_account = Account(name=name, email=email, password=password)
            session.add(new_account)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    # Retrieve all user accounts from database
    def get_all_accounts(self):
        session = self.session()
        try:
            accounts = session.query(Account).all()
            return accounts
        except Exception as e:
            session.rollback()
            raise e
        finally: session.close()


