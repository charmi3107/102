print()
print("Welcome to online textbooks buying store!!")
print()
print("Description: In this store you will able to buy textbooks from Class 8 to Class 10 at a very affordable price!! ")
print()

class books:
    def __init__(self,cardNo,name):
        self.cardNo=cardNo
        self.name=name

    def order(self):
        print("Please choose the class:")
        print("1.Class8 2.Class9 3.Class10")
        classno=int(input("Enter the class number: "))
        print()
        if(classno==1):
            print("Currently subjects for which books are available are: ")
            print("1.English 2.Science 3.Maths 4.History 5.Geography")
            print()
            purchase=input("Please put your choices: ")
            print("You have ordered: " + purchase)
            print()
            print("That will be ₹650")
            amount=int(input("Pay: "))
            pin_number=input("Enter pin number: ")
            
            if amount<650:
                print("Insufficient amount!")
                amount=int(input("Pay again: "))
                pin_number=input("Enter pin number: ")
                print("Thank You! You may expect your delivery within 3-4 days.")
                print()
            elif amount>650:
                    new_amount=amount-650
                    print( "Thank you. Your change is ₹"+str(new_amount))
                    print("You may expect your delivery within 3-4 days.")
                    print()
            else:
                print()
                print("Thank you! You may expect your delivery within 3-4 days.")
                print()

        elif(classno==2):
            print("Currently subjects for which books are available are: ")
            print("1.English 2.Science 3.Maths 4.History 5.Geography 6.German")
            print()
            purchase=input("Please put your choices: ")
            print("You have ordered: " + purchase)
            print()
            print("That will be ₹850")
            amount=int(input("Pay: "))
            pin_number=input("Enter pin number: ")
            
            if amount<850:
                print("Insufficient amount!")
                amount=int(input("Pay again: "))
                pin_number=input("Enter pin number: ")
                print("Thank You! You may expect your delivery within 3-4 days.")
                print()
            elif amount>850:
                    new_amount=amount-850
                    print()
                    print("Thank you. Your change is ₹"+str(new_amount))
                    print("You may expect your delivery within 3-4 days.")
                    print()
            else:
                print()
                print("Thank you! You may expect your delivery within 3-4 days.")
                print()

        elif(classno==3):
            print("Currently subjects for which books are available are: ")
            print("1.English 2.Science 3.Maths 4.History 5.Geography 6.German 7.Hindi 8.Marathi")
            print()
            purchase=input("Please put your choices: ")
            print("You have ordered: " + purchase)
            print()
            print("That will be ₹1000")
            amount=int(input("Pay: "))
            pin_number=input("Enter pin number: ")

            if amount<1000:
                print("Insufficient amount!")
                amount=int(input("Pay again: "))
                pin_number=input("Enter pin number: ")
                print("Thank You! You may expect your delivery within 3-4 days.")
                print()
            elif amount>1000:
                    new_amount=amount-1000
                    print( "Thank you. Your change is ₹"+str(new_amount))
                    print("You may expect your delivery within 3-4 days.")
                    print()
            else:
                print()
                print("Thank you! You may expect your delivery within 3-4 days.")
                print()


            

def main():
    name=input("Enter name: ")
    card_number=input("Insert card number: ")
    
    print("Welcome "+name+"!")
    print()
    new_user=books(card_number, name)

    if card_number.strip().isdigit():
        new_user.order()
        
    else:
        print("Please only enter numbers! If you enter a letter again, the app will lock you for 5 minutes.")
        card_number=input("Insert card number: ")
        if card_number.strip().isdigit():
            new_user.order()
    

if __name__ == "__main__":
    main()