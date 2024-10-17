from time import sleep
from hadrian.connections.database import database
from hadrian.connections.chatgpt import ChatGPTData, ChatGPTClient

data = ChatGPTData()
conn = ChatGPTClient(data)

db = database()
db.initialize_db()
# data.set_image("/home/pi64/Pictures/me.jpeg")
image_path = "/Users/molloyin/Pictures/hadrian-target.jpg"
data.set_image(image_path)
with open(image_path, "rb") as image_file:
    image_data = image_file.read() 
conn.query()

for i in range (1, 6):
    action = "Name jeff {i}"
    db.add_metric(i, action, image_data)
    print(f"should be adding: {action} {i}, {image_data}")
    sleep(1)

db.close()

# Perhaps have the camera -> query -> instructions loop a seperate thread from  
#   commanding RC. This way we can get around i/o blocking and send photos mid iteration

# TODO: times_not_seen counter 

# Event loop and diagnostics seperate threads

# highest priority: prove chatgpt api recieve img and return response
    # looks like we'll need to upload photo to website, API best at retrieving
    # image from URL https://community.openai.com/t/how-to-send-base64-images-to-assistant-api/752440/14
# establish connections 
# wait for start command from website
# img from camera -> send to gpt -> parse instructions -> command rc -> restart
# send diagnostics to website at each step
# before exit, send stats to website
