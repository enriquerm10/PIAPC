#!/usr/bin/env python3

import argparse
import subprocess
import sys
import WebScraping
import HashObtainer
import huntermail
import logging
import EXIFDataViewer
import cesar
import Servidor
import Puertos

def main():
    parser = argparse.ArgumentParser(prog='PIA',
                                     description='Script multitarea de ciberseguridad',
                                     usage='\n'
                                     'main.py A [-U] [-C]\n'
                                     'main.py B [-A] [-D] [-N]\n'
                                     'main.py C  \n'
                                     'main.py D [-R]\n'
                                     'main.py E [-M]\n'
                                     'main.py F \n'
                                     'main.py G [-I]\n')
    
    parser.add_argument(
        'script', help='Elija el script a ejecutar: '
        'A). WebScraping, B). APIhunter, C). Powershell, D). METADATA, E). CifradoyDecifrado, F).Servidor-Cliente, G).Escaner de Puertos ',
        type=str, choices=['A', 'B', 'C', 'D','E','F','G'])

    parser.add_argument('-U', '--URL', help='URL de la pagina web incluyendo "https://"')
    
    parser.add_argument('-C', '--Carpeta',
                        help='Nombre que se le asignará a la carpeta')
    parser.add_argument('-R', '--Directorio',
                        help='Ruta de la carpeta')
    parser.add_argument('-D', '--dominio',
                        help='Dominio de email')
    parser.add_argument('-A', '--api',
                        help = 'Agrega tu API key.')
    parser.add_argument('-N', '--numero',
                        help = 'Numero de correos (Maximo 10 si tienes plan gratuito).')
    parser.add_argument('-M', '--Modo',
                        help='Escriba el modo que desee encriptar/desencriptar')
    parser.add_argument('-I', '--target',
                        help='IP de la Maquina')
    

    

    try:
        logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)
        args = parser.parse_args()
        logging.info(args)
        
        if args.script == 'A':
            WebScraping.FuncionWS(args.URL, args.Carpeta)   
        elif args.script == 'B':
            api = args.api
            company = args.dominio
            numero = args.numero
            huntermail.hunterio(api,company,numero)
            
        elif args.script == 'C':
            p = subprocess.Popen(["powershell.exe",
                                  ".\\E1Script.ps1"],
                                 stdout=sys.stdout)
            
            p.communicate()

        elif args.script == 'D':
            EXIFDataViewer.printMeta(args.Directorio)

        elif args.script == 'E':
            cesar.cesarfuncion(args.Modo)

        elif args.script == 'F':
            print('Abrir otra terminal cmd y ejecutar archivo Cliente.py')

            Servidor.main()

        elif args.script == 'G':
            Puertos.main(args.target)

        


            

        
        else:
            print('operando invalido')
        
            


    except:
        print("main: falta un operando\nPruebe 'main -h' o 'main --help' para más información.")
        logging.error("main: falta un operando\nPruebe 'main -h' o 'main --help' para más información.")



        

if __name__ == "__main__":
    main()
    
    
