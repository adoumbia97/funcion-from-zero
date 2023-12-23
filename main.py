from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from mylib.bot import scrape

class Story(BaseModel):
    text: str


app=FastAPI()

class Wiki(BaseModel):
    name: str

@app.post("/wiki")
async def predict_story(wiki: Wiki):
    result=scrape(wiki.name)
    payload={"wikipage": result}
    json_compatible_item_data=jsonable_encoder(payload)
    return JSONResponse(content=json_compatible_item_data)

@app.get('/')
async def root():
    return {'messsage': "Hello functions"}



if __name__ == '__main__':
    uvicorn.run(app, port=8080, host="0.0.0.0")

