# Program to calculate profit or loss percentage

# Step 1: Input
cp, sp = map(float, input("Enter Cost Price and Selling Price: ").split())

# Step 2: Conditions
if sp > cp:
    profit = sp - cp
    profit_percent = (profit / cp) * 100
    print("Profit", round(profit_percent, 2), "%")
elif sp < cp:
    loss = cp - sp
    loss_percent = (loss / cp) * 100
    print("Loss", round(loss_percent, 2), "%")
else:
    print("No Profit No Loss")
