from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Entrees - REST API")


@app.get("/")
async def root():
    return JSONResponse({"msg": "Hello ROOT!"})
