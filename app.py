from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get user input
        company = request.form["company"]
        typename = request.form["typename"]

        ram = int(request.form["ram"])
        weight = float(request.form["weight"])
        inches = float(request.form["inches"])

        cpu = request.form["cpu"]
        gpu = request.form["gpu"]

        ssd = int(request.form["ssd"])
        hdd = int(request.form["hdd"])

        os_name = request.form["os"]

        # Create DataFrame
        data = pd.DataFrame({
            "Company": [company],
            "TypeName": [typename],
            "Ram": [ram],
            "Weight": [weight],
            "Inches": [inches],
            "CPU Brand": [cpu],
            "GPU Brand": [gpu],
            "SSD": [ssd],
            "HDD": [hdd],
            "OS": [os_name]
        })

        # Predict
        prediction = model.predict(data)[0]

        return render_template(
            "index.html",
            prediction_text=f" Estimated Laptop Price: ₹ {prediction:,.2f}"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f" Error: {str(e)}"
        )


@app.errorhandler(404)
def page_not_found(error):
    return render_template(
        "index.html",
        prediction_text=" Page Not Found"
    ), 404


if __name__ == "__main__":
    app.run(debug=True)