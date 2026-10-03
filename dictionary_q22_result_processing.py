student = {
    "name": "Abhishek",
    "python": 85,
    "dbms": 72,
    "maths": 91,
    "dsa": 68
}
marks=student.copy()
del marks["name"]
total=sum(marks.values())
avg=total/len(marks)
student["total"]=total
student["Average"]=avg
if avg>=85:
    result="Distinction"
elif avg>=70:
    result="First Division"
elif avg>=60:
    result="Second Divison"
else:
    result="Needs Improvement"
student["result"]=result
print(student)