from flask import Flask, render_template, request, redirect, url_for
from com.epislab.auth.login_controller import LoginController
from com.epislab.auth.login_model import LoginModel
from com.epislab.bmi.bmi_controller import BmiController
from com.epislab.bmi.bmi_model import BmiModel
from com.epislab.calculator.calc_controller import CalcController
from com.epislab.calculator.calc_model import CalcModel
from com.epislab.grade.grade_controller import GradeController

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
   
   controller = LoginController(username, password)
   resp: LoginModel = controller.getResult()
   
   return redirect(url_for(resp.result))

@app.route('/calc',methods=["POST", "GET"])
def calc():
   print("🦉전송된 데이터 방식 : ", request.method)
   
   if request.method == "POST":
      print("🥷POST 방식으로 전송된 데이터")
      num1 = request.form.get('num1')
      num2 = request.form.get('num2')
      opcode = request.form.get('opcode')

      controller = CalcController(num1=num1, opcode=opcode, num2=num2)
      resp: CalcModel = controller.getResult()
      
      render_html = '<h3>결과보기</h3>'
      render_html += f"{resp.num1}{resp.opcode}{resp.num2}={resp.result}"

      return render_template("calculator/calc.html", 
                           render_html=render_html)
   else:
      print("🧑‍🚒GET 방식으로 전송된 데이터")
      return render_template("calculator/calc.html")
   
@app.route('/bmi',methods=["POST", "GET"])
def bmi():
   print("🦉전송된 데이터 방식 : ", request.method)
   
   if request.method == "POST":
      print("🥷POST 방식으로 전송된 데이터")
      height = request.form.get('height')
      weight = request.form.get('weight')

      controller = BmiController(height=height, weight=weight)
      resp:BmiModel = controller.getResult()

      
      render_html = '<h3>결과보기</h3>'
      render_html += f"{resp.height}cm {resp.weight}kg의 BMI는 {resp.result}"
    
      return render_template("calculator/bmi.html", 
                           render_html=render_html)
   else:
      print("🧑‍🚒GET 방식으로 전송된 데이터")
      return render_template("calculator/bmi.html")
   
@app.route('/discount',methods=["POST", "GET"])
def discount():
   print("🦉전송된 데이터 방식 : ", request.method)
   
   if request.method == "POST":
      print("🥷POST 방식으로 전송된 데이터")
      
      return render_template("calculator/discount.html")
   else:
      print("🧑‍🚒GET 방식으로 전송된 데이터")
      return render_template("calculator/discount.html")
   

@app.route('/gugudan',methods=["POST", "GET"])
def gugudan():
   print("🦉전송된 데이터 방식 : ", request.method)
   
   if request.method == "POST":
      print("🥷POST 방식으로 전송된 데이터")
      
      return render_template("calculator/gugudan.html")
   else:
      print("🧑‍🚒GET 방식으로 전송된 데이터")
      return render_template("calculator/gugudan.html")
   
@app.route('/grade',methods=["POST", "GET"])
def grade():
   print("🦉전송된 데이터 방식 : ", request.method)
   
   if request.method == "POST":
      print("🥷POST 방식으로 전송된 데이터")
      name = request.form.get('name')
      korean = request.form.get('korean')
      english = request.form.get('english')
      math = request.form.get('math')
      society = request.form.get('society')
      science = request.form.get('science')

      controller = GradeController(name=name, korean=korean, english=english, 
                                   math=math, society=society, science=science)
      resp = controller.getResult()
      render_html = '<h3>결과보기</h3>'
      render_html += f"{resp.name}님의 성적은 {resp.result}입니다."
      
    
      return render_template("grade/grade.html", 
                           render_html=render_html)
   else:
      print("🧑‍🚒GET 방식으로 전송된 데이터")
      return render_template("grade/grade.html")

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
