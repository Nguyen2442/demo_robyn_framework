from typing import List, Optional
from robyn import Robyn, jsonify
import json

import dataclasses
import strawberry
import strawberry.utils.graphiql


@strawberry.type
class User:
    name: str


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> Optional[User]:
        return User(name="Hello")


schema = strawberry.Schema(Query)

app = Robyn(__file__)


@app.get("/")
async def get():
    return strawberry.utils.graphiql.get_graphiql_html()


@app.post("/")
async def post(request):
    body = json.loads(bytearray(request["body"]).decode("utf-8"))
    query = body["query"]
    variables = body.get("variables", None)
    context_value = {"request": request}
    root_value = body.get("root_value", None)
    operation_name = body.get("operation_name", None)

    data = await schema.execute(
        query,
        variables,
        context_value,
        root_value,
        operation_name,
    )

    return jsonify(
        {
            "data": (data.data),
            **({"errors": data.errors} if data.errors else {}),
            **({"extensions": data.extensions} if data.extensions else {}),
        }
    )


if __name__ == "__main__":
    app.start()
