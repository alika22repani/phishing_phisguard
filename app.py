from flask import Flask, render_template, request
import joblib
from feature_extractor import extract_features

app = Flask(__name__)

# Load model dan scaler
model = joblib.load("model/knn_model.pkl")
scaler = joblib.load("model/scaler.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    url = request.form["url"]
    features = extract_features(url)
    features_scaled = scaler.transform(features)
    
    print("RAW features:", features)
    print("SCALED features:", features_scaled)
    print("Prediction:", model.predict(features_scaled)[0])
    
    prediction = model.predict(features_scaled)[0]
    result = "SAFE WEBSITE" if prediction == 0 else "PHISHING WEBSITE"
    
    feature_names = ['NumDots', 'UrlLength', 'NumDash', 'NoHttps', 'IpAddress', 
                     'HostnameLength', 'PathLength', 'QueryLength', 
                     'NumSensitiveWords', 'NumNumericChars']
    
    features_dict = dict(zip(feature_names, features[0]))
    
    return render_template(
        "result.html",
        url=url,
        result=result,
        features=features_dict
    )

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)