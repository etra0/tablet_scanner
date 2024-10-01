from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from time import sleep
import colorsys
import asyncio

app = FastAPI()

COLOR = ""

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open('index.html') as f:
        INDEX = f.read()
    return INDEX

@app.get("/server", response_class=HTMLResponse)
async def read_server():
    with open('server.html') as f:
        INDEX = f.read()
    return INDEX

@app.websocket('/ws/server')
async def websocket_server(ws: WebSocket):
    global COLOR
    await ws.accept()
    while True:
        COLOR = await ws.receive_text()

@app.websocket('/ws/client')
async def websocket_client(ws: WebSocket):
    await ws.accept()
    last_color = ''
    while True:
        if COLOR == last_color:
            await asyncio.sleep(0.1)
        else:
            await ws.send_text(COLOR)
            last_color = COLOR
