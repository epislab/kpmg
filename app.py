from flask import Flask, render_template, request, redirect, url_for
from com.epislab.auth.login_controller import LoginController
from com.epislab.auth.login_model import LoginModel
from com.epislab.calculator.calc_controller import CalcController
from com.epislab.calculator.calc_model import CalcModel

app = Flask(__name__)   
@app.route('/')
def intro():
   return render_template("auth/login.html")

@app.route('/home')
def home():
   print("😎홈페이지로 이동")
   return render_template("index.html")


@app.route('/login', methods=["post"])
def login():
   print("😎로그인 알고리즘")
   username = request.form.get('username')
   password = request.form.get('password')
   print("🔑username:", username)
   print("🍳password:", password)

   login = LoginModel()
   login.username = username
   login.password = password
   
   controller = LoginController()
   resp: LoginModel = controller.getResult(login)
   
   return redirect(url_for(resp.result))
   


@app.route('/calc',methods=["POST", "GET"])
def calc():
   print("🦉전송된 데이터 방식 : ", request.method)
   
   if request.method == "POST":
      print("🥷POST 방식으로 전송된 데이터")
      num1 = request.form.get('num1')
      num2 = request.form.get('num2')
      opcode = request.form.get('opcode')

      print("num1:", num1)
      print("num2:", num2)
      print("opcode:", opcode)

      calc = CalcModel()
      calc.num1 = int(num1)
      calc.num2 = int(num2)
      calc.opcode = opcode

      controller = CalcController()
      resp: CalcModel = controller.getResult(calc)
      
      print(f"{resp.num1}{resp.opcode}{resp.num2}={resp.result}")
      print("😊플러스 성공")
      return render_template("calculator/calc.html", 
                           num1 = resp.num1,opcode = resp.opcode, 
                           num2 = resp.num2, result = resp.result)
   else:
      print("🧑‍🚒GET 방식으로 전송된 데이터")
      return render_template("calculator/calc.html")


@app.route('/manufacture_fin_review')
def manufacture_fin_review():

   return render_template("esg/finchat_reports/manufacture_fin_review.html")

@app.route('/finance_visuals')
def finance_visuals():

   return render_template("esg/finchat_reports/finance_visuals.html")

@app.route('/retail_finbot')
def retail_finbot():

   return render_template("esg/finchat_reports/retail_finbot.html")




@app.route('/energy_esg_collector')
def energy_esg_collector():

   return render_template("esg/esg_analytics/energy_esg_collector.html")

@app.route('/esg_fin_viz_analystics')
def esg_fin_viz_analystics():

   return render_template("esg/esg_analytics/esg_fin_viz_analystics.html")

@app.route('/manufacture_esg_reporter')
def manufacture_esg_reporter():

   return render_template("esg/esg_analytics/manufacture_esg_reporter.html")






@app.route('/build_finance_auto')
def build_finance_auto():

   return render_template("esg/esg_finimpact/build_finance_auto.html")

@app.route('/health_care_fin_Bot')
def health_care_fin_Bot():

   return render_template("esg/esg_finimpact/health_care_fin_Bot.html")

@app.route('/retail_finance_auto')
def retail_finance_auto():

   return render_template("esg/esg_finimpact/retail_finance_auto.html")




   



if __name__ == '__main__':
    app.run(debug=True)


app.config['TEMPLATES_AUTO_RELOAD'] = True
