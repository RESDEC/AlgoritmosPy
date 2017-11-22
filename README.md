# AlgoritmosPy
Proyecto en Python con los algoritmos utilizados para RESDEC

Para poder hacer uso de los archivos .py de los algoritmos es necesario tener lo siguiente:

- Python: 2.7.+
- scikit-surprise 1.0.3 (paquete con los algoritmos de Surprise)
- pip (paquete)
- setuptools (paquete)
- six (paquete)
- IDE: PyCharm

Una vez instalado Python, los paquetes se pueden descagar directamente una vez abierto el proyecto en PyCharm en:

File >> Settings >> Project:AlgoritmosPy

Ahi, verificamos que nuestro projecto este usando como interprete la version de Python 2.7.+ (en caso de no tener, buscamos la carpeta donde instalamos Python) 
y procedemos a agregarle los paquetes que necesitamos al interprete.

Una vez listo los paquetes, podemos ejecutar cada unos de los aloritmos en la carpeta "src/algorithms" para ver los resultados.

Estructura:

-src
  |-algorithms 	>> algoritmos de Resdec
    |-BaselineOnly.py
    |-CoClustering
    |-...
  |-config	>> archivos de configuracion del proyecto
    |- configuration.py
  |-data	>> data de lectura para los algoritmos
    |- android.data	
    |- wordpress.data	
    |- wordpress_tags.data  
  |-servicios
    |- ...

