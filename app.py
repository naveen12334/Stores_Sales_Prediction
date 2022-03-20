from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("pred_sale.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        item_weight= float(request.form['item_weight'])
        item_fat_content=float(request.form['item_fat_content'])
        item_visibility= float(request.form['item_visibility'])
        item_type= float(request.form['item_type'])
        item_mrp = float(request.form['item_mrp'])
        outlet_establishment_year= float(request.form['outlet_establishment_year'])
        outlet_size= float(request.form['outlet_size'])
        outlet_location_type= float(request.form['outlet_location_type'])
        outlet_type= float(request.form['outlet_type'])

    prediction=model.predict([[
            item_weight,
            item_fat_content,
            item_visibility,
            item_type,
            item_mrp,
            outlet_establishment_year,
            outlet_size,
            outlet_location_type,
            outlet_type
        ]])
    output=round(prediction[0],2)

    return render_template('home.html',prediction_text="Sales Prediction is $ {}".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)

