async function send() {
    const message = document.getElementById("userInput").value;

    const response = await fetch("https://your-flask-backend-url/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    });

    const data = await response.json();
    document.getElementById("responseBox").innerText = data.response;
}
