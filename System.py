__author__ = 'jos'

class System():
    def __init__(self, name, roles, environment):
        if isinstance(roles, str):
            roles = [ roles, ]

        self.name = name
        self.roles = roles
        self.environment = environment

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)



