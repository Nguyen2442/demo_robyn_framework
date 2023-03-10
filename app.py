from robyn import Robyn, jsonify, Router, WS
from helper import get_item
import json
from model import Fruit
from bson import ObjectId
from celery import Celery
from schemas import FruitPostModel

app = Robyn(__file__)
websocket = WS(app, "/ws")


#-----------celery
celery = Celery(
    "Hello",
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0"
)

@celery.task
def run_hello():
    import time
    for i in range(1, 100):
        time.sleep(2)
        print("Hello", i)
    return


# ---------websocket------------#

websocket_state = 0

@websocket.on("message")
async def message(websocket_id):
    print(websocket_id)
    global websocket_state
    if websocket_state == 0:
        response = "Whaaat??"
    elif websocket_state == 1:
        response = "Whooo??"
    elif websocket_state == 2:
        response = "*chika* *chika* Slim Shady."
    websocket_state = (websocket_state + 1) % 3
    print(response)
    return response


@websocket.on("close")
def close():
    print("GoodBye world, from ws")
    return "GoodBye world, from ws"


@websocket.on("connect")
def connect():
    print("Hello world, from ws ")
    return "Hello world, from ws"



# ------------Middleware---------------#
@app.before_request("/")
async def hello_before_request(request):
    print(100*"hi")
    print("before")
    request["headers"]["before"] = "before_request"
    print(request)
    return request


@app.after_request("/")
def hello_after_request(request):
    print("after")
    print(request)


def custom_middleware(view_func):
    async def middleware(request, *args, **kwargs):
        print(10*"Middleware ")
        return await view_func(request, *args, **kwargs)
    return middleware



@app.get("/")
@custom_middleware
async def hello(request):
    return "Hello, world!"


# ----------- routes -------
@app.get("/fruits")
async def all_fruits(request):
    all_fruits = Fruit.find()
    result = [
        {
            "fruit_id": str(fruit.id),
            "name": fruit.name,
            "create_at": str(fruit.create_at),
            "update_at": str(fruit.update_at)
        }
        async for fruit in all_fruits
    ]
    result_sorted = sorted(result, key=lambda k: k['create_at'])
    return {
        "status_code": 200,
        "type": "json",
        "body": jsonify({
            "message": "Get all fruits successfully!",
            "status": True,
            "fruit": result_sorted
        })
    }



@app.get("/fruit/:id")
async def get_fruit(request):
    fruit_id = request['params']['id']
    existing_fruit = await Fruit.find_one({
        "id": ObjectId(fruit_id)
    })
    if not existing_fruit:
        return {
            "status_code": 404,
            "type": "json",
            "body": jsonify(
                {
                    "message": "Fruit not found!"
                }
            )
        }
    result = {
        "id": str(existing_fruit.id),
        "name": existing_fruit.name
    }
    return {
        "status_code": 200,
        "type": "json",
        "body": jsonify({
            "fruit": result
        })
    }



@app.post("/fruit")
async def add_fruit(input_data):
    request_data = json.loads(bytearray(input_data['body']).decode("utf-8"))
    fruit_data = FruitPostModel(**request_data)
    new_fruit = Fruit(name=fruit_data.name)
    await new_fruit.commit()
    return {
        "status_code": 201,
        "type": "json",
        "body": jsonify(
            {
                "message": "created"
            }
        )
    }


@app.put("/fruit/:id")
async def update_fruit(request):
    id = request["params"]["id"]
    request_body = json.loads(bytearray(request['body']).decode("utf-8"))

    fruit_id = ObjectId(id)
    existing_fruit = await Fruit.find_one({
        "id": ObjectId(fruit_id)
    })
    if not existing_fruit:
        return {
            "status_code": 404,
            "type": "json",
            "body": jsonify(
                {
                    "message": "Fruit not found!"
                }
            )
        }
    existing_fruit.name = request_body.get("name")
    await existing_fruit.commit()
    return {
        "status_code": 200,
        "type": "json",
        "body": jsonify(
            {
                "message": "Updated Fruit successfully!"
            }
        )
    }


@app.delete("/fruit/:id")
async def delete_fruit(request):
    id = request["params"]["id"]

    fruit_id = ObjectId(id)
    existing_fruit = await Fruit.find_one({
        "id": ObjectId(fruit_id)
    })
    if not existing_fruit:
        return {
            "status_code": 404,
            "type": "json",
            "body": jsonify(
                {
                    "message": "Fruit not found!"
                }
            )
        }
    await existing_fruit.delete()
    return {
        "status_code": 200,
        "body": jsonify(
            {
                "message": "Deleted Fruit successfully!"
            }
        ), 
        "type": "json"
    }



# ------- byte response ----- #
@app.get("/binary_output_async")
async def binary_output_async(request):
    return b"OK"


@app.get("/binary_output_response_async")
async def binary_output_response_async(request):
    return Response(
        status_code=200,
        headers={"Content-Type": "application/octet-stream"},
        body="OK",
    )


# ----------- startup/shutdown handler -----------#
async def startup_handler():
    print("Starting up")


@app.shutdown_handler
def shutdown_handler():
    print("Shutting down")




if __name__ == "__main__":
    app.startup_handler(startup_handler)
    app.start(port=8080)
    #run_hello()