import sqlite3
import pandas
import pyfiglet
from os import system
from sys import platform

def clearscreen():
    if platform == "linux" or platform == "linux2" or "darwin":
        system('clear')
    elif platform == "win32":
        system('cls')

clearscreen()

def create(db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (id INTEGER PRIMARY KEY AUTOINCREMENT,items TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(db,item,quantity,price):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    try:
        cur.execute("INSERT INTO store (items,quantity,price) VALUES (?,?,?)",(item,quantity,price))
        conn.commit()
    except sqlite3.OperationalError:
        print("create a database first")
    conn.close()
def view(db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    data = pandas.DataFrame(rows, columns=["S.No","ITEM","QTY","PRICE"])
    data = data.set_index('S.No')
    return data
def delete(db,item):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE id=?",(item,))
    conn.commit()
    conn.close()
def update(db,quantity,price,item):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE id=?",(quantity,price,item,))
    conn.commit()
    conn.close()

inp = 1
db=""

print("Enter Name Of Your Database or press 1 to create new")
op = input()
if op=="1":
    print("Enter Name Of Your New Database")
    dbn = input()
    db=dbn+".db"
    create(db)
else:
    db=op+".db"

while inp!=5:
    clearscreen()
    covart = pyfiglet.figlet_format("StoreDB")
    print(covart+"                                    ᵇʸ ᶻᵃᶦⁿ ˢʰᵃᶦᵏʰ")
    print("SELECT an Option")
    print("----------------------")
    print("1. INSERT into table")
    print("2. Show Table")
    print("3. Delete Entry")
    print("4. Update Entry")
    print("5. Exit")
    print("----------------------")

    print("\nEnter You Choice:")
    try:
        inp = int(input())
        if inp==1:
            print("Enter the Item Name")
            it = input()
            print("Enter Quantity")
            qty = int(input())
            print("Enter Price")
            prc = float(input())
            insert(db,it,qty,prc)

        elif inp==2:
            print("-------------------------")
            print(view(db))
            print("\nPress Enter To Continue")
            wait = input()

        elif inp==3:
            print(view(db))
            print("\nEnter S.No. of item to delete")
            item = int(input())
            delete(db,item)

        elif inp==4:
            print(view(db))
            print("\nEnter S.No. of item to update")
            item = int(input())
            print("Enter New Quantity")
            qty = int(input())
            prc = float(input())
            update(db,qty,prc,item)

        elif inp==5:
            print("Program Exited Successfully")

        else:
            print("Wrong Input: %s"%inp)
            print("Press Enter To Continue")
            input()
    except:
        print("Wrong Input Recieved. Press Enter To Continue")
        input()
