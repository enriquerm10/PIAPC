from pyhunter import PyHunter

def hunterio(api, company, numero):
    hunter = PyHunter(api)
    res = hunter.domain_search(company=company, limit=10)
    f = open('correos.txt','w+')
    cont = 0
    for i in range(int(numero)):
        if (res['emails'][i]['first_name'] is not None):
            info = ('[+] '+res['emails'][i]['first_name']+' '+res['emails'][i]['last_name']+': '+res['emails'][i]['value'])
            cont = cont + 1
            f.write('%s\n' %info)
    print('\nSe guardaron ',cont,' correos.')

def Main():
    info = 'Script para buscar correos de compañias en especifico.'
    parser = argparse.ArgumentParser(info)
    parser.add_argument('-A', '--api', required = True, 
                        help = 'Agrega tu API key de hunter.io')
    parser.add_argument('-D', '--dominio', required = True, 
                        help = 'Dominio de email')
    parser.add_argument('-N', '--numero', required = True,
                        help = 'Numero de correos (Maximo 10 si tienes plan gratuito).')
    args = parser.parse_args()
    #Api: a9a72185866678dbe162035e06aaf11920eca0c2
    api = args.api
    company = args.dominio
    numero = args.numero
    hunterio(api,company,numero)

if __name__ == '__main__':
    try:
        from pyhunter import PyHunter
        import argparse
        Main()
    except ImportError as error:
        import os
        print("Error on Packages, Installing Packages")
        os.system('pip install pyhunter')
        print("Packages Installed, Re-Run")
        exit()
