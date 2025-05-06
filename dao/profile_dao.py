from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker
from models.profile import Profile

class ProfileDAO:
    """
    Profile Data Access Object to manipulate profile data in the SQLite database.
    """
    def __init__(self, db_url="sqlite:///../pennypilot.db"):
        self.engine = create_engine(db_url)

       # Call session() when needed
        self.session = sessionmaker(bind=self.engine)


    def add_profile(self, email, number, name):
        """
        Add new profile fo a user to the database.
        :param email: Email of a user.
        :param number: Profile number.
        :param name: Name of the new profile.
        :return: True if profile added.
        """
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


    def get_profile(self, email, number):
        """
        Get profile name from database.
        :param email: Email of user.
        :param number: Profile number.
        :return: Name of profile if exists, otherwise "notfound"
        """
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




