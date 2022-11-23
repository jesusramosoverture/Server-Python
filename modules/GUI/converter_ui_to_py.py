################################################################################
# Author: Jesus Ramos Membrive
# Version: 1.0
# Project: DaVitri
# Overture Life S.L.
################################################################################
""" PyQt5 uic module convert ui file (XML code) into py file (Python code)"""

from PyQt5 import uic

with open('form.ui', 'r') as file_in:
    file_out = open('ui_form.py', 'w')
    uic.compileUi(file_in, file_out, execute=True)
file_out.close()

if file_out:
    print("Conversion successfully")
else:
    print("Task failed successfully")
