#snippet: (fapp + enter)

from bson.objectid import ObjectId
from foods_db import Foods_data
from flask import Flask,render_template, request, redirect
app = Flask(__name__)
#name <=> app



@app.route('/')#'/' trang chu
def index():
    return "Hello c4e30"

@app.route('/say-hi')#'/say-hi' :

def say_hi():
    return "Hello everyone"

@app.route('/say-hi/<name>')

def say_hi_2(name):
    return "xin chao {}". format(name) 

@app.route('/tong/<int:a>/<int:b>')

def sum(a,b):
    tong = a + b
    return str(tong)         #kieu tra ve tren phai la int or tuple 
#
@app.route('/food')

def food():
    foods = Foods_data.find()
    # title = "thit lon"
    # description = "rat ngon"
    # link = "https://image-us.24h.com.vn/upload/1-2018/images/2018-02-14/1518583095-171-vi-sao-khong-gia-dinh-nao-cung-cho-an-thit-cho-1-1517544835-width640height400.jpg"
    return render_template('food.html',foods = foods)   


@app.route("/food/<id>")#detail

def detail(id):
    
    detail_food = Foods_data.find_one({"_id": ObjectId(id)})

    return render_template("food_detail.html", detail_food = detail_food)


@app.route('/food/add_food', methods = ['GET', 'POST'])
def add_food():
    if request.method == "GET":
        return render_template("add_food.html")
    elif request.method == "POST":
        
        form = request.form
        
        new_food = {
            "title": form["title"],
            "description":form["description"],
            "link": form["link"],
            'type': form["type"],

        }
        Foods_data.insert_one(new_food)
        return redirect("/food")


@app.route('/food/edit/<id>', methods = ["GET", "POST"])
def edit_food(id):
    food = Foods_data.find_one({"_id":ObjectId(id)})
    if request.method == "GET":
        return render_template("edit_food.html", food = food )
    elif request.method == "POST":
        form = request.form
        new_value = {"$set": {
            "title":form['title'],
            "description":form["description"],
            'link':form['link'],
            'type':form['type'],

        }}
        Foods_data.update_one(food, new_value)
        return redirect('/food')

@app.route('/food/delete/<id>')
def delete(id):
    food = Foods_data.find_one({"_id":ObjectId(id)})
    Foods_data.delete_one(food)
    return redirect("/food")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        form = request.form
        # if (form["user"] == "longdeptrai" and form["pass"] == "123456"):
        #     return "welcome"
        # else:
        #     return "user not found"
        print(form)
        return "Hello world"

@app.route('/register', methods = [ 'GET', 'POST'])

def register():
    if request.method == 'POST':
        form = request.form
        print(form)
        return "register page"

# khi app chay truc tiep:(python app.py)
#neu chay gian tiep name == namefile chay gian tiep 
if __name__ == '__main__':
  app.run( debug=True)



