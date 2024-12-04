import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime
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

        # adding system status
        self.system_operational = True
        self.last_activity_time = time.time()

        # creating the labels for clock and status
        self.create_gui()
        self.start_system_clock()  # starting the clock

    def create_gui(self):
        self.label = tk.Label(self.window, text="Welcome to the ATM", font=("Arial", 16))
        self.label.pack(pady=10)

        # clock display
        self.clock_label = tk.Label(self.window, text="", font=("Arial", 12))
        self.clock_label.pack(pady=5)

        # status display
        self.status_label = tk.Label(self.window, text="System Status: Operational", 
                                    font=("Arial", 10), fg="green")
        self.status_label.pack(pady=5)
        
        self.insert_card_button = tk.Button(self.window, text="Insert Card", command=self.insert_card)
        self.insert_card_button.pack(pady=5)

        self.enter_pin_button = tk.Button(self.window, text="Enter PIN", command=self.enter_pin, state=tk.DISABLED)
        self.enter_pin_button.pack(pady=5)

        self.withdraw_button = tk.Button(self.window, text="Withdraw Cash", command=self.withdraw_cash, state=tk.DISABLED)
        self.withdraw_button.pack(pady=5)

        self.deposit_button = tk.Button(self.window, text="Deposit Cash", command=self.deposit_cash, state=tk.DISABLED)
        self.deposit_button.pack(pady=5)    

        self.balance_button = tk.Button(self.window, text="Check Balance", command=self.check_balance, state=tk.DISABLED)
        self.balance_button.pack(pady=5)

        self.eject_card_button = tk.Button(self.window, text="Eject Card", command=self.eject_card, state=tk.DISABLED)
        self.eject_card_button.pack(pady=5)

    def start_system_clock(self):
        # Update system clock display and check for timeout
        current_time = datetime.now().strftime("%H:%M:%S")
        self.clock_label.config(text=f"System Time: {current_time}")
        
        # check for transaction timeout (30 seconds)
        if self.card_inserted and time.time() - self.last_activity_time > 30:
            messagebox.showwarning("Timeout", "Session timeout - card will be ejected")
            self.eject_card()
        
        # update system status randomly (for demonstration)
        if time.time() % 60 == 0:  # every minute
            if self.system_operational:
                self.status_label.config(text="System Status: Operational", fg="green")
            else:
                self.status_label.config(text="System Status: Error", fg="red")
        
        self.window.after(1000, self.start_system_clock)  # update every second
   
    def insert_card(self):
        if not self.card_inserted:
            self.card_inserted = True
            self.label.config(text="Card Inserted. Please Enter PIN.")
            self.enter_pin_button.config(state=tk.NORMAL)
            self.insert_card_button.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Error", "Card already inserted.")

    def enter_pin(self):
        self.last_activity_time = time.time()
        pin_input = simpledialog.askstring("PIN Entry", "Enter your 4-digit PIN:")
        if pin_input == self.pin:
            self.label.config(text="PIN Correct. Choose a Transaction.")
            self.withdraw_button.config(state=tk.NORMAL)
            self.deposit_button.config(state=tk.NORMAL)
            self.balance_button.config(state=tk.NORMAL)
            self.eject_card_button.config(state=tk.NORMAL)
            self.enter_pin_button.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Error", "Incorrect PIN.")

    def withdraw_cash(self):
        self.last_activity_time = time.time()
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

    def deposit_cash(self):
        self.last_activity_time = time.time()
        amount = simpledialog.askfloat("Deposit", "Enter amount to deposit:")
        
        if amount is None:  # User clicked "Cancel"
            messagebox.showinfo("Info", "Deposit canceled.")
            return
            
        if amount <= 0:
            messagebox.showerror("Error", "Invalid amount entered.")
            return
            
        self.account_balance += amount
        messagebox.showinfo("Success", 
            f"Deposit successful!\nNew Balance: ${self.account_balance:.2f}")

    def check_balance(self):
        self.last_activity_time = time.time()
        messagebox.showinfo("Balance", f"Your account balance is: ${self.account_balance:.2f}")

    def eject_card(self):
        self.card_inserted = False
        self.label.config(text="Card Ejected. Thank you for using the ATM.")
        self.insert_card_button.config(state=tk.NORMAL)
        self.enter_pin_button.config(state=tk.DISABLED)
        self.withdraw_button.config(state=tk.DISABLED)
        self.deposit_button.config(state=tk.DISABLED)
        self.balance_button.config(state=tk.DISABLED)
        self.eject_card_button.config(state=tk.DISABLED)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    atm = ATMSystem()
    atm.run()
