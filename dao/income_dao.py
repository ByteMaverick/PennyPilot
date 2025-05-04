from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.income import Income

class IncomeDAO:
    def __init__(self, db_url="sqlite:///../pennypilot.db"):
        self.engine = create_engine(db_url)

       # Call session() when needed
        self.session = sessionmaker(bind=self.engine)

    # Add new income for a user
    def add_income(self, account_id, amount, date, category):
        session = self.session()
        try:
            new_income = Income(account_id = account_id, amount = amount, date = date, category = category)
            session.add(new_income)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    # Retrieve all incomes of a user
    def get_user_incomes(self, account_id):
        session = self.session()
        try:
            user_incomes = session.query(Income).filter_by(account_id = account_id).all()
            return user_incomes
        except Exception as e:
            session.rollback()
            raise e
        finally: session.close()

    def delete_all(self):
        session = self.session()
        try:
            session.query(Income).delete()
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()