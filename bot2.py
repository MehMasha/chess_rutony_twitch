# import asyncio
 
# import websockets
 
# # create handler for each connection
 
# async def handler(websocket, path):
 
#     data = await websocket.recv()
 
#     reply = f"Data recieved as:  {data}!"
 
#     # await websocket.send(reply)
 
 
 
# start_server = websockets.serve(handler, "127.0.0.1", 8383)
 
 
 
# asyncio.get_event_loop().run_until_complete(start_server)
 
# asyncio.get_event_loop().run_forever()


import asyncio
import json
from websockets.sync.client import connect
import time
import queue
from threading import Thread
from game import main

def hello(q):
    with connect("ws://localhost:8383/Chat") as websocket:
        while True:
            message = websocket.recv()
            # print(f"Received: {message}")
            js = json.loads(message)
            text = js.get('text_text')
            username = js.get('user')
            user_id = js.get('user_id')
            site = js.get('site')
            try:
                text = text.strip().split()
                if len(text) >= 1:
                    command = text[0]
                    if command == '!move':
                        if len(text) == 3:
                            start = text[1]
                            finish = text[2]
                            q.put_nowait(f'{start} {finish}')
                            print(f'{username} с {site} походил {start} {finish}')

            except:
                pass
            # q.put_nowait(f'{start} {finish}')
            time.sleep(1)




q = queue.Queue()


try:
    # create two new threads
    t1 = Thread(target=hello, args=(q, ))
    t2 = Thread(target=main, args=(q, ))

    # start the threads
    t1.start()
    t2.start()
    # start the threads
    t1.join()
    t2.join()
except:
    pass



#  {
#     "id":423,
#     "message_id":"1682275753865",
#     "user_id":"",
#     "site":"GoodGame",
#     "site_cut":"GG",
#     "site_img":"<img src='./../../themes/goodgame.png' />",
#     "sub":" <span class=\"icon icon-star\" style=\"color:#BD70D7\"></span>",
#     "moderator":"",
#     "rank":"",
#     "rank_img":"",
#     "rank_msg_qty":285,
#     "rank_credits_qty":528,
#     "rank_time":"25:27",
#     "x2":2,
#     "user":"sniak",
#     "color_nick":"#BD70D7",
#     "user_avatar":"",
#     "channel_avatar":"",
#     "text":" всё ок  ",
#     "text_text":"всё ок",
#     "reply":0,
#     "clear_chat":false,
#     "color_text":"",
#     "spec_user":false,
#     "spec_img":"",
#     "sub_alert":false,
#     "fol_alert":false,
#     "don_alert":false,
#     "host_alert":false,
#     "system":false,
#     "type":"message"}

# {"user_id":"123306286","user":"rayon_goslink""text":"А что на питоне в основном делают? Бэкенд? ","text_text":"А что на питоне в основном делают? Бэкенд?",

# from websocket import create_connection


# ws = create_connection("ws://localhost:8383/Chat")
# print("Sending 'Hello, World'...")
# ws.send("Hello, World")
# print("Sent")
# print("Receiving...")
# while True:
#   result =  ws.recv()
#   print("Received '%s'" % result)

