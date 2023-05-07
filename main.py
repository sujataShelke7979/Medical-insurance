from flask import Flask, jsonify, render_template, request
from project_app.utils import MedicalInsurance

# Creating instance here
# 'app' is standard variable
app = Flask(__name__)

# @app.route("/") --> USED TO GET HOME API
# @app.route("/furniture") --> You will get 'Furniture' Page here

@app.route("/")
def hello_flask():
    print("Welcome to Medical Insurance company")
    return render_template("index.html")


@app.route("/predict_charges",methods=["POST","GET"])
def get_insurance_charges():
    if request.method =="GET":
        print("We are in a GET Method")
       


        age=int(request.args.get("age"))
        sex=(request.args.get("sex"))
        bmi=float(request.args.get("bmi"))
        children=int(request.args.get("children"))
        smoker=request.args.get("smoker")
        region=request.args.get("region")

    
    
    
    
    med_ins=MedicalInsurance(age,sex,bmi,children,smoker,region)
    charges=med_ins.get_predicted_charges()
    return render_template("index.html",prediction=charges)
print("__name__-->",__name__)
if __name__=="__main__":
    #app.run(host="0.0.0.0",post=5000,debug=false)
    app.run()

