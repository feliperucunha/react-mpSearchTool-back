# -*- coding: utf-8 -*
    
import os
import re

def pesquisar_registro(txt):
    resultado = ''
    mylist = []
    z = []

    
    for path, x, arquivos in os.walk('ioepa_arquivos_teste/'):
        
        for arquivo in arquivos:

            with open( 'ioepa_arquivos_teste/'+arquivo, 'rb' ) as a:
                for linha in a:
                    resultado = re.search(txt.lower(), str(linha.lower()))
                   
                    if resultado:
                        #registro = linha.split(',')
                        res = '<a href="http://ioepa.com.br/arquivos/'+arquivo[0:4]+'/'+arquivo[:-4]+'.pdf>'+arquivo[:-4]+'.pdf</a>'
                        dic = { "nome": res }
                       # trecho = str(linha)
                        print(res)
                        #print(trecho)
                        return dic;
            a.close()
            
 return pesquisar_registro('kel'); #Stockwell
#print (pesquisar_registro('kel')) # Nome da variavel e posição do resultado dsp do '='