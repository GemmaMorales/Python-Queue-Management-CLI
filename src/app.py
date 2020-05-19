import json
from DataStructures import Queue
from sms import send

# there queue has to be declared globally (outside any other function)
# that way all methods have access to it
queue = Queue(mode="FIFO")
    
def print_queue():
    # you must print on the console the entire queue list
    print("Printing the entire list...")
    print(queue.get_queue())

def add(name, phone_number):
    queue.enqueue({"name":name, "phone":phone_number})
    send("Your name has been added to the queue.", phone_number)
    return queue    

def dequeue():
    customer_number = queue.get_queue()
    send("Your table is ready.", customer_number[0]["phone"])
    queue.dequeue()
    return queue
    
def save():
    with open('data.json', 'w') as json_file:
        json.dump(queue.get_queue(), json_file)
        json_file.close()
    pass

def load():
    with open('data.json', 'r') as json_file:
        print(json_file)
    pass 
        
    
print("\nHello, this is the Command Line Interface for a Queue Managment application.")
stop = False
while stop == False:
    
    print('''
What would you like to do (type a number and press Enter)?
- Type 1: For adding someone to the Queue.
- Type 2: For removing someone from the Queue.
- Type 3: For printing the current Queue state.
- Type 4: To export the queue to the queue.json file.
- Type 5: To import the queue from the queue.json file.
- Type 6: To quit
    ''')

    option = int(input("Enter a number:"))
    # add your options here using conditionals (if)
    if option == 3:
        print_queue()
    elif option == 6:
        print("Bye bye!")
        stop = True
    elif option == 1:
        name = input("Enter the name you want to add to the list:")
        phone_number = input("Enter the phone number where you can be contacted")
        add(name, phone_number)
    elif option == 2:
        dequeue()
    elif option == 4:
        save()
    elif option == 5:
        load()
    else:
        print("Invalid option "+str(option))
