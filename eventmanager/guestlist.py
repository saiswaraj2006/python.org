#because it is created for appending the guest into it
#it is global list used for all functions in this file
guest=[]
def add_guest(name):
    if name not in guest:
        guest.append(name)
def show_guest():
    return guest
#it returns all guests name who has invited
 