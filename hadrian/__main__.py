from time import sleep
from hadrian.connections.database import database
from hadrian.connections.chatgpt import ChatGPTData, ChatGPTClient

data = ChatGPTData()
conn = ChatGPTClient(data)

# data.set_image("/home/pi64/Pictures/me.jpeg")
data.set_image("/Users/molloyin/Pictures/hadrian-target.jpg")
conn.query()
# Close the database connection when done

# Event loop and diagnostics seperate threads

# highest priority: prove chatgpt api recieve img and return response
    # looks like we'll need to upload photo to website, API best at retrieving
    # image from URL https://community.openai.com/t/how-to-send-base64-images-to-assistant-api/752440/14
# establish connections 
# wait for start command from website
# img from camera -> send to gpt -> parse instructions -> command rc -> restart
# send diagnostics to website at each step
# before exit, send stats to website
