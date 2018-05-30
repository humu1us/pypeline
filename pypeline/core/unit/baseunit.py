class BaseUnit:
    # Units contexts
    # CTX_NORMAL: The pipeline execute the unit calling run() method directly
    # CTX_ISOLATED: The pipeline execute the unit using a separated process
    CTX_NORMAL = 0
    CTX_ISOLATED = 1

    # Units types:
    UNIT_SRC = 0
    UNIT_DST = 1
    UNIT_PROC = 2

    def __init__(self, ctx, unit_type):
        self.__context = ctx
        self.__type = unit_type
        self.__drawer = None

    def context_type(self):
        return self.__context

    def unit_type(self):
        return self.__type

    def set_drawer(self, drawer):
        self.__drawer = drawer

    def run(self):
        NotImplementedError("Error, this is an abstract method")

    # This method is used to identify a Unit.
    # the expected is a dictionary with the followings fields:
    # name: unit name
    # description: short description
    # long_description: long description
    # type: unit type
    # context: context type
    # return: return value or None
    # data: data expected or None
    # author: your name
    # help: how to use
    #
    # Implement this method allow to use this unit from
    # command line as plugin
    def identify(self):
        NotImplementedError("Error, this is an abstract method")
