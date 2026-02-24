from fastapi import WebSocket, WebSocketDisconnect
import asyncio
import random

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    received_messages = set()

    async def send_periodic():
        while True:
            await asyncio.sleep(random.uniform(2, 5))
            if random.random() < 0.65:
                await websocket.send_text("Это лучшая тема, что есть. Хотя…")
            else:
                await websocket.send_text("Надо менять тему…")

    async def receive_and_respond():
        while True:
            data = await websocket.receive_text()
            if data not in received_messages:
                received_messages.add(data)
                await websocket.send_text("Да? Хорошо. Спасибо за поддержку!")

    #конкурентно
    sender_task = asyncio.create_task(send_periodic())
    receiver_task = asyncio.create_task(receive_and_respond())

    try:
        await asyncio.gather(sender_task, receiver_task)
    except WebSocketDisconnect:
        #отключился – отменяем задачи
        sender_task.cancel()
        receiver_task.cancel()
    except Exception:
        #другие ошибки – тоже отмена
        sender_task.cancel()
        receiver_task.cancel()
        raise
    finally:
        await websocket.close()