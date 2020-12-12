import joblib
import pandas as pd
from flask import Flask, request, render_template

app = Flask(__name__)
model = joblib.load('sales.sav')

@app.route('/')
def home():
    return render_template('predict.html')

@app.route('/predict',methods=['POST'])
def y_predict():
    if request.method == "POST":
        ds = request.form["date"]
        a={"ds":[ds]}
        ds=pd.DataFrame(a)
        prediction = model.predict(ds)
        print(prediction)
        output=round(prediction.iloc[0,15])
        print(output)
        return render_template('predict.html',output="The sale value on selected date is {} thousands".format(output))
    return render_template("predict.html")
    
if __name__ == "__main__":
    app.run(debug=True)





