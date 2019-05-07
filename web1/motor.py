from flask import Flask, render_template,request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
from motor_data import all_data

app = Flask(__name__)

@app.route('/list_motor')
def result():
  all_motor = all_data.find() 
  return render_template("return_data.html", all_motor = all_motor)

@app.route('/motor', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("motor.html")
    
    elif request.method == 'POST':
        form = request.form
        new_motor = {"hang":form["hang"],
        "fee":form["fee"],
        "link":form["link"],
        "year":form["year"],
        }
        all_data.insert_one(new_motor)
        
        return redirect("/list_motor")

if __name__ == '__main__':
  app.run(debug=True)
 