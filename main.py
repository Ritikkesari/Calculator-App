from mylib.calculator import *
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/power/{num1}")
async def power_num(num1: int):

    res = power(num1)
    print(res)
    return {"result": res}

@app.get("/add/{num1}/{num2}")
async def add_num(num1: int,num2: int):

    res = add(num1,num2)
    print(res)
    return {"result": res}



if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='127.0.0.1')

