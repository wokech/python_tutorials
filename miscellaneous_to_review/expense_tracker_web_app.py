# Still in development

import streamlit as st

class Expense:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            st.success("Expense removed successfully.")
        else:
            st.error("Invalid expense index.")

    def view_expenses(self):
        if len(self.expenses) == 0:
            st.info("No expenses found.")
        else:
            st.write("Expense List:")
            for i, expense in enumerate(self.expenses, start=1):
                st.write(f"{i}. Date: {expense.date}, Description: {expense.description}, Amount: ${expense.amount:.2f}")

    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        st.write(f"Total Expenses: ${total:.2f}")

# Streamlit UI
def main():
    tracker = ExpenseTracker()

    st.title("Expense Tracker")

    menu = ["Add Expense", "Remove Expense", "View Expenses", "Total Expenses"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Expense":
        st.subheader("Add Expense")
        date = st.text_input("Enter the date (YYYY-MM-DD):")
        description = st.text_input("Enter the description:")
        amount = st.number_input("Enter the amount:", min_value=0.0, format="%.2f")
        if st.button("Add"):
            expense = Expense(date, description, amount)
            tracker.add_expense(expense)
            st.success("Expense added successfully.")

    elif choice == "Remove Expense":
        st.subheader("Remove Expense")
        index = st.number_input("Enter the expense index to remove:", min_value=1, step=1) - 1
        if st.button("Remove"):
            tracker.remove_expense(index)

    elif choice == "View Expenses":
        st.subheader("View Expenses")
        tracker.view_expenses()

    elif choice == "Total Expenses":
        st.subheader("Total Expenses")
        tracker.total_expenses()

if __name__ == "__main__":
    main()
