let socket;

document.addEventListener("DOMContentLoaded", () => {
    if (!socket) {
        //socket = io.connect('http://' + document.domain + ':' + location.port);
        socket = io.connect('https://' + document.domain + ':' + location.port);
        console.log('Connected to WebSocket');

        socket.on('message', function(msg) {
            console.log('Received message:', msg);
            addReceivedMessage(msg);
        });
    } else {
        console.log('Socket already connected');
    }

    document.getElementById('messageInput').addEventListener('keyup', function(event) {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });

    document.getElementById('sendbutton').addEventListener('click', function() {
        sendMessage();
    });
});

function sendMessage() {
    const messageInput = document.getElementById('messageInput');
    const message = messageInput.value;
    if (message !== "") {
        console.log('Sending message:', message);
        addSentMessage(message);
        socket.emit('message', message);
        messageInput.value = '';
    }
}

function addReceivedMessage(message) {
    const messages = document.getElementById('messages');
    const messageWrapper = document.createElement('div');
    messageWrapper.classList.add('message-wrapper');
    const newMessage = document.createElement('div');
    newMessage.classList.add('message-box', 'message-received');
    newMessage.innerHTML = message;
    messageWrapper.appendChild(newMessage);
    messages.appendChild(messageWrapper);
    messages.scrollTop = messages.scrollHeight;
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