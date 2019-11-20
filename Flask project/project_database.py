from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base=declarative_base()

class Register(Base):
	__tablename__='register'

	id=Column(Integer,primary_key=True)
	name=Column(String(250),nullable=False)
	surname=Column(String(100),nullable=False)
	regd_no=Column(String(50),nullable=False)
	mobile=Column(String(20),nullable=False)
	branch=Column(String(100),nullable=False)
	email=Column(String(250),nullable=False)

engine= create_engine('sqlite:///bvc.db')
Base.metadata.create_all(engine)
print("Data base is created!!!")