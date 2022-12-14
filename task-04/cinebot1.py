import telebot
import requests
import csv , io

yourkey = '260cef2a'
bot_id = '5641826161:AAGlQBJg2HefvzxFykJS5cczhWKwogNOfY8'

bot = telebot.TeleBot('5641826161:AAGlQBJg2HefvzxFykJS5cczhWKwogNOfY8')

s = io.StringIO()
buf = io.BytesIO()

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    


@bot.message_handler(func=lambda message : botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    movieName = message.text.replace('/movie ', "")

    bot.reply_to(message, 'Getting movie info...')
    api_url = f"http://www.omdbapi.com/?apikey={yourkey}&t={movieName}"
    movie = requests.get(api_url).json()

    poster_url = movie['Poster']
    title = movie['Title']
    year = movie['Year']
    Rating = movie['imdbRating']
    

    csv.writer(s).writerows([title , year , Rating ,])
    s.seek(0)



    buf.write(s.getvalue().encode())
    buf.seek(0)


    buf.name = f'datas.csv'
    bot.send_photo(message.chat.id, poster_url, f'Title: {title}\nYear released: {year} \nRating: {Rating}')
    def export(message):
        bot.send_document(message.chat.id,buf)

@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
    
bot.infinity_polling()