import telebot
from telebot import types

API_TOKEN = '8592205332:AAHzjwPDyHFX2Cv7OkDzCP22hFzyWEs_SGw'
ADMIN_ID = 6523586283
bot = telebot.TeleBot(API_TOKEN)

# ان لائن بٹن برائے کنٹرول
def get_control_panel():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("📍 Live Location", callback_data="loc"),
        types.InlineKeyboardButton("💬 Read SMS", callback_data="sms"),
        types.InlineKeyboardButton("📸 Secret Photo", callback_data="cam"),
        types.InlineKeyboardButton("🔒 Lock Screen", callback_data="lock"),
        types.InlineKeyboardButton("🗑️ Wipe Data", callback_data="wipe")
    )
    return markup

@bot.message_handler(commands=['start'])
def welcome(message):
    user_id = message.chat.id
    caption = "Welcome To The Dangerous World Of Awais Mayo 👿👑👿\n\nاس بوٹ کو استعمال کرنے کے لیے 10 ریفرلز مکمل کریں یا ایڈمن سے رابطہ کریں۔"
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📢 Join Group 1", url="https://t.me/awaisblackhacker1"))
    # (باقی گروپس کے بٹن بھی یہاں آئیں گے)
    markup.add(types.InlineKeyboardButton("✅ Check Status", callback_data="check"))
    
    try:
        with open('I.png', 'rb') as img:
            bot.send_photo(user_id, img, caption=caption, reply_markup=markup)
    except:
        bot.send_message(user_id, caption, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == "check":
        bot.send_message(call.message.chat.id, "🔓 آپ کو ابھی تک اپروو نہیں کیا گیا۔ ریفرل یا پیمنٹ مکمل کریں۔")
    else:
        # جب علی کسی بٹن پر کلک کرے گا، تو ڈیٹا ایڈمن کو بھی جائے گا
        bot.send_message(ADMIN_ID, f"🚨 علی (ID: {call.message.chat.id}) نے '{call.data}' کمانڈ بھیجی ہے!")
        bot.answer_callback_query(call.id, f"کمانڈ '{call.data}' بھیج دی گئی ہے!")

bot.polling()
  
