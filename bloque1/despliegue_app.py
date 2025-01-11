import os
import sys
from subprocess import call

def crear(port_param='9080'):

    call(['git', 'clone', 'https://github.com/CDPS-ETSIT/practica_creativa2.git'])
    call(['sudo', 'apt-get', 'update'])
    call(['sudo', 'apt-get', 'install', '-y', 'python3-pip'])
    os.chdir('practica_creativa2/bookinfo/src/productpage')

     # Modifica "requirements.txt" para arreglar conflictos
    requirements = 'requirements.txt'
    with open(requirements, 'r') as file:
        lines = file.readlines()
    with open(requirements, 'w') as file:
        for line in lines:
            if line.startswith('requests=='):
                file.write('requests\n')
        else:
            file.write(line)

    call(['pip3', 'install', '-r', 'requirements.txt'])
    call(['pip', 'install', '--upgrade', 'json2html'])

    os.environ['GROUP_NUMBER'] = '44'

    # Modificar productpage_monolith.py
    with open('productpage_monolith.py', 'r') as fin, open('productpage_monolith_temp.py', 'w') as fout:
        for line in fin:
            if 'flood_factor = 0' in line:
                fout.write(line)
                fout.write(os.linesep + 'groupNumber = 0 if (os.environ.get("GROUP_NUMBER") is None) else int(os.environ.get("GROUP_NUMBER"))' + os.linesep)
            elif 'def front' in line:
                fout.write(line)
                fout.write('    group = groupNumber,' + os.linesep)
            elif '\'productpage.html\',' in line:
                fout.write(line)
                fout.write('    group = group,' + os.linesep)                
            else:
                fout.write(line)

    os.rename('productpage_monolith_temp.py', 'productpage_monolith.py')

    # Modificar templates/productpage.html
    os.chdir('templates')
    with open('productpage.html', 'r') as fin, open('productpage_temp.html', 'w') as fout:
        for line in fin:
            if '{% block title %}Simple Bookstore App{% endblock %}' in line:
                fout.write(line.replace(
                    '{% block title %}Simple Bookstore App{% endblock %}',
                    '{% block title %}Simple Bookstore App - Grupo: {{ group }}{% endblock %}'
                ))
            else:
                fout.write(line)

    os.rename('productpage_temp.html', 'productpage.html')

    print("Aplicación creada correctamente.")


def start(port='9080'):
 os.chdir('practica_creativa2/bookinfo/src/productpage')
 call(['python3', 'productpage_monolith.py', port])
    

def liberar():
    call(['rm', '-rf', 'practica_creativa2'])

if __name__ == "__main__":
    param = sys.argv
    if len(param) < 2:
        print("Debes indicar un comando: 'arrancar' o 'liberar'.")
    elif param[1] == "crear":
        crear()
    elif param[1] == "arrancar":
        start()
    elif param[1] == "liberar":
        liberar()
    else:
        print("Comando no reconocido. Usa 'arrancar' o 'liberar'.")
