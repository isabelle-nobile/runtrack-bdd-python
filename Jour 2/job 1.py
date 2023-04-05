import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SQLplateforme$98",
    database="LaPlateforme"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM etudiants")
resultat = cursor.fetchall()

for row in resultat:
    print(row)

cursor.close()
conn.close()
