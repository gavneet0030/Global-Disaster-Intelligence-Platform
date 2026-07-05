import joblib

model = joblib.load(
    "app/ml/model.pkl"
)


def predict_risk(
    temperature,
    humidity,
    wind_speed,
    pressure,
    rainfall
):

    prediction = model.predict([[
        temperature,
        humidity,
        wind_speed,
        pressure,
        rainfall
    ]])

    return prediction[0]