def mainMenu():
    global root
    root = Tk() #setting up window
    root.geometry("520x550")
    root.title("Main menu")
    root.resizable(False, False)
    root.configure(bg="green")

    frametitle = Frame(root, bg="light blue") #setting up frame
    frametitle.grid(row=1, column=0, columnspan=1, padx=180, pady=10)
    Label(frametitle, text="Main Menu", font=("Aptos", 16), bg="white").grid(row=1, column=1, columnspan=2, padx=20, pady=20)

    framebutton = Frame(root, bg="white")
    framebutton.grid(row=2, column=0, columnspan=1, padx=15, pady=15)

    #set up buttons for each menu
    custMenuButton = Button(framebutton, text="Customer Menu", bg="white", width=15, command=customerMenu)
    custMenuButton.grid(row=1, column=1, padx=20, pady=20)

    instructorMenuButton = Button(framebutton, text="Instructor Menu", bg="white", width=15, command=instructorMenu)
    instructorMenuButton.grid(row=2, column=1, padx=20, pady=20)

    ownerMenuButton = Button(framebutton, text="Owner Menu", bg="white", width=15, command=ownerMenu)
    ownerMenuButton.grid(row=3, column=1, padx=20, pady=20)

    sessionMenuButton = Button(framebutton, text="Session Menu", bg="White", width=15, command=sessionMenu)
    sessionMenuButton.grid(row=4, column=1, padx=20, pady=20)

    rentalMenuButton = Button(framebutton, text="Rental Menu", bg="white", width=15, command=rentalMenu)
    rentalMenuButton.grid(row=5, column=1, padx=20, pady=20)

    storageMenuButton = Button(framebutton, text="Storage Menu", bg="white", width=15, command=storageMenu)
    storageMenuButton.grid(row=6, column=1, padx=20, pady=20)

    payMenuButton = Button(framebutton, text="Payment Menu", bg="white", width=15, command=payMenu)
    payMenuButton.grid(row=7, column=1, padx=20, pady=20)

def mainMenu2():
    global root
    root = Tk() #setting up window
    root.geometry("520x550")
    root.title("Main Menu")
    root.resizable(False, False)
    root.configure(bg="green")

    frametitle = Frame(root, bg="light blue") #setting up frame
    frametitle.grid(row=1, column=0, columnspan=1, padx=180, pady=10)
    Label(frametitle, text="Main Menu", font=("Aptos", 16), bg="white").grid(row=1, column=1, columnspan=2, padx=20, pady=20)

    framebutton = Frame(root, bg="white")
    framebutton.grid(row=2, column=0, columnspan=1, padx=15, pady=15)

    #setting up buttons
    custMenuButton = Button(framebutton, text = "Customer Menu", bg="white", width = 15, command=customerMenu)
    custMenuButton.grid(row=1, column=1, padx=20, pady=20)

    sessionMenuButton = Button(framebutton, text="Session Menu", bg="White", width=15, command=sessionMenu)
    sessionMenuButton.grid(row=4, column=1, padx=20, pady=20)

    rentalMenuButton = Button(framebutton, text="Rental Menu", bg="white", width=15, command=rentalMenu)
    rentalMenuButton.grid(row=5, column=1, padx=20, pady=20)

    storageMenuButton = Button(framebutton, text="Storage Menu", bg="white", width=15, command=storageMenu)
    storageMenuButton.grid(row=6, column=1, padx=20, pady=20)
