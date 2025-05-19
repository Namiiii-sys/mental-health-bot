const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");
const suggestions = document.querySelectorAll(".suggestions button");

sendBtn.onclick = sendMessage;
suggestions.forEach(btn => btn.onclick = () => {
  userInput.value = btn.textContent;
  sendMessage();
});


function appendMessage(content, sender) {
  const msg = document.createElement("div");
  msg.className = "message " + sender;
  msg.innerHTML =  marked.parse(content);
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function sendMessage() {
  const message = userInput.value.trim();
  if (!message) return;
  
  appendMessage(message, "user");
  userInput.value = "";

  appendMessage("Typing...", "bot");

  fetch("/api/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  })
  .then(res => res.json())
  .then(data => {
    chatBox.lastChild.remove(); // remove "Typing..."
    appendMessage(data.response, "bot");
  })
  .catch(err => {
    chatBox.lastChild.remove();
    appendMessage("Sorry, something went wrong 💔", "bot");
  });
}
