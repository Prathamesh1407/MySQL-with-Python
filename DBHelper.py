import mysql.connector as connector

class DBHelper:
    def __init__(self, ch, pword):
        self.con = connector.connect(
            host="localhost", port="3306", user="root", password=pword
        )
        cur = self.con.cursor()
        if ch == 0:
            Database = input("Enter Database name ")
            cur.execute("create database {}".format(Database))
        else:
            self.printDatabase()
            Database = input("\nEnter the Existing Database name ")
        self.con = connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password=pword,
            database=Database,
        )

    def insert_user(self, tname):
        cols = self.showColumns(tname)
        counter = 0
        ipt = []
        columns = []
        for col in cols:
            ip = input(col[0] + " : ")
            columns.append(col[0])
            ipt.append(ip)
        length = len(columns)
        query1 = "insert into {} values(".format(tname)
        while length > 0:
            if length == 1:
                query1 += "%s"
            else:
                query1 += "%s,"
            length = length - 1
        query1 += ")"
        cur = self.con.cursor()
        cur.execute(query1, ipt)
        self.con.commit()
        print("-----------Inserted In DB------------")

    def fetch_all(self, tname):
        col = self.showColumns(tname)
        query = "SELECT * FROM {}".format(tname)
        cur = self.con.cursor()
        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        columns = [str(column[0]) for column in col]
        columns = "   ".join(columns)
        print(columns)
        print("")
        for row in result:
            print(row)
        print("")

    def delete_user(self, tname):
        self.fetch_all(tname)
        delC = input("\nBy which column do you want to Delete the Entry ")
        dele = input("Enter {} value to delete ".format(delC))
        query = "delete from {} where {}='{}'".format(tname, delC, dele)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()  # if we do not commit it the data will get delete temporarily
        print("----------Deleted from DB-----------")

    def update_user(self, tname):
        self.fetch_all(tname)
        updC = input("\nIn which column do you want to Update the Entry ")
        upde = input("Enter {} value to update ".format(updC))
        conC = input("By which column you want to set a condition ")
        cone = input("Enter {} value to apply a condition ".format(conC))
        query = "update {} set {}='{}' where {}='{}'".format(
            tname, updC, upde, conC, cone
        )
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("-----------Updated-----------")

    def delete_all(self, tname):
        query = "delete from {}".format(tname)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def search(self, tname):
        self.fetch_all(tname)
        seaC = input("\nBy which column do you want to Search the Entry ")
        seae = input("Enter {} value to Search ".format(seaC))
        query = "select * from {} where {}='{}'".format(tname, seaC, seae)
        cur = self.con.cursor()
        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        print()
        for row in result:
            print(row)
        print()

    def create(self, tname):
        print("How many columns you want to add in table")
        count = int(input())
        query = "create table {} ({} {})".format(
            tname, input("Enter column name : "), input("Enter Data type of column : ")
        )
        cur = self.con.cursor()
        cur.execute(query)
        self.add(count - 1, tname)
        self.con.commit()

    def printDatabase(self):
        cur = self.con.cursor()
        print("These are your Exisiting Databases\n")
        cur.execute("show databases")
        for databases in cur:
            print(databases[0])

    def printTables(self):
        cur = self.con.cursor()
        print("These are your Exisiting Tables\n")
        cur.execute("show tables")
        for tables in cur:
            print(tables[0])

    def add(self, count, table):
        while count > 0:
            query = "alter table {} add column {} {}".format(
                table, input("Enter column name "), input("Enter Data type of column ")
            )
            cur = self.con.cursor()
            cur.execute(query)
            count = count - 1

    def showColumns(self, tname):
        cur = self.con.cursor()
        cur.execute("desc {}".format(tname))
        col = []
        for cols in cur.fetchall():
            col.append(cols)
        cur.close()
        return col

    def addAtri(self, tname):
        cur = self.con.cursor()
        cname = input("Enter column name to be added with a Constraint ")
        pname = input("Enter constraint to be added to {} ".format(cname))
        query = "alter table {} add constraint {} ({})".format(tname, pname, cname)
        cur.execute(query)
        cur.close()
        print("---------Constraint Added---------")

    def delAtri(self, tname):
        cur = self.con.cursor()
        pname = input("Enter column name in which you want to delete the constraint ")
        query = "alter table {} drop constraint {}".format(tname, pname)
        print(query)
        cur.execute(query)
        cur.close()
        print("---------Constraint Removed---------")
        
    def forKey(self,tname):
        self.printTables()
        cur=self.con.cursor()
        pname=input("Enter existing table you want to apply foreign key (parent table) ")
        pcname=input("Enter the column name that's primary key you want to point (parent table column) ")
        cname=input("Enter name of child table or current table")
        query="alter table {} add foreign key ({}) references {} ({})".format(tname,cname,pname,pcname)
        cur.execute(query)
        cur.close()

