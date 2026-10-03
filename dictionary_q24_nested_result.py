students = {
    "Abhishek": {"marks": 85},
    "Rahul": {"marks": 62},
    "Aman": {"marks": 94},
    "Rohan": {"marks": 48}
}

for key,value in students.items():
        if value["marks"] >= 85:
            value["result"]="Excellent"
        elif value["marks"]>=60:
            value["result"]="Good"
        elif value["marks"]>=50:
            value["result"]="Pass"
        else:
             value["result"]="fail"
print(students.items())