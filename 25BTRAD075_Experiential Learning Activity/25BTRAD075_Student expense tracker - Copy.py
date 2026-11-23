import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import date

# DATABASE
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    category TEXT,
    amount REAL,
    type TEXT,
    date TEXT
)
""")
conn.commit()


# COLORS
BG = "#0B0F19"
SIDEBAR = "#111827"
CARD = "#161E2E"
PURPLE = "#8B5CF6"
WHITE = "#F9FAFB"
GRAY = "#94A3B8"
GREEN = "#22C55E"
RED = "#EF4444"


class ExpenseTracker:

    def __init__(self, root):

        self.root = root
        self.root.title("NOVA | Expense Tracker")
        self.root.geometry("1200x750")
        self.root.minsize(1000, 650)
        self.root.configure(bg=BG)

        self.create_sidebar()
        self.create_main_area()

        self.update_dashboard()
        self.load_transactions()

    # SIDEBAR
    def create_sidebar(self):

        sidebar = tk.Frame(
            self.root,
            bg=SIDEBAR,
            width=230
        )
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        tk.Label(
            sidebar,
            text="✦ NOVA",
            font=("Segoe UI", 25, "bold"),
            bg=SIDEBAR,
            fg=PURPLE
        ).pack(pady=(35, 5))

        tk.Label(
            sidebar,
            text="PERSONAL FINANCE",
            font=("Segoe UI", 9),
            bg=SIDEBAR,
            fg=GRAY
        ).pack(pady=(0, 45))

        self.menu_button(sidebar, "▣   Dashboard")
        self.menu_button(sidebar, "↗   Transactions")
        self.menu_button(sidebar, "◈   Analytics")

        tk.Frame(
            sidebar,
            bg="#263247",
            height=1
        ).pack(fill="x", padx=20, pady=30)

        tk.Label(
            sidebar,
            text="YOUR FINANCES,\nUNDER CONTROL.",
            font=("Segoe UI", 12, "bold"),
            bg=SIDEBAR,
            fg=WHITE,
            justify="left"
        ).pack(side="bottom", pady=35)

    def menu_button(self, parent, text):

        button = tk.Button(
            parent,
            text=text,
            font=("Segoe UI", 11),
            bg=SIDEBAR,
            fg=GRAY,
            activebackground=CARD,
            activeforeground=WHITE,
            relief="flat",
            anchor="w",
            padx=25,
            pady=15,
            cursor="hand2"
        )
        button.pack(fill="x", padx=10, pady=3)

    # MAIN AREA
    def create_main_area(self):

        self.main = tk.Frame(self.root, bg=BG)
        self.main.pack(side="left", fill="both", expand=True)

        # HEADER
        header = tk.Frame(self.main, bg=BG)
        header.pack(fill="x", padx=35, pady=(30, 20))

        tk.Label(
            header,
            text="Dashboard",
            font=("Segoe UI", 26, "bold"),
            bg=BG,
            fg=WHITE
        ).pack(side="left")

        tk.Label(
            header,
            text=date.today().strftime("%d %B %Y"),
            font=("Segoe UI", 11),
            bg=BG,
            fg=GRAY
        ).pack(side="right", pady=12)

        tk.Label(
            self.main,
            text="Welcome back! Here's your financial overview.",
            font=("Segoe UI", 11),
            bg=BG,
            fg=GRAY
        ).pack(anchor="w", padx=38)

        self.create_cards()
        self.create_input()
        self.create_table()

    # DASHBOARD CARDS
    def create_cards(self):

        container = tk.Frame(self.main, bg=BG)
        container.pack(fill="x", padx=25, pady=25)

        self.income_value = self.create_card(
            container, "TOTAL INCOME", "₹ 0.00", GREEN
        )

        self.expense_value = self.create_card(
            container, "TOTAL EXPENSES", "₹ 0.00", RED
        )

        self.balance_value = self.create_card(
            container, "AVAILABLE BALANCE", "₹ 0.00", PURPLE
        )

    def create_card(self, parent, title, value, accent):

        card = tk.Frame(
            parent,
            bg=CARD,
            padx=18,
            pady=20
        )
        card.pack(side="left", fill="both", expand=True, padx=8)

        tk.Label(
            card,
            text=title,
            font=("Segoe UI", 9, "bold"),
            bg=CARD,
            fg=GRAY
        ).pack(anchor="w")

        label = tk.Label(
            card,
            text=value,
            font=("Segoe UI", 21, "bold"),
            bg=CARD,
            fg=accent
        )
        label.pack(anchor="w", pady=(12, 0))

        return label

    # ADD TRANSACTION
    def create_input(self):

        frame = tk.Frame(
            self.main,
            bg=CARD,
            padx=20,
            pady=15
        )
        frame.pack(fill="x", padx=33, pady=5)

        tk.Label(
            frame,
            text="＋  ADD TRANSACTION",
            font=("Segoe UI", 12, "bold"),
            bg=CARD,
            fg=WHITE
        ).grid(row=0, column=0, columnspan=4, sticky="w", pady=(0, 15))

        self.description = self.create_entry(
            frame, "Description", 0, 1
        )

        self.amount = self.create_entry(
            frame, "Amount (₹)", 1, 1
        )

        self.category = ttk.Combobox(
            frame,
            values=[
                "Food", "Travel", "Shopping",
                "Bills", "Education", "Entertainment", "Other"
            ],
            state="readonly",
            font=("Segoe UI", 10),
            width=18
        )
        self.category.grid(row=1, column=2, padx=8, pady=5)
        self.category.set("Food")

        self.transaction_type = ttk.Combobox(
            frame,
            values=["Income", "Expense"],
            state="readonly",
            font=("Segoe UI", 10),
            width=15
        )
        self.transaction_type.grid(row=1, column=3, padx=8, pady=5)
        self.transaction_type.set("Expense")

        tk.Button(
            frame,
            text="＋  ADD",
            command=self.add_transaction,
            font=("Segoe UI", 10, "bold"),
            bg=PURPLE,
            fg=WHITE,
            activebackground="#7042D8",
            activeforeground=WHITE,
            relief="flat",
            padx=20,
            pady=8,
            cursor="hand2"
        ).grid(row=2, column=1, pady=12, sticky="w")

    def create_entry(self, parent, placeholder, row, column):

        entry = tk.Entry(
            parent,
            font=("Segoe UI", 10),
            bg="#222D40",
            fg=WHITE,
            insertbackground=WHITE,
            relief="flat",
            width=20
        )

        entry.insert(0, placeholder)
        entry.grid(row=row, column=column, padx=8, pady=5, ipady=8)

        def clear_placeholder(event):
            if entry.get() == placeholder:
                entry.delete(0, tk.END)

        entry.bind("<FocusIn>", clear_placeholder)

        return entry

    # TRANSACTION TABLE
    def create_table(self):

        container = tk.Frame(self.main, bg=CARD)
        container.pack(fill="both", expand=True, padx=33, pady=15)

        tk.Label(
            container,
            text="  RECENT TRANSACTIONS",
            font=("Segoe UI", 13, "bold"),
            bg=CARD,
            fg=WHITE
        ).pack(anchor="w", pady=15)

        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Treeview",
            background=CARD,
            foreground=WHITE,
            fieldbackground=CARD,
            rowheight=35,
            borderwidth=0,
            font=("Segoe UI", 10)
        )

        style.configure(
            "Treeview.Heading",
            background="#222D40",
            foreground=WHITE,
            font=("Segoe UI", 10, "bold"),
            relief="flat"
        )

        style.map(
            "Treeview",
            background=[("selected", PURPLE)],
            foreground=[("selected", WHITE)]
        )

        columns = (
            "ID", "Description", "Category",
            "Amount", "Type", "Date"
        )

        self.table = ttk.Treeview(
            container,
            columns=columns,
            show="headings"
        )

        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=120, anchor="center")

        self.table.pack(fill="both", expand=True, padx=15, pady=10)

        tk.Button(
            container,
            text="DELETE SELECTED",
            command=self.delete_transaction,
            bg="#7F1D1D",
            fg=WHITE,
            activebackground=RED,
            activeforeground=WHITE,
            relief="flat",
            font=("Segoe UI", 9, "bold"),
            padx=15,
            pady=8,
            cursor="hand2"
        ).pack(anchor="e", padx=15, pady=12)

    # ADD TRANSACTION
    def add_transaction(self):

        description = self.description.get().strip()
        amount = self.amount.get().strip()
        category = self.category.get()
        transaction_type = self.transaction_type.get()

        if not description or description == "Description" or not amount:
            messagebox.showerror("Error", "Enter all transaction details!")
            return

        try:
            amount = float(amount)

            if amount <= 0:
                raise ValueError

        except ValueError:
            messagebox.showerror("Error", "Enter a valid positive amount!")
            return

        cursor.execute("""
            INSERT INTO transactions
            (description, category, amount, type, date)
            VALUES (?, ?, ?, ?, ?)
        """, (
            description,
            category,
            amount,
            transaction_type,
            date.today().strftime("%Y-%m-%d")
        ))

        conn.commit()

        self.description.delete(0, tk.END)
        self.amount.delete(0, tk.END)

        self.update_dashboard()
        self.load_transactions()

        messagebox.showinfo(
            "Success",
            "Transaction added successfully!"
        )

    # DASHBOARD UPDATE
    def update_dashboard(self):

        cursor.execute(
            "SELECT SUM(amount) FROM transactions WHERE type='Income'"
        )
        income = cursor.fetchone()[0] or 0

        cursor.execute(
            "SELECT SUM(amount) FROM transactions WHERE type='Expense'"
        )
        expenses = cursor.fetchone()[0] or 0

        balance = income - expenses

        self.income_value.config(text=f"₹ {income:,.2f}")
        self.expense_value.config(text=f"₹ {expenses:,.2f}")
        self.balance_value.config(text=f"₹ {balance:,.2f}")

    # LOAD TRANSACTIONS
    def load_transactions(self):

        for item in self.table.get_children():
            self.table.delete(item)

        cursor.execute(
            "SELECT * FROM transactions ORDER BY id DESC"
        )

        for row in cursor.fetchall():
            self.table.insert("", tk.END, values=row)

    # DELETE TRANSACTION
    def delete_transaction(self):

        selected = self.table.selection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Select a transaction first!"
            )
            return

        if messagebox.askyesno(
            "Confirm",
            "Are you sure you want to delete this transaction?"
        ):

            item = self.table.item(selected[0])
            transaction_id = item["values"][0]

            cursor.execute(
                "DELETE FROM transactions WHERE id=?",
                (transaction_id,)
            )

            conn.commit()

            self.update_dashboard()
            self.load_transactions()


# RUN APPLICATION
if __name__ == "__main__":

    root = tk.Tk()
    app = ExpenseTracker(root)

    root.mainloop()

    conn.close()