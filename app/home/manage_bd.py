

from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import scoped_session, sessionmaker
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# para ejecutar SQL
db = scoped_session(sessionmaker(bind=engine))
db.execute("commit;")

# para usar pandas
df.to_sql('usuarios2', con=engine, if_exists="replace", index_label = "ID")
da = pd.read_sql('usuarioss', engine)

username =["Angel", "Javier", "Mari Luz"]
email = ["angel.r.chicote@gmail", "javier@molorramo.com","mariluz@molorramo.com"]
level = [10, 9,9]
password = [hash_pass("hola1919"), hash_pass("Molo2020"), hash_pass("Molo2020")]
id=[0,1,2]


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

CREATE TABLE usuarios (
    ID int NOT NULL,
    USERNAME varchar(255) NOT NULL,
    EMAIL varchar(255),
    LEVEL int default 0,
    PRIMARY KEY (ID),
    PASSWORD BINARY
);

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
