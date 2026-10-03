students = {
    "Abhishek": {"marks": 85, "course": "BCA"},
    "Rahul": {"marks": 72},
    "Aman": {"marks": 91, "course": "BCA"},
    "Rohan": {"marks": 48}
}
for key , value in students.items():
    course=value.get("course","Not Available")
    print(key, "- Course:", course)