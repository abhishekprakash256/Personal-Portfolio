document.addEventListener("DOMContentLoaded", () => {
    const socket = io.connect('http://' + document.domain + ':' + location.port);
    console.log('Connected to WebSocket');

    socket.on('message', function(msg) {
        console.log('Received message:', msg);
        const messages = document.getElementById('messages');
        const newMessage = document.createElement('div');
        newMessage.classList.add('message-box', 'message-received'); // Add the custom class for received messages
        newMessage.innerHTML = msg;
        messages.appendChild(newMessage);
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
        addSentMessage(message); // Add sent message to the UI
        socket.emit('message', message); // Send message to the server
        messageInput.value = '';
    }
}

function addSentMessage(message) {
    const messages = document.getElementById('messages');
    const newMessage = document.createElement('div');
    newMessage.classList.add('message-box', 'message-sent'); // Add the custom class for sent messages
    newMessage.innerHTML = message;
    messages.appendChild(newMessage);
    messages.scrollTop = messages.scrollHeight;
}