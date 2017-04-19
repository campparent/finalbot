# coding: utf-8

#configuration

MY_CONSUMER_KEY = "texcukzLHvHtw0cD3blITb04o"
MY_CONSUMER_SECRET = "qJv2w2t5Y5JorAogh4vfmr1izbAVH49sEpXd2GKviD0hI6ITY0"
MY_ACCESS_TOKEN_KEY = "853675322629398528-yYbTBki9AP6bLRqAEyySQCusbX6iKKO"
MY_ACCESS_TOKEN_SECRET = "afkzLMIaRCp8ghJDVhAs8kFLxbdMJqoezwjqFaamM4Iyc"

SOURCE_ACCOUNTS = ["realDonaldTrump", "JustinTrudeau"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 1 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = "testcorpus.txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API. You can use the included testcorpus.txt, if needed.
TWEET_ACCOUNT = "machinmachin_" #The name of the account you're tweeting to.