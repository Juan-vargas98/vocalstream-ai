from fastapi import FastAPI, WebSocket
import asyncio

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "VocalStream AI Backend Running"}

@app.websocket("/ws/audio")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Aquí recibiremos los datos de audio del micrófono
            data = await websocket.receive_bytes()
            # Por ahora, devolvemos un mensaje de confirmación asíncrono
            await websocket.send_json({"status": "audio_received", "bytes": len(data)})
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await websocket.close()