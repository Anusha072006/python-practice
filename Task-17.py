# DICTIONARY 

student = {
    "name": "Anu",
    "age": 22,
    "course": "Python",
    "marks": 85,
    "city":"Bangalore"
}
print(student.get("name"))
print(student.get("age"))
print(student.get("marks"))
print(student.get("college"))
print(student.get("gist"))

student={"age":22}
student.update({"age":23})
print(student)

student={"marks":85}
student.update({"marks":90})
print(student)

student={"college":"GIST"}
student.update({"college":"GIST"})
print(student)

student={"city":"Bangalore"}
student.update({"city":"Bangalore"})
print(student)

student={"age":23 ,"marks":85}
student.update({"age":26,"marks":78})
print(student)

-------------------------------------------------------------------------------------------------------------
employee = {
    "name": "Ravi",
    "age": 25,
    "salary": 40000,
    
}

employee={"salary":4000}
employee.update({"salary":45000})
print(employee)
employee.update({"department":"IT"})

print(employee.get("department"))
print(employee)

---------------------------------------------------------------------------------------------------------------------------------------------------------------
product={
    "price":50000

}

product={"price":50000}
product.update({"price":55000})
print(product)
product.update({"color":"Silver"})
print(product)

product.update({"ram":"8GB"})
print(product)

print(product.get("price"))
print(product.get("color"))
print(product.get("ram"))


