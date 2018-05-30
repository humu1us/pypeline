from pypeline.core.baseunit import BaseUnit

# From this type of Unit the Pipeline class expect
# a returned object from run() method


class SRCUnit(BaseUnit):
    def __init__(self, ctx):
        super().__init__(ctx, BaseUnit.UNIT_SRC)
