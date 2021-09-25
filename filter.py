# Get the data by giving user_id/company_id using filter.

from sqlalchemy import create_engine, MetaData

engine = create_engine('postgresql://postgres:jaya24@localhost/firstdb', echo=True)
stmt = "Select * from company inner Join user_data on company.company_id=user_data.company_id"
stmt2 ="Select * from company left Join user_data on company.company_id=user_data.company_id"
stmt3 = "Select * from company full outer Join user_data on company.company_id=user_data.company_id"
stmt4 = "Select * from user_data where user_id in (20001, 20002)"
rs = engine.execute(stmt)
for r in rs:
     print(r)
rs = engine.execute(stmt2)
for r in rs:
     print(r)
rs = engine.execute(stmt3)
for r in rs:
     print(r)
rs = engine.execute(stmt4)
for r in rs:
     print(r)