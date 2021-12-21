from fastapi import FastAPI, Request
from app.AreaCalculator import calculate_area_acres

app = FastAPI()

'''
A function to get the request using fast-api and 
return the calculated area in acres.
'''
@app.get('/')
async def get_input(request:Request):

    packet = await request.json()
    length = packet['length']
    width = packet['width']
    area = calculate_area_acres(length, width)
    return area 

