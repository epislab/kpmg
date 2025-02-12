

from com.epislab.bmi.bmi_model import BmiModel
from com.epislab.bmi.bmi_service import BmiService


class BmiController:

    def __init__(self, **kwargs):
        self.height = kwargs.get('height')
        self.weight = kwargs.get('weight')

    def getResult(self) -> BmiModel:
        bmi = BmiModel()
        bmi.height = self.height
        bmi.weight = self.weight
        service = BmiService()
        return service.execute(bmi)
        

       
        