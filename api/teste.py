def pesquisar( arq, txt ):
    nome = ""
    with open( arq, 'r' ) as a:
        for linha in a:
            linha = linha.strip('\n')
            if nome == "":
                if txt in linha.split():
                    nome = linha
            else:
                registro = linha.split(',')
                dic = { "nome"       : nome,         \
                        "cod"        : registro[0],  \
                        "pais_nasc"  : registro[1],  \
                        "ano_nasc"   : registro[2],  \
                        "pais_morte" : registro[3],  \
                        "ano_morte"  : registro[4] }
                return dic;
    return pesquisar( 'fisicos.txt', 'Einstein' );

#print(pesquisar( 'fisicos.txt', 'Einstein' ))

