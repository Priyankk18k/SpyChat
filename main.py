from spy_details import spy_rating,spy_age,spy_name,spy_salutation,spy_is_online
STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']
# Default status message which will show to the user.
friends_name = []
friends_age = []
friends_rating = []
friends_is_online = []
# Default empty entry of friend details
print 'Hello,Let\'s get started'

print"Welcome to SpyChat"
question="Do you want to continue as " + spy_salutation + " " + spy_name + " (Y/N)? "
existing=raw_input(question)
def add_status(current_status_message):
    updated_status_message = None
    if current_status_message != None:
        print 'Your current status message is %s \n' % (current_status_message)
        # Printing of the latest message.
    else:
        print 'You don\'t have any status message currently \n'
    default = raw_input("Do you want to select from the older status (y/n)? ")
    if default.upper() == "N":
        #.upper is used to convert the input to uppercase
        new_status_message = raw_input("What status message do you want to set? ")
        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            #Used to enter the the new message tot the last of the available list.
            updated_status_message = new_status_message
    elif default.upper() == 'Y':
        item_position = 1
        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1
        message_selection = int(raw_input("\nChoose from the above messages "))
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]
            # -1 is used because list starts from 0 if user enter 2 then it will be 1 for us.
    else:
        print 'The option you chose is not valid! Press either y or n.'
    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You did not update your status message'

    return updated_status_message
def add_friend():
    #function to add a new friend.

    new_name = raw_input("Please add your friend's name: ")
    new_salutation = raw_input("Are they Mr. or Ms.?: ")

    new_name = new_name + " " + new_salutation

    new_age = input("Age?")

    new_rating = input("Spy rating?")
    if len(new_name) > 0 and new_age > 12 and new_rating >= spy_rating:
        friends_name.append(new_name)
        friends_age.append(new_age)
        friends_rating.append(new_rating)
        friends_is_online.append(True)
        # Assigning the values of the new friend to the empt friends details.
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends_name)

def start_chat(spy_name,spy_age, spy_rating):
    current_status_message = None
    spy_name = spy_salutation + " " + spy_name
    if spy_age > 12 and spy_age < 50:
     print "Authentication complete. Welcome %s  age:%d    and rating of: %.2f   Proud to have you onboard" % (spy_name, spy_age, spy_rating)
    # Showing  whether the authentication is complete or not.
     show_menu = True
     while show_menu:

        menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
        menu_choice = input(menu_choices)

        if menu_choice == 1:
            current_status_message = add_status(current_status_message)
        elif menu_choice == 2:
            number_of_friends = add_friend()
            print 'You have %d friends' % (number_of_friends)
        else:
            show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a spy'

if existing == "Y":
    start_chat(spy_name,spy_age, spy_rating)
else:
    spy_name = ''
    spy_salutation = ''
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False

    spy_name = input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy_name) > 0:
        spy_salutation = input("Should I call you Mr. or Ms.?: ")

        spy_age = input("What is your age?")


        spy_rating = input("What is your spy rating?")


        spy_is_online = True

        start_chat(spy_name, spy_age, spy_rating)
    else:
        print 'Please add a valid spy name'



