document.addEventListener("DOMContentLoaded", () => {
    const socket = io.connect('https://' + document.domain + ':' + location.port);

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
        socket.send(message);
        messageInput.value = '';
    }
}
