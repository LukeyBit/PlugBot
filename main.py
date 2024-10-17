from api.bot import bot, send_updates, setup_db
import time
import schedule
import threading

setup_db()

def main():
    schedule.every().day.at("03:36").do(send_updates)
    
    print("Scheduler is set")

    while True:
        schedule.run_pending()
        time.sleep(1)
        
def run_bot():
    bot.polling()
    

scheduler_thread = threading.Thread(target=main)
scheduler_thread.start()
print("Scheduler is running")

print("Bot is running")
bot.polling()



