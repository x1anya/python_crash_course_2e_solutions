guests = []
guests.append("Colleen Mccullough")
guests.append("Stephen King")
guests.append("J.K. Rowling")
print(f"Hey {guests[0]}, would you like to have dinner with me?")
print(f"Hey {guests[1]}, would you like to have dinner with me?")
print(f"Hey {guests[2]}, would you like to have dinner with me?")

print(f"Oops! {guests[2]} can not join our dinner!")
guests[2] = "Neil Gaiman"
print(f"Hey {guests[0]}, would you like to have dinner with me?")
print(f"Hey {guests[1]}, would you like to have dinner with me?")
print(f"Hey {guests[2]}, would you like to have dinner with me?")

print(f"Good news! I found a bigger table! Now we can invite more guests!")
guests.insert(0, "Dan Brown")
guests.insert(2, "Agatha Christie")
guests.insert(5, "Ken Follett")
print(f"Hey {guests[0]}, would you like to have dinner with me?")
print(f"Hey {guests[1]}, would you like to have dinner with me?")
print(f"Hey {guests[2]}, would you like to have dinner with me?")
print(f"Hey {guests[3]}, would you like to have dinner with me?")
print(f"Hey {guests[4]}, would you like to have dinner with me?")
print(f"Hey {guests[5]}, would you like to have dinner with me?")

print(f"Bad news! I can only invite two guests now!")
print(f"Dear {guests.pop()}, I am really sorry to inform you that I can not invite you for dinner because of unexpected situations. Sorry for the inconvenience.")
print(f"Dear {guests.pop()}, I am really sorry to inform you that I can not invite you for dinner because of unexpected situations. Sorry for the inconvenience.")
print(f"Dear {guests.pop()}, I am really sorry to inform you that I can not invite you for dinner because of unexpected situations. Sorry for the inconvenience.")
print(f"Dear {guests.pop()}, I am really sorry to inform you that I can not invite you for dinner because of unexpected situations. Sorry for the inconvenience.")
print(f"Hey {guests[0]}, I am glad to inform you that you are invited to our dinner. Hope you enjoy it!")
print(f"Hey {guests[1]}, I am glad to inform you that you are invited to our dinner. Hope you enjoy it!")
del guests[0]
del guests[0]
print(guests)