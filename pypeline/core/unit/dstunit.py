from pypeline.core.baseunit import BaseUnit

# From this type of Unit the Pipeline class
# never check for a return value from run()
# method. But requires a value to store, show, etc


class DSTUnit(BaseUnit):
    def __init__(self, ctx):
        super().__init__(ctx, BaseUnit.UNIT_DST)

    def run(self, data):
        NotImplementedError("Error, this is an abstract method")
