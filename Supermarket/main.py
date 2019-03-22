#1/bin/python3
#main logic of program.Uses instances of CheckoutRegister and Product

from register import CheckoutRegister

def main():

    product_list = []
    customer = CheckoutRegister('./federation.db')

    print("\t\nWelcome to federation supermarket\n")

    while True:
        bar_code = int(input("Please enter the barcode for your item: "))

        product_list.append(customer.scan_item(bar_code))
        new_product = input("Would you like to scan another item?(Y/N) ").upper()
        if new_product == 'Y' or new_product =='YES':
            continue #continue while loop
        elif new_product =='N' or new_product =='NO':
            break #get out of loop
        else:
            print("Invalid option")
    print(product_list)
    # product_list.accept_payment()
    return


def get_float(prompt):
    '''Get cash given by client  '''

    value=float()

    while True:
        try:
            value=float(input(prompt))
            if value<0.0:
                print("We don't accept negative money!")
                continue
            break
        except ValueError:
            print("Please enter a valid floating point value.")
    return value

main()
