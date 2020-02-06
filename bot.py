from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
import telegram
import logging
import praw

telegram_token = "1090442251:AAFeDFouF4nXiZmOf5XgBoxjzNEJPKEbrLk" 
reddit_id = "rNo7QxlenjQfZQ"
reddit_secret = "zaJOgHEhKuD2bYqZd8Jtn0ZHW14"
gyfcat_id = "2_H4celp"
gyfcat_secret = "h4BmLazyRD3YAYm802nQcySg1QzM2Gg4sBXjLtaStAca4y6gz52GgmE7W8sdEAd1"

updater = Updater(token=telegram_token, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

reddit = praw.Reddit(client_id= reddit_id,
                     client_secret= reddit_secret,
                     user_agent='pra8eek')

def meme(update, context):
	try:
		k = int(context.args[-1])
		if k > 10 :
			context.bot.send_message(chat_id=update.effective_chat.id, text="Itna mat has bhosdike dast ho jayenge!")
			context.bot.send_message(chat_id=update.effective_chat.id, text="10 se zyada memes nahi ayenge -_-!")
			k = 10
	except :
		k = 1
	print(k)

	fetched = False
	kcopy = k

	try :
		subr = context.args[0]
		print(subr)
		if subr == "menu" :
			fetched = True
			context.bot.send_message(chat_id=update.effective_chat.id, text="Here are the categories: cricket | ouija | code | meirl | gay")
			context.bot.send_message(chat_id=update.effective_chat.id, text="Happy to add more. You already know the developer")
			return
		elif subr == "code" :
			subreddit = "ProgrammerHumor"
		elif subr == "ouija" :
			subreddit = "jesuschristouija"
		elif subr == "cricket" :
			subreddit = "cricketshitpost"	
		elif subr == "meirl" :
			subreddit = "me_irl"
		elif subr == "gay" :
			subreddit = "SuddenlyGay"
		else :
			subreddit = "2meirl4meirl"
	except :
		subreddit = "2meirl4meirl"

	if not fetched :
		print("subreddit is: ", subreddit)
		print("count is: ", k)

	time = "day"

	while not fetched :
		fetchCount = 0

		print("Searching")
		for submission in reddit.subreddit(subreddit).top(time_filter = time, limit = k) :
			if submission.url[-3:] == "jpg" :
				fetchCount += 1
	
		if fetchCount >=  kcopy:
			sent = 0 
			fetched = True
			print("Sending ")

			for submission in reddit.subreddit(subreddit).top(time_filter = "day", limit = k) :
				if submission.url[-3:] == "jpg" :
					sent += 1
					context.bot.send_photo(chat_id=update.effective_chat.id, photo=submission.url)
					print(submission.url)
					if sent == kcopy :
						break

			print("Sent")
		else :
			k = k*2
			if k > 100 :
				time = "all"
			if k > 200 :
				context.bot.send_message(chat_id=update.effective_chat.id, text="Something went wrong! Try with a lower count")


def boob(update, context):
	try:
		k = int(context.args[-1])
		if k > 10 :
			context.bot.send_message(chat_id=update.effective_chat.id, text="Arre havasi mutthal sale! Jaake pornhub chala")
			context.bot.send_message(chat_id=update.effective_chat.id, text="10 se zyada nahi milega, apne lund ko control me rakh!")
			k = 10
	except :
		k = 1

	fetched = False
	kcopy = k

	try :
		choice = context.args[0]
		if choice == "menu" :
			fetched = True
			context.bot.send_message(chat_id=update.effective_chat.id, text="Here are the categories: " + 
				"pic | desi | paki | teen | boob | cute | pussy | ass")
			context.bot.send_message(chat_id=update.effective_chat.id, text="Happy to add more. You already know the developer")

		elif choice == "pic" :
			subreddit = "nsfw"
		elif choice == "desi" :
			subreddit = "indiangirls"
		elif choice == "paki" :
			subreddit = "PakiBeauties"
		elif choice == "teen" :
			subreddit = "legalteens"
		elif choice == "boob" :
			subreddit = "Boobies"
		elif choice == "cute" :
			subreddit = "adorableporn"
		elif choice == "pussy" :
			subreddit = "pussy"
		elif choice == "ass" :
			subreddit = "ass"
		else :
			subreddit = "nsfw"
	except :
		 subreddit = "nsfw"

	if not fetched :
		print("subreddit is: ", subreddit)
		print("count is: ", k)

	time = "day"

	while not fetched :
		fetchCount = 0

		print("Searching")
		for submission in reddit.subreddit(subreddit).top(time_filter = time, limit = k) :
			if submission.url[-3:] == "jpg" :
				fetchCount += 1
	
		if fetchCount >=  kcopy:
			sent = 0 
			fetched = True
			print("Sending ")

			for submission in reddit.subreddit(subreddit).top(time_filter = time, limit = k) :
				if submission.url[-3:] == "jpg" :
					sent += 1
					context.bot.send_photo(chat_id=update.effective_chat.id, photo=submission.url)
					if sent == kcopy :
						break
			print("Sent")
		else :
			k = k*2
			k = k*2
			if k > 100 :
				time = "all"
			if k > 200 :
				context.bot.send_message(chat_id=update.effective_chat.id, text="Something went wrong! Try with a lower count")


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="A gaye aap apni ma chudwane!")


def reply(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text="Paka mat na *betichod*",
							 parse_mode=telegram.ParseMode.MARKDOWN)


def who(update, context):
    for x in context.args :
    	x = x.lower()
    	if x == "prateek" :
    		reply = "Prateek tera baap hai bhosdike"
    	elif x == "priyam" :
    		reply = "Priyam to Abrol ka choda hai"
    	elif x == "abhishek" :
    		reply = "Abhishek to baniya hai sala randibaaz"
    	elif x == "vedaant" or x == "vedant" :
    		reply = "Bhainse ka naam mat lo yaar please"
    	elif x == "deepesh" :
    		reply = "Chane khilao is bhosdiwale Deepesh ko"
    	elif x == "anshul" :
    		reply = "Londiyabazi karwa lo is behen k lode se bas"
    	else :
    		reply = "Kisi ka bhi naam le lega kya. Randi hai kya bhosdike"
    	context.bot.send_message(chat_id=update.effective_chat.id, text=reply)


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text, reply))
dispatcher.add_handler(CommandHandler('who', who))
dispatcher.add_handler(CommandHandler('meme', meme))
dispatcher.add_handler(CommandHandler('nsfw', boob))

def memetrial():
	for submission in reddit.subreddit("nsfw_gif").top(time_filter = "day", limit = 20) :
		print(submission.url)
		print()

# memetrial()
updater.start_polling()
