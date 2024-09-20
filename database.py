import mysql.connector as sql
mydb=sql.connect(host="localhost",user="root",passwd="1260741", database="bank")
cursor=mydb.cursor()
def createcustomertable():
    cursor.execute("create table if not exists customers(username varchar(20) not null, password varchar(20) not null, name varchar(20) not null, age integer not null,city varchar(20) not null, balance integer not null,  account_number integer, status boolean)")
mydb.commit()
def query(q):
    cursor.execute(q)
    result=cursor.fetchall()
    mydb.commit()
    return result

if __name__=="__main__":
    createcustomertable()