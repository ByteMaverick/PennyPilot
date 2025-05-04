from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.bank_records import BankRecords

class BankRecordsDAO:
    def __init__(self, db_url="sqlite:///../pennypilot.db"):
        self.engine = create_engine(db_url)

       # Call session() when needed
        self.session = sessionmaker(bind=self.engine)

    # Add updated balance for a user
    def  add_record(self, id,timestamp, description, credit,debit, actionId,balance,category):

        session = self.session()
        try:
            new_record = BankRecords(id= id, timestamp = timestamp, description = description, credit =credit, debit = debit, actionId = actionId, balance = balance, category = category  )
            session.add(new_record)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_all_records(self):
        session = self.session()
        try:
            record_history = session.query(BankRecords).all()
            return record_history
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_ids(self):
        session = self.session()
        try:
            existing_ids = set(r[0] for r in session.query(BankRecords.id).all())
            return existing_ids
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_actionIds(self):
        session = self.session()
        try:
            existing_actionIds = set(r[0] for r in session.query(BankRecords.actionId).all())
            return existing_actionIds
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_all(self):
        session = self.session()
        try:
            record_history = session.query(BankRecords).all()
            return record_history
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def delete_all(self):
        session = self.session()
        try:
            session.query(BankRecords).delete()
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

