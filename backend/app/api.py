from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# automated documentation-- localhost:xxxx/docs
app = FastAPI()

origins = [
   "http://localhost:5173",
   "localhost:5173"
]

# allows software to function beyond what it's capable of
# ig in this case communication with web server?
# eg using requests from different IP / protocol / address / domain etc
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# get method and its return methods with JSON body
# tags is for documentation
# "/" decorator adds/changes functionality 
@app.get("/", tags=["root"])
async def read_root() -> dict:
    #JSON
    return {"message": "Todo List App return message"}