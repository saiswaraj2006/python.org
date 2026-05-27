from eventmanager import invitation
print(invitation.create_invitation("Soumya", "Brother's Marriage"))
print(invitation.create_invitation("priya", "Brother's Marriage"))
from eventmanager import guestlist
guestlist.add_guest("soumya")
guestlist.add_guest("priya")
print("guestlist:",guestlist.show_guest())

'''import eventmanager.remainder as r
print(dir(r))
'''

from eventmanager import remainder
print(remainder.send_remainder("soumya", "Brother's Marriage"))
print(remainder.send_remainder("priya", "Brother's Marriage"))
#or directly in one method


from eventmanager import invitation, guestlist, remainder
guestlist.add_guest("soumya")
guestlist.add_guest("priya")

print(invitation.create_invitation("soumya", "Brother's Marriage"))
print(invitation.create_invitation("priya","Brother's Marriage"))
print(remainder.send_remainder("soumya", "Brother's Marriage"))
print(remainder.send_remainder("priya", "Brother's Marriage"))
print("guestlist:",guestlist.show_guest())





