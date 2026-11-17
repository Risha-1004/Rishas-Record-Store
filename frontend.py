import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="recordstore"
)

while True:
    print("\n=============================================")
    print("    RISHA'S RECORD STORE     ")
    print("=============================================")
    print("1. Add New Record Stock")
    print("2. Edit Record Price/Title")
    print("3. Discontinue/Remove Album")
    print("4. Sales & Inventory Analytics")
    print("5. Generate Sales Charts")
    print("6. Exit Application")
    print("=============================================")
    
    choice = input("Select an option (1-6): ")
    
    if choice == '1':
        print("\n--- Add New Record ---")
        iid = int(input("Enter Record/Item ID: "))
        title = input("Enter Album Title: ")
        artist = input("Enter Artist Name: ")
        print("Genres: [Pop] [Electronic & Dance] [Alternative Rock] [Indie & Folk] [R&B & Soul] [Hip-Hop]")
        genre = input("Enter Genre from above: ")
        price = int(input("Enter Price (₹): "))
        
        cursor = conn.cursor()
        query = "INSERT INTO Vinyls (ItemID, Title, Artist, Genre, Price, CopiesSold) VALUES (%s, %s, %s, %s, %s, 0)"
        values = (iid, title, artist, genre, price)
        
        cursor.execute(query, values)
        conn.commit()
        print("Album stock successfully added!")
        cursor.close()
        
    elif choice == '2':
        print("\n--- Edit Record Details ---")
        iid = int(input("Enter the Item ID to edit: "))
        
        print("What details do you want to edit?")
        print("A. Update Price")
        print("B. Update Album Title")
        editchoice = input("Select choice (A/B): ").upper()
        
        cursor = conn.cursor()
        if editchoice == 'A':
            newprice = int(input("Enter new Price (₹): "))
            query = "UPDATE Vinyls SET Price = %s WHERE ItemID = %s"
            cursor.execute(query, (newprice, iid))
            conn.commit()
            print("Price updated successfully!")
            
        elif editchoice == 'B':
            newtitle = input("Enter new Album Title: ")
            query = "UPDATE Vinyls SET Title = %s WHERE ItemID = %s"
            cursor.execute(query, (newtitle, iid))
            conn.commit()
            print("Album title updated successfully!")
        else:
            print("Invalid Selection.")
        cursor.close()

    elif choice == '3':
        print("\n--- Discontinue Album From Stock ---")
        iid = int(input("Enter the Item ID to remove: "))
        
        cursor = conn.cursor()
        query = "DELETE FROM Vinyls WHERE ItemID = %s"
        cursor.execute(query, (iid,))
        conn.commit()
        
        print(f"Record ID {iid} successfully deleted from database inventory!")
        cursor.close()

    elif choice == '4':
        query = "SELECT * FROM Vinyls"
        dfstore = pd.read_sql(query, con=conn)
        
        print("\n=== Active Store Inventory (Pandas DataFrame) ===")
        print(dfstore.to_string(index=False)) 
        
        print("\n=== Business Analytics Summary ===")
        print(f"Total Unique Album Titles:  {dfstore['ItemID'].count()}")
        print(f"Average Album Price:        ₹{dfstore['Price'].mean():.2f}")
        print(f"Most Expensive Vinyl:       ₹{dfstore['Price'].max()}")
        print(f"Total Records Sold Globally: {dfstore['CopiesSold'].sum()} units")
        
        print("\n=== Total Sales Units by Music Genre ===") 
        print(dfstore.groupby('Genre')['CopiesSold'].sum())
        
    elif choice == '5':
        dfstore = pd.read_sql("SELECT * FROM Vinyls", con=conn)
        
        print("\n--- Store Visualizations ---")
        print("A. View Individual Album Sales Performance (Horizontal Bar Chart)")
        print("B. View Market Share by Genre (Pie Chart)")
        sub_choice = input("Select chart type (A/B): ").upper()
        
        if subchoice == 'A':
            plt.figure(figsize=(12, 7))
            plt.barh(dfstore['Title'], dfstore['CopiesSold'], color='darkmagenta', edgecolor='black')
            plt.title('Store Distribution: Top Selling Vinyl Records', fontsize=14, fontweight='bold')
            plt.xlabel('Number of Units Sold', fontsize=12)
            plt.ylabel('Album Titles', fontsize=12)
            plt.tight_layout()
            plt.show() 
            
        elif subchoice == 'B':
            genredata = dfstore.groupby('Genre')['CopiesSold'].sum()
            
            plt.figure(figsize=(8, 8))
            plt.pie(genre_data, labels=genre_data.index, autopct='%1.1f%%', 
                    colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#d5a6bd'], startangle=140, 
                    wedgeprops={'edgecolor': 'black', 'linewidth': 1})
            plt.title('Music Genre Revenue & Popularity Share', fontsize=14, fontweight='bold')
            plt.tight_layout()
            plt.show()
        else:
            print("Invalid visual selection.")
            
    elif choice == '6':
        print("\nExiting Store System.")
        conn.close()
        print("Thanks a lot for visiting!")
        break
        
    else:
        print("Invalid choice, please select 1-6.")
