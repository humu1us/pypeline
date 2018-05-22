from multiprocessing import Process
from multiprocessing import Manager
from pypeline.core.baseunit import BaseUnit


class Pipeline:
    def __init__(self, units=[]):
        self.__units = units

    def __is_structure_good(self):
        if self.__units[0].unit_type() != BaseUnit.UNIT_SRC:
            return False
        if self.__units[-1].unit_type() != BaseUnit.UNIT_DST:
            return False

        for i in range(1, len(self.__units) - 1):
            if self.__units[i].unit_type() != BaseUnit.UNIT_PROC:
                return False

        return True

    def __execute_normal(self, unit, data=None):
        if unit.unit_type() != BaseUnit.UNIT_SRC:
            data = unit.run(data=data)
        else:
            data = unit.run()
        return data

    def __execute_isolated(self, unit, data=None):
        return_data = Manager().dict()
        worker = Process(target=unit.run, args=(data, return_data))
        worker.start()
        worker.join()

        return dict(return_data)

    def start(self):
        if not self.__is_structure_good():
            raise RuntimeError("Pipeline structure error")

        data = None
        for unit in self.__units:
            ctx = unit.context_type()
            if ctx == BaseUnit.CTX_NORMAL:
                data = self.__execute_normal(unit, data)
            elif ctx == BaseUnit.CTX_ISOLATED:
                data = self.__execute_isolated(unit, data)
            else:
                raise RuntimeError("Context type not supported")
