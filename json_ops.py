import json

# with open(r"C:\Users\RaghulRamesh\PycharmProjects\pythonProject\trainer_info.json","r") as jfo:
#     info=json.load(jfo)
#     print(f"Trainer Name:{info['Name']}, Technology:{info['Tech']}")
#     print(info)

training_details={
    'tech':'Python',
    'duration':'5days',
    "classroom":False,
    "Certificatiom":None,
    "Schedule":{
        "day1":"Introduction",
        "day2":{
            "Morning":"Data Structure",
            "Noon":"Functions"
        }
    }
}

with open("course.json","w") as fo:
    json.dump(training_details,fo,indent=5)