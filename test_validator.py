from app.validators.event_validator import EventValidator

good_event = {
    "title": "Flood",
    "latitude": 28.61,
    "longitude": 77.20,
    "source": "NASA"
}

bad_event = {
    "title": "",
    "latitude": 200,
    "longitude": None,
    "source": ""
}

print("Good Event:", EventValidator.validate(good_event))
print("Bad Event :", EventValidator.validate(bad_event))