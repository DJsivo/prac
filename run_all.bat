@echo off
chcp 65001 >nul
echo Launching microservices...
echo.

start "Root Server" cmd /k ".venv\Scripts\activate && cd root_server && uvicorn app:app --host 127.0.0.1 --port 8000 --reload"
start "WebSocket Server" cmd /k ".venv\Scripts\activate && cd server && uvicorn websocket:app --host 127.0.0.1 --port 8001 --reload"
start "Client Server" cmd /k ".venv\Scripts\activate && cd client && uvicorn main:app --host 127.0.0.1 --port 8002 --reload"

echo.
echo Servers started!
echo Open: http://root.local
echo.
pause