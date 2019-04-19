#snippet: (fapp + enter)



from flask import Flask,render_template
app = Flask(__name__)
#name <=> app

foods = [
    {   'title':"thit cho",
        'description': "rat ngon",
        'link':"https://image-us.24h.com.vn/upload/1-2018/images/2018-02-14/1518583095-171-vi-sao-khong-gia-dinh-nao-cung-cho-an-thit-cho-1-1517544835-width640height400.jpg",
        'type': 'eat'  
    },
    {   "title": "buncha",
        "description":"kha ngon",
        "link": "https://www.196flavors.com/wp-content/uploads/2019/02/bun-cha-2-FP.jpg",
        'type': 'eat'  },
    
    {"title":"com ga",
            "description": "hoi ngon",
            "link":"https://media.foody.vn/res/g70/692641/prof/s/foody-mobile-foody-mobile-foody-a-922-636428010244489101.jpg",
            'type': 'eat'  },
    {"title": "tra dao cam sa",
    "description":"chet",
    "link":"https://www.huongnghiepaau.com/wp-content/uploads/2017/07/649c1b234f9e05214b0a8859fe37993f.jpg",
    'type': 'drink'  
    },
   {"title": "nuoc chanh",
    "description":"dau bung",
    "link":"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Lemonade_%28Lime_version%29.jpg/300px-Lemonade_%28Lime_version%29.jpg",
    'type': 'drink'  
    },
    {"title": "bia",
    "description":"good",
    "link":"https://znews-photo.zadn.vn/w660/Uploaded/iutmtn/2018_06_28/biahanoi1.jpg",
    'type': 'drink'  
    }
    ]
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
   
    # title = "thit lon"
    # description = "rat ngon"
    # link = "https://image-us.24h.com.vn/upload/1-2018/images/2018-02-14/1518583095-171-vi-sao-khong-gia-dinh-nao-cung-cho-an-thit-cho-1-1517544835-width640height400.jpg"
    return render_template('food.html',foods = foods)   
@app.route("/food/<int:index>")#detail

def detail(index):
    detail_food = foods[index]
    return render_template("food_detail.html", detail_food = detail_food)

# khi app chay truc tiep:(python app.py)
#neu chay gian tiep name == namefile chay gian tiep 
if __name__ == '__main__':
  app.run( debug=True)



