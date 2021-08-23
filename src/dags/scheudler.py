from datetime import datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

####################################################
# 1. DEFINE PYTHON FUNCTIONS
####################################################


# <-- Remember to include "**kwargs" in all the defined functions
def scrap_and_store(**kwargs):

    return


def alert_if_new(**kwargs):  # <-- Remember to include "**kwargs" in all the defined functions

    return


# <-- Remember to include "**kwargs" in all the defined functions
def monitor_store_alert(**kwargs):

    return


############################################
# 2. DEFINE AIRFLOW DAG (SETTINGS + SCHEDULE)
############################################

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['user@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'scheduler',
    default_args=default_args,
    description='Scrap job postings and alert if somethin unseen comes out',
    catchup=False,
    start_date=datetime(2021, 8, 23, 9, 0, 0),
    schedule_interval='@hourly',
    # schedule_interval= '* 7 * * *'
)

##########################################
# 3. DEFINE AIRFLOW OPERATORS
##########################################

monitor_store_alert = PythonOperator(
    task_id='monitor_store_alert',
    python_callable=monitor_store_alert,
    provide_context=True,
    dag=dag,
)

##########################################
# 4. DEFINE OPERATORS HIERARCHY
##########################################

monitor_store_alert
