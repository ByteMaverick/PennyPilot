from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker
from models.profile import Profile

class ProfileDAO:
    def __init__(self, db_url="sqlite:///../pennypilot.db"):
        self.engine = create_engine(db_url)

       # Call session() when needed
        self.session = sessionmaker(bind=self.engine)

    # Add new profile to database
    def add_profile(self, email, number, name):
        session = self.session()
        try:
            new_profile = Profile(email=email, number=number, name=name)
            session.add(new_profile)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    # Get profile name from database
    def get_profile(self, email, number):
        session = self.session()
        try:
            profile = session.query(Profile).filter_by(email=email, number=number).one()
            return profile.name
        except NoResultFound:
            return "notfound"
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()




