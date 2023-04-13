import tkinter as tk

class MyFullNameApp:
    def __init__(self, master):
        self.master = master
        master.title("Midterm Exam 2")
        master.config(bg="white")
        master.geometry("800x400")
        master.resizable(False, False)
        master.option_add("*Font", "Verdana")

        

        self.given_name_label = tk.Label(master, text="Enter Given Name:", fg="red")
        self.given_name_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)

        self.middle_name_label = tk.Label(master, text="Enter Middle Name:", fg="red")
        self.middle_name_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)

        self.last_name_label = tk.Label(master, text="Enter Last Name:", fg="red")
        self.last_name_label.grid(row=3, column=0, sticky="w", padx=10, pady=10)

        self.full_name_label = tk.Label(master, text="Enter My Full Name is:", fg="red")
        self.full_name_label.grid(row=4, column=0, sticky="w", padx=10, pady=10,)

        self.given_name_entry = tk.Entry(master)
        self.given_name_entry.grid(row=1, column=1, padx=10, pady=10)

        self.middle_name_entry = tk.Entry(master)
        self.middle_name_entry.grid(row=2, column=1, padx=10, pady=10)

        self.last_name_entry = tk.Entry(master)
        self.last_name_entry.grid(row=3, column=1, padx=10, pady=10)

        self.full_name_entry = tk.Entry(master, state="readonly", readonlybackground="white")
        self.full_name_entry.grid(row=4, column=1, padx=10, pady=10)

        self.show_full_name_button = tk.Button(master, text="Show Full Name", command=self.show_full_name, bg="white",
                                               width=15)
        self.show_full_name_button.grid(row=5, column=1, padx=10, pady=10)

        self.clear_all_button = tk.Button(master, text="Clear All", command=self.clear_all, bg="white", width=15)
        self.clear_all_button.grid(row=6, column=1, padx=10, pady=10)

    def show_full_name(self):
        given_name = self.given_name_entry.get()
        middle_name = self.middle_name_entry.get()
        last_name = self.last_name_entry.get()
        full_name = f"{last_name}, {given_name} {middle_name}"
        self.full_name_entry.config(state="normal")
        self.full_name_entry.config(fg="red")
        self.full_name_entry.delete(0, tk.END)
        self.full_name_entry.insert(0, full_name)
        self.full_name_entry.config(state="readonly")

    def clear_all(self):
        self.given_name_entry.delete(0, tk.END)
        self.middle_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.full_name_entry.config(state="normal")
        self.full_name_entry.delete(0, tk.END)
        self.full_name_entry.config(state="readonly")


if __name__ == "__main__":
    root = tk.Tk()
    app = MyFullNameApp(root)
    root.mainloop()