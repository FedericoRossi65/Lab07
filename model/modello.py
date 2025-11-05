from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        # TODO
    # vado a prendere tutte le epoche elimando i duplicati utilizzando un set da artefatto.dao.estrazionedati
    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        # TODO
        lista_epoca = []
        for art in self._artefatto_dao.estrazione_dati():
            lista_epoca.append(art.epoca)

        lista_epoca_unica = (list(set(lista_epoca)))
        print(lista_epoca_unica)
        return lista_epoca_unica



    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        # TODO
        lista_musei = []
        for mus in self._museo_dao.estrazione_dati():
            lista_musei.append(mus.nome)
        print(lista_musei)
        return lista_musei

#debug per getepoche
l = Model()
l.get_epoche()
l.get_musei()#debug per getmusei