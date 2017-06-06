'''
Created on May 29, 2017

@author: duncan

Show how to make initite connection to mysql using sqlalchemy, and to execute simple insert and select query
'''

from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import text
from sqlalchemy.sql.functions import func, user
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

'''
 create_engine() returns instance of engine, echo parameter allows for sqlalchemy to be verbose in its logs
 declarative_base() returns repositiry that allows to register domain entities
 sessionmaker() returns session which is the major object to interface with the database.
'''
engine = create_engine("mysql://root:password@localhost:3306/customercaredb", echo=True)
base= declarative_base()
Session = sessionmaker(bind=engine)

'''
one to many relationship
'''
class User(base):
    __tablename__= "user2"
    id = Column(Integer,primary_key=True)
    firstName= Column(String(50))
    secondName=Column(String(50))
    address= relationship("Address")
    
class Address(base):
    __tablename__="Address"
    id= Column(Integer,primary_key=True)
    email_address= Column(String(20))
    user_id= Column(Integer,ForeignKey('user2.id'))

base.metadata.create_all(engine)

session = Session()

userOne= User(firstName='Purity',secondName='Ndiithi')
userOne.address=[Address(email_address="duncan@mail.com")]
userTwo= User(firstName='Whake',secondName='Light')
userTwo.address=[Address(email_address="Whake@mail.com")]
userThree = User(firstName='Schole',secondName='Timothy')
userThree.address=[Address(email_address="schole@mail.com")]


session.add(userOne)
session.add(userOne)
session.add(userTwo)
session.add(userThree)
'''

session.commit()

'''

'''
filter_by(),  uses keyword arguments - takes only one argument
filter(), which uses more flexible SQL expression language constructs
'''

for instance in session.query(User).filter_by(firstName='Duncan').order_by(User.id).all():
     print(instance.secondName, instance.firstName)

print("\nUsing query parameters\n")

for instance in session.query(User).filter(text('firstName=:value and secondName=:name')).params(value='Duncan', name='Ndiithi').order_by(User.id).all():
     print(instance.secondName, instance.firstName)

print("\nUsing entirely string-based statement\n")

for instance in session.query(User).from_statement(text('select * from user2 where firstName=:para1')).params(para1='Mercy'):
     print(instance.secondName, instance.firstName)

print("\nMatching table columns to entity attributes \n")
     
stmt = text("SELECT id, firstName,secondName FROM user2 where firstName=:name")
stmt = stmt.columns(User.id, User.secondName, User.firstName)

for instance in session.query(User).from_statement(stmt).params(name='Duncan').all():
    print(instance.secondName, instance.firstName)

print("Counting records")

totalUsers=session.query(User).count()
print(totalUsers)


print("Counting individual records")

idCount=session.query(func.count(User.id)).scalar()
print(idCount)


print("\nQuering with joins\n")

for instance in session.query(User.firstName,User.secondName,Address.email_address).join(Address).all():
     print(instance.secondName, instance.firstName,instance.email_address)
     
print("\nQuering with joins\n")
    
for i,a in session.query(User,Address).join(Address).all():
     print(i.secondName, i.firstName,a.email_address)

