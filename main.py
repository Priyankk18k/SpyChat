from spy_details import spy,friends,Spy,Chatmessage
from steganography.steganography import Steganography
from datetime import datetime
import csv
from termcolor import colored

STATUS_MESSAGES = ["Available","busy","At Work"]
# Default status message which will show to the user.
# Default empty entry of friend details
print 'Hello,Let\'s get started'

print"Welcome to SpyChat"

question="Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
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

def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s aged %d with rating %.2f is online' % (item_number +1, friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1

    friend_choice = input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position

def send_message():

    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)

    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
    }

    friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready!"



def read_message():

    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
    }

    friends[sender].chats.append(new_chat)

    print "Your secret message has been saved!"

def read_chat_history():
   read_for = select_a_friend()
   if len(friends[read_for].chats) > 0:
       for chat in friends[read_for].chats:
           b=colored(chat.time.strftime('%A,%d %B %Y %H:%M:%S'),'blue')

           if chat.sent_by_me:
               print'[%s] %s: %s' % (b,'you said:',chat.message)
           else:
               print '[%s] %s read:%s'%(b,friends[read_for].name,chat.message)
   else:
        print " There is no chat history "

#Function to load the friends
def loadFriends():
    with open("friends.csv", "rb") as friends_list:   #open the csv file as friends_data in read mode
        reader = list(csv.reader(friends_list))        #convert each line into list


        for row in reader[1:]:
           print(row)
        friends.append(spy)

def loadMessage():
    with open("chats.csv", "rb") as chat_box:
        reader = list(csv.reader(chat_box))

        for row in reader[1:]:
            chatDetails = Chatmessage(row[1], row[2])
            spy.chats.append(chatDetails)
            print"Messages loaded successfully"


# This function add the new friend in the friend list
def add_friend():
    new_friend = Spy('', '', 0, 0)

    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name
    # Combining name and salutation and again storing it in a name variable.

    new_friend.age = input("Age?")
    new_friend.rating = input("Spy rating?")
    if len(new_friend.name) > 0 and  new_friend.age > 12 and new_friend.age <50 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        with open("friends.csv", "a") as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([new_friend.name, new_friend.salutation, new_friend.age, new_friend.rating, True])

        # Assigning the values of the new friend to the new friends function.
        print "%s %s is now your friend" % (new_friend.salutation, new_friend.name)
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)


def start_chat(spy):
    current_status_message = None
    loadFriends()
    loadMessage()


    spy.name = spy.salutation + " " + spy.name
    if spy.age > 12 and spy.age< 50:
     print "Authentication complete. Welcome %s  age:%d    and rating of: %.2f   Proud to have you onboard" % (spy.name, spy.age, spy.rating)
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
        elif menu_choice == 3:
            send_message()
        elif menu_choice == 4:
            read_message()
        elif menu_choice == 5:
            read_chat_history()
        else:
            show_menu=False
    else:
        print 'Sorry you are not of the correct age to be a spy'

if existing.upper() == "Y":
    start_chat(spy)
else:
    spy = Spy('', '', 0, 0.0,)

    spy.name = input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy.name) > 0:
        spy.salutation = input("Should I call you Mr. or Ms.?: ")

        spy.age = input("What is your age?")


        spy.rating = input("What is your spy rating?")




        start_chat(spy)
    else:
        print 'Please add a valid spy name'



