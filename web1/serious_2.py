from flask import Flask, render_template
app = Flask(__name__)
user = {"long":{"name":"Vu Duc Long","age": 19, "phonenumber":"0975797406" },
        "minh" : {"name":"Vu Duc Minh ", "age": 26, "phonenumber": "dont know"},
        "hai ": {"name":"Hoang Hai", "age": 24, "phonenumber": "dont know"},
    }

@app.route('/user/<user_name>')
def users(user_name):
    
    return render_template('user.html', user_name = user_name, user = user)

if __name__ == '__main__':
  app.run(debug=True)
 

