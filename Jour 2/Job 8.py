import mysql.connector

class ZOO:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def create(self, nom, race, id_cage, date_naissance, pays_origine):
        sql = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        val = (nom, race, id_cage, date_naissance, pays_origine)
        self.cursor.execute(sql, val)
        self.conn.commit()
        return self.cursor.lastrowid

    def read(self, id):
        sql = "SELECT * FROM animal WHERE id_cage = %s"
        val = (id,)
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        if result is None:
            return None
        else:
            return {'id': result[0], 'nom': result[1], 'race': result[2], 'id_cage': result[3], 'date_naissance': result[4], 'pays_origine': result[5]}

    def update(self, id, nom=None, race=None, id_cage=None, date_naissance=None, pays_origine=None):
        sql = "UPDATE animal SET"
        val = []
        if nom is not None:
            sql += " nom = %s,"
            val.append(nom)
        if race is not None:
            sql += " race = %s,"
            val.append(race)
        if id_cage is not None:
            sql += " id_cage = %s,"
            val.append(id_cage)
        if date_naissance is not None:
            sql += " date_naissance = %s,"
            val.append(date_naissance)
        if pays_origine is not None:
            sql += " pays_origine = %s,"
            val.append(pays_origine)
        sql = sql.rstrip(",") + " WHERE id = %s"
        val.append(id)
        self.cursor.execute(sql, tuple(val))
        self.conn.commit()
        return True


    def delete(self, id):
        sql = "DELETE FROM animal WHERE id = %s"
        val = (id,)
        self.cursor.execute(sql, val)
        self.conn.commit()
        return self.cursor.rowcount

    def read_all(self):
        sql = "SELECT a.*, a.nom as animal_nom FROM animal e JOIN cage s ON e.id_service = s.id"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        animals = []
        for result in results:
            animal = {'id': result[0], 'nom': result[1], 'race': result[2], 'id_cage': result[3], 'date_naissance': result[4], 'pays_origine': result[5]}
            animals.append(animal)
        return animals
    
    def calcul_superficie_total(self):
        sql = "SELECT SUM(superficie) AS superficie_totale FROM cage"
        self.cursor.execute(sql)
        results = self.cursor.fetchone()

        return "La somme des capacités des salles est de :", results[0]

    def close(self):
        self.cursor.close()
        self.conn.close()

animal = ZOO('localhost', 'root', 'SQLplateforme$98', 'zoo')

nouvel_id = animal.create('Zouli', 'Giraffe', 1, '1997-01-01', 'Nigeria')
print(nouvel_id)

read = animal.read(0)
print(read)

update = animal.update(id=2, nom='Boba', race='Loup', id_cage=2, date_naissance='2011-01-01', pays_origine='France')
print(update)

delete_id_animal = animal.delete(1)

read_all = animal.read_all()
print(read_all)

cage_superficie = animal.calcul_superficie_total()
print(cage_superficie)

