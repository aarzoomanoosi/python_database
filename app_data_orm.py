import orm.database_orm

database_orm = orm.database_orm

# print('-------------------------------------------- ORM Test (Movies) --------------------------------------------')
# results = database_orm.getall()
# # rercords = results.fetchall()
# # print(f'Total records: {len(rercords)}')
# # for row in rercords:
# #     print(row)

# results = database_orm.getall_new()
# rercords = results.fetchall()
# print(f'Total records: {len(rercords)}')
# for row in rercords:
#     print(row)

print('-------------------------------------------- ORM Test (Users) --------------------------------------------')
database_orm.create_user_table()
# insert to user table
database_orm.insert_user({
    'firstName': 'Aarzoo1',
    'lastName': 'Manoosi1',
    'email': 'aarzoo1_manoosi1@abc.com'
})
# get all users
results = database_orm.get_all_users()
for row in results:
    print(row.fetchall())

print('-------------------------------------------- ORM Test (Create_Insert_Get) --------------------------------------------')
# insert to role table
database_orm.insert_role_orm([{
    'role_name': 'admin',
    'dept_name': 'Cloud',
    'role_desc': 'admin of the department',
    'is_active': True
}])
# get all roles
results = database_orm.get_allrole_orm()

for row in results:
    print(row)