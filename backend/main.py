import uvicorn

# app(folder name).api(file name):app(what we called FastAPI in api.py)
# "reload=True" reloads for very change since its one page web app
if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)