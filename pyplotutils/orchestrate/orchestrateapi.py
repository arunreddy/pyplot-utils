import os
from porc import Client

class OrchestrateAPI:
    '''Wrapper with helper functions on top of pyorc: official orchestration python client'''

    def pingApi(self):
        return self.client.ping().raise_for_status()

    def __init__(self):
        self.name = 'Orchestrate API'
        self.host =  "api.orchestrate.io/v0"
        self.client = Client(os.environ['ORCHESTRATE_API_KEY'],self.host)




if __name__ == '__main__':
    os.environ['ORCHESTRATE_API_KEY']= '0cba3170-3f9c-4aa2-ac5b-85ab155dcacf'
    oapi = OrchestrateAPI()
    print(oapi.client)