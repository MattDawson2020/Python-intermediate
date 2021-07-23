import psycopg2
from dotenv import load_dotenv
load_dotenv()
import os
password = os.environ.get("db_pass")


def create_table():
    conn = psycopg2.connect(f"dbname='database1' user='postgres' password={password} host='localhost' port='5432'")
    #if db exists this connects to it, if not it creates the DB
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    # unlike postgreSQL you have to explicitly commit changes
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect(f"dbname='database1' user='postgres' password={password} host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s, %s, %s)", (item, quantity, price))
    # ? ? ? syntax is meant to be a best practice
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect(f"dbname='database1' user='postgres' password={password} host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    ## unlike postgress where you save to a result and map to a returned object, you can use builtin fetchall to return a list
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect(f"dbname='database1' user='postgres' password={password} host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update(item, quantity, price):
    conn = psycopg2.connect(f"dbname='database1' user='postgres' password={password} host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store  SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()


create_table()
insert('Wine Glass', 8, 10.5)
insert('Mug', 10, 4)
print(view())

delete('Wine Glass')
print(view())

update('Mug', 3, 5)
print(view())