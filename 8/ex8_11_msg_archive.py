def show_messages(msgs):
	for msg in msgs:
		print(msg)


def send_messages(msgs, sent):
	while msgs:
		msg = msgs.pop()
		print(msg)
		sent.append(msg)


msgs = ["I love Python!", 
		"I want to learn how to programme in Python!", 
		"I would like to read a book about Python."]

sent_messages = []

send_messages(msgs[:], sent_messages)
show_messages(msgs)
show_messages(sent_messages)