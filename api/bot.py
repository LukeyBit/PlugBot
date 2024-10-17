from dotenv import load_dotenv
import os
import telebot
from psycopg2 import connect

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

def get_connection():
    return connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )

def setup_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id PRIMARY KEY)')
    conn.commit()
    cursor.close()
    conn.close()
    
def add_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (id) VALUES (%s)', (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    
def remove_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    
def get_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM users')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return [user[0] for user in users]
    
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['subscribe'])
def subscribe(message):
    add_user(message.chat.id)
    bot.reply_to(message, 'You have been subscribed to daily electricity price updates for SE3!')
    
@bot.message_handler(commands=['unsubscribe'])
def unsubscribe(message):
    remove_user(message.chat.id)
    bot.reply_to(message, 'You have been unsubscribed from daily electricity price updates for SE3.')
    
def send_updates():
    users = get_users()
    for user in users:
        bot.send_photo(user, open('prices.png', 'rb'))
        bot.send_message(user, 'Here are the latest electricity prices for SE3.')
