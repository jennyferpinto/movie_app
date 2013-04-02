from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

ENGINE = None
Session = None

Base = declarative_base()

### Class declarations go here
class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key = True)
	age = Column(Integer, nullable = True)
	gender = Column(String(2), nullable = True)
	occupation = Column(String(64), nullable = True)
	zipcode = Column(String(15), nullable = True)

class Movies(Base):
	__tablename__ = "movies"

	id = Column(Integer, primary_key = True)
	name = Column(String(140))
	released_at = Column(String(64))
	imdb_url = Column(String(300))

class Ratings(Base):
	__tablename__ = "ratings"

	id = Column(Integer, primary_key = True)
	user_id = Column(Integer(64))
	movie_id = Column(Integer(64))
	rating = Column(Integer(64))


### End class declarations

def connect():
	global ENGINE
	global Session

	ENGINE = create_engine("sqlite:///ratings.db", echo = True)
	Session = sessionmaker(bind=ENGINE)

	return Session()

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
