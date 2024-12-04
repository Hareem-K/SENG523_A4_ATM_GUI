import tkinter as tk
from tkinter import messagebox, simpledialog

import time

# pip install tk
# python atm_system.py

class ATMSystem:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("ATM System")
        
        # Initialize system states
        self.pin = "1234"
        self.account_balance = 1000.0
        self.card_inserted = False
        
        self.create_gui()

    def create_gui(self):
        self.label = tk.Label(self.window, text="Welcome to the ATM", font=("Arial", 16))
        self.label.pack(pady=10)
        
        self.insert_card_button = tk.Button(self.window, text="Insert Card", command=self.insert_card)
        self.insert_card_button.pack(pady=5)

        self.enter_pin_button = tk.Button(self.window, text="Enter PIN", command=self.enter_pin, state=tk.DISABLED)
        self.enter_pin_button.pack(pady=5)

        self.withdraw_button = tk.Button(self.window, text="Withdraw Cash", command=self.withdraw_cash, state=tk.DISABLED)
        self.withdraw_button.pack(pady=5)

        self.balance_button = tk.Button(self.window, text="Check Balance", command=self.check_balance, state=tk.DISABLED)
        self.balance_button.pack(pady=5)

        self.eject_card_button = tk.Button(self.window, text="Eject Card", command=self.eject_card, state=tk.DISABLED)
        self.eject_card_button.pack(pady=5)

    def insert_card(self):
        if not self.card_inserted:
            self.card_inserted = True
            self.label.config(text="Card Inserted. Please Enter PIN.")
            self.enter_pin_button.config(state=tk.NORMAL)
            self.insert_card_button.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Error", "Card already inserted.")

    def enter_pin(self):
        pin_input = simpledialog.askstring("PIN Entry", "Enter your 4-digit PIN:")
        if pin_input == self.pin:
            self.label.config(text="PIN Correct. Choose a Transaction.")
            self.withdraw_button.config(state=tk.NORMAL)
            self.balance_button.config(state=tk.NORMAL)
            self.eject_card_button.config(state=tk.NORMAL)
            self.enter_pin_button.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Error", "Incorrect PIN.")

    def withdraw_cash(self):
        amount = simpledialog.askfloat("Withdrawal", "Enter amount to withdraw:")
        if amount is None:  # User clicked "Cancel"
            messagebox.showinfo("Info", "Withdrawal canceled.")
            return
        if amount <= self.account_balance:
            self.account_balance -= amount
            messagebox.showinfo("Success", f"Withdrawal successful. Remaining Balance: ${self.account_balance:.2f}")
        elif amount > self.account_balance:
            messagebox.showerror("Error", "Insufficient funds.")
        else:
            messagebox.showerror("Error", "Invalid amount entered.")


    def check_balance(self):
        messagebox.showinfo("Balance", f"Your account balance is: ${self.account_balance:.2f}")

    def eject_card(self):
        self.card_inserted = False
        self.label.config(text="Card Ejected. Thank you for using the ATM.")
        self.insert_card_button.config(state=tk.NORMAL)
        self.enter_pin_button.config(state=tk.DISABLED)
        self.withdraw_button.config(state=tk.DISABLED)
        self.balance_button.config(state=tk.DISABLED)
        self.eject_card_button.config(state=tk.DISABLED)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    atm = ATMSystem()
    atm.run()
