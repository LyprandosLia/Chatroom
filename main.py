from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List


app = FastAPI()

#ConnectionManager -> class that handles the connections
class ConnectionManager:
    def __init__(self):
        #
        self.active_connections: List[WebSocket] = []
    #function that adds a new connection to the WebSocket List (appends the list with the new connection)
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    #function that removes an already existed connection (removes it from the list)
    async def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
    
    #function of broadcasting the messages betweeen connections
    async def broadcast(self, message: str):
        disconnected = []
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except Exception:
                disconnected.append(connection)

        for conn in disconnected:
            self.disconnect(conn)

#creating the connection manager
manager = ConnectionManager()

#accepting connection from ws//localhost:8000/ws 
@app.websocket("/ws")

#this function runs each time a new user is connected
async def websocket_endpoint(websocket : WebSocket):
    #connecting and keeping the connection to the websockets list so we know who is online and whos not
    await manager.connect(websocket)
    try:

        await websocket.send_text("Type your username")
        username = await websocket.receive_text()
        await manager.broadcast(f"{username} connected")
        #while there are messages
        while True:
            #accepting  the message
            data= await websocket.receive_text()
            #broadcasting it to the connected users
            await manager.broadcast(f"{username} : {data}")
    #works for disconnects and informing the online users that one user has left
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"{username} disconnected")

