
import unicorn
from fastapi import FastAPI

#import tweepy

from src.services import get_trends_from_mongo, save_trends

from src.responses import TrendItem

from src.connection import trends_collection


app = FastAPI()

@app.get("/trends", response_model=List[TrendItem])
def get_trends_route():
    
    return get_trends_from_mongo()


if __main__ = "__main__":

    trends = get_trends_from_mongo()

    if not trends:
        save_trends()

    unicorn.run(app, host="0.0.0.0", port=8080)