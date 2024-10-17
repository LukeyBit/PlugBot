from api.scraper import create_plot
from api.bot import bot, send_updates
import time
import schedule
import threading

def main():
    schedule.every().day.at("03:00").do(send_updates)

    while True:
        schedule.run_pending()
        time.sleep(1)
        
def run_bot():
    bot.polling()
    

scheduler_thread = threading.Thread(target=main)
scheduler_thread.start()

bot.polling()



