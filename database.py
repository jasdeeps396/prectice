import sqlite3
class Database:
    table='expenses'
    def __init__(self,name='mydb.sqlite3'):
        self.con=sqlite3.connect(name)
        print('connected')
    
    def run(self,query):
        try:
            self.con.execute(query)
            
            self.con.commit() 
            return True
        except Exception as e:
            print(query,e)
            return False

    
    def create_table(self):
        query="""
            CREATE TABLE expenses(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item TEXT,
                price DOUBLE
            )
        """
        return self.run(query)
    
    def add(self,item,price):
        query=f"""
            INSERT INTO {self.table} VALUES(
                null,
                '{item}',
                {price}
            )
        """ 
        return self.run(query)

    def delete(self,id):
        query =f"""
            DELET FROM {self.table} WHERE id ={id}
        """
        return self.run(query)
    
    def view(self):
        query=f" SELECT * FROM {self.table}"
        try:
            result=self.con.execute(query)
            return result.fetchall()
        except Exception as e:
            print('error')
            print(e)