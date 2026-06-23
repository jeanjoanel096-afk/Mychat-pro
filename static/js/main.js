// Chat Socket.io
const socket = io();

function sendMsg() {
    const msg = document.getElementById('msgInput').value;
    socket.emit('send_message', { sender: "John", message: msg });
}

// Video Reward Timer (Sistèm 30 segond)
function watchAd() {
    let timeLeft = 30;
    const btn = document.getElementById('adBtn');
    btn.disabled = true;
    
    let timer = setInterval(() => {
        btn.innerText = timeLeft + "s";
        timeLeft--;
        if(timeLeft < 0) {
            clearInterval(timer);
            btn.innerText = "Jwenn 25 Pwen";
            btn.disabled = false;
        }
    }, 1000);
}
