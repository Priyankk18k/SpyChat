from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class Chatmessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now().strftime("%b %d %Y %H:%M:%S")
        self.sent_by_me = sent_by_me

spy = Spy('Priyank', 'Mr', 20, 4.5)    # Spy object
# Friends
friend_one = Spy('Chinmay', 'Mr.', 20, 4.5)
friend_two = Spy('Riya', 'Ms.', 21, 3.5)
friend_three = Spy('Shivam', 'Mr', 22, 4.0)


friends = [friend_one, friend_two, friend_three]

