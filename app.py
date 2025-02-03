from flask import Flask, render_template, request
app = Flask(__name__)   
@app.route('/')
def login():

   return render_template("auth/login.html")

@app.route('/home')
def home():
   print("😎홈페이지로 이동")
   return render_template("index.html")

@app.route('/plus')
def plus():
   print("➕더하기연산")
   return render_template("calculator/plus.html")

@app.route('/minus')
def minus():
   print("➖더하기연산")
   return render_template("calculator/minus.html")

@app.route('/multiple')
def multiple():
   print("✖️곱셈연산")
   return render_template("calculator/multiple.html")

@app.route('/divide')
def divide():
   print("➗나눗셈연산")
   return render_template("calculator/divide.html")


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
