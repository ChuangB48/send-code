import asyncio
import websockets

# 定義 WebSocket 連接處理函數
async def handler(websocket):
    print("Client connected")

    # 傳送一個歡迎訊息給前端
    await websocket.send("Hello, Client!")

    while True:
        try:
            # 等待接收來自客戶端的訊息
            message = await websocket.recv()
            print(f"Received message: {message}")
            
            # 回應訊息
            await websocket.send(f"Server received: {message}")
        except websockets.exceptions.ConnectionClosed:
            print("Connection closed")
            break

# 設置 WebSocket 伺服器
async def main():
    start_server = await websockets.serve(handler, "localhost", 8080)
    print("Server running on ws://localhost:8080")
    await start_server.wait_closed()

# 使用 asyncio.run 啟動事件循環
asyncio.run(main())