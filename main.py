from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chat = ChatBot('cctmx')
trainer = ListTrainer(chat)

data = open("data.txt","r")

trainer.train(data.readlines())

while True:
	user = input(">>")
	response = chat.get_response(user)
	print ("bot: "+str(response))
