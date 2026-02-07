class Message:
    message_counter = 0 

    def __init__(self, sender, content):
        Message.message_counter += 1
        self.id = Message.message_counter
        self.sender = sender
        self.content = content
        
    def __str__(self):
        
        return f"({self.id}) {self.sender.username}: {self.content}"

class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None
    
    def join_chatroom(self, chatroom):
        if self.chatroom:
            print(f"{self.username} is already in a chatroom.")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.username} joined {chatroom.name}")
    
    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.username} is not in any chatroom.")
        else:
            room_name = self.chatroom.name
            self.chatroom.remove_user(self)
            self.chatroom = None
            print(f"{self.username} left {room_name}")
    
    def send_message(self, content):
        if not self.chatroom:
            print(f"{self.username} cannot send a message (not in chatroom).")
        else:
            self.chatroom.broadcast(self, content)

class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []
    
    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
    
    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
    
    def broadcast(self, sender, content):
        new_msg = Message(sender, content)
        self.messages.append(new_msg)
        print(new_msg)
    
    def show_chat_history(self):
        print(f"\n--- Chat History of {self.name} ---")
        for msg in self.messages:
            print(msg)
        print("------------------------------\n")

if __name__ == "__main__":
    room = ChatRoom("Python Language")
    
    u1 = User("Sayan")
    u2 = User("Samata")
    u3 = User("Charlie")
     
    u1.join_chatroom(room)
    u2.join_chatroom(room)
    
    u1.send_message("Hello Everyone!")
    u2.send_message("Hey Guys, What's Up?")
    
    room.show_chat_history()
    
    u1.leave_chatroom()
    u2.leave_chatroom()
    u3.leave_chatroom() 