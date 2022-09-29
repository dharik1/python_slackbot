# python_slackbot
Integrated Hubot using slack RTM Client, which listen to slack events and respond with image/file upload to slack thread.

# Pre Requisite:
1. Install python
2. Install SlackClient
3. pip install python-dotenv (if you use .env file)
4. Install selenium
5. Download the webdriver and move it to your project directory

# Summary:
You can find Hubot in slack, to integrate it you need to get xoxb token i.e., Bot token.
By using Bot token and RTM client you can make the bot listen to events and respond back accordingly.
If you are using new slack app or bot, you need to have both Slack App token and Bot Token for listening to slack events.
Few old apps are only having Bot token, so you can make use of RTM clients there.

# I got this Response from slack after long hustle :)

Unfortunately, an app-level token (which starts with `xapp-`) cannot be generated from a Hubot integration. Additionally, the Hubot integration is not compatible with the 'Socket Modee Client' feature in our **Python Slack SDK** (https://slack.dev/python-slack-sdk/socket-mode/index.html).
In order to generate an app-level token (starts with `xapp-`), you must first create a Slack API app (from here: https://api.slack.com/apps), and then follow the steps in the following Socket Mode doc section:
https://api.slack.com/apis/connections/socket#token
However, if you want to continue using your Hubot integration which generates a bot token (stats with `xoxb-), then you'll need to use our 'RTM API' feature (https://api.slack.com/rtm) instead of our 'Socket Mode' feature.
We hope that helps to clear things up, and thanks for checking in about this.


**Ref**:
https://api.slack.com/rtm

https://slack.dev/python-slack-sdk/real_time_messaging.html


