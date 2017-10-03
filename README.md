# ZenPacks.community.Telegram
Zenoss ZenPack for sending notifications to Telegram

This ZenPack will allow you to send notifications to Telegram using data instead of SMS.

1.	 Create a bot using the BotFather https://telegram.me/BotFather
2.	Once created, you will receive an API key, save the key as you will need it in the configuration
3.	If using a channel, make the channel public with a unique name (e.g. ZenPackTesting) and add your bot to the channel as an administrator, you will need to search for your bot’s name (e.g. Zen_TG_Bot0
4.	Once it’s added, you will need to use the Telegram Bot API to send a message to determine the Chat ID https://api.telegram.org/botTOKENOFTHEBOT/sendMessage?chat_id=@ZenPackTesting&text=Test
5.	You will get a Chat ID value back (-1234567890), you can make the channel private now if you wish.
6.	After installing, you will get a new Notification Type, enter in your Chat ID and Bot Token.
7.	If using a group, add your bot to the group and use the following API link to determine the chat ID:
https://api.telegram.org/bot<YourBOTToken>/getUpdates

