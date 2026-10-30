ast = ""
store=int(input("Enter number of stores: "))
for i in range (store):
    sales=int(input("Enter today's number of sales in store "+str(i+1)+": "))
    sales=int(sales)
    sales=sales/100
    sales=int(sales)
    for j in range (sales):
        ast=ast+"*"
    ast=ast+"/n"