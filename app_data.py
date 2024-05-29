import seed_data
import data_api.database

database = data_api.database

database.create_movie_table()

data = seed_data.getdata()
# print to check data has been retrieved or not
# print('**** Print seed data **** \n', data)

# insert movie record to Movie table
database.insert('Movies', data)
moviedata = database.getall('Movies')

print('-------------------------------------------- Data Api Test (Movies) --------------------------------------------')
print(f'Total movies: {len(moviedata)}')

movie_2024 = database.get('Movies', 2024)
print(movie_2024)
print(f"Total movies of year (2024): {len(movie_2024)}")

