document.addEventListener("DOMContentLoaded", () => {
    const socket = io.connect('http://' + document.domain + ':' + location.port);
    console.log('Connected to WebSocket');

    socket.on('message', function(msg) {
        console.log('Received message:', msg);
        const messages = document.getElementById('messages');
        const messageWrapper = document.createElement('div');
        messageWrapper.classList.add('message-wrapper');
        const newMessage = document.createElement('div');
        newMessage.classList.add('message-box', 'message-received');
        newMessage.innerHTML = msg;
        messageWrapper.appendChild(newMessage);
        messages.appendChild(messageWrapper);
        messages.scrollTop = messages.scrollHeight;
    });

    document.getElementById('messageInput').addEventListener('keyup', function(event) {
        if (event.key === 'Enter') {
            sendMessage(socket);
        }
    });

    document.getElementById('sendbutton').addEventListener('click', function() {
        sendMessage(socket);
    });
});

function sendMessage(socket) {
    const messageInput = document.getElementById('messageInput');
    const message = messageInput.value;
    if (message !== "") {
        console.log('Sending message:', message);
        addSentMessage(message);
        socket.emit('message', message);
        messageInput.value = '';
    }
}

function addSentMessage(message) {
    const messages = document.getElementById('messages');
    const messageWrapper = document.createElement('div');
    messageWrapper.classList.add('message-wrapper', 'sent');
    const newMessage = document.createElement('div');
    newMessage.classList.add('message-box', 'message-sent');
    newMessage.innerHTML = message;
    messageWrapper.appendChild(newMessage);
    messages.appendChild(messageWrapper);
    messages.scrollTop = messages.scrollHeight;
}
