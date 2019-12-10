from airflow.plugins_manager import AirflowPlugin
from apitojson_plugin.operators.apitojson_operator import APIToJSONOperator

class APIToJSONPlugin(AirflowPlugin):
    name = "apitojson_plugin"
    hooks = []
    operators = [APIToJSONOperator]
    executors = []
    macros = []