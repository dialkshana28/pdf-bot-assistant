import telebot
from telebot import types

# Your assistant bot token (create new bot from @BotFather)
BOT_TOKEN = "7955194455:AAHjaIOt18YUFUZD5YmYzP57gNIcgH07lZA"
bot = telebot.TeleBot(BOT_TOKEN)

# Main menu keyboard
def main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton("📚 FAQ")
    btn2 = types.KeyboardButton("💳 Payments")
    btn3 = types.KeyboardButton("⚙️ Settings")
    btn4 = types.KeyboardButton("📞 Contact Support")
    markup.add(btn1, btn2, btn3, btn4)
    return markup

# FAQ menu
def faq_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("How to use PDF bot?", callback_data="faq_use")
    btn2 = types.InlineKeyboardButton("File size limits?", callback_data="faq_size")
    btn3 = types.InlineKeyboardButton("Supported formats?", callback_data="faq_formats")
    btn4 = types.InlineKeyboardButton("Privacy policy?", callback_data="faq_privacy")
    btn5 = types.InlineKeyboardButton("← Back", callback_data="back_main")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    return markup

# Payment menu
def payment_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Premium Plans", callback_data="pay_plans")
    btn2 = types.InlineKeyboardButton("Payment Methods", callback_data="pay_methods")
    btn3 = types.InlineKeyboardButton("How to upgrade?", callback_data="pay_upgrade")
    btn4 = types.InlineKeyboardButton("Refund policy", callback_data="pay_refund")
    btn5 = types.InlineKeyboardButton("← Back", callback_data="back_main")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    return markup

# Settings menu
def settings_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Language", callback_data="settings_lang")
    btn2 = types.InlineKeyboardButton("Notifications", callback_data="settings_notify")
    btn3 = types.InlineKeyboardButton("← Back", callback_data="back_main")
    markup.add(btn1, btn2, btn3)
    return markup

# FAQ answers
faq_answers = {
    "faq_use": "📖 **How to use PDF bot:**\n\n1. Send any PDF file to the bot\n2. Choose your desired action (merge, split, convert, etc.)\n3. Wait for processing\n4. Download your result\n\nFor premium features, upgrade your plan!",
    "faq_size": "📏 **File size limits:**\n\n• Free users: Up to 10MB per file\n• Premium users: Up to 100MB per file\n• Maximum 50 files per merge operation",
    "faq_formats": "📄 **Supported formats:**\n\n• Input: PDF, DOC, DOCX, JPG, PNG, TXT\n• Output: PDF, DOCX, JPG, PNG\n• OCR support for scanned documents",
    "faq_privacy": "🔒 **Privacy policy:**\n\n• Your files are processed securely\n• Files are automatically deleted after 24 hours\n• We never share your data with third parties\n• End-to-end encryption for premium users"
}

# Payment answers
payment_answers = {
    "pay_plans": "💎 **Premium Plans:**\n\n**Monthly:** $4.99/month\n- Unlimited PDF operations\n- Priority processing\n- 100MB file limit\n- Ad-free experience\n\n**Yearly:** $49.99/year (Save 17%)\n- All monthly benefits\n- Exclusive features\n- Lifetime updates\n\n**Lifetime:** $99.99 one-time\n- All features forever\n- No recurring charges",
    "pay_methods": "💳 **Payment Methods:**\n\n• Credit/Debit Cards (Visa, Mastercard)\n• PayPal\n• Google Pay\n• Apple Pay\n• Bank Transfer\n\nAll payments are secure and encrypted.",
    "pay_upgrade": "🚀 **How to upgrade:**\n\n1. Click on any premium plan\n2. Choose your payment method\n3. Complete the payment\n4. You'll receive confirmation instantly\n5. Start using premium features immediately!\n\nYour subscription activates within 5 minutes.",
    "pay_refund": "💰 **Refund Policy:**\n\n• 7-day money-back guarantee\n• Full refund if not satisfied\n• Contact support for refund requests\n• Processing time: 3-5 business days\n\nNote: Refunds not available for lifetime plans after 7 days."
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = """
🤖 **Welcome to PDF Bot Assistant!**

I'm here to help you with your PDF bot queries. Choose from the options below:

📚 **FAQ** - Common questions and answers
💳 **Payments** - Pricing and payment information
⚙️ **Settings** - Customize your experience
📞 **Contact Support** - Get help from our team

How can I assist you today?
    """
    bot.send_message(message.chat.id, welcome_text, 
                     reply_markup=main_menu(), 
                     parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == "📚 FAQ")
def faq_handler(message):
    bot.send_message(message.chat.id, "❓ **Frequently Asked Questions**\n\nSelect a question to learn more:", 
                     reply_markup=faq_menu(), 
                     parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == "💳 Payments")
def payment_handler(message):
    bot.send_message(message.chat.id, "💳 **Payment Information**\n\nChoose a topic to learn more:", 
                     reply_markup=payment_menu(), 
                     parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == "⚙️ Settings")
def settings_handler(message):
    bot.send_message(message.chat.id, "⚙️ **Settings**\n\nConfigure your preferences:", 
                     reply_markup=settings_menu(), 
                     parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == "📞 Contact Support")
def support_handler(message):
    support_text = """
📞 **Contact Support**

Need help? Reach out to us:

📧 Email: teamceylonservicess@gmail.com
💬 Telegram: @teamceylon
⏰ Hours: 24/7 support

Please describe your issue clearly and we'll get back to you ASAP!
    """
    bot.send_message(message.chat.id, support_text, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data.startswith("faq_"):
        answer = faq_answers.get(call.data, "Answer not found.")
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text=answer,
                             reply_markup=faq_menu(),
                             parse_mode='Markdown')
    
    elif call.data.startswith("pay_"):
        answer = payment_answers.get(call.data, "Answer not found.")
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text=answer,
                             reply_markup=payment_menu(),
                             parse_mode='Markdown')
    
    elif call.data == "back_main":
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="❓ **Frequently Asked Questions**\n\nSelect a question to learn more:",
                             reply_markup=faq_menu(),
                             parse_mode='Markdown')
    
    elif call.data.startswith("settings_"):
        if call.data == "settings_lang":
            bot.answer_callback_query(call.id, "Language settings coming soon!")
        elif call.data == "settings_notify":
            bot.answer_callback_query(call.id, "Notification settings coming soon!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, 
                     "I didn't understand that. Please use the menu buttons below.",
                     reply_markup=main_menu())

if __name__ == "__main__":
    print("Bot Assistant is running...")
    bot.polling(none_stop=True)