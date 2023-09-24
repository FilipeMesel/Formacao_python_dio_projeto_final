
from typing import Any, Dict, List

import tweepy
from src.secrets import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SCRET
from src.constants import BRAZIL_WOE_ID


def _get_trends(woe_id: int, api: tweepy.API) -> list[Dict[str, Any]]:
    """Getting trending topics

    Args:
        woe_id (int): Identifier of location.

    Returns:
        list[Dict[str, Any]]: Trends list.
    """

    

    trends = api.trends_place(woe_id)
    
    return trends[0]["trends"]


def get_trends_from_mongo() -> list[Dict[str, Any]]:

    trends = trends_collection.find({})
    
    return trends


def save_trends() -> None:

    auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SCRET)

    auth = set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    trends = _get_trends(woe_id = BRAZIL_WOE_ID, api = api)
    trends_collection.insert_many(trends)