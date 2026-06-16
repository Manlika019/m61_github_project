weight = float(input("กรอกน้ำหนัก (กก.): "))
height = float(input("กรอกส่วนสูง (เมตร): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    result = "น้ำหนักต่ำกว่าเกณฑ์"
elif bmi < 25:
    result = "น้ำหนักปกติ"
elif bmi < 30:
    result = "น้ำหนักเกิน"
else:
    result = "โรคอ้วน"

print(f"BMI = {bmi:.2f}")
print(f"ผลการประเมิน : {result}")