from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import ttk
from tkinter import scrolledtext
import re
import tkinter as tk


#this connects to the database
#of the database doesnt exist it will create it
connection = sqlite3.connect("instructor.db")
cursor = connection.cursor()

#creates an owner table
SQL = """CREATE TABLE IF NOT EXISTS tblowner
        (
        ownerID INTEGER NOT NULL,
        ownerFirstname TEXT,
        ownerSurname TEXT,
        ownerUsername TEXT,
        ownerPassword TEXT,
        ownerLevel TEXT,
        ownerMobileNum TEXT,
        ownerDOB DATE,
        ownerPostcode TEXT,
        ownerEmail TEXT,
        ownerBlurb TEXT,
        primary key (ownerID)
        )
        """

#executes the command and creates owner table
cursor.execute(SQL)

#creates a instructor table
SQL = """CREATE TABLE IF NOT EXISTS tblinstructors
        (
        instructorID INTEGER NOT NULL,
        instructorFirstname TEXT,
        instructorSurname TEXT,
        instructorUsername TEXT,
        instructorPassword TEXT,
        instructorLevel TEXT,
        instructorMobileNum TEXT,
        instructorDOB DATE,
        instructorPostcode TEXT,
        instructorEmail TEXT,
        instructorBlurb TEXT,
        primary key (instructorID)
        )
        """

#executes the command and creates instructor table
cursor.execute(SQL)

#creates a customer table
SQL = """CREATE TABLE IF NOT EXISTS tblcustomer    
        (
        customerID INTEGER NOT NULL,
        customerFirstname TEXT
        customerSurname TEXT,
        customerMobileNum TEXT,
        customerDOB DATE,
        customerPostcode TEXT,
        customerEmail TEXT,
        customerLevel TEXT,
        primary key (customerID)
        )
        """

#executes the command and creates customer table
cursor.execute(SQL)

#creates a session table
SQL = """CREATE TABLE IF NOT EXISTS tblsession  
        (
        sessionID INTEGER NOT NULL,
        sessionName TEXT
        sessionDate DATE,
        sessionDuration TEXT,
        sessionTimeStart TEXT,
        sessionTimeEnd TEXT,
        sessionInstructor TEXT,
        sessionSize INTEGER,
        sessionMaxSize INTEGER,
        sessionCost REAL,
        sessionLevel INTEGER
        primary key (sessionID)
        )
        """

#executes the command and creates session table
cursor.execute(SQL)

#creates a rental table
SQL = """CREATE TABLE IF NOT EXISTS tblrental  
        (
        rentalID INTEGER NOT NULL,
        rentalEquipmentName TEXT
        rentalDate DATE,
        rentalTime TEXT,
        rentalCustomerName TEXT,
        rentalReturn TEXT,
        rentalQty INTEGER,
        rentalCost REAL,
        primary key (rentalID)
        )
        """

#executes the command and creates a rental table
cursor.execute(SQL)

#creates a storage table
SQL = """CREATE TABLE IF NOT EXISTS tblstorage  
        (
        storageID INTEGER NOT NULL,
        storageEquipmentName TEXT,
        storageDate DATE,
        storageSpace TEXT,
        storageCustomerName TEXT,
        storageReturn TEXT,
        storageItemQty INTEGER,
        storageCost REAL,
        primary key (storageID)
        )
        """

#executes the command and creates a storage table
cursor.execute(SQL)

#saves changes made to the database and closes the connection
connection.commit()
connection.close()



#function that will perform a presence check to ensure all data is entered
def presenceCheck(rec):
    presence = True
    for x in range(len(rec)):
        if rec[x] == "":
            presence = False
    return presence

#check entry fields to ensure that all characters entered are letters
def checkVal(text):
    valid = True
    for x in range(len(text)):
        if ord(text[x]) not in range (65,91):
            if ord(text[x]) not in range(97,123):
                valid = False
        return valid

#returns the 3rd field in a record
def getID3(ID):
    field = ID.split()
    return(field[2])

#returns 2nd field in a record
def getID2(ID):
    field = ID.split()
    return(field[1])

#returns 1st field in a record
def getID1(ID):
    field = ID.split()
    return(field[0])

def openMenu():
    global ans
    if ans == 1:
        mainMenu1()
    if ans == 2:
        mainMenu2()

