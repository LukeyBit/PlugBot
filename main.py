from api.bot import bot, send_updates, setup_db
import time
import schedule
import threading

setup_db()

def main():
    schedule.every().day.at("18:00").do(send_updates)
    
    print("Scheduler is set")

    while True:
        schedule.run_pending()
        time.sleep(1)
        
def run_bot():
    bot.polling()
    
# Run the bot polling in a separate thread
bot_thread = threading.Thread(target=run_bot)
bot_thread.start()
print("Bot is running")

# Run the scheduler in the main thread
main()