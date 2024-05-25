document.addEventListener("DOMContentLoaded", () => {
    const socket = io.connect('http://' + document.domain + ':' + location.port);
    console.log('Connected to WebSocket');

    socket.on('message', function(msg) {
        console.log('Received message:', msg);
        const messages = document.getElementById('messages');
        const newMessage = document.createElement('div');
        newMessage.innerHTML = msg;
        messages.appendChild(newMessage);
        messages.scrollTop = messages.scrollHeight;
    });

    document.getElementById('messageInput').addEventListener('keyup', function(event) {
        if (event.key === 'Enter') {
            sendMessage(socket);
        }
    });

    document.querySelector('button').addEventListener('click', function() {
        sendMessage(socket);
    });
});

function sendMessage(socket) {
    const messageInput = document.getElementById('messageInput');
    const message = messageInput.value;
    if (message !== "") {
        console.log('Sending message:', message);
        socket.send(message);
        messageInput.value = '';
    }
}
