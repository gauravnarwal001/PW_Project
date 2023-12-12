import mysql.connector as c

mydb = c.connect(host = "localhost",
                      user = 'root',
                      password = 'gaurav123456'
                      )

db = mydb.cursor()







# lst = ['abc','abcd','bank','ankit','bro','gauravnarwal','mohit','nahi','pagal','ra','rahul']
# for i in lst:
#     a = f'drop database {i}'
#     db.execute(a)



# db.execute('show databases')
# lst = []
# for i in db:
#     lst.append(i)
#     print(i)

# db.execute('show databases')
# lst = []
# for i in db:
#     for j in i:
#         print(j)

# db.execute('use gaurav1')
# table = f"create table gaurav3(name varchar (50), number int (50),datetime datetime)"
# db.execute(table)
# db.execute('show tables')
# for i in db:
#     print(i)


# db.execute(f'insert into gaurav1 values("rahul",54238846)')
# mydb.commit()
# db.execute(f'select * from gaurav1')
# db.fetchall()
# print(db.fetchall())
# db.execute('desc gaurav1')
# for i in db:
#     print(i)

# db.execute('use narwal')
# db.execute('desc class1')
# result = db.fetchall()
# # for i in result:
# #     print(i[0])
# print(result)

# db.execute('insert into class values ('Gaurav',1,123,41)')
# db.commit()
db.execute('use narwal')
db.execute("INSERT INTO class VALUES ('narwal1', 1, 123, 41)")
mydb.commit()
