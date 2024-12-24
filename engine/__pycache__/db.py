import sqlite3

conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key,name VARCHAR(100),path VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'Epic Games','F:\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe')"
# cursor.execute(query)
# conn.commit()

# query = "DELETE FROM sys_command WHERE id = 5"
# cursor.execute(query)
# conn.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key,name VARCHAR(100),url VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO web_command VALUES (null,'GitHub','https://github.com/')"
cursor.execute(query)
conn.commit()