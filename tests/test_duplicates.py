from app.utils.duplicate_checker import DuplicateChecker

events = [

    {
        "title": "Flood",
        "latitude": 28.61,
        "longitude": 77.20
    },

    {
        "title": "Flood",
        "latitude": 28.6101,
        "longitude": 77.2001
    },

    {
        "title": "Earthquake",
        "latitude": 30.1,
        "longitude": 70.4
    }

]

unique = DuplicateChecker.remove_duplicates(events)

print("Before :", len(events))
print("After  :", len(unique))