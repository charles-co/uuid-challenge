from fastapi import FastAPI, status
import uuid
import datetime
import pickle

app = FastAPI()

@app.get("/generate-token", status_code=status.HTTP_200_OK)
async def generate_token():
    _uuid = uuid.uuid4()
    timestamp = datetime.datetime.now().isoformat()
    data = {timestamp: str(_uuid)}
    db = None

    try:
        with open("db", "rb") as database:
            db = pickle.load(database)
    except FileNotFoundError:
        print("file hasn't been created yet")

    with open("db", "wb") as database:
        if db:
            update = {**data, **db}
            pickle.dump(update, database)
            data = update
        else:
            pickle.dump(data, database)

    return data
    
