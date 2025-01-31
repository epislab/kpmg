from flask import Flask, render_template, request
app = Flask(__name__)   
@app.route('/')
def index():
    return render_template('index.html')    

@app.route('/minus')
def minus():
    return render_template('minus.html')    



if __name__ == '__main__':
    app.run(debug=True)


app.config['TEMPLATES_AUTO_RELOAD'] = True
