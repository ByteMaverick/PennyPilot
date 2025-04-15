from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.category import Category

class CategoryDAO:
    def __init__(self, db_url="sqlite:///../pennypilot.db"):
        self.engine = create_engine(db_url)

       # Call session() when needed
        self.session = sessionmaker(bind=self.engine)

    # Add category for a user
    def add_category(self, account_id, name):
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

    # Retrieve a user's categories
    def get_user_categories(self, account_id):
        session = self.session()
        try:
            user_categories = session.query(Category).filter_by(account_id = account_id).all()
            return user_categories
        except Exception as e:
            session.rollback()
            raise e
        finally: session.close()