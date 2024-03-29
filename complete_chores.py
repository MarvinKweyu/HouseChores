#!/bin/python3

from room import HouseChores
import sys
import getopt
import getpass


def main():
    'Give options for command line arguments'

    try:
        (opts, args) = getopt.getopt(
            sys.argv[1:], 'hi:o:', ['help', 'input=', 'output='])

    except getopt.GetoptError as err:  # an option has been passed without a value
        print(err)
        sys.exit(2)

    # if options have been passed
    if len(opts) != 0:
        # loop over options:ex,[(i,HouseChores.xlsx),(o,Updated_timetable.xlsx)]
        for (option, item) in opts:
            if option in ('-h', '--help'):
                usage()
                sys.exit(2)
            elif option in ('-i', 'input'):
                input_file = item
            elif option in ('-o', 'output'):
                output_file = item
            else:
                usage()
                sys.exit(2)
    else:  # no options have been passed
        usage()
        sys.exit(2)
    accept_files(input_file, output_file)
    return


def accept_files(input_file, output_file):
    '''Accept command line argument files and create new timetable '''

    timetable = HouseChores(input_file, output_file)

    print("\nWriting to file...")
    new_table = timetable.create_table()
    print("\nFinishing up..")
    sender_email, password = prompt_notification()
    timetable.notification(sender_email, password, new_table)
    print("Done")

    return


def prompt_notification():
    """
    Show a prompt to the user to send the files via email
    """

    user_selection = input(
        "\n Do you want to send a notification to the subjects involved? (y/n)")

    if user_selection.strip() == 'y':
        sender_email = input("Enter your gmail: ")
        password = getpass.getpass()
        sender_email, password
    else:
        print("Goodbye!")
        sys.exit()


def usage():
    'Display program usage'

    print("\npython complete_chores.py -i <old_timetable> -o <new_timetable>")
    print("Where <new_timetable> is a name the user suggests")


if __name__ == '__main__':
    main()
