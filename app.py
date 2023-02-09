from robyn import Robyn, jsonify, static_file, Router
from helper import get_item
import json


app = Robyn(__file__)


fake_fruit_database = [
    {"id":1, "fruit":"Apple"},
    {"id":2, "fruit":"Orange"},
    {"id":3, "fruit":"Pineapple"}
]


@app.get("/")
async def hello(request):
    
    return "Hello, world!"

@app.get("/index")
async def get_page(request):
    return static_file("./index.html")

@app.get("/fruits")
def all_fruits(request):
    return jsonify(fake_fruit_database)



@app.get("/fruit/:id")
def get_fruit(request):
    id = request['params']['id']
    fruit_id = int(id)
    

    fruit = get_item(fruit_id, fake_fruit_database)

    if fruit == {}:
        return {"status_code":404,"body":"Fruit not Found", "type": "text"}
    else:    
        return jsonify(fruit)



@app.post("/fruit")
def add_fruit(request):
    
    body = bytearray(request['body']).decode("utf-8")

    fruit = json.loads(body)
   

    new_id = fake_fruit_database[-1]['id'] + 1
    
    fruit_dict = {"id":new_id, "fruit":fruit['fruit']}
    
    fake_fruit_database.append(fruit_dict)
    return {"status_code":201, "body":jsonify(fruit_dict), "type": "json"}



@app.put("/fruit/:id")
def update_fruit(request):
    id = request["params"]["id"]
    body = bytearray(request['body']).decode("utf-8")
    fruit = json.loads(body)

    fruit_id = int(id)
    fruit_dict = get_item(fruit_id,fake_fruit_database)

    if fruit_dict == {}:
        return {"status_code":404,"body":"Fruit not Found", "type": "text"}
    else:    
        fruit_dict['fruit'] = fruit['fruit']
        return jsonify(fruit)
    


@app.delete("/fruit/:id")
def delete_fruit(request):
    id = request["params"]["id"]
    
    fruit_id = int(id)
    fruit_dict = get_item(fruit_id,fake_fruit_database)

    if fruit_dict == {}:
        return {"status_code":404,"body":"Fruit not Found", "type": "text"}
    else:    
        fake_fruit_database.remove(fruit_dict)
        return jsonify({"Message":"Fruit was deleted"})


app.start()
