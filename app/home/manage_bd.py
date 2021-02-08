

from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import scoped_session, sessionmaker,clear_mappers
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# para ejecutar SQL
db = scoped_session(sessionmaker(bind=engine))
db.execute("commit;")

# para usar pandas
df.to_sql('usuarios', con=engine, if_exists="replace", index_label = "ID")
pedidos = pd.read_sql('usuarios', engine)
data = pd.merge(pedidos, usuarios, left_on='id_cliente', right_on='id', how="inner")

username =["Angel", "Javier", "Mari Luz"]
email = ["angel.r.chicote@gmail", "javier@molorramo.com","mariluz@molorramo.com"]
level = [10, 9,9]
password = [hash_pass("hola1919"), hash_pass("Molo2020"), hash_pass("Molo2020")]
id=[0,1,2]
from sqlalchemy.orm import mapper, sessionmaker
metadata = MetaData(engine)
from sqlalchemy import Column, Integer


Session = sessionmaker(bind=engine)
session = Session()


df = pd.DataFrame(list(zip(username, email,level,password)),
               columns =[ 'username',"email", "level", "password"])

a=[{'email': 'hola@gmail.com', 'level': 0, 'username': None, 'id': 1}, {'email': 'a@gmail.com', 'level': 0, 'username': None, 'id': 2}]






import  PyMySQL
import pymysql

db=pymysql.connect("qado842.molorramo.com","qado842","Molorramo20","qado842") #This saves a connection object into db

host = "qado842.molorramo.com"
user = "qado842"
password = "Molorramo20"
database = "qado842"



cursor=db.cursor()
cursor.execute("drop table usuarios;")


a=cursor.execute("select * from usuarios;")

from sqlalchemy import create_engine,Table, Column, Integer, String, MetaData,Binary
engine = create_engine('sqlite:///college.db', echo = True)
engine = create_engine("mysql://qado842:Molorramo20@qado842.molorramo.com/qado842", encoding='latin1', echo=True)
meta = MetaData()

usuarios = Table('usuarios', meta,
   Column('id', Integer, primary_key = True),
   Column('email', String),
   Column('username', String),
   Column("password", Binary),
   Column("level" , Integer, nullable=True, default=0)
)

meta.create_all(engine)
