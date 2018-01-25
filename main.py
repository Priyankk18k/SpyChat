from spy_details import spy
STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']
# Default status message which will show to the user.
friends= []
# Default empty entry of friend details
print 'Hello,Let\'s get started'

print"Welcome to SpyChat"
question="Do you want to continue as " + spy['salutation'] + " " + spy['name'] + " (Y/N)? "
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
# selection function
#By this function we select a friend from friend list for performing a various function on selecting friend
def select_friend():
    item_no=0
    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % ((item_no + 1),friend['name'])
        item_no = item_no + 1
        updated_item_no=item_no-1
        friend_choice = raw_input("Choose friend from list?")
        friend_choice_position = int(friend_choice) - 1
        return friend_choice_position
# This function add the new friend in the friend list
def add_friend():
    new_friend={
        'name':'',
        'age':'',
        'salutation':'',
        'rating': 0.0
    }
    new_friend['name'] = raw_input("Please add your friend's name: ")
    new_friend['salutation'] = raw_input("Are they Mr. or Ms.?: ")

    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']
    # Combining name and salutation and again storing it in a name variable.

    new_friend['age'] = input("Age?")
    new_friend['rating'] = input("Spy rating?")
    if len(new_friend['name']) > 0 and  new_friend['age'] > 12 and new_friend['rating'] >= spy['rating']:
        friends.append(new_friend)

        # Assigning the values of the new friend to the new friends function.
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)

def start_chat(spy):
    current_status_message = None
    spy['name'] = spy['salutation'] + " " + spy['name']
    if spy['age'] > 12 and spy['age']< 50:
     print "Authentication complete. Welcome %s  age:%d    and rating of: %.2f   Proud to have you onboard" % (spy['name'], spy['age'], spy['rating'])
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
    start_chat(spy)
else:
    spy = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'is_online': False
    }

    spy['name'] = input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy['name']) > 0:
        spy['salutation'] = input("Should I call you Mr. or Ms.?: ")

        spy['age'] = input("What is your age?")


        spy['rating'] = input("What is your spy rating?")


        spy['is_online'] = True

        start_chat(spy)
    else:
        print 'Please add a valid spy name'



