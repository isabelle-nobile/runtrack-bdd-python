import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SQLplateforme$98",
    database="LaPlateforme"
)

cursor = conn.cursor()

cursor.execute("SELECT SUM(superficie) as superficie_totale from etage;")
resultat = cursor.fetchone()
total_superficie = resultat[0]

print("La superficie de La Plateforme est de", total_superficie, "m2")

cursor.close()
conn.close()
