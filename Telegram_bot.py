

import telebot

bot = telebot.TeleBot("1253507210:AAFN8nyYPEKZhhU4JjTfFgID8cnVWAvr5rU")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	bot.reply_to(message, message.text)

bot.polling( none_stop = True )