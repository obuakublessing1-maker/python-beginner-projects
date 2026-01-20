import pandas as pd
import matplotlib.pyplot as plt
#Expense data
data = {"Category" : ["Meals","Transport","Subscription", "Meals","Utilities","Transport"],"Amount": [2500,1500,3000, 1800,4000,1200]}
df = pd.DataFrame(data)
#Personal expenses (Meals &Subscription)
personal_expenses = df[df["Category"].isin(["Meals","Subscription"])]
print("Personal Expenses:")
print(personal_expenses)
#Highest single Expenses
most_spending = df[df["Amount"]==df["Amount"].max()]
print("\nHighest Expense:")
print(most_spending)
#Total spending per Category
category_total = df.groupby("Category")["Amount"].sum()
print("\nTotal spending by Category")
print(category_total)
#Plot: Spending by category
plt.figure()
category_total.plot(kind="bar")
plt.title("Total spending by Category")
plt.xlabel("Category")
plt.ylabel("Amount(N)")
plt.show()
