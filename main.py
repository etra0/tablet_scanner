from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from time import sleep
import colorsys
import asyncio

app = FastAPI()

COLOR_QUEUE = asyncio.Queue()

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
    await ws.accept()
    while True:
        color = await ws.receive_text()
        await COLOR_QUEUE.put(color)

@app.websocket('/ws/client')
async def websocket_client(ws: WebSocket):
    await ws.accept()
    while True:
        new_color = await COLOR_QUEUE.get()
        await ws.send_text(new_color)
