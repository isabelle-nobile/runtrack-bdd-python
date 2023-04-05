import mysql.connector

class Employes:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def create(self, nom, prenom, salaire, id_service):
        sql = "INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        val = (nom, prenom, salaire, id_service)
        self.cursor.execute(sql, val)
        self.conn.commit()
        return self.cursor.lastrowid

    def read(self, id):
        sql = "SELECT * FROM employes WHERE id = %s"
        val = (id,)
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        if result is None:
            return None
        else:
            return {'id': result[0], 'nom': result[1], 'prenom': result[2], 'salaire': result[3], 'id_service': result[4]}

    def update(self, id, nom=None, prenom=None, salaire=None, id_service=None):
        employe = self.read(id)
        if employe is None:
            return False
        else:
            if nom is not None:
                employe['nom'] = nom
            if prenom is not None:
                employe['prenom'] = prenom
            if salaire is not None:
                employe['salaire'] = salaire
            if id_service is not None:
                employe['id_service'] = id_service
            sql = "UPDATE employes SET nom = %s, prenom = %s, salaire = %s, id_service = %s WHERE id = %s"
            val = (employe['nom'], employe['prenom'], employe['salaire'], employe['id_service'], id)
            self.cursor.execute(sql, val)
            self.conn.commit()
            return True

    def delete(self, id):
        sql = "DELETE FROM employes WHERE id = %s"
        val = (id,)
        self.cursor.execute(sql, val)
        self.conn.commit()
        return self.cursor.rowcount

    def read_all(self):
        sql = "SELECT e.*, s.nom as service_nom FROM employes e JOIN services s ON e.id_service = s.id"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        employes = []
        for result in results:
            employe = {'id': result[0], 'nom': result[1], 'prenom': result[2], 'salaire': result[3], 'id_service': result[4], 'service_nom': result[5]}
            employes.append(employe)
        return employes

    def close(self):
        self.cursor.close()
        self.conn.close()

employes = Employes('localhost', 'root', 'SQLplateforme$98', 'LaPlateforme')

nouvel_id = employes.create('Julien', 'Greg', 3500.0, 1)
print(nouvel_id)

