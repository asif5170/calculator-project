"""
it is better to declare the variables in the beginning
so that options 2 not directly error
"""
#variables
has_data = False
product = ""
total = 0
grand_total = 0
per_person = 0


# loop
while True:
    print("\n----MENU------")
    print("1. Add Product")
    print("2. Show Bill")
    print("3. Exit...\n")

    choice = input("Enter Choice (1-3): ")

    if choice == '1':
        product = input("Enter Product Name : ")
        price = float(input("Enter Price : "))
        qty = int(input("Enter Quantity : "))
        discount = float(input("Enter Discount % : "))
        tips = float(input("Enter Tips % : "))
        people = int(input("Number of People : "))

        # step2: Calculations
        total = price * qty
        dis_amount = total * (discount / 100)
        final_price = total - dis_amount
        tip = final_price * (tips / 100)
        grand_total = final_price + tip

        if people != 0:
            per_person = grand_total / people
            has_data = True
            print("✅ Data Save Successfully.\n")
        else:
            print("❌ Error:People cannot be zero!")
            has_data = False
       

    # step3: output
    elif choice == '2':

        if has_data:
            print("\n--------BILL--------")
            print(f"Product Name  : {product}")
            print(f"Total         : {total:.2f}")
            print(f"Final         : {grand_total:.2f}")
            print(f"Per Person    : {per_person:.2f}")
            print("----------------------\n")
        else:
            print("❗️Please ADD Product first!.\n")

    elif choice == '3':
        print("Exiting.....")
        break
    else:
        print("❗️Invalid choice! Please enter 1,2 or 3.\n")