
import json

p = {
    "fname": "prasad",
    "lname": "keluskar",
    "address": "mumbai",
    "dob": "21/08/91",
    "mobile": "9860678999",

}
#  Sorting json

sort_string = json.dumps(p, indent=3, sort_keys=True)
print(sort_string)

#  job detail
job = '{ "detail": {"company": "facebook", "profile": "QA"}}'

#  check type of obj
obj = json.loads(job)
print("Type of obj:", type(obj))

#  get json data

print("my profile:", obj.get('detail'))
