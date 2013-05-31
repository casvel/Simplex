__author__ = 'david'

#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# Importamos el módulo pygtk y le indicamos que use la versión 2
import pygtk

pygtk.require("2.0")

# Luego importamos el módulo de gtk y el gtk.glade, este ultimo que nos sirve
# para poder llamar/utilizar al archivo de glade
import gtk
import gtk.glade


class MainWin:
    def __init__(self):
        # Le decimos a nuestro programa que archivo de glade usar (puede tener
        # un nombre distinto del script). Si no esta en el mismo directorio del
        # script habría que indicarle la ruta completa en donde se encuentra
        self.widgets = gtk.glade.XML("Simplex.glade")

        # Creamos un pequeño diccionario que contiene las señales definidas en
        # glade y su respectivo método (o llamada)
        signals = {"on_solve_clicked": self.on_solve_clicked,
                   "on_graphic_clicked": self.on_graphic_clicked,
                   "gtk_main_quit": gtk.main_quit}

        # Luego se auto-conectan las señales.
        self.widgets.signal_autoconnect(signals)

        # Ahora obtenemos del archivo glade los widgets que vamos a
        # utilizar (en este caso son label1 y entry1)
        self.entrada = self.widgets.get_widget("entrada")
        self.salida = self.widgets.get_widget("salida")

    # Se definen los métodos, en este caso señales como "destroy" ya fueron
    # definidas en el .glade, así solo se necesita definir "on_button1_clicked"
    def on_button1_clicked(self, widget):
        texto = self.entrada.get_text()
        self.salida.set_text(texto)

# Para terminar iniciamos el programa
if __name__ == "__main__":
    MainWin()
    gtk.main()