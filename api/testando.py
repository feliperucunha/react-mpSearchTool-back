from busca import pesquisar_registro
import json
import os
import re

def pesquisar():
    data = request.json
    pesq = pesquisar_registro(fel)
    print(pesq)
    return jsonify(fel)
