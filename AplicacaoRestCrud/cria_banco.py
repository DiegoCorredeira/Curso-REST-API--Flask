import sqlite3
## ARQUIVO PARA EXEMPLOS!!!
conn = sqlite3.connect('apisongs.db')
cursor = conn.cursor()


create_table = "CREATE TABLE IF NOT EXISTS songs (id INTEGER PRIMARY KEY, \
                name text, artist text, album text, release_date date, time text)"

adding_song = "INSERT INTO songs VALUES (NULL, 'Crying Lightning', 'Arctic Monkeys', 'Humbug', '2009-08-19', '3:45') "

cursor.execute(create_table)
cursor.execute(adding_song)

conn.commit()
conn.close()