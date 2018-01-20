from spy_details import spy_rating,spy_age,spy_name,spy_salutation,spy_is_online
print "Hello!"

print 'Let\'s get started'

print"Welcome to SpyChat"
question="Do you want to continue as " + spy_salutation + " " + spy_name + " (Y/N)? "
existing=raw_input(question)
def start_chat(spy_name,spy_age, spy_rating):

    if spy_age > 12 and spy_age < 50:
     print "Authentication complete. Welcome %s  age:%d    and rating of: %.2f   Proud to have you onboard" % (spy_name, spy_age, spy_rating)
    # Showing  whether the authentication is complete or not.

     menu_choice = "What do you want to do ?\n 1-ADD a Status Update\n 2-QUIT"
     menu_choice = input(menu_choice)
     if menu_choice == 1:
         print("Status is updated")
     else:
         pass



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
    spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy_name) > 0:
        spy_salutation = raw_input("Should I call you Mr. or Ms.?: ")

        spy_age = input("What is your age?")

        spy_rating = input("What is your spy rating?")

        spy_is_online = True
        start_chat(spy_name, spy_age, spy_rating)

    else:
        print 'Please add a valid spy name'