from flask import Flask, render_template,request
app = Flask(__name__)


@app.route('/motor', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("motor.html")
    
    elif request.method == 'POST':
        form = request.form
       
        print(form)
        return "good"

if __name__ == '__main__':
  app.run(debug=True)
 