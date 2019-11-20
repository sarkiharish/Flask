from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base=declarative_base()

class Register(Base):
	__tablename__='Teacher_information'

	id=Column(Integer,primary_key=True)
	NAME=Column(String(250),nullable=False)
	SURNAME=Column(String(100),nullable=False)
	QUALIFICATION=Column(String(50),nullable=False)
	MOBILE=Column(String(20),nullable=False)
	BRANCH=Column(String(100),nullable=False)
	YEAR_OF_EXPERIENCE=Column(String(20),nullable=False)

engine= create_engine('sqlite:///teacher.db')
Base.metadata.create_all(engine)
print("Data base is created!!!")