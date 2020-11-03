

from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import scoped_session, sessionmaker
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# para ejecutar SQL
db = scoped_session(sessionmaker(bind=engine))
db.execute("commit;")

# para usar pandas
df.to_sql('encimeras', con=engine)
da = pd.read_sql('encimeras', engine)


a=[{'email': 'hola@gmail.com', 'level': 0, 'username': None, 'id': 1}, {'email': 'a@gmail.com', 'level': 0, 'username': None, 'id': 2}]






import  PyMySQL
import pymysql


db=pymysql.connect("qado842.molorramo.com","qado842","Molorramo20","qado842") #This saves a connection object into db
cursor=db.cursor()
cursor.execute("SELECT VERSION()")

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'

mysql = MySQL(app)




