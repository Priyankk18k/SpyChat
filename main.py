print "Hello!"

print 'Let\'s get started'

spy_name = input("Welcome to spy chat, you must tell me your spy name first: ")

if len(spy_name) > 0:
    # To verify the length of the spy

    print 'Welcome ' + spy_name + '. Glad to have you back with us.'

    spy_salutation = raw_input("Should I call you Mister or Miss?: ")
    # Raw_input becasue to get the string value only

    spy_name = spy_salutation + " " + spy_name
    # Print spy salutation and spy name and store it in the spy_name

    print "Alright " + spy_name + ". I'd like to know a little bit more about you before we proceed..."

    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False
    # Initializing the values .

    spy_age = int(input("What is your age? Please give a valid number"))
    # Taking input from the user and converting the input to integer values

    while(spy_age):

        if spy_age > 12 and spy_age < 50:

            spy_rating = input("What is your spy rating? Please give a valid Rating number")

            if spy_rating > 4.5:
                print 'Great ace!'
            elif spy_rating > 3.5 and spy_rating <= 4.5:
                print 'You are one of the good ones.'
            elif spy_rating >= 2.5 and spy_rating <= 3.5:
                print 'You can always do better'
            else:
                print 'We can always use somebody to help in the office.'

            spy_is_online = True
            # Showing spy is online or not


            print "Authentication complete. Welcome %s  age:%d    and rating of: %f   Proud to have you onboard" % (spy_name,spy_age,spy_rating)
             # Showing  whether the authentication is complete or not.




    else:
        print 'Sorry you are not of the correct age to be a spy'


else:

    print "A spy needs to have a valid name. Try again please."