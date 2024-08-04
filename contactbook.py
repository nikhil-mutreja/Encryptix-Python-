from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

class ContactBook(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.contacts = {}
        self.username = "admin"
        self.password = "admin"

        self.title("Contact Book")
        self.geometry("600x400")

        self.style = Style()
        self.style.configure('Header.TFrame', background="blue")
        self.style.configure('Header.TLabel', background="blue", foreground="white", font=("Arial", 20))
        self.style.configure('TButton', font=("Arial", 12))
        self.style.configure('TLabel', font=("Arial", 12))
        self.style.configure('TEntry', font=("Arial", 12))

        self.show_login_screen()

    def show_login_screen(self):
        self.clear_screen()

        login_frame = Frame(self)
        login_frame.pack(pady=50)

        Label(login_frame, text="Username:", style='TLabel').grid(row=0, column=0, pady=5)
        self.username_entry = Entry(login_frame, style='TEntry')
        self.username_entry.grid(row=0, column=1, pady=5)

        Label(login_frame, text="Password:", style='TLabel').grid(row=1, column=0, pady=5)
        self.password_entry = Entry(login_frame, show="*", style='TEntry')
        self.password_entry.grid(row=1, column=1, pady=5)

        Button(login_frame, text="Login", style='TButton', command=self.login).grid(row=2, column=1, pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == self.username and password == self.password:
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

    def show_main_menu(self):
        self.clear_screen()

        header_frame = Frame(self, style='Header.TFrame')
        header_frame.pack(fill=X)
        Label(header_frame, text="My Contact Book", style='Header.TLabel').pack(pady=10)

        content_frame = Frame(self)
        content_frame.pack(fill=BOTH, expand=True)

        Button(content_frame, text="Add Contact", command=self.add_contact).pack(pady=5)
        Button(content_frame, text="View Contact List", command=self.view_contacts).pack(pady=5)
        Button(content_frame, text="Search Contact", command=self.search_contact).pack(pady=5)
        Button(content_frame, text="Update Contact", command=self.update_contact).pack(pady=5)
        Button(content_frame, text="Delete Contact", command=self.delete_contact).pack(pady=5)
        Button(content_frame, text="Change Password", command=self.change_password).pack(pady=5)
        Button(content_frame, text="Logout", command=self.show_login_screen).pack(pady=5)

    def add_contact(self):
        self.clear_screen()

        frame = Frame(self)
        frame.pack(pady=20)

        Label(frame, text="Name:", style='TLabel').grid(row=0, column=0, pady=5)
        self.name_entry = Entry(frame, style='TEntry')
        self.name_entry.grid(row=0, column=1, pady=5)

        Label(frame, text="Phone Number:", style='TLabel').grid(row=1, column=0, pady=5)
        self.phone_entry = Entry(frame, style='TEntry')
        self.phone_entry.grid(row=1, column=1, pady=5)

        Label(frame, text="Email:", style='TLabel').grid(row=2, column=0, pady=5)
        self.email_entry = Entry(frame, style='TEntry')
        self.email_entry.grid(row=2, column=1, pady=5)

        Label(frame, text="Address:", style='TLabel').grid(row=3, column=0, pady=5)
        self.address_entry = Entry(frame, style='TEntry')
        self.address_entry.grid(row=3, column=1, pady=5)

        Button(frame, text="Save Contact", style='TButton', command=self.save_contact).grid(row=4, column=1, pady=5)
        Button(frame, text="Back", style='TButton', command=self.show_main_menu).grid(row=5, column=1, pady=5)

    def save_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts[phone] = {'name': name, 'email': email, 'address': address}
            messagebox.showinfo("Success", "Contact saved successfully!")
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Name and Phone Number are required!")

    def view_contacts(self):
        self.clear_screen()

        frame = Frame(self)
        frame.pack(pady=20)

        row = 0
        for phone, details in self.contacts.items():
            Label(frame, text=f"Name: {details['name']}", style='TLabel').grid(row=row, column=0, pady=5)
            Label(frame, text=f"Phone: {phone}", style='TLabel').grid(row=row, column=1, pady=5)
            row += 1

        Button(frame, text="Back", style='TButton', command=self.show_main_menu).grid(row=row, column=1, pady=5)

    def search_contact(self):
        self.clear_screen()

        frame = Frame(self)
        frame.pack(pady=20)

        Label(frame, text="Enter Name or Phone Number:", style='TLabel').grid(row=0, column=0, pady=5)
        self.search_entry = Entry(frame, style='TEntry')
        self.search_entry.grid(row=0, column=1, pady=5)

        Button(frame, text="Search", style='TButton', command=self.perform_search).grid(row=1, column=1, pady=5)
        Button(frame, text="Back", style='TButton', command=self.show_main_menu).grid(row=2, column=1, pady=5)

    def perform_search(self):
        search_term = self.search_entry.get()
        results = {phone: details for phone, details in self.contacts.items() if search_term in phone or search_term in details['name']}

        self.clear_screen()

        frame = Frame(self)
        frame.pack(pady=20)

        if results:
            row = 0
            for phone, details in results.items():
                Label(frame, text=f"Name: {details['name']}", style='TLabel').grid(row=row, column=0, pady=5)
                Label(frame, text=f"Phone: {phone}", style='TLabel').grid(row=row, column=1, pady=5)
                row += 1
        else:
            Label(frame, text="No contacts found!", style='TLabel').pack(pady=20)

        Button(frame, text="Back", style='TButton', command=self.search_contact).pack(pady=20)

    def update_contact(self):
        self.clear_screen()

        frame = Frame(self)
        frame.pack(pady=20)

        Label(frame, text="Enter Phone Number to Update:", style='TLabel').grid(row=0, column=0, pady=5)
        self.update_phone_entry = Entry(frame, style='TEntry')
        self.update_phone_entry.grid(row=0, column=1, pady=5)

        Button(frame, text="Search", style='TButton', command=self.load_contact_for_update).grid(row=1, column=1, pady=5)
        Button(frame, text="Back", style='TButton', command=self.show_main_menu).grid(row=2, column=1, pady=5)

    def load_contact_for_update(self):
        phone = self.update_phone_entry.get()
        if phone in self.contacts:
            self.clear_screen()

            frame = Frame(self)
            frame.pack(pady=20)

            Label(frame, text="Name:", style='TLabel').grid(row=0, column=0, pady=5)
            self.update_name_entry = Entry(frame, style='TEntry')
            self.update_name_entry.insert(0, self.contacts[phone]['name'])
            self.update_name_entry.grid(row=0, column=1, pady=5)

            Label(frame, text="Email:", style='TLabel').grid(row=1, column=0, pady=5)
            self.update_email_entry = Entry(frame, style='TEntry')
            self.update_email_entry.insert(0, self.contacts[phone]['email'])
            self.update_email_entry.grid(row=1, column=1, pady=5)

            Label(frame, text="Address:", style='TLabel').grid(row=2, column=0, pady=5)
            self.update_address_entry = Entry(frame, style='TEntry')
            self.update_address_entry.insert(0, self.contacts[phone]['address'])
            self.update_address_entry.grid(row=2, column=1, pady=5)

            Button(frame, text="Update Contact", style='TButton', command=lambda: self.save_updated_contact(phone)).grid(row=3, column=1, pady=5)
            Button(frame, text="Back", style='TButton', command=self.show_main_menu).grid(row=4, column=1, pady=5)
        else:
            messagebox.showerror("Error", "Contact not found!")

    def save_updated_contact(self, phone):
        self.contacts[phone]['name'] = self.update_name_entry.get()
        self.contacts[phone]['email'] = self.update_email_entry.get()
        self.contacts[phone]['address'] = self.update_address_entry.get()
        messagebox.showinfo("Success", "Contact updated successfully!")
        self.show_main_menu()

    def delete_contact(self):
        self.clear_screen()

        frame = Frame(self)
        frame.pack(pady=20)

        Label(frame, text="Enter Phone Number to Delete:", style='TLabel').grid(row=0, column=0, pady=5)
        self.delete_phone_entry = Entry(frame, style='TEntry')
        self.delete_phone_entry.grid(row=0, column=1, pady=5)

        Button(frame, text="Delete", style='TButton', command=self.perform_delete).grid(row=1, column=1, pady=5)
        Button(frame, text="Back", style='TButton', command=self.show_main_menu).grid(row=2, column=1, pady=5)

    def perform_delete(self):
        phone = self.delete_phone_entry.get()
        if phone in self.contacts:
            del self.contacts[phone]
            messagebox.showinfo("Success", "Contact deleted successfully!")
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Contact not found!")

    def change_password(self):
        self.clear_screen()

        frame = Frame(self)
        frame.pack(pady=20)

        Label(frame, text="Old Password:", style='TLabel').grid(row=0, column=0, pady=5)
        self.old_password_entry = Entry(frame, show="*", style='TEntry')
        self.old_password_entry.grid(row=0, column=1, pady=5)

        Label(frame, text="New Password:", style='TLabel').grid(row=1, column=0, pady=5)
        self.new_password_entry = Entry(frame, show="*", style='TEntry')
        self.new_password_entry.grid(row=1, column=1, pady=5)

        Label(frame, text="Confirm Password:", style='TLabel').grid(row=2, column=0, pady=5)
        self.confirm_password_entry = Entry(frame, show="*", style='TEntry')
        self.confirm_password_entry.grid(row=2, column=1, pady=5)

        Button(frame, text="Change Password", style='TButton', command=self.save_new_password).grid(row=3, column=1, pady=5)
        Button(frame, text="Back", style='TButton', command=self.show_main_menu).grid(row=4, column=1, pady=5)

    def save_new_password(self):
        old_password = self.old_password_entry.get()
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if old_password == self.password:
            if new_password == confirm_password:
                self.password = new_password
                messagebox.showinfo("Success", "Password changed successfully!")
                self.show_main_menu()
            else:
                messagebox.showerror("Error", "New passwords do not match!")
        else:
            messagebox.showerror("Error", "Old password is incorrect!")

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = ContactBook()
    app.mainloop()
