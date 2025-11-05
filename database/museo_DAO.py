from database.DB_connect import ConnessioneDB



"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        self._cnx = ConnessioneDB.get_connection() #connessione al database

    # TODO
    #estrapolazione dei musei dal database
    def estrazione_dati(self):
        from model.museoDTO import Museo
        try:

            cursor = self._cnx.cursor()
            query = """ SELECT * FROM museo"""
            cursor.execute(query)
            lista_musei = []
            for row in cursor:
                #print(row)
                musTemp = Museo(row[0], row[1], row[2])
                lista_musei.append(musTemp)
            cursor.close()
            self._cnx.close()


            return lista_musei
        except Exception as e:
            print('Errore nella lettura dati dal database')




#dao = MuseoDAO() # verifco funzionamento
#dao.estrazione_dati()

