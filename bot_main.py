import telebot
import pyowm

bot = telebot.TeleBot("1439324992:AAGnBi1xx-mR2jyTzW3iJPzRzM-YTHaexGM")
owm = pyowm.OWM("d32211f650eb14ec244040886fdb75f5")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Hi! I am a weather checker bot. I was made to tell you about actual weather and give some recomendation about clothes =)")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Send me the city name you want to check weather in")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    try:
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place( message.text )
        w = observation.weather
        temp = w.temperature('celsius')["temp"]

        answer = "City: " + message.text + "\nWeather: " + w.detailed_status	 + "\n"
        answer += "Temperature: " + str(temp) + "\n\n" 

        if temp < 0:
            answer += "Bruh!! Cold! Put some winter clothes on"
        elif temp < 10: 
            answer += "Autumn jacket and warm sweater - best choice for such temperature"
        elif temp < 20:
            answer += "Hmmm. I think you should wear some long sleeve clothes on"
        else:
            answer += "Lucky! You can wear anything you want!"
        bot.send_message(message.chat.id, answer)
    
    except pyowm.commons.exceptions.NotFoundError:
    	bot.send_message(message.chat.id, "Invalid city name")

bot.polling( none_stop = True )
