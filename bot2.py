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
            js = json.loads(message)
            text = js.get('text_text')
            username = js.get('user')
            user_id = js.get('user_id')
            site = js.get('site_cut')
            try:
                text = text.strip().split()
                if len(text) >= 1:
                    command = text[0]
                    if command == '!move':
                        if len(text) == 3:
                            start = text[1]
                            finish = text[2]
                            q.put_nowait([start, finish, username, site])
                            print(f'{username} с {site} походил {start} {finish}')
            except:
                pass
            time.sleep(1)


q = queue.Queue()
players = queue.Queue()


try:
    t1 = Thread(target=hello, args=(q, ))
    t2 = Thread(target=main, args=(q, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
except:
    pass



