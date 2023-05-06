from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
from procesar_csv import procesar_archivos_csv

from datetime import datetime

with DAG(
    dag_id='dag_desafio',
    start_date=datetime(2023, 5, 5, 18, 0, 0), 
    schedule_interval='0 18 * * *',  # Ejecutar a las 18:00:00 todos los días
    catchup=True  #Ejecutar tareas antiguas
) as dag:

    start_task = EmptyOperator(
        task_id='start'
    )

    procesar_csv = PythonOperator(
        task_id='procesar_csv',
        python_callable=procesar_archivos_csv,
        dag=dag
    )

    end_task = EmptyOperator(
        task_id='end'
    )

    start_task >> procesar_csv >> end_task

