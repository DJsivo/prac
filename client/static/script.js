document.addEventListener("DOMContentLoaded", () => {
    const ws = new WebSocket("ws://ws.local/ws");
    const status = document.getElementById("status");
    const message = document.getElementById("message");
    const button = document.getElementById("button");

    function disableConnection() {
        status.textContent = "Соединение потеряно";
        button.disabled = true;
    }

    ws.onopen = () => {
        status.textContent = "Соединение установлено";
        button.disabled = false;
    };

    ws.onmessage = (event) => {
        message.textContent = event.data;
    };

    ws.onclose = () => {
        disableConnection();
    };

    ws.onerror = () => {
        disableConnection();
    };

    button.onclick = () => {
        // Отправляем уникальное сообщение (метка времени + случайное число)
        ws.send(`${Date.now()}-${Math.random()}`);
    };
});