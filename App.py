import flask
import jsonify
from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('used_car_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])

def predict():
    


    if request.method == 'POST':
        Year = int(request.form['Year'])
        Km_driven = int(request.form['Km_driven'])
        Km_driven2 = np.log(Km_driven)
        Fuel_Type= request.form['Fuel_Type']


        if (Fuel_Type == 'Diesel'):
            fuel_Diesel=1
            fuel_Electric=0
            fuel_LPG=0
            fuel_Petrol=0

        elif (Fuel_Type == 'Electric'):
            fuel_Diesel = 0
            fuel_Electric = 1
            fuel_LPG = 0
            fuel_Petrol = 0

        elif(Fuel_Type == 'LPG'):
            fuel_Diesel = 0
            fuel_Electric = 0
            fuel_LPG = 1
            fuel_Petrol = 0



        else:
            fuel_Diesel = 0
            fuel_Electric = 0
            fuel_LPG = 0
            fuel_Petrol = 1

        Seller_Type = request.form['Seller_Type_Individual']
        if (Seller_Type == 'Individual'):
            seller_type_Individual = 1
            seller_type_TrustmarkDealer=0

        else:
            seller_type_Individual = 0
            seller_type_TrustmarkDealer = 1

        Transmission_Mannual = request.form['Transmission_Mannual']
        if (Transmission_Mannual == 'Mannual'):
            transmission_Mannual = 1
        else:
            transmission_Mannual = 0

        Owner = request.form['Owner']
        if (Owner=='other'):
            fourth_owner=0
            second_owner=0
            first_owner=0
            third_owner=0
        elif (Owner=='second'):
            fourth_owner=0
            second_owner=0
            first_owner=0
            third_owner=0
        elif (Owner=='f'):
            fourth_owner=0
            second_owner=0
            first_owner=0
            third_owner=0
        else:
            fourth_owner = 0
            second_owner = 0
            first_owner = 0
            third_owner = 0


        prediction = model.predict([[Year, Km_driven2, fuel_Diesel, fuel_Electric, fuel_LPG, fuel_Petrol,
                                     seller_type_Individual, seller_type_TrustmarkDealer, transmission_Mannual,
                                     fourth_owner, second_owner, first_owner, third_owner]])
        output = round(prediction[0], 2)
        if output < 0:
            return render_template('index.html', prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html', prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)







