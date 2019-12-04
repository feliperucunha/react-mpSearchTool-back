# -- coding: utf-8 -

import os
import re

def pesquisar_registro(txt):
    resultado = ''
    res = []
    z = []

    for path, x, arquivos in os.walk('ioepa_arquivos_teste/'):
        
        for arquivo in arquivos:

            with open( 'ioepa_arquivos_teste/'+arquivo, 'rb' ) as a:
                for linha in a:
                    resultado = re.search(txt.lower(), str(linha.lower()))
                   
                    if resultado:
                        res = '<a href="http://ioepa.com.br/arquivos/'+arquivo[0:4]+'/'+arquivo[:-4]+'.pdf>'+arquivo[:-4]+'.pdf</a>'
                        #trecho = str(linha)
                        #z.append(res+'/'+trecho)
                        dic = { "nome" : res }

            a.close()
      
        #return z ; #Stockwell
        return print(dic)
        

print (pesquisar_registro('kell')) # Nome da variavel e posição do resultado dsp do '='