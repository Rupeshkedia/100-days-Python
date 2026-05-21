import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# =========================================================================
# 1. DATABASE SETUP
# =========================================================================
def init_db():
    """Initializes the SQLite database and creates the subjects table."""
    conn = sqlite3.connect("sgpa_tracker.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_name TEXT NOT NULL,
            credits REAL NOT NULL,
            grade TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Grade Point Mapping (C=5, B=6, B+=7, A=8, A+=9, O=10)
GRADE_POINT_MAP = {
    "O": 10, "A+": 9, "A": 8, "B+": 7, "B": 6, "C": 5, "D": 4, "F": 0
}

# =========================================================================
# 2. GUI APPLICATION CLASS
# =========================================================================
class SGPACalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Semester SGPA Tracker & Calculator")
        self.root.geometry("650x550")
        self.root.config(bg="#f4f6f9")
        
        init_db()
        self.create_widgets()
        self.load_data_from_db()

    def create_widgets(self):
        # Heading Style - FIXED: Changed padding=10 to padx=10, pady=10
        title_label = tk.Label(self.root, text="SGPA Calculator & SQL Logger", 
                               font=("Arial", 16, "bold"), bg="#2c3e50", fg="white", padx=10, pady=10)
        title_label.pack(fill=tk.X)

        # ─── INPUT FRAME ──────────────────────────────────────────────────
        input_frame = tk.LabelFrame(self.root, text=" Add New Subject ", font=("Arial", 10, "bold"), bg="#f4f6f9", padx=10, pady=10)
        input_frame.pack(fill=tk.X, padx=15, pady=10)

        # Subject Name Input
        tk.Label(input_frame, text="Subject Name:", bg="#f4f6f9", font=("Arial", 9)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_name = tk.Entry(input_frame, width=25, font=("Arial", 10))
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        # Credits Input
        tk.Label(input_frame, text="Credits:", bg="#f4f6f9", font=("Arial", 9)).grid(row=0, column=2, sticky="w", padx=5, pady=5)
        self.entry_credits = tk.Entry(input_frame, width=8, font=("Arial", 10))
        self.entry_credits.grid(row=0, column=3, padx=5, pady=5)

        # Grade Dropdown Selection
        tk.Label(input_frame, text="Grade:", bg="#f4f6f9", font=("Arial", 9)).grid(row=0, column=4, sticky="w", padx=5, pady=5)
        self.combo_grade = ttk.Combobox(input_frame, values=list(GRADE_POINT_MAP.keys()), width=6, state="readonly", font=("Arial", 10))
        self.combo_grade.grid(row=0, column=5, padx=5, pady=5)
        self.combo_grade.current(4) # Defaults to 'B'

        # Buttons Frame
        btn_frame = tk.Frame(input_frame, bg="#f4f6f9")
        btn_frame.grid(row=1, column=0, columnspan=6, pady=10)

        btn_add = tk.Button(btn_frame, text="Add Subject to SQL", command=self.add_subject, bg="#27ae60", fg="white", font=("Arial", 10, "bold"), padx=10)
        btn_add.pack(side=tk.LEFT, padx=5)

        btn_clear_db = tk.Button(btn_frame, text="Clear All Records", command=self.clear_all_records, bg="#c0392b", fg="white", font=("Arial", 10, "bold"), padx=10)
        btn_clear_db.pack(side=tk.LEFT, padx=5)

        # ─── TABLE VIEW FRAME ─────────────────────────────────────────────
        table_frame = tk.Frame(self.root, bg="#f4f6f9")
        table_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)

        # Setting up standard Treeview layout for tabular display
        columns = ("id", "name", "credits", "grade", "weighted")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=8)
        
        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="Subject Name")
        self.tree.heading("credits", text="Credits")
        self.tree.heading("grade", text="Grade")
        self.tree.heading("weighted", text="Weighted Points")

        self.tree.column("id", width=40, anchor="center")
        self.tree.column("name", width=250, anchor="w")
        self.tree.column("credits", width=80, anchor="center")
        self.tree.column("grade", width=80, anchor="center")
        self.tree.column("weighted", width=120, anchor="center")
        
        self.tree.pack(fill=tk.BOTH, expand=True)

        # ─── SCORE DISPLAY SUMMARY FRAME ──────────────────────────────────
        self.summary_frame = tk.Frame(self.root, bg="#ecf0f1", bd=1, relief=tk.SOLID)
        self.summary_frame.pack(fill=tk.X, padx=15, pady=15)

        self.lbl_summary = tk.Label(self.summary_frame, text="Total Credits: 0.0  |  Weighted Points: 0.0\nCalculated Semester SGPA: 0.00", 
                                    font=("Arial", 11, "bold"), bg="#ecf0f1", fg="#2c3e50", pady=10)
        self.lbl_summary.pack()

    # =========================================================================
    # 3. DATABASE OPERATIONS & BUSINESS LOGIC
    # =========================================================================
    def add_subject(self):
        """Validates inputs, saves them to SQLite, and updates the application UI."""
        name = self.entry_name.get().strip()
        credits_str = self.entry_credits.get().strip()
        grade = self.combo_grade.get()

        if not name:
            messagebox.showerror("Error", "Please enter a valid subject name.")
            return
        
        try:
            credit_val = float(credits_str)
            if credit_val <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Credits must be a valid number greater than 0.")
            return

        # Write to SQLite Database File
        conn = sqlite3.connect("sgpa_tracker.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO grades (subject_name, credits, grade) VALUES (?, ?, ?)", 
                       (name, credit_val, grade))
        conn.commit()
        conn.close()

        # Reset inputs
        self.entry_name.delete(0, tk.END)
        self.entry_credits.delete(0, tk.END)
        
        # Refresh screen layout elements
        self.load_data_from_db()

    def load_data_from_db(self):
        """Fetches up-to-date data rows directly out of SQL table and renders updates."""
        # Clean current table rendering view
        for row in self.tree.get_children():
            self.tree.delete(row)

        conn = sqlite3.connect("sgpa_tracker.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, subject_name, credits, grade FROM grades")
        rows = cursor.fetchall()
        conn.close()

        total_credits = 0.0
        total_weighted_points = 0.0

        for row in rows:
            db_id, sub_name, credit, grade = row
            grade_point = GRADE_POINT_MAP.get(grade, 0)
            weighted_points = credit * grade_point
            
            total_credits += credit
            total_weighted_points += weighted_points
            
            # Injecting freshly queried table rows into the visual UI canvas grid
            self.tree.insert("", tk.END, values=(db_id, sub_name, f"{credit:.1f}", grade, f"{weighted_points:.1f}"))

        # Calculate final values
        if total_credits > 0:
            sgpa = total_weighted_points / total_credits
            self.lbl_summary.config(
                text=f"Total Credits: {total_credits:.1f}  |  Weighted Points: {total_weighted_points:.1f}\nCalculated Semester SGPA: {sgpa:.2f}",
                fg="#27ae60" if sgpa >= 6.0 else "#c0392b"
            )
        else:
            self.lbl_summary.config(text="Total Credits: 0.0  |  Weighted Points: 0.0\nCalculated Semester SGPA: 0.00", fg="#2c3e50")

    def clear_all_records(self):
        """Drops all existing records stored in the SQLite schema table safely."""
        if messagebox.askyesno("Confirm Clear", "Are you sure you want to permanently delete all stored subjects from the SQL Database?"):
            conn = sqlite3.connect("sgpa_tracker.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM grades")
            conn.commit()
            conn.close()
            self.load_data_from_db()

# =========================================================================
# 4. RUN TIME ENTRYPOINT
# =========================================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = SGPACalculatorApp(root)
    root.mainloop()