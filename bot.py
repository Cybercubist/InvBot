import telebot
from telebot import types
from telebot.types import Message
import requests
from math import sqrt

from Other import finAPI
from Other import Ideas
from Other import Markets
from Other import Whatsnew

bot = telebot.TeleBot('YOUR_BOT_TOKEN')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello, Investor. How may I help? That is what I can do:'
    +'\n/help — Help\n/menu — Menu\n/ideas — Investment ideas\n/markets — Short market review'
    +'\n/financials — Assets info\n/whatsnew — Latest updates')
    
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'InvBot is an investment and finance bot, which has few features.'
    +' To choose a feature press /menu. You can also use commands adding slash, for example /ideas. '
    +' To get info about assets use $ symbol, for example $FB')

@bot.message_handler(commands=['ideas'])
def ideas_message(message):
    keyboard = types.InlineKeyboardMarkup(row_width=3);
    next_idea = types.InlineKeyboardButton(text='Next', callback_data='ideas2')
    keyboard.add(next_idea);
    bot.send_message(message.chat.id, text = Ideas[0], parse_mode='html', reply_markup=keyboard)
    
@bot.message_handler(commands=['markets'])
def ideas_message(message):
    keyboard = types.InlineKeyboardMarkup(row_width=3);
    next_idea = types.InlineKeyboardButton(text='Back to menu', callback_data='menu')
    keyboard.add(next_idea);
    bot.send_message(message.chat.id, text = Markets[0], parse_mode='html', reply_markup=keyboard)
    
@bot.message_handler(commands=['financials'])
def financials_message(message):
    bot.send_message(message.chat.id, 'Enter asset ticker. Before the ticker please type "$" symbol, for example "$AAPL"')
    stockinfo = message.text
    stockinfo = finAPI(stockinfo)
    bot.send_message(message.chat.id, stockinfo)
    
@bot.message_handler(commands=['whatsnew'])
def valuemaster_message(message):
    bot.send_message(message.chat.id, text=Whatsnew, parse_mode='html')
      
@bot.message_handler(commands=['menu'])
def menu_message(message):
    keyboard = types.InlineKeyboardMarkup(row_width=3);
    key_markets_condition = types.InlineKeyboardButton(text='Market conditions', callback_data='markets');
    keyboard.add(key_markets_condition);
    key_ideas = types.InlineKeyboardButton(text='Investment ideas', callback_data='ideas');
    keyboard.add(key_ideas);
    key_financials = types.InlineKeyboardButton(text='Asset info', callback_data='financials');
    keyboard.add(key_financials);
    key_whatsnew = types.InlineKeyboardButton(text="What's new?", callback_data='whatsnew');
    keyboard.add(key_whatsnew);
    question = 'What do you want to do?';
    bot.send_message(message.chat.id, text=question, reply_markup=keyboard)
    
@bot.message_handler(func=lambda m: True)
def random_message(message):
    usersLine = message.text
    if usersLine[0] != '$':
        bot.send_message(message.chat.id, "Haha, I don't get it! Please, try again or come back to /menu")
    else:
        stockinfo = message.text
        stockinfo = stockinfo.replace("$","")
        stockinfo = finAPI(stockinfo)
        bot.send_message(message.chat.id, stockinfo)
        
@bot.callback_query_handler(func=lambda m: True)
def callback_worker(call):
        
    if call.data == 'financials':
        bot.send_message(call.message.chat.id, 'Enter asset ticker. Before the ticker please type "$" symbol, for example "$FB"')    
        
    elif call.data == 'ideas':
        f = Ideas
        keyboard = types.InlineKeyboardMarkup(row_width=3);
        next_idea = types.InlineKeyboardButton(text='Next', callback_data='ideas2')
        keyboard.add(next_idea);
        bot.send_message(call.message.chat.id, text=f[0], parse_mode='html', reply_markup=keyboard)
        
    elif call.data == 'ideas2':
        f = Ideas
        keyboard = types.InlineKeyboardMarkup(row_width=3);
        next_idea = types.InlineKeyboardButton(text='Next', callback_data='ideas3')
        keyboard.add(next_idea);
        bot.send_message(call.message.chat.id, text=f[1], parse_mode='html', reply_markup=keyboard)
        
    elif call.data == 'ideas3':
        f = Ideas
        keyboard = types.InlineKeyboardMarkup(row_width=3);
        next_idea = types.InlineKeyboardButton(text='Next', callback_data='ideas4')
        keyboard.add(next_idea);
        bot.send_message(call.message.chat.id, text=f[2], parse_mode='html', reply_markup=keyboard)
        
    elif call.data == 'ideas4':
        f = Ideas
        keyboard = types.InlineKeyboardMarkup(row_width=3);
        next_idea = types.InlineKeyboardButton(text='Next', callback_data='ideas5')
        keyboard.add(next_idea);
        bot.send_message(call.message.chat.id, text=f[3], parse_mode='html', reply_markup=keyboard)
        
    elif call.data == 'ideas5':
        f = Ideas
        keyboard = types.InlineKeyboardMarkup(row_width=3);
        next_idea = types.InlineKeyboardButton(text='Next', callback_data='ideas6')
        keyboard.add(next_idea);
        bot.send_message(call.message.chat.id, text=f[4], parse_mode='html', reply_markup=keyboard)
        
    elif call.data == 'ideas6':
        keyboard = types.InlineKeyboardMarkup(row_width=3);
        back_menu = types.InlineKeyboardButton(text='Back to menu', callback_data='menu')
        keyboard.add(back_menu);
        bot.send_message(call.message.chat.id, text=Ideas[5], parse_mode='html', reply_markup=keyboard)
        
    elif call.data == 'markets':
        keyboard = types.InlineKeyboardMarkup(row_width=3);
        back_menu = types.InlineKeyboardButton(text='Back to menu', callback_data='menu')
        keyboard.add(back_menu);
        bot.send_message(call.message.chat.id, text = Markets[0], parse_mode='html', reply_markup=keyboard)
        
    elif call.data == 'menu':
        keyboard = types.InlineKeyboardMarkup(row_width=3);
        key_markets_condition = types.InlineKeyboardButton(text='Market conditions', callback_data='markets');
        keyboard.add(key_markets_condition);
        key_ideas = types.InlineKeyboardButton(text='Investment ideas', callback_data='ideas');
        keyboard.add(key_ideas);
        key_financials = types.InlineKeyboardButton(text='Asset info', callback_data='financials');
        keyboard.add(key_financials);
        key_whatsnew = types.InlineKeyboardButton(text="What's new?", callback_data='whatsnew');
        keyboard.add(key_whatsnew);
        question = 'What do you want to do?';
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    
    elif call.data == 'whatsnew':
        bot.send_message(call.message.chat.id, text=Whatsnew, parse_mode='html')
    
bot.polling()