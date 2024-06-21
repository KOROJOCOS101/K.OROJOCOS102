import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Function to handle the search and display of employee information
def search_employee():
    name = name_entry.get().strip().title()  # Get the user's name and format it
    department = department_entry.get().strip().title()  # Get and format the department

    # Create a 'Name' column by concatenating 'SURNAME' and 'FIRST NAME'
    if 'Name' not in df.columns:
        df['Name'] = df['SURNAME'].str.title() + ' ' + df['FIRST NAME'].str.title()

    # Search for the employee in the dataset
    employee = df[(df['Name'] == name) & (df['DEPARTMENT'] == department)]

    if not employee.empty:
        # Exclude the entered employee from the list of other members in the department
        other_members = df[(df['DEPARTMENT'] == department) & (df['Name'] != name)]
        other_member_names = other_members['Name'].tolist()

        messagebox.showinfo("Employee Found", f"Welcome, {name}!\nOther members of {department} department:\n{', '.join(other_member_names)}")
    else:
        messagebox.showerror("Employee Not Found", f"No employee named {name} found in {department} department.")

# Read the dataset
df = pd.read_csv('GIG-logistics.csv')

# Create the main window
root = tk.Tk()
root.title("Employee Verification")
root.geometry("400x200")

# Label and entry for the user's name
name_label = tk.Label(root, text="Enter Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Label and entry for the user's department
department_label = tk.Label(root, text="Enter Department:")
department_label.pack()
department_entry = tk.Entry(root)
department_entry.pack()

# Button to submit the information and search for the employee
submit_button = tk.Button(root, text="Verify", command=search_employee)
submit_button.pack()

# Run the main event loop
root.mainloop()
