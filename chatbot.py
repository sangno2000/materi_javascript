import openai
import os
import telegram

openai.api_key = "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"
bot = telegram.Bot(token= "5802299351:AAGFrt54fuG82YyR6rS-oVTT378eb63iVbk")

def handle_messege(message):
	response = openai.Completion.create(
		engine="text-davinci-002",
		prompt=message.text,
		max_tokens=1024,
		temperature=0.5,
	).choices[0].text

	bot.send_massage(chat_id=message.chat.id, text=response)

updater = telegram.ext.Updater(bot=bot)
updater.dispatcher.add_handler(telegram.ext.MessageHandler(filters=telegram.ext.filters.text, callback=handle_message))
	updater.start_polling()	

