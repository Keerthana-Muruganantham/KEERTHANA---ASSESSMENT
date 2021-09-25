#  Create engine by giving postgres connection string and
#  create the table with given data types using SQLAlchemy.

from datetime import date
from sqlalchemy import create_engine
from sqlalchemy import MetaData,Table, Column, String, Integer, Date, ForeignKey
engine = create_engine('postgresql://postgres:jaya24@localhost/firstdb', echo=True)
meta = MetaData()

class Company():
    def companytable(self):
        students = Table(
            'company', meta,
            Column('company_id', Integer, primary_key=True),
            Column('company_name', String),
            Column('location', String),
        )
        students.create( bind=engine)

class User():
    def usertable(self):
        stmt = "Create table user_data (user_id int primary key, user_name varchar(255), company_id int, joining_date Date, foreign key (company_id) references company(company_id))"

        engine.execute(stmt)


compobj = Company()
compobj.companytable()
userobj = User()
userobj.usertable()