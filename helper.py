

def get_item(id: int, db: list):
    fruit = {}
    for dic in db:
        for val in dic.values():
            if val == id:
                fruit = dic
    return fruit

                


