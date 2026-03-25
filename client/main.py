from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import htpy as html

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

THEME = "\"Логистика и отслеживание отправлений\""

@app.get("/", response_class=HTMLResponse)
async def client_page():
    return str(html.html[
        html.head[
            html.title[f"Была выбрана тема {THEME}"],
            html.script(src="/static/script.js", defer=True),
            html.link(rel="stylesheet", href="/static/style.css")
        ],
        html.body[
            html.h1[f"Была выбрана тема {THEME}"],
            html.h2(id="status"),
            html.p(id="message"),
            html.button(id="button", disabled=True)["Классная тема!"]
        ]
    ])
