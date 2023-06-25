import time

from fastapi import FastAPI, Header, Request, responses, status

from api.logger import get_logger

logger = get_logger(__name__)

app = FastAPI(
    title='Hoot',
    description='Generate random numbers based on Unix Epoch'   
)

@app.get(f'/{app.title.lower()}/unix')
async def get_unix():
    unix_time = int(time.time())
    message =  f'Hoot! Hoot! You called the get_unix function! Your unix time is {unix_time}. Hoot Hoot!'
    logger.info(message)
    return responses.JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'message': message
        }
    )

@app.get(f'/{app.title.lower()}/scheduled')
async def get_unix_scheduled():
     unix_time = int(time.time())
     message = f'Hoot! Hoot!  You called the get_unix_scheduled function! Your unix time is {unix_time}! Hoot! Hoot!'
     logger.info(message)
     return responses.JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'message': message 
        }
    )