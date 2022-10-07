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
        htmlLi1 = ""
        htmlLi2 = ""
        """
        htmlLi1 = '<li class="nav-item" role="presentation" >' + \
                   '<a href="./{}.html"> <button style="width: 100%!important; color:black" class="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile-tab-pane" type="button" role="tab" aria-controls="profile-tab-pane" aria-selected="false">'+ \
                   'Gestión Territorial'+ \
                   '</button></a></li>'

                   <li class="nav-item" role="presentation" style="background:#C0CBD1;" >
                    <a href="/Recursos_Infraestructura.html"><button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home-tab-pane" type="button" role="tab" aria-controls="home-tab-pane" aria-selected="true">Recursos e Infraestructura</button></a> 
                    </li>   

        
        """
        for n,k in detalle.iterrows():
            print(k["vista"],k["id_comuna"])
            vista_id = k['vista_id']
            vista_nombre = k['nombre']
            try:
                htmlAux1 = f"""<li class="nav-item" role="presentation" >
                            <a href="./{vista_id}.html"> <button style="width: 100%!important; color:black" class="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile-tab-pane" type="button" role="tab" aria-controls="profile-tab-pane" aria-selected="false">
                            {vista_nombre}
                            </button></a></li>"""
                htmlLi1 = htmlLi1 + htmlAux1
                print(htmlLi1)
                htmlAux2 = f"""<li class="nav-item" role="presentation" style="background:#C0CBD1;" >
                            <a href="/{vista_id}.html"><button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home-tab-pane" type="button" role="tab" aria-controls="home-tab-pane" aria-selected="true">
                                {vista_nombre}
                            </button>
                            </a></li> """
                htmlLi2 = htmlLi2 + htmlAux2
            except:
                pass
            
            try:
                shutil.copy("base/base_vista.html", f"publicaciones2/{j['nombre']}/{k['vista_id']}.html")
            except:
                pass
            try:                
                if(k["portada"] == 1):
                    print("entro")
                    f = open (f"publicaciones2/{j['nombre']}/index.html",'r')
                    contenido = f.read()
                    f.close()
                    print("leyo")
                    with open(f"publicaciones2/{j['nombre']}/index.html", 'w', encoding='utf-8') as file:
                        contenido = contenido.replace("***VISTAPORTADA***",k["vista_id"] + ".html")
                        print("cambio")
                        file.write(contenido)
                    print("termino")
            except Exception as e:
                print("Error" + str(e))

        #for n,k in detalle.iterrows():


        #***comuna***

    return

if __name__ == '__main__':
    print("Comenzo...")
    main()