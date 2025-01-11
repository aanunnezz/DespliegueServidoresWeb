
def start(port_param = '9080'):

        call(['git', 'clone', 'https://github.com/CDPS-ETSIT/practica_creativa2.git'])
        call(['sudo', 'apt-get', 'update'])
        call(['sudo', 'apt-get', 'install', '-y', 'python3-pip'])
        os.chdir('practica_creativa2/bookinfo/src/productpage')
        call(['pip3', 'install', '-r', 'requirements.txt'])

        os.environ['GROUP_NUMBER'] = '44'

        fin = open('productpage_monolith.py', 'r')
        fout = open('productpage_monolith.py', 'w')

        for line in fin: 

            if 'flood_factor = 0' in line:
                fout.write(line)
                fout.write(os.linesep 'groupNumber = int(os.environ['GROUP_NUMBER'])\n')
            elif '\'productpage.html\',' in line:
                fout.write(line)
                fout.write('\tgroup = groupNumber,' + os.linesep)
            elif 'def front' in line:
                fout.write(line)
                fout.write('\tgroup = groupNumber,' + os.linesep)
            else:
                fout.write(line)    

        fin.close()
        fout.close()

        os.chdir('templates')
        fin = open('productpage.html', 'r')
        fout = open('productpage.html', 'w')

        for line in fin:
            if {% block title %}Simple Bookstore App{% endblock %} in line:
                fout.write(line.replace('{% block title %}Simple Bookstore App - Grupo: {{ group }}{% endblock %}' + os.linesep))
            else:
                fout.write(line)    

        fin.close()
        fout.close()
        

def liberar():
	call(['rm', '-rf', 'practica_creativa2'])


param = sys.argv

if param[1] == "arrancar":
        arrancar()

if param[1] == "liberar":
	liberar()  
    
else:
    print("Comando no reconocido. Usa 'arrancar' o 'liberar'.")
              
