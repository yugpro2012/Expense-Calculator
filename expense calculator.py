from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
import csv

# Initialize the main window
root = ttk.Window(themename="united")
root.title("Expense Calculator")
root.geometry("350x600")  # Smaller window size for mobile
root.resizable(width=False, height=False)

# Categories for expenses
categories = ["Housing", "Transportation", "Food", "Utilities", "Healthcare"]
subcategories = {
    "Housing": ["Rent/EMI", "Property", "Taxes", "Maintenance","Repairs", "Electricity Bill", "Water Bill"],
    "Transportation": ["Car loan Payments", "Car Fuel", "Car Insurance", "Maintenance","Repairs", "Public Transportation", "Parking Fees"],
    "Food": ["Groceries", "Dining Out", "Online orders", "Snacks","Beverages"],
    "Utilities": ["Electricity", "Water", "Gas, Internet", "Phone"],
    "Healthcare": ["Medical Bills", "Medications", "Dental Care", "Vision Care"]
}

# Function to switch frames
def show_frame(frame):
    frame.tkraise()

# Main Frame for entering expenses
main_frame = ttk.Frame(root)
main_frame.grid(row=0, column=0, sticky="nsew")

# Treeview Frame for viewing expenses
treeview_frame = ttk.Frame(root)
treeview_frame.grid(row=0, column=0, sticky="nsew")

# Configure rows and columns for main frame to stretch and center widgets
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_rowconfigure(1, weight=1)
main_frame.grid_rowconfigure(2, weight=1)
main_frame.grid_rowconfigure(3, weight=1)
main_frame.grid_rowconfigure(4, weight=1)
main_frame.grid_rowconfigure(5, weight=1)
main_frame.grid_rowconfigure(6, weight=1)
main_frame.grid_rowconfigure(7, weight=1)
main_frame.grid_rowconfigure(8, weight=1)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_columnconfigure(2, weight=1)

# Title with centered text and padding (in main frame)
title = ttk.Label(main_frame, text="Expense Tracker", font=("Arial", 14, "bold"), bootstyle="info")
title.grid(row=0, column=1, pady=10, sticky="n")  # Reduced font size and padding

# Amount Entry (in main frame)
amount_label = ttk.Label(main_frame, text="Amount", font=("Helvetica", 10), bootstyle="dark")
amount_label.grid(row=1, column=1, padx=20, sticky='w')  # Align to the left
amount_entry = ttk.Entry(main_frame, width=20, bootstyle="info")
amount_entry.grid(row=2, column=1, padx=20, pady=3, sticky="ew")  # Smaller width and padding

# Category Dropdown (in main frame)
category_label = ttk.Label(main_frame, text="Category", font=("Helvetica", 10), bootstyle="dark")
category_label.grid(row=3, column=1, padx=20, sticky='w')  # Align to the left
category_dropdown = ttk.Combobox(main_frame, values=categories, state="readonly", width=18, bootstyle="info")
category_dropdown.grid(row=4, column=1, padx=20, pady=3, sticky="ew")  # Smaller width and padding

# Subcategory Dropdown (hidden initially, in main frame)
sub_category_label = ttk.Label(main_frame, text="Subcategory", font=("Helvetica", 10), bootstyle="dark")
sub_category_label.grid(row=5, column=1, padx=20, sticky='w')
sub_category_label.grid_remove()  # Initially hidden

sub_category = ttk.Combobox(main_frame, values=[], state="readonly", width=18, bootstyle="info")
sub_category.grid(row=6, column=1, padx=20, pady=3, sticky="ew")  # Smaller width and padding
sub_category.grid_remove()  # Initially hidden

# Function to update subcategories when category changes
def update_subcategories(event):
    selected_category = category_dropdown.get()
    
    # Update subcategory options
    sub_category['values'] = subcategories.get(selected_category, [])  
    
    # Make subcategory dropdown visible if a category is selected
    if selected_category:
        sub_category_label.grid()
        sub_category.grid()
    else:
        sub_category_label.grid_remove()
        sub_category.grid_remove()

# Bind the category dropdown to update subcategories when a selection is made
category_dropdown.bind("<<ComboboxSelected>>", update_subcategories)

# Function to add an expense to the treeview
def add_expense():
    amount = amount_entry.get()
    selected_category = category_dropdown.get()
    selected_subcategory = sub_category.get()
    
    # Validate that an amount and category are selected
    if amount and selected_category:
        tree.insert('', 'end', values=(amount, selected_subcategory, selected_category))
        
        # Automatically adjust the column width based on content length
        adjust_column_width(tree, 'Amount', amount)
        adjust_column_width(tree, 'Description', selected_subcategory)
        adjust_column_width(tree, 'Category', selected_category)
        
        # Clear input fields
        amount_entry.delete(0, 'end')
        category_dropdown.set('')
        sub_category.set('')
        
        # Hide subcategory again
        sub_category_label.grid_remove()
        sub_category.grid_remove()

# Add validation to ensure only digits can be entered in the Amount field
def validate_amount(P):
    return P.isdigit() or P == ""  # Allows digits or an empty string

vcmd = (root.register(validate_amount), '%P')
amount_entry.config(validate="key", validatecommand=vcmd)

# Function to automatically adjust column width based on content
def adjust_column_width(tree, col_name, new_value):
    current_width = tree.column(col_name, width=None)  # Get the current width of the column
    text_width = len(new_value) * 7  # Estimate pixel width based on character count (7 pixels per character)

    # If the new value's width is larger than the current column width, resize the column
    if text_width > current_width:
        tree.column(col_name, width=text_width)

# Add Expense Button (in main frame)
add_button = ttk.Button(main_frame, text="Add Expense", bootstyle="primary", width=16, command=add_expense)
add_button.grid(row=7, column=1, pady=5, sticky="ew")  # Smaller width and padding

# "View" Button to switch to the Treeview Frame
view_button = ttk.Button(main_frame, text="View Expenses", bootstyle="success", width=16, command=lambda: show_frame(treeview_frame))
view_button.grid(row=8, column=1, pady=5, sticky="ew")  # Smaller width and padding

### Treeview Frame (for viewing expenses) ###

# Configure rows and columns for treeview frame
treeview_frame.grid_rowconfigure(0, weight=1)
treeview_frame.grid_columnconfigure(0, weight=1)

# Treeview for displaying expenses (in treeview frame)
tree_frame = ttk.Frame(treeview_frame)
tree_frame.grid(row=0, column=0, pady=5, padx=10, sticky='nsew')

# Configure the Treeview (in treeview frame)
tree = ttk.Treeview(tree_frame, columns=('Amount', 'Description', 'Category'), show='headings', height=10)
tree.heading('Amount', text='Amount')
tree.heading('Description', text='Description')
tree.heading('Category', text='Category')

# Set initial column widths
tree.column('Amount', width=80)
tree.column('Description', width=120)  # Adjusted for better fit
tree.column('Category', width=80)

# Add a vertical scrollbar for the Treeview
scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
scrollbar.pack(side='right', fill='y')
tree.configure(yscrollcommand=scrollbar.set)

# Pack the treeview (in treeview frame)
tree.pack(fill='both', expand=True)

# "Back" Button to switch back to the main frame
back_button = ttk.Button(treeview_frame, text="Back", bootstyle="warning", width=16, command=lambda: show_frame(main_frame))
back_button.grid(row=1, column=0, pady=5)

# CSV Export Button
def export_to_csv():
    # Get all items in the treeview
    rows = tree.get_children()
    
    # Create a CSV file and write the data
    with open('expenses.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(['Amount', 'Description', 'Category'])
        
        # Write data from treeview
        for row in rows:
            writer.writerow(tree.item(row, 'values'))

    print("Data exported to 'expenses.csv'")

# CSV Export Button (in treeview frame)
export_button = ttk.Button(treeview_frame, text="Export to CSV", bootstyle="info", width=16, command=export_to_csv)
export_button.grid(row=2, column=0, pady=10)

# Configure the grid row/column weights for resizing
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Show the main frame initially
show_frame(main_frame)

# Start the Tkinter main loop
root.mainloop()
