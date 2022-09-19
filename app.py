from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('mini.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def man():
    return render_template('index.html')

@app.route('/predict',  methods=['POST'])
def home():
    data=[]
    data1 = request.form['ph']
    data2 = request.form['conductivity']
    data3 = request.form['turbidity']
    arr = np.array([[data1, data2, data3]])
    pred = model.predict(arr)
    return render_template('after.html', data=pred)

@app.route('/button1', methods=["GET", "POST"])
def button1():
    return render_template("projectdetails.html")
@app.route('/button2', methods=["GET", "POST"])
def button2():
    return render_template("Factors.html")
@app.route('/conductivity', methods=["GET", "POST"])
def conductivity():
    return render_template("Conductivity.html")
@app.route('/hardness', methods=["GET", "POST"])
def hardness():
    return render_template("Hardness.html")
@app.route('/ph', methods=["GET", "POST"])
def ph():
    return render_template("pH.html")
@app.route('/Turbidity', methods=["GET", "POST"])
def Turbidity():
    return render_template("Turbidity.html")
@app.route('/chloramines', methods=["GET", "POST"])
def chloramines():
    return render_template("Chloramines.html")
@app.route('/solids', methods=["GET", "POST"])
def solids():
    return render_template("Solids.html")
@app.route('/sulphates', methods=["GET", "POST"])
def sulphates():
    return render_template("Sulphates.html")
@app.route('/trihalomethanes', methods=["GET", "POST"])
def trihalomethanes():
    return render_template("Trihalomethanes.html")

if __name__ == "__main__":
    app.run(debug=True)
