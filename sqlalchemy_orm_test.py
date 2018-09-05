from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()

class UserRules(Base):
    __tablename__ = 'user_rules'

    id = Column(Integer, primary_key=True)
    input = Column(String)
    output = Column(String)
    date_from = Column(String)
    date_to = Column(String)
    personnell_version = Column(String)

Base.metadata.create_all(engine)

# create instance
user_1 = UserRules(input='Adamm', output='Adam')
user_1.input
user_1.output

# Create Session
Session = sessionmaker(bind=engine)
session = Session()
session.add(user_1)

u = session.query(UserRules).first()

u.input
