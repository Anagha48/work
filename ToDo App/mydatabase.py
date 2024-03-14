import sqlite3
class MyDatabase:
    def __init__(self):
        self.con=sqlite3.connect("mydatabase.db")
        print("connected")
        self.cur=self.con.cursor()
        print("cursor object created")
        sql="create table if not exists mybook(id integer primary key autoincrement,title varchar(1000),description varchar(1000),date DATE NOT NULL);"
        self.cur.execute(sql)
        print("table created")
        self.cur.execute("select * from mybook")
        print(self.cur.fetchall())

    def insert(self,sql):
        self.cur.execute(sql)
        self.con.commit()
        print("inserted")
    
    
    def view(self):
        self.cur.execute('select * from mybook')
        data = self.cur.fetchall()
        return data
    
    def update(self,sql):
        self.cur.execute(sql)
        self.con.commit()

    def delete(self,sql):
        self.cur.execute(sql)
        self.con.commit() 
        
    def selectone(self,sql):
        self.cur.execute(sql)
        d = self.cur.fetchone()
        print(d)
        return d
  

mydb=MyDatabase()