import os
import pandas as pd


def procesar_archivos_csv():
    # Directorios de entrada y salida
    input_dir = '/opt/input'
    output_dir = '/opt/output/'

    # Iterar sobre los archivos CSV en la carpeta de entrada
    for filename in os.listdir(input_dir):
        if filename.endswith('.csv'):
            # Cargar el archivo CSV
            input_path = os.path.join(input_dir, filename)
            df = pd.read_csv(input_path)

            # Eliminar filas con valores nulos
            df = df.dropna()

            # Agrupa los registro por los campos 'STNAME'y'YEAR', suma los registros del campo 'AAWDT'
            df = df.groupby(['STNAME','YEAR'])['AAWDT'].sum().reset_index(name='SumaAAWDT')

            # Guardar el archivo procesado en la carpeta de salida
            output_path = os.path.join(output_dir, filename)
            df.to_csv(output_path, index=False)
    
