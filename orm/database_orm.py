# Using SQLAlchemy
import sqlalchemy

def getall(): # sample code to fetch data (from movies table) to use sql command
    engine = sqlalchemy.create_engine('sqlite:///movie.db', echo=True) # echo=True to show all the info log

    with engine.connect() as conn:
        results = conn.execute(sqlalchemy.text("SELECT * FROM Movies"))
        return results
    
def getall_new(): # sample code to use ORM to fetch the data (from movies table)
    engine = sqlalchemy.create_engine('sqlite:///movie.db', echo=True) # echo=True to show all the info log

    metadata = sqlalchemy.MetaData()

    movies_table = sqlalchemy.Table("Movies", metadata, 
                                    sqlalchemy.Column("Title", sqlalchemy.Text),
                                    sqlalchemy.Column("Director", sqlalchemy.Text),
                                    sqlalchemy.Column("Year", sqlalchemy.Integer))
    
    metadata.create_all(engine)

    with engine.connect() as conn:
        return conn.execute(sqlalchemy.select(movies_table))

def create_user_table(): # Create a user table (use Sql command)
    engine = sqlalchemy.create_engine('sqlite:///movie.db', echo=True) # echo=True to show all the info log

    with engine.connect() as conn:
        conn.execute(sqlalchemy.text('''CREATE TABLE IF NOT EXISTS Users (id integer primary key autoincrement, 
                                     first_name text, last_name text, email text)'''))
        conn.commit()

def insert_user(data): # insert record (use Sql command)
    engine = sqlalchemy.create_engine('sqlite:///movie.db', echo=True) # echo=True to show all the info log

    with engine.connect() as conn:
        insert_stmt = f'INSERT INTO Users (first_name, last_name, email) VALUES ("{data["firstName"]}", "{data["lastName"]}", "{data["email"]}")'
        print(insert_stmt)
        conn.execute(sqlalchemy.text(insert_stmt))
        conn.commit()
        
def get_all_users(): # get records (use Sql command)
    engine = sqlalchemy.create_engine('sqlite:///movie.db', echo=True) # echo=True to show all the info log
    with engine.connect() as conn:
        return conn.execute(sqlalchemy.text("SELECT * FROM Users")),

def insert_role_orm(data):
    engine = sqlalchemy.create_engine('sqlite:///movie.db')
    metadata = sqlalchemy.MetaData()
    user_tables = sqlalchemy.Table("roles", metadata,
                                   sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                                   sqlalchemy.Column("role_name", sqlalchemy.String),
                                   sqlalchemy.Column("dept_name", sqlalchemy.String),
                                   sqlalchemy.Column("role_desc", sqlalchemy.String),
                                   sqlalchemy.Column("is_active", sqlalchemy.Boolean)
                                )
    
    metadata.create_all(engine)

    with engine.connect() as conn:
        conn.execute(sqlalchemy.insert(user_tables).values(data))
        conn.commit()
    
def get_allrole_orm():
    engine = sqlalchemy.create_engine('sqlite:///movie.db')
    metadata = sqlalchemy.MetaData()
    user_tables = sqlalchemy.Table("roles", metadata,
                                   sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                                   sqlalchemy.Column("role_name", sqlalchemy.String),
                                   sqlalchemy.Column("dept_name", sqlalchemy.String),
                                   sqlalchemy.Column("role_desc", sqlalchemy.String),
                                   sqlalchemy.Column("is_active", sqlalchemy.Boolean)
                                )
    
    metadata.create_all(engine)

    with engine.connect() as conn:
        results = conn.execute(sqlalchemy.select(user_tables))
        conn.commit()
        return results