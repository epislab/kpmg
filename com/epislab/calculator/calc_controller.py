
from com.epislab.calculator.calc_model import CalcModel
from com.epislab.calculator.calc_service import CalcService


class CalcController:

    def __init__(self):
        pass

    def getResult(self, calc: CalcModel):
        service = CalcService()
        return service.execute(calc)


