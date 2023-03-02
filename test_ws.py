from websocket import create_connection

BASE_URL = "ws://127.0.0.1:8080"


def test_web_socket(session):
    ws = create_connection(f"{BASE_URL}/ws")
    assert ws.recv() == "Hello world, from ws"
    ws.send("My name is?")
    assert ws.recv() == "Whaaat??"
    ws.send("My name is?")
    assert ws.recv() == "Whooo??"
    ws.send("My name is?")
    assert ws.recv() == "*chika* *chika* Slim Shady."
    # print(ws.recv())
    print("okkkkkkkkkkk")
    return "ok"


test_web_socket("message")