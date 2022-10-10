is_good_credit=True
price=1000000

if is_good_credit:
    print("Buyer has good credit")
    print(f"Down Payment is: ${price*0.1}")
else:
    print("Buyer has not good credit")
    print(f"Down Payment is: ${price * 0.2}")