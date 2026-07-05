import os
import random
import pandas as pd

os.makedirs("dataset", exist_ok=True)

rows = []

disaster_types = [
    "Flood",
    "Earthquake",
    "Cyclone",
    "Wildfire",
    "Landslide"
]

for i in range(10000):

    temperature = random.randint(10, 50)
    humidity = random.randint(20, 100)
    wind_speed = random.randint(1, 45)
    pressure = random.randint(980, 1025)
    rainfall = random.randint(0, 500)

    disaster = random.choice(disaster_types)

    score = (
        temperature * 0.25
        + humidity * 0.20
        + wind_speed * 0.30
        + rainfall * 0.20
        + (1025 - pressure) * 0.15
    )

    if score < 35:
        risk = "Low"
    elif score < 55:
        risk = "Medium"
    elif score < 75:
        risk = "High"
    else:
        risk = "Extreme"

    rows.append(
        {
            "temperature": temperature,
            "humidity": humidity,
            "wind_speed": wind_speed,
            "pressure": pressure,
            "rainfall": rainfall,
            "disaster_type": disaster,
            "risk": risk,
        }
    )

df = pd.DataFrame(rows)

df.to_csv(
    "dataset/disaster_dataset.csv",
    index=False
)

print("Dataset Generated Successfully")