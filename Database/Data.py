import sqlite3

class Data:
    def __init__(self):
        self.connection = sqlite3.connect("Database.db")
        self.conn = self.connection.cursor()

    def extractData(self, value):
        self.conn.execute(value)
        rows = self.conn.fetchall()
        return rows
    
    def editData(self, value):
        self.conn.execute(value)
    
    def removeData(self, value):
        self.conn.execute(value)
    
    def closeConnection(self):
        self.conn.close()