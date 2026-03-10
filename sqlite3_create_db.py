# import sqlite3

# conn = sqlite3.connect("qr.db")
# c = conn.cursor()

# c.execute("""
# CREATE TABLE IF NOT EXISTS qr_codes(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# code TEXT,
# destination TEXT,
# created_at TEXT
# )
# """)

# c.execute("""
# INSERT INTO qr_codes(code,destination,created_at)
# VALUES ('test123','https://google.com','2026-03-09')
# """)

# conn.commit()
# conn.close()

# print("Table created successfully")



import sqlite3

conn = sqlite3.connect("qr.db")
c = conn.cursor()
import os
print(os.path.abspath("qr.db"))
c.executescript("""

CREATE TABLE IF NOT EXISTS qr_codes(
id INTEGER PRIMARY KEY AUTOINCREMENT,
code TEXT,
destination TEXT,
created_at TEXT
);

CREATE TABLE IF NOT EXISTS visits(
id INTEGER PRIMARY KEY AUTOINCREMENT,
qr_id INTEGER,
ip TEXT,
device TEXT,
time TEXT
);

INSERT INTO qr_codes(id,destination)
VALUES(26,'https://ramadan-nice-kareem-11.netlify.app/');
""")

conn.commit()
conn.close()

print("Database initialized")