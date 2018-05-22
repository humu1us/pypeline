from pypeline.core.baseunit import BaseUnit

# From this type of Unit Pipeline class expect
# a return value from run() method and the pipeline
# will try to send a parameter called data to the
# run function


class ProcessUnit(BaseUnit):
    def __init__(self, ctx):
        super().__init__(ctx, BaseUnit.UNIT_PROC)

    def run(self, data, return_data):
        NotImplementedError("Error, this is a abstract method")
