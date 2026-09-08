class Expense():
    def add_expense(self):
        amount=input("enter the amount:")
        category=input("enter the category:")
        file = open("expense.txt","a")
        file.write(amount + "," + category + "\n")
        file.close()
    def view_expense(self):
        file = open("expense.txt","r")
        for line in file:
            amount,category= line.split(",")
            print(amount,category)
        file.close()
    def total_expense(self):
        file = open("expense.txt","r")
        total = 0
        for line in file:
            amount,category= line.split(",")
            amount=int(amount)
            total = total + amount
        file.close()
        print(total)
e = Expense()
e.add_expense()
e.view_expense()
e.total_expense()