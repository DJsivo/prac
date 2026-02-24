from .websocket import websocket_endpoint

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
import htpy as html

app = FastAPI()

THEME = "Логистика и отслеживание отправлений"

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    if "text/html" not in request.headers.get("accept", ""):
        raise HTTPException(status_code=406, detail="Not Acceptable")
    return str(html.html[
        html.head[html.title[THEME]],
        html.body[html.h1[THEME]]
    ])