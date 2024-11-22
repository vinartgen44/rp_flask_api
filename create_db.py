import sqlite3

conn = sqlite3.connect("people.db")
print("Datebase created and opened successfully")

colums = [
    "id INTEGER PRIMARY KEY",
    "lname VARCHAR UNIQUE",
    "fname VARCHAR",
    "timestamp DATATIME",
]

create_table_cmd = f"CREATE TABLE people ({', '.join(colums)})"
conn.execute(create_table_cmd)
print("Table created successfully")

people = [
    "1, 'Fairy', 'Tooth', '2022-01-01 01:01:01'",
    "2, 'Ruprecht', 'Knecht', '2022-01-01 01:01:01'",
    "3, 'Bunny', 'Easter', '2022-01-01 01:01:01'",
]

for person in people:
    insert_cmd = f"INSERT INTO people VALUES ({person})"
    conn.execute(insert_cmd)

conn.commit()
print("Records created successfully")
cur = conn.execute("SELECT * FROM people")
people = cur.fetchall()
for person in people:
    print(person)


conn.close()
