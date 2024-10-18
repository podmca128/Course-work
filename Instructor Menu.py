def instructorMenu():
        root.destroy() #Destroys Main Menu
        def destroy(): #destroys Instructor Menu + opens Main Menu
            top.destroy()
            openMenu()

        def edit(): #edits records in the database
                def EditInstructor():
                        connection = sqlite3.connect("instructor.db")
                        cursor = connection.cursor()

                        #getting field, value and search entry fields and assigning them to new variables
                        field_edit = field.get()
                        value_edit = value.get()
                        search_edit = value.get()

                        if search_edit != "": #checks if all fields are filled
                            #assigns the id fieldof the selected record to a variable
                            instructorIDD = getID(search_edit)

                            #validation check for new values entered
                            validation = True
                            #presence checks
                            presenceCheck(field_edit)
                            presenceCheck(value_edit)
                            presenceCheck(search_edit)

                            if field_edit != "instructorDOB":
                                #updates database
                                cursor.execute(f"UPDATE tblinstructors SET {field_edit} = '{value_edit}' WHERE instructorID = {instructorIDD}")
                                messagebox.showinfo(title = "Edit Instructor", message = "You have changed instructor details")
                                connection.commit()
                                connection.close()
                                #close edit window
                                rootEdit.destroy()
                                #update form in staff menu
                                DisplayForm()

                            else:
                                #format check for the DOB
                                ValidDOB = re.match("[0-9]{2}[/]{1}[0-9]{2}[/]{1}[0-9]{4}", value_edit)
                                if(not ValidDOB):
                                    validation=False
                                    messagebox.showinfo(title = "Error",
                                    message = "Error - Enter data in form XX/XX/XXXX")
                                    #place the edit window as top
                                    rootEdit.lift()

                                else:
                                    #update database if DOB format check s passed
                                    cursor.execute(f"UPDATE tblinstructors SET {field_edit} = '{value_edit}' WHERE instructorID = {instructorIDD}")
                                    messagebox.showinfo(title = "Edit Instructor", message = "You have successfully changed the instructor details")
                                    connection.commit()
                                    connection.close()
                                    #close edit window
                                    rootEdit.destroy()
                                    #update form in instructor menu
                                    DisplayForm()

                        else:
                            #runs if presence check isnt passed
                            messagebox.showinfo(title = "Error",
                            message = "Error - All fields not filled")
                            #place edit window as top
                            rootEdit.lift()

                #edit window
                global value, field, search

                rootEdit = Tk()
                rootEdit.geometry("306x195")
                rootEdit.title("Edit Instructor")
                rootEdit.resizable (False,False)
                rootEdit.configure(bg = "green")

                #create header
                frameEdit = Frame(rootEdit, bg="light blue")
                frameEdit.grid(row=1, column=1, columnspan=3, padx=10, pady=10)
                Label(frameEdit, text = "Instructor Edit", font=("aptos, 16"), width=20, bg="white").grid(row=1, column=1, columnspan=2, padx=10, pady=10)

                connection = sqlite3.connect("instructor.db")
                cursor = connection.cursor()

                #search of instructor database to get details for drop menu
                instructor = []
                for row in cursor.execute("SELECT instructorFirstname, instructorSurname, instructorID FROM tblinstructors"):
                        instructor.append(row)
                #creating dropdown menu
                search = ttk.Combobox(rootEdit, values = instructor)
                search.place(x = 153, y = 70)
                Label(rootEdit, text = "Instructor name", width = 19, bg = "white").place(x=10, y=70)

                field = ttk.Combobox(rootEdit, text="a")
                field.place(x=153, y=100)
                field.config(values=("instructorID", "instructorFirstname", "instructorSurname instructorUsername instructorPassword instructorLevel instructorMobileNum instructorDOBinstructorPostcode  instructorEmail instructorBlurb"))
