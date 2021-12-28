from fastapi import FastAPI, Request
import uvicorn

from app.bmiCalc import calculate_bmi


'''
A function to get the request using fast-api and 
return the calculated bmi.
'''
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/bmi")
async def get_input(request:Request):
    packet = await request.json()
    weight = packet['weight']
    height = packet['height']
    bmi = calculate_bmi(weight, height)
    return  {"BMI:": bmi}