from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.category import Category

class CategoryDAO:
    """
    Category Data Access Object to manipulate category data in the SQLite database.
    """
    def __init__(self, db_url="sqlite:///../pennypilot.db"):
        self.engine = create_engine(db_url)

       # Call session() when needed
        self.session = sessionmaker(bind=self.engine)


    def add_category(self, account_id, name):
        """
        Add a new category for a user to the database.
        :param account_id: ID of a user's account.
        :param name: Name of a user's account.
        :return: None.
        """
        session = self.session()
        try:
            new_category = Category(account_id = account_id, name = name)
            session.add(new_category)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()


    def get_user_categories(self, account_id):
        """
        Get a user's categories from the database.
        :param account_id: ID of a user's account.
        :return: Categories of a user's account.
        """
        session = self.session()
        try:
            user_categories = session.query(Category).filter_by(account_id = account_id).all()
            return user_categories
        except Exception as e:
            session.rollback()
            raise e
        finally: session.close()


    def delete_all(self):
        """
        Delete all categories from the database.
        :return: None.
        """
        session = self.session()
        try:
            session.query(Category).delete()
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()