import flet as ft
from UI.view import View
from model.modello import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view
        self._view.set_controller(self)
        self._view.load_interface()

        self.popola_dropdown()


        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown(self):
        musei = self._model.get_musei()
        epoche = self._model.get_epoche()
        self._view.filt_epoca.options.clear()
        self._view.filt_musei.options.clear()
        for mus in musei:
            opzione = ft.dropdown.Option(mus)
            self._view.filt_musei.options.append(opzione)
        for e in epoche:
            option= ft.dropdown.Option(e)
            self._view.filt_epoca.options.append(option)

        self._view.update()




    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA ARTEFATTI
    # TODO
