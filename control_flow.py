bill_total = 95 
discount = 10

if bill_total > 100:
    print('You get a discount of 10%')
    bill_total = bill_total - (bill_total * discount / 100)
    print(f'Your total bill is $ {bill_total:.2f}')
    
if bill_total > 100:
        print("Bill is grater than 100")
        bill_total = bill_total - discount
else:
        print("Bill is less than 100")
        
        print("Total bill:" + str(bill_total))