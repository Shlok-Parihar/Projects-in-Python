import tkinter as tk
from tkinter import Scrollbar, Canvas, Frame, messagebox, Toplevel
from tkinter import *
import mysql.connector
from PIL import Image, ImageTk
from tkinter import font as tkFont  # Import font module
from functools import partial  # For partial function binding
import re, os
import pyglet

# Validation needed. email phone.


root = tk.Tk()
root.title("Sunshine Autos")
root.geometry("1280x720")
pyglet.font.add_file('Carattere-Regular.ttf')

# # Title with large font and in bold
# title_font = tkFont.Font(family="Helvetica", size=62, weight="bold")  # Adjust font as needed
# title_label = tk.Label(root, text="Sunshine Autos", font=title_font)
# title_label.place(x=265, y=50)  # Add padding below the title



def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="S#l0k022",
            database="cars_showroom"



        )
        if connection.is_connected():
            print("Connection Successful.")
        return connection
    except mysql.connector.Error as err:
        print(f"Connection Error Found : {err}")
        return None

db_conn = connect_to_db()

def create_transparent_background(image_path, opacity):
    original = Image.open(image_path).convert("RGBA")
    transparent = Image.new("RGBA", original.size)

    for x in range(original.width):
        for y in range(original.height):
            r, g, b, a = original.getpixel((x, y))
            new_a = int(a * opacity)  # Adjusting the alpha for transparency
            transparent.putpixel((x, y), (r, g, b, new_a))

    return transparent


try:
    bg_image = create_transparent_background('sunshine-autos-logo.jpg', 0.2)  # Adjust opacity here
    bg_image = bg_image.resize((1280, 720))
    bg_tk = ImageTk.PhotoImage(bg_image)
    
    bg_label = Label(root, image=bg_tk)
    bg_label.image = bg_tk  # Reference to avoid garbage collection
    bg_label.place(x=0, y=0)


except Exception as e:
    print(f"Error loading images: {e}")



class ScrollableFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Create a canvas for the scrollable area
        self.canvas = Canvas(self)
        self.canvas.config(width=1920, height=420)
        self.scrollbar = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas)

        # Configure the canvas
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # Create a window in the canvas
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Pack everything
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Bind mouse wheel scrolling
        self.bind_scroll()

    def bind_scroll(self):
        # Bind mouse wheel scrolling.
        self.canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)

    def on_mouse_wheel(self, event):
        self.canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def on_mouse_wheel_up(self, event):
        self.canvas.yview_scroll(-1, "units")

    def on_mouse_wheel_down(self, event):
        self.canvas.yview_scroll(1, "units")

# Create the main window

scrollable_frame = ScrollableFrame(root)
scrollable_frame.pack(fill="both", expand=True)
scrollable_frame.place(x=5, y=165)  # Adjust position as needed

# Adjust the logo image Settings from here.
try:
    logo_image = Image.open('sunshine-autos-logo.jpg')  # Update with your logo file name
    logo_image = logo_image.resize((330, 185))  # Resize logo if needed
    logo_tk = ImageTk.PhotoImage(logo_image)

    logo_label = tk.Label(root, image=logo_tk)
    logo_label.image = logo_tk  # Keep a reference to avoid garbage collection
    logo_label.place(x=50, y=20)  # Add some padding at the top
except Exception as e:
    print(f"Error loading images: {e}")

# Title with large font and in bold
title_font = tkFont.Font(family="Helvetica", size=42, weight="bold")  # Adjust font as needed
title_label = tk.Label(root, text="Welcome to Sunshine Autos", font=title_font, bg='pink', fg='orange')
title_label.place(x=430, y=75)  # Add padding below the title

# Scrollview
scrollable_frame = ScrollableFrame(root)
scrollable_frame.pack(fill="both", expand=True)
scrollable_frame.place(x=49, y=220)  # Adjust position as needed

def buynow(car_vin, image_path):
    # add Dictionary mapping and make it work like switch cases, and we done.
    #est_list = [[4, 2, 1], [1, 2, 3]], sub_dict = {1 : “gfg”, 2: “best”, 3 : “CS”, 4 : “Geeks”} Output : [[‘Geeks’, ‘best’, ‘gfg’], [‘gfg’, ‘best’, ‘CS’]]
    # Explanation : Matrix elements are substituted using dictionary. Input : test_list = [[4, 2, 1]], sub_dict = {1 : “gfg”, 2: “best”, 4 : “Geeks”} Output : [[‘Geeks’, ‘best’, ‘gfg’]]

    print(f"Buy Now button clicked for VIN: {car_vin}")  # Debugging statement

    if not db_conn or not db_conn.is_connected():
        messagebox.showerror("Connection Error", "Not connected to the database.")
        return

    try:
        purchase = Toplevel(root)
        purchase.title("Buy your Car")
        purchase.geometry("640x540")
        purchase.attributes('-topmost', True)

        try:
            car_image = Image.open(image_path)  # Open the image file
            resized_car_image = car_image.resize((300, 200))  # Resize the image
            car_image_tk = ImageTk.PhotoImage(resized_car_image)  # Convert to PhotoImage
            car_image_label = tk.Label(purchase, image=car_image_tk)
            car_image_label.image = car_image_tk  # Keep a reference
            car_image_label.grid(column=1, sticky='ew', pady=10)  # Add some padding
        except Exception as e:
            print(f"Error loading car image: {e}")

        # Labels for customer information
        Label(purchase, text="Full Name:", font=("Helvetica", 12)).grid(row=1, column=0, sticky='e', padx=10, pady=10)
        name_var = StringVar()
        Entry(purchase, textvariable=name_var, width=40).grid(row=1, column=1, padx=10, pady=10)

        Label(purchase, text="Phone:", font=("Helvetica", 12)).grid(row=2, column=0, sticky='e', padx=10, pady=10)
        phone_var = StringVar()
        Entry(purchase, textvariable=phone_var, width=40).grid(row=2, column=1, padx=10, pady=10)

        # Label(purchase, text="Address:", font=("Helvetica", 12)).grid(row=3, column=0, sticky='e', padx=10, pady=10)
        # add_var = StringVar()
        # Entry(purchase, textvariable=add_var, width=40).grid(row=3, column=1, padx=10, pady=10)

        Label(purchase, text="Email Address:", font=("Helvetica", 12)).grid(row=4, column=0, sticky='e', padx=10, pady=10)
        email_var = StringVar()
        Entry(purchase, textvariable=email_var, width=40).grid(row=4, column=1, padx=10, pady=10)

        # Display the car VIN as a label (uneditable)
        Label(purchase, text="Car VIN:", font=("Helvetica", 12)).grid(row=5, column=0, sticky='e', padx=10, pady=10)
        carvin_label = Label(purchase, text=car_vin, font=("Helvetica", 12))  # Display VIN here
        carvin_label.grid(row=5, column=1, sticky='w', padx=10, pady=10)

        # Empty label for spacing
        Label(purchase, text="", font=("Helvetica", 12)).grid(row=6, column=0, sticky='e', padx=10, pady=10)

        # Insert function for processing the purchase
        def insert():
            name = name_var.get().strip()
            phone = phone_var.get().strip()
            # address = add_var.get().strip()
            email = email_var.get().strip()

            # Basic Validation
            if not name:
                messagebox.showwarning(purchase)
                messagebox.showwarning("Input Error", "Please enter your full name.", parent=purchase)

                return
            
            if not phone.isdigit() or len(phone) != 10:
                messagebox.showwarning("Input Error", "Please Enter Phone number correctly.", parent=purchase)
                return
            
            pattern = r'^[^@]+@[^@]+\.[^@]+$'
            if not re.match(pattern, email):
                messagebox.showwarning("Input Error","Please enter correct format of email", parent=purchase)
                return

            if not (name, phone, email):
                messagebox.showwarning("Input Error", "Transaction failed.", parent=purchase)
            # Further validation can be added here (e.g., email format, phone number digits)

            # Update the database
            try:

                cursor = db_conn.cursor()
                # Insert into customers table
                insert_query = """
                INSERT INTO customers (Cust_Name, Cust_phone, Cust_email, CustCar_VIN)
                VALUES (%s, %s, %s, %s)
                """
                cursor.execute(insert_query, (name, phone, email, car_vin))

                # Update the car status to 'SOLD'
                update_query = """
                UPDATE cars
                SET Cars_Status = 'SOLD'
                WHERE Cars_VIN = %s
                """
                cursor.execute(update_query, (car_vin,))
                db_conn.commit()
                
                congrats = Toplevel(purchase)
                congrats.title("Congratulations.!")
                congrats.geometry("560x560")
                congrats.attributes("-topmost", True)
                
                try:
                    bg_image = create_transparent_background('sunshine-autos-logo.jpg', 0.2)  # Adjust opacity here
                    bg_image = bg_image.resize((560, 560))
                    bg_tk = ImageTk.PhotoImage(bg_image)
                    
                    bg_label = Label(congrats, image=bg_tk)
                    bg_label.image = bg_tk  # Reference to avoid garbage collection
                    bg_label.place(x=0, y=0)
                except Exception as e:
                    print(f"Error loading images: {e}")


                congrats_label = tk.Label(congrats, text="Congratulations.!!", font=("Carattere Regular", 28, "bold"), fg="green", bg="pink")
                congrats_label.place(x=155, y=40)
                


                def thanks():
                    purchase.destroy()
                    congrats.destroy()

                    return

                try:
                    car_image = Image.open(image_path)  # Open the image file
                    resized_car_image = car_image.resize((380, 230))  # Resize the image
                    car_image_tk = ImageTk.PhotoImage(resized_car_image)  # Convert to PhotoImage
                    car_image_label = tk.Label(congrats, image=car_image_tk)
                    car_image_label.image = car_image_tk  # Keep a reference
                    car_image_label.place(x=80, y=110)  # Add some padding
                except Exception as e:
                    print(f"Error loading car image: {e}", parent=purchase)
                
                tk.Button(congrats, text="Thank You.", bg="yellow", fg="black", command=thanks, font="Carattere-Regular.ttf").place(x=190,y=420)

                # messagebox.showinfo("Success", "Transaction successful. Congratulations!", parent=purchase)
                
                cursor.close()
            except mysql.connector.Error as err:
                print(f"DB Error: {err}")
                messagebox.showerror("Database Error", f"Error: {err}", parent=purchase)
                db_conn.rollback()

        # Confirm Button
        Button(
            purchase,
            text="CONFIRM",
            command=insert,
            width=25,
            border=5,
            bg="green",
            fg="white",
            height=2
        ).grid(row=6, column=1, sticky='ews', padx=10, pady=10)

    except Exception as e:
        print(f"Error in buynow: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}",parent=purchase)


def display_cars_from_db():
    try:
        cursor = db_conn.cursor(dictionary=True)
        query = "SELECT * FROM cars_showroom.cars"
        cursor.execute(query)

        rows = cursor.fetchall()
        for index, car in enumerate(rows):
            # Load image
            try:
                img = Image.open(car['Cars_Image'])  # Get images from car_array
                resized_image = img.resize((400, 240))  # Resize the image
                tk_image = ImageTk.PhotoImage(resized_image)  # Convert to PhotoImage

                # Create a Label to display the image
                label = tk.Label(scrollable_frame.scrollable_frame, image=tk_image)
                label.image = tk_image  # Reference to avoid garbage collection
                label.grid(row=index, column=0, padx=5, pady=5)  # Image in Column 0
            except Exception as e:
                print(f"Error loading image for {car['Cars_Name']}: {e}")
                continue  # Skip this car if image fails to load

            desc_font = tkFont.Font(family="Garamond", size=12)
            head_font = tkFont.Font(family="Times New Roman", size=16, weight="bold")

            # Heading in Column 1
            heading_label = tk.Label(scrollable_frame.scrollable_frame, text=car["Cars_Name"], font=("Arial", 16, "bold"), relief="raised")
            heading_label.grid(row=index, column=1, sticky="n", padx=10, pady=5)

            # Description in Column 1
            description_label = tk.Label(scrollable_frame.scrollable_frame, text=car["Cars_Description"], font=desc_font, wraplength=400, justify="left")
            description_label.grid(row=index, column=1, sticky="ew", padx=10, pady=5)  # Description in Column 1

            # VIN Label in Column 1
            vin_label = tk.Label(scrollable_frame.scrollable_frame, text=f"VIN: {car['Cars_VIN']}", font=("Arial", 16, "bold"))
            vin_label.grid(row=index, column=2, sticky="n", padx=10, pady=5)  # Adjust padding as needed

            # Price in Column 2
            car_price = tk.Label(scrollable_frame.scrollable_frame, text=car["Cars_Price"], font=("Helvetica", 14, "bold"), fg="green")
            car_price.grid(row=index, column=3, sticky="nw", padx=10, pady=5)

            car_status = tk.Label(scrollable_frame.scrollable_frame, text=car["Cars_Status"], font=("Helvetica", 14, "bold"), fg=("green" if car["Cars_Status"] == "SOLD" else "blue"), relief="groove")
            car_status.grid(row=index, column=3, sticky="ew", padx=10, pady=5)

            if car["Cars_Status"] == "SOLD":  # Check if the car is sold
                try:  # Attempt to fetch the customer name from the database
                    cursor = db_conn.cursor(dictionary=True)  # Important: dictionary cursor
                    get_customer_query = """
                        SELECT Cust_name 
                        FROM cars_showroom.customers 
                        WHERE Cust_ID = (SELECT Cust_ID FROM customers WHERE CustCar_VIN = %s)
                    """  # Assuming you have a sales table linking cars and customers 
                    cursor.execute(get_customer_query, (car['Cars_VIN'],))
                    customer_record = cursor.fetchone()
                    cursor.close()

                    customer_name = customer_record['Cust_name'] if customer_record else "Unknown Customer"  # Handle cases where customer isn't found

                    customer_label = tk.Label(scrollable_frame.scrollable_frame, text=f"Sold to: {customer_name}", font=("Helvetica", 12))
                    customer_label.grid(row=index, column=1, sticky="s", padx=5, pady=2)  # Adjust grid position as needed

                except mysql.connector.Error as err:
                    print(f"Error fetching customer name: {err}")
                    customer_label = tk.Label(scrollable_frame.scrollable_frame, text="Error fetching customer", font=("Helvetica", 12), fg="red")
                    customer_label.grid(row=index, column=1, sticky="sew", padx=5, pady=2)

            else:  # Only show "Buy Now" button if the car is not sold
                tk.Button(
                    scrollable_frame.scrollable_frame,
                    text="Buy Now",
                    command=lambda v=car['Cars_VIN'], img=car['Cars_Image']: buynow(v, img),
                    bg="blue",
                    fg="white",
                    font=head_font,
                    width=10
                ).grid(row=index, column=4, sticky="ew", pady=5)

    except Exception as e:
        print(f"Error loading cars: {e}")
# Start the Tkinter event loop

display_cars_from_db()
root.mainloop()
