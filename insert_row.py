#  Insert 10 rows in each table.

from sqlalchemy import create_engine, MetaData
from sqlalchemy import insert

engine = create_engine('postgresql://postgres:jaya24@localhost/firstdb', echo=True)
meta = MetaData()

statement = "INSERT INTO company (company_id, company_name, location) VALUES ('10001', 'Saturam', 'Bangalore')"
engine.execute(statement)

statement = "INSERT INTO user_data (user_id, user_name, company_id, joining_date) VALUES ('20006', 'Karthi','10005', '31/10/2020')"
engine.execute(statement)
