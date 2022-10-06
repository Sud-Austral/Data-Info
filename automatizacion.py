import requests
import json
import pandas as pd
import datetime
import sys
from distutils.dir_util import copy_tree
import os
import shutil

def main():

    try:
        shutil.rmtree("publicaciones2")
    except:
        pass

    try:
        os.mkdir("publicaciones2")
    except:
        pass

    df = pd.read_excel("comunas_origen.xlsx", sheet_name="comunas")
    for i,j in df.iterrows():
        print(j["titulo"])
        #copy_tree(fr"{os.getcwd()}/luis/bases/main", fr"{os.getcwd()}/publicaciones2/{j['nombre']}")
        copy_tree("base",f"publicaciones2/{j['nombre']}")
        f = open (f"publicaciones2/{j['nombre']}/index.html",'r')
        contenido = f.read()
        f.close()
        with open(f"publicaciones2/{j['nombre']}/index.html", 'w', encoding='utf-8') as file:
            contenido = contenido.replace("***comuna***",j["titulo"])
            file.write(contenido)

        detalle = pd.read_excel("comunas_origen.xlsx", sheet_name=j['nombre'])
        for n,k in detalle.iterrows():
            print(k["vista"],k["id_comuna"])
            if(k["portada"] == 1):
                with open(f"publicaciones2/{j['nombre']}/index.html", 'w', encoding='utf-8') as file:
                    contenido = contenido.replace("***VISTAPORTADA***",j["vista_id"])
                    file.write(contenido)

        #***comuna***

    return

if __name__ == '__main__':
    print("Comenzo...")
    main()