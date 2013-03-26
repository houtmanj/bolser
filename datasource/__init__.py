__author__ = 'jos'

def extractSystems(dic):
    import System
    assert isinstance(dic, dict)

    if dic.has_key('systems'):
        return dic['systems']

    if not dic.has_key('name'):
        return

    return System.System(name=dic['name'], roles=dic['role'], environment=dic['environment']);

def copyf(systemlist, key, valuelist):
    return [sys for sys in systemlist if sys.__dict__[key] in valuelist]


class Datasource():

    def getSystem(self, systemname=None, role=None, status=None):
        pass



class JsonDatasource(Datasource):

    def __init__(self):
        import json

        json_data = open("/Users/jos/Documents/bolser/example_systems.json")

        self.__loaded_data = json.load(json_data, object_hook=extractSystems)

    def getSystem(self, systemname=None, role=None, environment=None):

        filtered = self.__loaded_data[:]

        if systemname is not None:
            filtered =  copyf(filtered, 'name', systemname )

        if role is not None:
            filtered =  copyf(filtered, 'role', role )

        if environment is not None:
            filtered =  copyf(filtered, 'environment', environment )

        return filtered


