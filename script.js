const messageInput = document.getElementById('message-input');
const sendBtn = document.getElementById('send-btn');
const chatForm = document.getElementById('chat-form');

// Add event listener to send button
sendBtn.addEventListener('click', () => {
    const message = messageInput.value;
    if (message.trim() !== '') {
        // Send the message to the server here
        console.log(`Message sent: ${message}`);
        messageInput.value = '';
    }
});

// Simulate receiving a message from the server
function receiveMessage(message) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message');
    messageElement.innerHTML = `<img src="user.jpg" alt="User Image"> ${message}`;
    document.querySelector('.message-container').appendChild(messageElement);
}

// Simulate receiving a new message from the server every 2 seconds
setInterval(() => {
    const message = `New message from user!`;
    receiveMessage(message);
}, 2000);

// Add event listener to form submission
chatForm.addEventListener('submit', (e) => {
    e.preventDefault();
});
