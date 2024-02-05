from dotenv import load_dotenv
from internet_speed_twitter_bot import InterNetSpeedTwitterBot

load_dotenv()

internet_speed_twitter_bot = InterNetSpeedTwitterBot()
internet_speed_twitter_bot.get_internet_speed()
# internet_speed_twitter_bot.tweet_at_provider()
