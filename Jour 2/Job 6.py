import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SQLplateforme$98",
    database="LaPlateforme"
)

cursor = conn.cursor()

cursor.execute("SELECT SUM(capacite) FROM salles")
resultat = cursor.fetchone()[0]

print("La somme des capacités des salles est de :", resultat)

cursor.close()
conn.close()
