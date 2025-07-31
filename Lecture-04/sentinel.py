# keep_going = 'y'
# while keep_going == 'y':
#     sales = float(input('Enter the amount of sales: '))
#     comm_rate = float(input('Enter the commission rate: '))
#     commission = sales * comm_rate
#     print('the commission is $', format(commission, ',.2f'))
#     keep_going = input("do you want to continue? (y/n): ")

keep_going = 'y'
while keep_going == 'y':
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))
    commission = sales * comm_rate
    print('the commission is $', format(commission, ',.2f'))
    keep_going = input("do you want to continue? (y/n): ")



