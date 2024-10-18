from time import sleep
from hadrian.connections.rover import Rover
from hadrian.connections.camera import Camera 
from hadrian.connections.database import database
from hadrian.connections.chatgpt import ChatGPTData, ChatGPTClient

image_path = "/home/pi/Projects/hadrian/current_image.jpg"
iter_limit = 100

rover = Rover()
data = ChatGPTData()
conn = ChatGPTClient(data)
camera = Camera(image_path)
db = database(image_path)
db.initialize()

for i in range (1, iter_limit):
    camera.take_image()
    data.set_image(image_path)
    with open(image_path, "rb") as image_file:
        image_data = image_file.read() 

    conn.query()
    action = data.response
    if action == "STOP": break
    db.add_metric(i, action, image_data)
    rover.run_from_response(action)
    sleep(1)

db.close()
rover.cleanup()
