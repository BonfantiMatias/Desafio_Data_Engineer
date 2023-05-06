# Airflow en Docker para procesar archivo CSV

Este es un desafío de Data Engineer que tiene como objetivo crear un entorno de Airflow en Docker para procesar un archivo CSV. Para resolver el desafío, se utilizó la imagen oficial de Docker de Airflow y se modificaron solo 3 líneas para no instalar los DAG de ejemplo y agregar dos carpetas como volúmenes compartidos: una para cargar los archivos "input" y otra para guardar los procesados "output".

  

El dataset utilizado fue descargado desde la página "https://data.seattle.gov/" y cuenta con 430 registros. El procesamiento del archivo consiste en agrupar los registros de 2 claves (Stname y Year) y sumar los de la clave Aawdt generando. El archivo de salida contiene solo 3 claves y los registros agrupados. Este proceso se realiza mediante una función guardada en "procesar_csv.py" y se ejecuta diariamente a las 18 horas mediante el DAG "Desafio.py". Ambos archivos se encuentran guardados dentro de la carpeta dags.

  

## Requisitos

 - Docker compose

  

## Pasos para ejecutar el proyecto

Clonar el repositorio:

  

    git clone "https://github.com/tu-usuario/repo.git"

  

Ejecutar el siguiente comando para construir y correr la imagen de Docker:

  

    mkdir -p ./dags ./logs ./plugins ./input ./output

    echo -e "AIRFLOW_UID=$(id -u)" > .env

    docker compose up airflow-init

    sudo docker-compose  up 

Al terminar esperamos unos segundos para ingresar a airflow en en navegador web. La direccion es

  

    http://localhost:8080/

  

el usuario y pass es **"airflow"**

  

Ir al menú "DAGs" de Airflow y habilitar el DAG "Desafio".

  

Verificar que la función de procesamiento de datos se esté ejecutando correctamente y que los archivos de salida se estén guardando en la carpeta "output".

  

¡Listo! Ahora los archivos de salida estarán disponibles en la carpeta "output" y se actualizarán diariamente a las 18 horas.