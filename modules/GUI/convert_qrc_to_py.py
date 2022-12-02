import subprocess

bashCommand = "pyrcc5 Icons.qrc -o Icons.py"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

bashCommand_2 = "pyrcc5 style.qrc -o style.py"
process_2 = subprocess.Popen(bashCommand_2.split(), stdout=subprocess.PIPE)
output_2, error_2 = process_2.communicate()
