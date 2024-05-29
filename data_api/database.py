# Inserting single record or multipel records to table in sqlite database
# Fetching all records or per where clause from table in sqlite database
# Using Python Data Api
import sqlite3

def create_movie_table(): #create a movie table
    connection = sqlite3.connect("movie.db")
    cursor = connection.cursor()

    # Create a table
    cursor.execute('CREATE TABLE IF NOT EXISTS Movies (Title TEXT, Director TEXT, Year INT)') 

    connection.commit()
    connection.close()

def insert(table, data): # insert record(s) to the table
    if table is None or data is None:
        print('Either table or data is null')    

    connection = sqlite3.connect("movie.db")
    cursor = connection.cursor()       

    if type(data) is list: # if data has array of objects
        moviedata = []        
        for d in data:
            moviedata.append((d["Title"], d["Director"], d["Year"]))
        # print('************ ', moviedata)
        cursor.executemany(f'INSERT INTO {table} VALUES (?, ?, ?)', moviedata)
    else: # if data has single object
        cursor.execute(f"INSERT INTO {table} VALUES (?, ?, ?)", (data["Title"], data["Director"], data["Year"]))

    connection.commit()
    connection.close()

def getall(table): # get all records
    connection = sqlite3.connect("movie.db")
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {table}')
    data = cursor.fetchall()
    connection.close()
    return data

def get(table, year): # get record per year
    connection = sqlite3.connect("movie.db")
    cursor = connection.cursor()
    release_year = (2024,)
    cursor.execute(f"SELECT * FROM {table} WHERE Year=?", release_year)
    data = cursor.fetchall()
    connection.close()
    return data
