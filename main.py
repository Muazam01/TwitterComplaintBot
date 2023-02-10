
import time
import InternetSpeedTwitterBot



ISP_DOWNLOAD_SPEED=100
ISP_UPLOAD_SPEED=100

bot=InternetSpeedTwitterBot.TwitterBot()
bot.getinternetspeed()
time.sleep(10)
if int(float(bot.download_speed))<ISP_DOWNLOAD_SPEED and int(float(bot.upload_speed))<ISP_UPLOAD_SPEED:
    bot.tweet_at_provider()
else:
    print("Your speed is optimum")



