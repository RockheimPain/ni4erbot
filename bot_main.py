import telebot
import pyowm

bot = telebot.TeleBot("1439324992:AAGnBi1xx-mR2jyTzW3iJPzRzM-YTHaexGM")
owm = pyowm.OWM("d32211f650eb14ec244040886fdb75f5")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Здоров, я погодний бот. Буду казати тобі інфу про погоду і давати рекомендації щодо одягу =)")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Напиши мені назву міста, погоду в якому ти хочеш взнати")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place( message.text )
    w = observation.get_weather()
    temp = w.get_temperatuire('celsius')["temp"]

    answer = "В місті " + message.text + " зараз " + w.get_detailed_status() + "\n"
    answer += "Температура зараз близько " + str(temp) + "\n\n" 

    if temp < 0:
    	answer += "Дубак с*ка! Зимову куртку і файні теплі ґачі на базу!"
  	elif temp < 10:
		answer += "Осіння куртка і теплий светрик в таку погоду стане чудовим вибором"
  	elif temp < 20:
		answer += "Ну, хоча би кофточку напяль"
 	else:
		answer += "Нормас: хоч в трусах топай"
    bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )

