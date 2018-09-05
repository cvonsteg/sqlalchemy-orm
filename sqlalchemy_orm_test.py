from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json


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

# Create Session
Session = sessionmaker(bind=engine)
session = Session()
session.add(user_1)

# request rules api here
with open('test.json', 'r') as f:
    data = json.load(f)

rules = []
for rule in data.get('object'):
    id = rule.get('id')
    input = rule.get('input')
    output = rule.get('output')
    date_from = rule.get('date_from')
    date_to = rule.get('date_to')
    personell_v = data.get('reference')
    rules.append(UserRules(id=id, input=input, output=output, date_from=date_from, date_to=date_to, personnell_version=personell_v))

session.add_all(rules)