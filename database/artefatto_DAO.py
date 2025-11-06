from database.DB_connect import ConnessioneDB


"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass




    #estrapolazione dati dal database degli artefatti
    def estrazione_dati(self):
        from model.artefattoDTO import Artefatto
        try:
            cnx = ConnessioneDB.get_connection()
            cursor = cnx.cursor()
            query = """ SELECT * FROM artefatto"""
            cursor.execute(query)
            lista_artefatti = []
            for row in cursor:
                #print(row)
                artTemp = Artefatto(row[0], row[1], row[2], row[3], row[4])
                lista_artefatti.append(artTemp)
            cursor.close()
            cnx.close()
            return lista_artefatti
        except Exception as e:
            print('Errore nella lettura dati dal database')
            return []


#da = ArtefattoDAO() # verifica che funzioni l'estrapolazione
#da.estrazione_dati()
