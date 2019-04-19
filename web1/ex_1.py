from flask import Flask, render_template,redirect
app = Flask(__name__)

    
    
@app.route('/aboutme')
def something():
    return """hello im long, i'm 19 ,i live in Chuc Son - CHuong My- Ha NOi, i'm first year student in Post Telecomunication Institute of Technology, my major is telecomunication .
     I have many hobbies : sing , playing guitar, football, travel,... My family have 7 people, my parents, my grandparents, my young brother , my sister and me .
        My parents are both teacher . Both of my grandparents are farmer...  
         """


@app.route('/school')
def go_to():
    
    return redirect("http://techkids.vn")


if __name__ == '__main__':
  app.run(debug=True)
 