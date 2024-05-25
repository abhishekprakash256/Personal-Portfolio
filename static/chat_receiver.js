document.addEventListener("DOMContentLoaded", () => {
    const socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('message', function(msg) {
        const messages = document.getElementById('messages');
        const newMessage = document.createElement('div');
        newMessage.innerHTML = msg;
        messages.appendChild(newMessage);
    });
});
