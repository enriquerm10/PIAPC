from socket import *
import time
import logging

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)


startTime = time.time()


def main(target):
   logging.info(target)
   t_IP = gethostbyname(target)
   print ('Iniciando escaneo en el host: ', t_IP)
      
   for i in range(50, 200):
       s = socket(AF_INET, SOCK_STREAM)
         
       conn = s.connect_ex((t_IP, i))
       if(conn == 0) :
          print ('Puerto %d: ABIERTO' % (i,))
       s.close()
   print('Tiempo de ejecucion:', time.time() - startTime)

#192.168.1.245
