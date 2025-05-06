from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.bank_records import BankRecords

class BankRecordsDAO:
    """
    Balance Records Data Access Object to manipulate bank records data in SQLite database.
    """
    def __init__(self, db_url="sqlite:///../pennypilot.db"):
        self.engine = create_engine(db_url)

       # Call session() when needed
        self.session = sessionmaker(bind=self.engine)


    def  add_record(self, id,date, description, credit,debit, actionId,balance,category):
        """
        Add updated bank record for a user to the database.
        :param id: ID of bank record.
        :param date: Date of bank record.
        :param description: Description of bank record.
        :param credit: Whether credit.
        :param debit: Whether debit.
        :param actionId: Action id of bank record.
        :param balance: Balance of bank record.
        :param category: Category of bank record.
        :return: None.
        """

        session = self.session()
        try:
            new_record = BankRecords(id= id, date = date, description = description, credit =credit, debit = debit, actionId = actionId, balance = balance, category = category  )
            session.add(new_record)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()


    def get_all_records(self):
        """
        Get all bank records.
        :return: Record history.
        """
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
        """
        Get existing IDs of all bank records in database.
        :return: All existing IDs of bank records.
        """
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
        """
        Get existing actionIds of all bank records in database.
        :return: All existing actionIds of bank records.
        """
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
        """
        Get all bank records.
        :return: History of all bank records.
        """
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
        """
        Delete all bacnk records from database.
        :return: None.
        """
        session = self.session()
        try:
            session.query(BankRecords).delete()
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

