from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")

# Load dataset for dropdowns
df = pd.read_csv("data/final_laptop_data.csv")


@app.route("/")
def home():

    companies = sorted(df["Company"].unique())
    types = sorted(df["TypeName"].unique())
    cpus = sorted(df["CPU Brand"].unique())
    gpus = sorted(df["GPU Brand"].unique())
    os_list = sorted(df["OS"].unique())

    return render_template(
        "index.html",
        companies=companies,
        types=types,
        cpus=cpus,
        gpus=gpus,
        os_list=os_list
    )


@app.route("/predict", methods=["POST"])
def predict():

    data = pd.DataFrame({

        "Company": [request.form["company"]],
        "TypeName": [request.form["typename"]],
        "Ram": [int(request.form["ram"])],
        "Weight": [float(request.form["weight"])],
        "Inches": [float(request.form["inches"])],
        "CPU Brand": [request.form["cpu"]],
        "GPU Brand": [request.form["gpu"]],
        "SSD": [int(request.form["ssd"])],
        "HDD": [int(request.form["hdd"])],
        "OS": [request.form["os"]]

    })

    prediction = model.predict(data)

    companies = sorted(df["Company"].unique())
    types = sorted(df["TypeName"].unique())
    cpus = sorted(df["CPU Brand"].unique())
    gpus = sorted(df["GPU Brand"].unique())
    os_list = sorted(df["OS"].unique())

    return render_template(
        "index.html",
        prediction_text=f"Estimated Laptop Price: ₹{prediction[0]:,.2f}",
        companies=companies,
        types=types,
        cpus=cpus,
        gpus=gpus,
        os_list=os_list
    )


if __name__ == "__main__":
    app.run(debug=True)