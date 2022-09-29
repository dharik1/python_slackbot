from email import message
import os
from pathlib import Path
from dotenv import load_dotenv
from slack import RTMClient
from slack.errors import SlackApiError
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image

load_dotenv()

@RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    message=data.get('text', [])
    if 'text' in data and '.opm' in message.lower():
    
        #customizing the input based on messag
        #str = data.get('text', [])
      
        revstr = message.rsplit(' ', 1)[-1]
        revstr = revstr.lower()
     
        laststr = revstr[-1]
        splitstr = message.split(' ')
        
                
        if len(revstr) == 2 and len(splitstr) == 2 and laststr in 'dhm':
            channel_id = data['channel']
            thread_ts = data['ts']
            user = data['user']
            
            try:
                response = web_client.chat_postMessage(
                    channel=channel_id,
                    text=f"Hi <@{user}>! Just a sec..Preparing your request...",
                    thread_ts=thread_ts
                )
            except SlackApiError as e:
                # You will get a SlackApiError if "ok" is False
                assert e.response["ok"] is False
                assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
                print(f"Got an error: {e.response['error']}")
            
            
            driver = webdriver.Chrome()
            
            # URL of website
            #used revstr to concat my url
            url = "xyz url.com"
            
            # Opening the website
            driver.get(url)
            #you can make below function to wait untill your page loads, here I used class.name

            elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "flot-overlay")))

            driver.save_screenshot("snap.png")

            try:
                response = web_client.files_upload(    
                file='snap.png',
                initial_comment='Here you go!!!',
                channels=channel_id,
                text=f"Hi <@{user}>!",
                thread_ts=thread_ts)

            except SlackApiError as e:
                # You will get a SlackApiError if "ok" is False
                assert e.response["ok"] is False
                assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
                print(f"Got an error: {e.response['error']}")
            finally:
                driver.quit()
            
        else:
            try:
                channel_id = data['channel']
                thread_ts = data['ts']
                user = data['user']
                response = web_client.chat_postMessage(
                    channel=channel_id,
                    text=f"Hi <@{user}>! Thanks for reaching out. Please use commands like...",
                    thread_ts=thread_ts
                )
            except SlackApiError as e:
                # You will get a SlackApiError if "ok" is False
                assert e.response["ok"] is False
                assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
                print(f"Got an error: {e.response['error']}")
            

                


rtm_client = RTMClient(token=os.environ["SLACK_TOKEN"])
rtm_client.start()
