The bot selects an Amazon Affiliate link from a txt file, chosen randomly, containing an Amazon product and concatenates it with a motivational phrase, which you can request from any artificial intelligence, to post a tweet every 35 minutes.
This bot is designed to avoid spending a cent, promoting products for free, and getting paid for it.
AMAZON PAYS YOU A COMMISSION IF THE PRODUCT IS PURCHASED USING YOUR LINK. SEARCH FOR AMAZON AFFILIATE VIDEOS.
You can adapt it and post any phrase. I connected it with ChatGPT’s APIs, but it had issues due to the limited number of requests accepted for free by ChatGPT.
Remember to create a folder and place everything inside the same folder.
You can use any IDE you want, but I used Visual Studio Code (VSC) on Windows.

This bot is free, but if you want to support me as the creator, you can donate:

BTC:

	1LVocwYpWnd59Juyfhyum7JiVRXAmqAaWb

ETH (BSC):

	0x44d27c323a0b0a7ec9d2cf2ccfa173f15ce27ef5

BNB (BSC):

	0x44d27c323a0b0a7ec9d2cf2ccfa173f15ce27ef5

XRP:

	rNxp4h8apvRis6mJf9Sh8C6iRxfrDWN7AV

	Memo: 401375175

USDT (TRX):

	TFjbSrQVmAqaeuGzUsPHVTM2nDD1LweY5k

RVN:

	RFLbQboprMwgeuXGTPy3h6gW72Lvfgkgrs

Installation Instructions

1- Install Python and pip: Make sure you have Python and pip installed on your system.
You can download Python from python.org.

2- Install the dependencies: Open a terminal or command line and run the following commands
to create a virtual environment (optional) and install tweepy.

RUN THIS COMMAND IN THE TERMINAL:

	pip install tweepy

If prompted to update pip (install pip-24.1.2):

	python.exe -m pip install --upgrade pip

3- Prepare Files

Create tweets.txt file: This file should contain the product links you want to tweet,
one per line.

Create phrases.txt file: This file should contain motivational phrases, one per line.

Create an executable file: x-bot.py (paste the code from step 6).

4- Configure your API keys: Make sure you have your Twitter API V2 keys. To get them,
open your Twitter account at https://developer.twitter.com/en.

Configure Twitter Credentials:

Replace the values of the variables in the x-bot.py file:

		API_KEY, API_SECRET_KEY, ACCESS_TOKEN,

		ACCESS_TOKEN_SECRET,

		BEARER_TOKEN with your own Twitter API credentials.

5- Code Explanation

File Reading: The motivational phrases and tweets are read from phrases.txt and
tweets.txt files.

Random Selection Without Repetition: A tweet and a motivational phrase are selected randomly,
ensuring they are not repeated until all options have been used.
Sets are used to track the phrases and tweets already used.

Process Reset: When all phrases and tweets have been used, the sets are cleared to restart
the process and allow them to be used again.

Tweet Posting: The tweet is posted on Twitter by concatenating the motivational phrase with
the product link.

Wait: The bot waits 35 minutes before posting the next tweet. This time is to avoid exceeding
the limit of 1500 tweets per month for free accounts.
Paid accounts can reduce the time between tweets.

File Structure, copy and paste as many as you want.

tweets.txt:

	https://www.amazon.com/product1
	https://www.amazon.com/product2
	https://www.amazon.com/product3


phrases.txt:

	Don’t miss out on this amazing product!
	This product can change your life. Try it now!
	Take advantage of this unique opportunity with this product!
	Discover the wonders of this product today!


With this approach, the bot will ensure that all phrases and links are posted randomly and without repetition, until all options have been used, at which point the process will restart.

6- Open a file called "x-bot.py" and paste the following code:

It is included in the `x-bot.py` file.


7- In the terminal, run the following command:

	python x-bot.py  

ENJOY YOUR CODE!!!!
