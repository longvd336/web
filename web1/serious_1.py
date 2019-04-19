from flask import Flask, render_template
app = Flask(__name__)

@app.route('/bmi')

def bmi():
    return "CHuc nang tinh bmi"
@app.route('/bmi/<weight>')
def weight(weight):
    return "your weight: {}". format(weight)
@app.route('/bmi/<weight>/<height>')

# def height(weight,height):
#     conversion = int(height)/100

#     bmi = int(weight)/(conversion**2)
#     if bmi < 16:
#         return "Severely underweight"
#     elif bmi < 18.5:
#         return "Underweight" 
#     elif bmi < 25:
#         return "Normal"
#     elif bmi < 30:
#         return "Overweight"
#     else:
#         return "Obese"

# if __name__ == '__main__':
#   app.run(debug=True)


#C2: using render_template()

def height(weight,height):
    conversion = int(height)/100
    bmi = int(weight)/(conversion**2)
    total = []
    total.append(int(weight))
    total.append(int(height))

    return render_template("bmi.html", bmi = bmi,total = total)

if __name__ == '__main__':
    app.run(debug=True)


