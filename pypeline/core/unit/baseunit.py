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

    def __init__(self, ctx, unit_type, drawer=None):
        self.__context = ctx
        self.__type = unit_type
        self._drawer = drawer

    def context_type(self):
        return self.__context

    def unit_type(self):
        return self.__type

    def run(self):
        NotImplementedError("Error, this is an abstract method")
