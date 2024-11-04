from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import font as tkFont
from tkinter import filedialog
import re



root = Tk()
root.title("Sunshine Autos")
root.geometry("1280x720")

################################################################################################################################################################################################################
################################################################################################################################################################################################################
################################################################################################################################################################################################################
################################################################################################################################################################################################################

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
        print(f"Error Found : {err}")
        return None

db_conn = connect_to_db()


################################################################################################################################################################################################################
################################################################################################################################################################################################################
################################################################################################################################################################################################################
################################################################################################################################################################################################################

def create_transparent_background(image_path, opacity):
    original = Image.open(image_path).convert("RGBA")
    transparent = Image.new("RGBA", original.size)

    for x in range(original.width):
        for y in range(original.height):
            r, g, b, a = original.getpixel((x, y))
            new_a = int(a * opacity)  # Adjusting the alpha for transparency
            transparent.putpixel((x, y), (r, g, b, new_a))

    return transparent

#BG image
try:
    bg_image = create_transparent_background('sunshine-autos-logo.jpg', 0.2)  # Adjust opacity here
    bg_image = bg_image.resize((1280, 720))
    bg_tk = ImageTk.PhotoImage(bg_image)
    
    bg_label = Label(root, image=bg_tk)
    bg_label.image = bg_tk  # Reference to avoid garbage collection
    bg_label.place(x=0, y=0)

    logo_image = Image.open('sunshine-autos-logo.jpg') 
    logo_image = logo_image.resize((165, 100))
    logo_tk = ImageTk.PhotoImage(logo_image)
    
    logo_label = tk.Label(root, image=logo_tk)
    logo_label.image = logo_tk
    logo_label.place(x=50, y=50)

except Exception as e:
    print(f"Error loading images: {e}")


# Title with large font and in bold
title_font = tkFont.Font(family="Helvetica", size=62, weight="bold")  # Adjust font
title_label = tk.Label(root, text="Sunshine Autos", font=title_font)
title_label.place(x=265, y=50)  # Add padding below the title

add_image = Image.open('add64.png')  # Replace with your image file
add_image = add_image.resize((50, 50))  # Resize as needed
add_photo = ImageTk.PhotoImage(add_image)
def add_inv():
    add_font = tkFont.Font(family="Ariel",size=12, weight="bold")
    Button(root, text=" Add Inventory", image=add_photo, compound=TOP,border=5, font=add_font, bg='white', fg='black', command=add_btn, width=120, height=88).place(x=940, y=50)
search_image = Image.open('search64.png')  # Replace with your image file
search_image = search_image.resize((50, 50))  # Resize as needed
search_photo = ImageTk.PhotoImage(search_image)
def search():
    add_font = tkFont.Font(family="Ariel",size=12, weight="bold")
    #     vin = search_vin_var.get().strip()
    #     upd_win.attributes('-top', True)
            
    #     if not vin:
    #         # upd_win.attributes('-top', False)
    #         messagebox.showwarning("Input Error", "Car VIN is required to search.", parent=upd_win)
    #         return
    #     try:
    #         cursor = db_conn.cursor()
    #         select_query = "SELECT * FROM cars_showroom.cars WHERE Cars_VIN = %s"
    #         cursor.execute(select_query, (vin,))
    #         record = cursor.fetchone()
    #         cursor.close()

    #         if record:
    #             name_var.set(record[1])
    #             type_var.set(record[2])
    #             price_var.set(record[3])
    #             status_var.set(record[4])
    #             year_var.set(record[5])
    #         else:
    #             messagebox.showinfo("Not Found", "No car found with the provided VIN.",parent=upd_win)
    #     except mysql.connector.Error as err:
    #         print(f"Database Error: {err}")

    # Button(upd_win, text="SEARCH", command=search, width=15, border=4).place(x=490, y=43)

    # Label(upd_win, text="Car Name : ", font=("Helvetica", 12)).place(x=45 ,y=170)
    # name_var = StringVar()
    # Entry(upd_win, textvariable=name_var, width=30).place(x=130 ,y=173)

    # Label(upd_win, text="Car Type : ", font=("Helvetica", 12)).place(x=45 ,y=220)
    # type_var = StringVar()
    # Entry(upd_win, textvariable=type_var, width=30).place(x=130 ,y=223)

    

    # Label(upd_win, text="Car Price : ", font=("Helvetica", 12)).place(x=45 ,y=120)
    # price_var = StringVar()
    # Entry(upd_win, textvariable=price_var, width=30).place(x=130 ,y=122)

    # Label(upd_win, text="Status : ", font=("Helvetica", 12)).place(x=375 ,y=220)
    # status_var = StringVar()
    # Entry(upd_win, textvariable=status_var, width=30).place(x=450 ,y=223)

    
    # Label(upd_win, text="Car Year : ", font=("Helvetica", 12)).place(x=375 ,y=170)
    # year_var = StringVar()
    # Entry(upd_win, textvariable=year_var, width=30).place(x=453 ,y=173)
    Button(root, text="Search", image=search_photo, compound=TOP,border=5, font=add_font, bg='white', fg='black', command=search_all, width=120, height=88).place(x=1080, y=50)
        

################################################################################################################################################################################################################
################################################################################################################################################################################################################
################################################################################################################################################################################################################
################################################################################################################################################################################################################

class ScrollableFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Create a canvas for the scrollable area
        self.canvas = Canvas(self)
        self.canvas.config(width=1920, height=490)
        
        self.scrollbar = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas)

        # self.bg_image = Image.open("path/to/your/sunshine_autos_logo.jpg")  # Load your image
        # self.bg_image = self.bg_image.resize((self.winfo_screenwidth(), self.winfo_screenheight()), Image.ANTIALIAS)
        # self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Configure the canvas
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # Create a window in the canvas
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Pack everything
        self.canvas.pack(side="left", fill=['both'], expand=True)
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


# Scrollview
scrollable_frame = ScrollableFrame(root)
scrollable_frame.pack(fill="both", expand=True)
scrollable_frame.place(x=5, y=165)  # Adjust position as needed

################################################################################################################################################################################################################
###############################################################################################################################################################################################################

def refresh_inventory_display():
    """Clears existing car displays and reloads data from the database."""
    for widget in scrollable_frame.scrollable_frame.winfo_children():
        widget.destroy()  # Clear existing widgets

################################################################################################################################################################################################################
###############################################################################################################################################################################################################


def display_cars_from_db():
  
    try:
        cursor = db_conn.cursor(dictionary=True)
        query = "SELECT * FROM cars_showroom.cars"
        cursor.execute(query)

        rows= cursor.fetchall()
        for index, car in enumerate(rows):
            # Load image
            # Frame(scrollable_frame.scrollable_frame, bd=2, relief="solid")
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
                        WHERE Cust_ID = (SELECT Cust_ID FROM customers WHERE CustCar_VIN = %s LIMIT 1)
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
                    customer_label.grid(row=index, column=1, sticky="w", padx=5, pady=2)




            #Delete Button in Column 3
            del_button = tk.Button(
                scrollable_frame.scrollable_frame,
                text="Delete",
                command=lambda v=car['Cars_VIN']: del_btn(v),  # Assign the function, DON'T call it
                bg="red",
                fg="white",
                font=head_font
            )
            del_button.grid(row=index, column=4, sticky="ew", pady=5)


            #Upgrade Button in Column 4
            updt_button = tk.Button(
                scrollable_frame.scrollable_frame,
                text="Update",
                bg='green',
                fg='White',
                font=head_font,
                command=lambda v=car['Cars_VIN']: updt_btn(v)  # Pass the car_vin here, use lambda function or else it doesnt work
            )
            updt_button.grid(row=index, column=5, sticky="ew", padx=5, pady=5)

    except Exception as e:
        print(f"Error loading cars: {e}")

################################################################################################################################################################################################################
###############################################################################################################################################################################################################


def del_btn(vin): # vin is passed as an argument here
    response = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete record at VIN = {vin}")
    if response:
        try:
            cursor = db_conn.cursor()
            delete_query = "DELETE FROM cars_showroom.cars WHERE Cars_VIN = %s"
            cursor.execute(delete_query, (vin,))
            db_conn.commit()
            
            if cursor.rowcount > 0:
                messagebox.showinfo("Success", "Record deleted successfully.")
                refresh_inventory_display() # Refresh display after deletion
                display_cars_from_db()
            else:
                messagebox.showwarning("Not Found", "No record found with the provided VIN.")
            cursor.close()

        except mysql.connector.Error as err:
            print(f"DB Error.{err}")
            messagebox.showerror("Database Error", f"Error: {err}")
            db_conn.rollback()
    else:
        messagebox.showinfo("Cancelled","Item Deletion Cancelled.")
    return


################################################################################################################################################################################################################
###############################################################################################################################################################################################################


        #     #Delete Button in Column 3
        #     del_button = tk.Button(
        #     scrollable_frame.scrollable_frame,
        #     text="Delete",
        #     bg='red',
        #     fg='White',
        #     font=head_font,
        #     command=lambda v=vin: del_btn(v)  # Pass the car_vin here
        # )
        # del_button.grid(row=index, column=4, sticky="ew", padx=5)
        


################################################################################################################################################################################################################
################################################################################################################################################################################################################
# UPDATE BUTTON FUNCTIONALITY
def updt_btn(vin):
    if not db_conn or not db_conn.is_connected():
        messagebox.showerror("Connection Error", "Not connected to the database.")
        return

    
    upd_win = tk.Toplevel(root)
    upd_win.title("Update Inventory")
    upd_win.geometry("720x505")
    upd_win.attributes('-topmost', True)
    

    try:
        cursor = db_conn.cursor(dictionary=True)
        select_query = """
        SELECT * FROM cars_showroom.cars WHERE Cars_VIN = %s"""
        cursor.execute(select_query, (vin,))
        record = cursor.fetchone()
        cursor.close

        if not record:
            messagebox.showinfo("Not Found", "No car Found with that VIN.", parent=upd_win)
            upd_win.destroy()
            return

        name_var = StringVar(value=record['Cars_Name'])  # Pre-fill with existing data
        type_var = StringVar(value=record['Cars_Type'])
        price_var = StringVar(value=record['Cars_Price'])
        status_var = StringVar(value=record['Cars_Status'])
        year_var = StringVar(value=record['Cars_Year'])
        desc_var = StringVar(value=record['Cars_Description'])
        img_path_var = StringVar(value=record['Cars_Image'])


        Label(upd_win, text="Car Name : ", font=("Helvetica", 12)).place(x=45 ,y=170)
        Entry(upd_win, textvariable=name_var, width=35).place(x=130 ,y=173)

        Label(upd_win, text="Car Type : ", font=("Helvetica", 12)).place(x=45 ,y=220)  
        Entry(upd_win, textvariable=type_var, width=35).place(x=130 ,y=223)

        Label(upd_win, text="Car Price : ", font=("Helvetica", 12)).place(x=45 ,y=120)   
        Entry(upd_win, textvariable=price_var, width=35).place(x=130 ,y=122)

        Label(upd_win, text="Status : ", font=("Helvetica", 12)).place(x=375 ,y=220)   
        Entry(upd_win, textvariable=status_var, width=35).place(x=450 ,y=223)

        Label(upd_win, text="Car Year : ", font=("Helvetica", 12)).place(x=375 ,y=120) # x of car price, y of car vin   
        Entry(upd_win, textvariable=year_var, width=35).place(x=450 ,y=122)

        Label(upd_win, text="Car Description : ", font=("Helvetica", 12)).place(x=45 ,y=315) # x of car price, y of car vin   
        Entry(upd_win, textvariable=desc_var, width=80).place(x=175 ,y=317)

        image_label = Label(upd_win, text=f"Image : {img_path_var.get()}", font=("Helvetica", 12))
        image_label.place(x=46, y=270)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    except mysql.connector.Error as err:
        print(f"DB Error.{err}")
        messagebox.showerror("Database Error", f"Error: {err}", parent=upd_win)
        db_conn.rollback()

    def update_files():
    # Try to get files from the PC to our app and store file paths in the DB
    # what about this? file paths.!!! today brain is not braingin
        file_path = filedialog.askopenfilename(parent=upd_win, title="Select an Image", 
        filetypes=[("Image Files", "*.jpg;*.JPG;*.jpeg;*.JPEG;*.png;*.PNG;*.gif;*.GIF;*.jfif;*.JFIF;*.webp;*.WEBP;"), ("All files", "*.*")])

        # print(file_path)
        if file_path:
            
            # Update the Label to show the file path
            img_path_var.set(file_path)
            image_label.config(text=f"Image : {file_path}")
    
    
    add_font = tkFont.Font(family="Ariel",size=11, weight="bold")
    Button(upd_win, text="Add Photos", compound=CENTER, border=5, font=add_font, bg='white', fg='black', command=update_files, width=10, height=2).place(x=180, y=420)

    def update():
        # vin = search_vin_var.get().strip()
        name = name_var.get().strip()
        type1 = type_var.get().strip()
        price = price_var.get().strip()
        status = status_var.get().strip()
        year = year_var.get().strip()
        img4 = img_path_var.get().strip()
        desc = desc_var.get().strip()

        # if not vin:
        #     messagebox.showwarning("Input Error", "Car VIN is required.", parent=upd_win)
        #     return
        
        if not name:
            messagebox.showwarning("Input Error", "Car Name is required.", parent=upd_win)
            return
        
        if not type1:
            messagebox.showwarning("Input Error", "Car Type is required.", parent=upd_win)
            return
        
        if not price.isdigit():
            messagebox.showwarning("Input Error", "Please enter a specific amount.", parent=upd_win)
            return

        if not status:
            messagebox.showwarning("Input Error", "Status can't be Empty.", parent=upd_win)
            return

        if not (year.isdigit() and len(year) == 4):
            messagebox.showwarning("Input Error", "Enter year in a YYYY format.", parent=upd_win)
            return
        
        if not img4:
            messagebox.showwarning("Input Error", "Please Select Correct image type.", parent=upd_win)
            return
        
        if not desc:
            messagebox.showwarning("Input Error", "Description too Long", parent=upd_win)
            return

        try:
            cursor = db_conn.cursor()
            update_query = """
            UPDATE cars_showroom.cars 
            SET Cars_Name = %s, Cars_Type = %s, Cars_Price = %s, Cars_Status = %s, Cars_Year = %s, Cars_Image = %s, Cars_Description = %s
            WHERE Cars_VIN = %s"""
            cursor.execute(update_query, (name_var.get(), type_var.get(), price_var.get(), status_var.get(), year_var.get(), img_path_var.get(), desc_var.get(), vin))
            db_conn.commit()
            messagebox.showinfo("Success", f"record at VIN = {vin}, has been updated successfully.", parent=upd_win)
            upd_win.destroy()
            cursor.close()

            refresh_inventory_display() # Refresh display after deletion
            display_cars_from_db()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        except mysql.connector.Error as err:
            print(f"DB Error.{err}")
            messagebox.showerror("Database Error", f"Error: {err}", parent=upd_win)
            db_conn.rollback()

    Button(upd_win, text="UPDATE", command=update, border=8, width=20, height=2, bg="Orange", fg="black").place(x=360,y=420)

################################################################################################################################################################################################################
################################################################################################################################################################################################################

def search_all():
    if not db_conn or not db_conn.is_connected():
        messagebox.showerror("Connection Error", "Not connected to the database.")
        return

    srch_win = tk.Toplevel(root)
    srch_win.title("Search Inventory")
    srch_win.geometry("720x396")
    srch_win.attributes('-top', True) ##################################### <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    Label(srch_win, text="Enter VIN to Search : ", font=("Helvetica", 12)).place(x=80, y=45)
    search_vin_var = StringVar()
    Entry(srch_win, textvariable=search_vin_var, width=35).place(x=250, y=47)

    def search():
        vin = search_vin_var.get().strip()
            
        if not vin:
            messagebox.showwarning("Input Error", "Car VIN is required to search.",parent=srch_win)
            return
        try:
            cursor = db_conn.cursor()
            select_query = "SELECT * FROM cars_showroom.cars WHERE Cars_VIN = %s"
            cursor.execute(select_query, (vin,))
            record = cursor.fetchone()
            cursor.close()


            # name_label = tk.Label(root, text=f"Car Name: {name}")
            # name_label.pack()

            # type_label = tk.Label(root, text=f"Car Type: {car_type}")
            # type_label.pack()

            # price_label = tk.Label(root, text=f"Car Price: {price}")
            # price_label.pack()





            if record:
                name_var.set(record[1])
                type_var.set(record[2])
                price_var.set(record[3])
                status_var.set(record[4])
                year_var.set(record[5])
                
            else:
                messagebox.showinfo("Not Found", "No car found with the provided VIN.", parent=srch_win)
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")

    Button(srch_win, text="SEARCH", command=search, width=15, border=4).place(x=490, y=43)

    Label(srch_win, text="Car Name : ", font=("Helvetica", 12)).place(x=45 ,y=170)
    name_var = StringVar()
    name_label = tk.Label(srch_win, font=("Helvetica", 10), textvariable=name_var).place(x=130, y=173)
    #Entry(upd_win, textvariable=name_var, width=30).place(x=130 ,y=173)

    Label(srch_win, text="Car Type : ", font=("Helvetica", 12)).place(x=45 ,y=220)
    type_var = StringVar()
    type_label = tk.Label(srch_win, font=("Helvetica", 10), textvariable=type_var).place(x=120, y=223)
    #Entry(upd_win, textvariable=type_var, width=30).place(x=130 ,y=223)

    

    Label(srch_win, text="Car Price : ", font=("Helvetica", 12)).place(x=45 ,y=120)
    price_var = StringVar()
    price_label = tk.Label(srch_win, font=("Helvetica", 10), textvariable=price_var).place(x=125, y=123) 
    #Entry(upd_win, textvariable=price_var, width=30).place(x=130 ,y=122)

    Label(srch_win, text="Status : ", font=("Helvetica", 12)).place(x=375 ,y=220)
    status_var = StringVar()
    status_label = tk.Label(srch_win, font=("Helvetica", 10), textvariable=status_var).place(x=430, y=223)
    #Entry(upd_win, textvariable=status_var, width=30).place(x=450 ,y=223)

    
    Label(srch_win, text="Car Year : ", font=("Helvetica", 12)).place(x=375 ,y=170)
    year_var = StringVar()
    year_label = tk.Label(srch_win, font=("Helvetica", 10), textvariable=year_var).place(x=450, y=173)
    #Entry(upd_win, textvariable=year_var, width=30).place(x=453 ,y=173)

    def update():
        vin = search_vin_var.get().strip()
        name = name_var.get().strip()
        type1 = type_var.get().strip()
        price = price_var.get().strip()
        status = status_var.get().strip()
        year = year_var.get().strip()

        if not vin:
            messagebox.showwarning("Input Error", "Car VIN is required.", parent=srch_win)
            return
        
        if not name:
            messagebox.showwarning("Input Error", "Car Name is required.", parent=srch_win)
            return
        
        if not type1:
            messagebox.showwarning("Input Error", "Car Type is required.", parent=srch_win)
            return
        
        if not price.isdigit():
            messagebox.showwarning("Input Error", "Please enter a specific amount.", parent=srch_win)
            return

        if not status:
            messagebox.showwarning("Input Error", "Status can't be Empty.", parent=srch_win)
            return

        if not (year.isdigit() and len(year) == 4):
            messagebox.showwarning("Input Error", "Enter year in a YYYY format.", parent=srch_win)
            return

        try:
            cursor = db_conn.cursor()
            update_query = """
            UPDATE cars_showroom.cars 
            SET Cars_Name = %s, Cars_Type = %s, Cars_Price = %s, Cars_Status = %s, Cars_Year = %s 
            WHERE Cars_VIN = %s"""
            cursor.execute(update_query, (name, type1, price, status, year, vin))
            db_conn.commit()
            messagebox.showinfo("Success", "Item updated successfully.",parent=srch_win)
            srch_win.destroy()
            cursor.close()
        except mysql.connector.Error as err:
            print(f"DB Error.{err}")
            messagebox.showerror("Database Error", f"Error: {err}")
            db_conn.rollback()

    # Button(upd_win, text="UPDATE", command=update, border=8, width=20, height=2, bg="Orange", fg="black").place(x=300,y=300)

################################################################################################################################################################################################################
################################################################################################################################################################################################################


def add_btn():
    if not db_conn or not db_conn.is_connected():
        messagebox.showerror("Connection Error. ", "Not connected to the database.")
        return

    add_win = tk.Toplevel(root)
    add_win.title("Add new Inventory")
    add_win.geometry("720x505")
    add_win.attributes('-top', True)
    

    top_font = tkFont.Font(family="Helvetica", size=42)  # Adjust font as needed
    top_label = tk.Label(add_win, text="Add New Cars", font=top_font)
    top_label.place(x=195, y=25)

      

    Label(add_win, text="Car VIN : ", font=("Helvetica", 12)).place(x=375 ,y=170)
    vin_var = StringVar()
    Entry(add_win, textvariable=vin_var, width=35).place(x=453 ,y=173)

    Label(add_win, text="Car Name : ", font=("Helvetica", 12)).place(x=45 ,y=170)
    name_var = StringVar() 
    Entry(add_win, textvariable=name_var, width=35).place(x=130 ,y=173)

    Label(add_win, text="Car Type : ", font=("Helvetica", 12)).place(x=45 ,y=220)
    type_var = StringVar()
    Entry(add_win, textvariable=type_var, width=35).place(x=130 ,y=223)

    Label(add_win, text="Car Price : ", font=("Helvetica", 12)).place(x=45 ,y=120)
    price_var = StringVar()
    Entry(add_win, textvariable=price_var, width=35).place(x=130 ,y=122)

    Label(add_win, text="Status : ", font=("Helvetica", 12)).place(x=375 ,y=220)
    status_var = StringVar()
    Entry(add_win, textvariable=status_var, width=35).place(x=450 ,y=223)

    Label(add_win, text="Car Year : ", font=("Helvetica", 12)).place(x=375 ,y=120) # x of car price, y of car vin
    year_var = StringVar()
    Entry(add_win, textvariable=year_var, width=35).place(x=450 ,y=122)

    Label(add_win, text="Car Description : ", font=("Helvetica", 12)).place(x=45 ,y=315) # x of car price, y of car vin
    desc_var = StringVar()
    Entry(add_win, textvariable=desc_var, width=80).place(x=175 ,y=317)

    img_path_var = StringVar()

    def add_files():
    # Try to get files from the PC to our app and store file paths in the DB
    # what about this? file paths.!!! today brain is not braingin
        file_path = filedialog.askopenfilename(parent=add_win, title="Select an Image", 
        filetypes=[("Image Files", "*.jpg;*.JPG;*.jpeg;*.JPEG;*.png;*.PNG;*.gif;*.GIF;*.jfif;*.JFIF;"), ("All files", "*.*")])

        # print(file_path)
        if file_path:
            
            # Update the Label to show the file path
            img_path_var.set(file_path)
            image_label.config(text=f"Image : {file_path}")
            

    # Create a Label to display the image path
    image_label = Label(add_win, text="Image : ", font=("Helvetica", 12))
    img_path_var = StringVar()
    image_label.place(x=46, y=270)


    add_font = tkFont.Font(family="Ariel",size=11, weight="bold")
    Button(add_win, text="Add Photos", compound=CENTER, border=5, font=add_font, bg='white', fg='black', command=add_files, width=10, height=2).place(x=180, y=420)

    def insert():
        vin = vin_var.get().strip()
        name = name_var.get().strip()
        type1 = type_var.get().strip()
        price = price_var.get().strip()
        status = status_var.get().strip()
        year = year_var.get().strip()
        img4 = img_path_var.get().strip()
        desc = desc_var.get().strip()

        # if not vin:
        #     messagebox.showwarning("Input Error", "Car VIN is required.", parent=add_win)          
        #     return

        if not name:
            messagebox.showwarning("Input Error", "Car Name is required.", parent=add_win)
            return

        if not type1:
            messagebox.showwarning("Input Error", "Car Type is required.", parent=add_win)
            return

        if not price.isdigit():
            messagebox.showwarning("Input Error", "Please enter a specific amount.", parent=add_win)
            return
        
        if not status:
            messagebox.showwarning("Input Error","Enter SOLD or ON SALE", parent=add_win)
            return
        
        if not year:
            messagebox.showwarning("Input Error","Please enter year in YYYY format.", parent=add_win)
            return
        
        if not img4:
            messagebox.showwarning("Input Error","Image error.", parent=add_win)
            return
        
        if not desc:
            messagebox.showwarning("Input Error", "Please enter description.", parent=add_win)
            return

        try:
            cursor = db_conn.cursor()
            update_query = """
            INSERT INTO cars_showroom.cars(Cars_Name, Cars_Type, Cars_Price, Cars_Status, Cars_Year, Cars_Image, Cars_Description)
            VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(update_query, (name, type1, price, status, year, img4, desc)) ######################################################################## ADD DESCRIPTION TOO #############################################################
            messagebox.showinfo("Success", "Item added to Inventory successfully.", parent=add_win)
            db_conn.commit()
            add_win.destroy()
            cursor.close()
            
            refresh_inventory_display() # Refresh display after deletion
            display_cars_from_db()

        except mysql.connector.Error as err:
            print(f"DB Error.{err}")
            messagebox.showerror("Database Error", f"Error: {err}", parent=add_win)
            db_conn.rollback()
        
    Button(add_win, text="CONFIRM", command=insert, border=8, width=20, height=2, bg="green", fg="white").place(x=360,y=420)


display_cars_from_db()
add_inv()
search()
root.mainloop()

# finally everything is done just make the delte and update to autofetch and update the field in it.
# and delete for delete in front of record == done || update for update in front of record (DONE..!!!)
# then we move to user gui.
