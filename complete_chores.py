#!/bin/python3

from room import HouseChores
import os
import sys
import getpass

def main():

    file = sys.argv[1]
    timetable = HouseChores(file)
    timetable.read_file()
    print("Writing to file...")
    new_timetable = input("Enter the name of the file to store the new timetable: ")
    timetable.write_to_file()
    print("Finishing up..")
    sender_email = input("Enter your gmail: ")
    password = getpass.getpass()
    timetable.notification(sender_email,password)
    print("Done")
    return

main()
