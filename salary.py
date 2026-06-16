salary = float(input("กรอกเงินเดือน: "))

tax = salary * 0.03
net_salary = salary - tax

print(f"ภาษีที่ต้องชำระ = {tax:.2f} บาท")
print(f"เงินเดือนสุทธิ = {net_salary:.2f} บาท")