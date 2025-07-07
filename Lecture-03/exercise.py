number = int(input("Enter number of hours worked: "))
hourly = int(input("Enter the hourly pay raate: "))
if number > 40: 
    gross_pay = ((number - 40) *1.5*hourly) + (40 * hourly)
else:
    gross_pay = (number * hourly)

print("Gross Pay : ", gross_pay)



