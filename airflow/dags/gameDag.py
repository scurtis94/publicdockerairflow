# airflow related
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
#from airflow.hooks import PostgresHook
from airflow.operators.bash_operator import BashOperator
# other packages
from datetime import datetime
from datetime import timedelta
import json
import requests

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 11, 17),
    'email_on_failure': False,
    'email_on_retry': False,
    'schedule_interval': '@daily',
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
}


def api_call():
    #code to call api and store data in dataframe
    response = requests.get("https://statsapi.web.nhl.com/api/v1/schedule?startDate=2018-10-20&endDate=2018-10-20",
                            verify=False)
    games = json.loads(response.text)
    for game in games["dates"][0]["games"]:
        print(game["gamePk"])
        print(game["gameDate"])
        print(game["teams"]["away"]["team"]["link"])


#def write_data():
    #code to pull api data from dataframe and put in table
    #pg_hook = PostgresHook(postgres_conn_id='hackweekdb')
    # for game in games["dates"][0]["games"]:
    #     pg_hook.run("""CALL hackweek.merge_games(%s, %s, %s, %s)""", parameters=(game["gamePk"], game["gameDate"],
    #                                                                              game["teams"]["away"]["team"]["link"],
    #                                                                              game["teams"]["home"]["team"]["link"]))


dag = DAG(
    dag_id='gameDag',
    description='dag to pull game data from api and insert into games table',
    default_args=default_args)


task1_api_call = PythonOperator(
    task_id='api_call',
    python_callable=api_call,
    dag=dag)


#task2_write_data = PythonOperator(
 #   task_id='write_data',
  #  python_callable=write_data,
   # dag=dag
#)


##task1_api_call >> task2_write_data
task1_api_call