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

    df = pd.read_excel("comunas_origen.xlsx")
    for i,j in df.iterrows():
        print(1,i)
        #copy_tree(fr"{os.getcwd()}/luis/bases/main", fr"{os.getcwd()}/publicaciones2/{j['nombre']}")
        copy_tree("main",f"publicaciones2/{j['nombre']}")
    return

if __name__ == '__main__':
    print("Comenzo...")
    main()