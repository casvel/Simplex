#! /usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'david'


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

# Para terminar iniciamos el programa
if __name__ == "__main__":
    MainWin()
    gtk.main()