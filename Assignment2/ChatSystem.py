class Message:
    message_counter = 0   ## Class variable to keep track of total messages

    # Constructor: runs when a new Message object is created
    def __init__(self, sender, content):
        Message.message_counter += 1        # increase counter
        self.id = Message.message_counter   # assign unique id
        self.sender = sender                # who sends message
        self.content = content              # message text
        
    def __str__(self):       # Defines how the object prints
        return f"({self.id}) {self.sender.username}: {self.content}"


# User class represents a chat user
class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None         # user is not in any chatroom initially
    
    
    # Join a chatroom
    def join_chatroom(self, chatroom):
        if self.chatroom:
            print(f"{self.username} is already in a chatroom.")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.username} joined {chatroom.name}")
    
    #leave a chatroom
    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.username} is not in any chatroom.")
        else:
            room_name = self.chatroom.name
            self.chatroom.remove_user(self)
            self.chatroom = None
            print(f"{self.username} left {room_name}")
    
    # Send a message to chatroom
    def send_message(self, content):
        if not self.chatroom:
            print(f"{self.username} cannot send a message (not in chatroom).")
        else:
            self.chatroom.broadcast(self, content)

# ChatRoom class manages users and messages
class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []     # list of users
        self.messages = []  # list of messages
    
    # Add user to room
    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
    
    #remove user from room
    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
    
    # Send message to everyone
    def broadcast(self, sender, content):
        new_msg = Message(sender, content)
        self.messages.append(new_msg)
        print(new_msg)
    
    # Display all past messages
    def show_chat_history(self):
        print(f"\n--- Chat History of {self.name} ---")
        for msg in self.messages:
            print(msg)
        print("------------------------------\n")

# Main program starts here
if __name__ == "__main__":
    room = ChatRoom("Python Language")
    
    u1 = User("Sayan")
    u2 = User("Samata")
    u3 = User("Srinika")
     
    u1.join_chatroom(room)
    u2.join_chatroom(room)
    
    u1.send_message("Hello Everyone!")
    u2.send_message("Hey Guys, What's Up?")
    
    room.show_chat_history()
    
    u1.leave_chatroom()
    u2.leave_chatroom()
    u3.leave_chatroom() 