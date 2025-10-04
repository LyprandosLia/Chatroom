# Cafe Chatroom

A simple **FastAPI chat application** with **WebSockets**, running inside **Docker**.

## Features

- Real-time chat with multiple users
- Show online users (soon to be made)
- Color-coded messages: your messages in blue, others in black (soon to be updated)
- System messages in italic gray (e.g., user connected/disconnected)

## Requirements

- Docker (Docker Desktop for Windows/macOS or Docker Engine for Linux)

## Running with Docker

1. Build the Docker image:

```bash
docker build -t cafe-chat .
```
2. Run the container

```bash
docker run -d -p 8000:8000 cafe-chat
```

3. Open your browser : ``` http://localhost:8000/ ``` to run the project
