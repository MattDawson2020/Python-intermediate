import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db")
    #if db exists this connects to it, if not it creates the DB
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    # unlike postgreSQL you have to explicitly commit changes
    conn.close()

def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?, ?, ?)", (item, quantity, price))
    # ? ? ? syntax is meant to be a best practice
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    ## unlike postgress where you save to a result and map to a returned object, you can use builtin fetchall to return a list
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()

def update(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store  SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    conn.commit()
    conn.close()

# insert('Wine Glass', 8, 10.5)
# insert('Mug', 10, 4)

print(view())
delete('Wine Glass')
print(view())

update('Mug', 3, 5)
print(view())