import sqlite3

conn = sqlite3.connect('dane.sqlite')
c = conn.cursor()

# c.execute('''
# CREATE TABLE transakcje
# (data TEXT, id INTEGER, cena REAL)
# ''')

c.execute('''
INSERT INTO transakcje VALUES('2023-05-24',11,17.50)
''')
c.execute('''
INSERT INTO transakcje VALUES('2023-05-24',12,17)
''')

lista = []
for row in c.execute('SELECT * FROM transakcje ORDER BY cena'):
    lista.append(row)

conn.commit()
conn.close()
print(lista)
