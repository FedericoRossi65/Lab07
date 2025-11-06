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
    def get_artefatti_filtrati(self, museo: str, epoca: str):
        """
        Restituisce la lista di artefatti filtrati per museo (tramite id) e/o epoca.
        Se l'utente non seleziona nessun filtro, restituisce tutti gli artefatti.
        """

        # Estrazione dei dati dal database
        artefatti = self._artefatto_dao.estrazione_dati()
        musei = self._museo_dao.estrazione_dati()

        # Se l'utente non seleziona alcun filtro → ritorna tutti gli artefatti
        if (not museo or museo.strip() == "") and (not epoca or epoca.strip() == ""):
            return artefatti

        # Ricavo l'id del museo selezionato (se l'utente ne ha scelto uno)
        id_museo = None
        if museo and museo.strip() != "":
            for m in musei:
                if m.nome.strip().lower() == museo.strip().lower():
                    id_museo = m.id
                    break

        # Filtro gli artefatti in base ai criteri selezionati
        artefatti_filtrati = []
        for art in artefatti:
            includi = True

            # Filtro per museo
            if id_museo is not None:
                if str(art.id_museo).strip() != str(id_museo).strip():
                    includi = False

            # Filtro per epoca
            if epoca and epoca.strip() != "":
                if art.epoca.strip().lower() != epoca.strip().lower():
                    includi = False

            if includi:
                artefatti_filtrati.append(art)

        return artefatti_filtrati

    # vado a prendere tutte le epoche elimando i duplicati utilizzando un set da artefatto.dao.estrazionedati
    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""

        lista_epoca = []
        for art in self._artefatto_dao.estrazione_dati():
            lista_epoca.append(art.epoca)

        lista_epoca_unica = (list(set(lista_epoca)))
        #print(lista_epoca_unica)
        return lista_epoca_unica



    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""

        lista_musei = []
        for mus in self._museo_dao.estrazione_dati():
            lista_musei.append(mus.nome)
        #print(lista_musei) # verifica funzionamento
        return lista_musei

#debug per getepoche
#l = Model()
#l.get_epoche()
#l.get_musei()#debug per getmusei