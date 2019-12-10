import os
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.exceptions import AirflowException
from airflow.utils.operator_helpers import context_to_airflow_vars
from datetime import datetime
from datetime import timedelta
import json
import requests
import pprint

class APIToJSONOperator(BaseOperator):


    @apply_defaults
    def __init__(self,
                url,
                params=None,
                headers=None,
                *args,
                **kwargs):
        super(APIToJSONOperator, self).__init__(*args, **kwargs)
        self.url = url
        self.params = params
        self.headers = headers

        if not url:
            raise AirflowException('No valid url endpoint supplied.')

        
        
    def execute(self, context):
        # Export context to make it available for callables to use.
        airflow_context_vars = context_to_airflow_vars(context, in_env_var_format=True)
        self.log.info("Exporting the following env vars:\n%s",
                      '\n'.join(["{}={}".format(k, v)
                                 for k, v in airflow_context_vars.items()]))
        os.environ.update(airflow_context_vars)
        #self.log.info(context['next_ds_nodash'])
        timestamp = context["ts_nodash"]
        fname = airflow_context_vars["AIRFLOW_CTX_DAG_ID"]
        fpath = "/usr/local/airflow/data/"+fname+timestamp+".json"
        response = requests.get(self.url, headers = self.headers, params = self.params, verify=False)
        f = open(fpath, "w+")
        f.write(response.text)
        f.close()