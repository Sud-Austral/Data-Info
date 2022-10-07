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
        comunaNombre = j["nombre"]
        #copy_tree(fr"{os.getcwd()}/luis/bases/main", fr"{os.getcwd()}/publicaciones2/{j['nombre']}")
        copy_tree("base",f"publicaciones2/{j['nombre']}")
        f = open (f"publicaciones2/{j['nombre']}/index.html",'r')
        contenido = f.read()
        f.close()
        with open(f"publicaciones2/{j['nombre']}/index.html", 'w', encoding='utf-8') as file:
            contenido = contenido.replace("***comuna***",j["titulo"])
            file.write(contenido)
        detalle = pd.read_excel("comunas_origen.xlsx", sheet_name=j['nombre'])
        try:
            shutil.copy(f"imagenes/portada_inicio/{comunaNombre}.png", f"publicaciones2/{j['nombre']}/assets/cochamo/portadainicio.jpg")
        except Exception as e:
            print("Error" + str(e))

            print("Error en la imagen")

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
        id_vista_li = []
        for n,k in detalle.iterrows():
            print(k["vista"],k["id_comuna"])
            vista_id = k['vista_id']
            vista_nombre = k['nombre']
            id_vista_li.append(vista_id)
            try:
                htmlAux1 = f"""<li class="nav-item" role="presentation" style="width: inherit;">
                            <a href="./{vista_id}.html"> <button style="width: 100%!important; color:black" class="nav-link ***{vista_id}***" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile-tab-pane" type="button" role="tab" aria-controls="profile-tab-pane" aria-selected="false">
                            {vista_nombre}
                            </button></a></li>"""
                htmlLi1 = htmlLi1 + htmlAux1
                print(htmlLi1)
                htmlAux2 = f"""<li class="nav-item" role="presentation" style="background:#C0CBD1;" >
                            <a href="./{vista_id}.html"><button class="nav-link ***{vista_id}***" id="home-tab" data-bs-toggle="tab" data-bs-target="#home-tab-pane" type="button" role="tab" aria-controls="home-tab-pane" aria-selected="true">
                                {vista_nombre}
                            </button>
                            </a></li> """
                htmlLi2 = htmlLi2 + htmlAux2
            except:
                pass            
            #try:
            #    shutil.copy("base/base_vista.html", f"publicaciones2/{j['nombre']}/{k['vista_id']}.html")
            #except:
            #    pass
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
        #f = open (f"publicaciones2/{j['nombre']}/base_vista.html",'r')
        f = open (f"base/base_vista.html",'r')
        contenido = f.read()
        f.close()
        for n,k in detalle.iterrows():

            vista_id = k['vista_id']
            vista_nombre = k['nombre']
            htmlFinal = contenido \
                        .replace("***LI1***",htmlLi1) \
                        .replace("***LI2***",htmlLi2)
            htmlFinal = htmlFinal.replace(f"***{vista_id}***","active") 
            for ids in id_vista_li:
                htmlFinal = htmlFinal.replace(f"***{ids}***","")
            
                
            with open(f"publicaciones2/{j['nombre']}/{vista_id}.html", 'w', encoding='utf-8') as file:
                file.write(htmlFinal)



        #***comuna***

    return

if __name__ == '__main__':
    print("Comenzo...")
    main()