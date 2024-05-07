import tweepy
from pprint import pprint
import schedule
from time import sleep

# API情報を記入
BEARER_TOKEN        = "AAAAAAAAAAAAAAAAAAAAAN9soQEAAAAArB%2BTLWYbbH8ZdnTiQsTXUpv%2FR1w%3DYjGp6PjJWQohQFEAHYhn6nA9cxfUZp3vFXxd77z7D9NR0ROWb5"
API_KEY             = "GxcQxYWO60NlHCksE5np0kXKy"
API_SECRET          = "h5sHjDfyqqdn9okkRSPHusZCEPjeNBsmD0az6I0NhVr0qejynm"
ACCESS_TOKEN        = "1356873070821089280-4J1kfUvj9c3P9xjkAycYCLpAgcrhA1"
ACCESS_TOKEN_SECRET = "rFqncZJo51Jhu5RIeeANUHAVxOdZ1J1IDhDHrbbw0y2Ih"


# クライアント関数を作成
def ClientInfo():
    client = tweepy.Client(bearer_token    = BEARER_TOKEN,
                           consumer_key    = API_KEY,
                           consumer_secret = API_SECRET,
                           access_token    = ACCESS_TOKEN,
                           access_token_secret = ACCESS_TOKEN_SECRET,
                          )
    
    return client


# メッセージを指定
message = """【拡散希望】
デュオカスタムを開催します！

日時：9/23(土)21:30~
応募方法：応募フォームに必要事項を提出
応募締切：9/21(木)23:59

詳細は下記のツイートをご覧ください！
https://twitter.com/kanoi_music/status/1696538206693675206?s=20

#かのいカスタム #Apexカスタム募集 #Apex募集 #ApexLegends"""

#01 定期実行するツイート関数を準備
def CreateTweet(message):
    tweet = ClientInfo().create_tweet(text=message)
    return tweet
    
#02 スケジュール登録
schedule.every().day.at("21:00").do(CreateTweet,message=message)

#03 イベント実行
while True:
    schedule.run_pending()
    sleep(1)
