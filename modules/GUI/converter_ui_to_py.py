#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  :Jesus Ramos Membrive
# Created Date: 24/11/2022
# version ='0.1'
# ---------------------------------------------------------------------------
""" PyQt5 uic module convert ui file (XML code) into py file (Python code)"""
# ---------------------------------------------------------------------------
from PyQt5 import uic
import subprocess

with open('form.ui', 'r') as file_in:
    file_out = open('ui_form.py', 'w')
    uic.compileUi(file_in, file_out, execute=True)
file_out.close()

bashCommand = "pyrcc5 Icons.qrc -o Icons_rc.py"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

bashCommand_2 = "pyrcc5 style.qrc -o style_rc.py"
process_2 = subprocess.Popen(bashCommand_2.split(), stdout=subprocess.PIPE)
output_2, error_2 = process_2.communicate()



if file_out:
    print("Conversion successfully")
else:
    print("Task failed successfully")
