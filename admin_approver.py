import telebot
from telebot import types

API_TOKEN = '8351902912:AAHBcLgG1QIEwYkyuBRfEz-K7OaChr_xYV4'
bot = telebot.TeleBot(API_TOKEN)
OWNER_ID = 6523586283

@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id == OWNER_ID:
        bot.send_message(OWNER_ID, "🛡️ ایڈمن پینل فعال ہے۔ یوزر کو اپروو کرنے کے لیے لکھیں: /approve [USER_ID]")

@bot.message_handler(commands=['approve'])
def approve(message):
    if message.chat.id == OWNER_ID:
        user_id = message.text.split()[1]
        # یہاں ہم علی کو میسج بھیجیں گے کہ وہ اپروو ہو گیا ہے
        bot.send_message(OWNER_ID, f"✅ یوزر {user_id} کو رسائی دے دی گئی ہے۔")
        # نوٹ: عملی طور پر یہاں ڈیٹا بیس اپڈیٹ ہوگا

bot.polling()

