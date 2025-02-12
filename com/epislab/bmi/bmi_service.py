from com.epislab.bmi.bmi_model import BmiModel


class BmiService:
    def __init__(self):
        pass


    def execute(self, bmi: BmiModel)-> BmiModel:
        height = bmi.height
        weight = bmi.weight
        height = int(height)
        weight = int(weight)
        height = height/100
        bmi = weight / (height * height)
        bmi = round(bmi, 2)
        bmi = str(bmi)
        bmi = bmi + "입니다."
        bmi = "당신의 BMI는 " + bmi
        bmi = bmi + "당신은 "
        if float(bmi) < 18.5:
            bmi = bmi + "저체중입니다."
        elif float(bmi) < 23:
            bmi = bmi + "정상체중입니다."
        elif float(bmi) < 25:
            bmi = bmi + "과체중입니다."
        elif float(bmi) < 30:
            bmi = bmi + "비만입니다."
        else:
            bmi = bmi + "고도비만입니다."
        bmi = bmi + "당신의 BMI는 " + bmi
        bmi = bmi + "당신은 "
        if float(bmi) < 18.5:
            bmi = bmi + "저체중입니다."
        elif float(bmi) < 23:
            bmi = bmi + "정상체중입니다."
        elif float(bmi) < 25:
            bmi = bmi + "과체중입니다."
        elif float(bmi) < 30:
            bmi = bmi + "비만입니다."
        else:
            bmi = bmi + "고도비만입니다."
        bmi = bmi + "입니다."
        bmi.result = bmi
        return bmi