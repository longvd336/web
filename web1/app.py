#snippet: (fapp + enter)
from pymongo import MongoClient
from bson.objectid import ObjectId
from foods_db import Foods_data, User
from flask import Flask,render_template, request, redirect, session
app = Flask(__name__)
#name <=> app
app.config['SECRET_KEY'] = '1*(#582@4#5869aaa'
# uri = 'https://cloud.mongodb.com/v2/5cbaeb05ff7a25138cf7afd8#metrics/replicaSet/5cc0579b9ccf644aff927a03/explorer/foods_app/Users/find'

# client = MongoClient(uri)

# all_user = client.foods_app

# all_data = all_user.Users


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
    
    if 'logged' in session:
        if session['logged'] :
            foods = Foods_data.find()
            return render_template('food.html',foods = foods)   
        else :
            return redirect('/login')
    else:
        return redirect('/login')

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
    if 'logged' in session:
        print("noob")
        if session['logged']:
            return redirect('/food')
        else:
            if request.method == 'GET':
                        
                return render_template("login.html")
            elif request.method == 'POST':
                form = request.form
                login_user = form['login_username']
                login_pass = form['login_password']
                user = User.find_one({'username':login_user})
                if user is None:
                    session['logged'] = False
                    return redirect('/login')

                else:
                    if login_pass == user['password']:
                        session['logged'] = True
                        return redirect('/food')
                    else:
                        session['logged'] = False
                        return redirect('/login')
                        
                # if (form["login_user"] == "longdeptrai" and form["login_pass"] == "123456"):
                #     session['logged'] = True
                #     return redirect('/food')
                # else:
                #     session['logged'] = False
                #     return redirect('/login')
    else:
        print("hello")
        session['logged'] = False
        return render_template('login.html')
        
@app.route('/logout')
def logout():
    if 'logged' in session:
        session['logged'] = False
    return redirect('/login')


@app.route('/register', methods = [ 'GET', 'POST'])

def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        form = request.form
        register_username = form['username']
        register_password = form['password']
            
        new_user = {
            'username':register_username,
            'password':register_password,
        }
        User.insert_one(new_user)
        return redirect("/login")

# khi app chay truc tiep:(python app.py)
#neu chay gian tiep name == namefile chay gian tiep 
if __name__ == '__main__':
  app.run( debug=True)



