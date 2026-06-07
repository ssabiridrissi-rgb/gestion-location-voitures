const toggleBtn = document.getElementById('chat-toggle');
const openAssistantBtn = document.getElementById('open-assistant');
const chatWindow = document.getElementById('chat-window');
const closeBtn = document.getElementById('chat-close');
const messagesEl = document.getElementById('chat-messages');
const inputEl = document.getElementById('chat-input');
const sendBtn = document.getElementById('chat-send');
const chatIcon = document.getElementById('chat-icon');

let history = [];
let isOpen = false;
let isWaiting = false;

function setChatOpen(nextValue) {
  isOpen = nextValue;
  chatWindow.classList.toggle('hidden', !isOpen);
  chatIcon.textContent = isOpen ? 'X' : 'AI';

  if (isOpen && history.length === 0) {
    startConversation();
  }

  if (isOpen) {
    inputEl.focus();
  }
}

toggleBtn.addEventListener('click', () => {
  setChatOpen(!isOpen);
});

if (openAssistantBtn) {
  openAssistantBtn.addEventListener('click', () => {
    setChatOpen(true);
  });
}

closeBtn.addEventListener('click', () => {
  setChatOpen(false);
});

inputEl.addEventListener('keydown', (event) => {
  if (event.key === 'Enter' && !isWaiting) {
    sendMessage();
  }
});

sendBtn.addEventListener('click', () => {
  if (!isWaiting) {
    sendMessage();
  }
});

function startConversation() {
  appendBotMessage("Bonjour ! Je suis Alex, votre conseiller AutoLoc. Pour vous trouver la voiture idéale, j'ai besoin de quelques infos. Quel est votre budget journalier approximatif (en DH) ?");
}

function sendMessage() {
  const text = inputEl.value.trim();

  if (!text) {
    return;
  }

  appendUserMessage(text);
  history.push({ role: 'user', content: text });
  inputEl.value = '';
  setWaiting(true);

  fetch('/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ messages: history })
  })
    .then((response) => response.json().then((data) => ({ ok: response.ok, data })))
    .then(({ ok, data }) => {
      removeTyping();

      if (!ok || data.error) {
        appendBotMessage(data.error || 'Erreur serveur.');
      } else {
        appendBotMessage(data.response);
        history.push({ role: 'assistant', content: data.response });
      }

      setWaiting(false);
    })
    .catch(() => {
      removeTyping();
      appendBotMessage("Impossible de joindre le serveur. Verifiez que Flask est demarre.");
      setWaiting(false);
    });
}

function appendUserMessage(text) {
  appendMessage(text, 'user');
}

function appendBotMessage(text) {
  appendMessage(text, 'bot');
}

function appendMessage(text, type) {
  const div = document.createElement('div');
  div.className = `msg ${type}`;
  div.textContent = text;
  messagesEl.appendChild(div);
  scrollToBottom();
}

function showTyping() {
  const div = document.createElement('div');
  div.className = 'msg bot typing';
  div.id = 'typing-indicator';
  div.innerHTML = '<span></span><span></span><span></span>';
  messagesEl.appendChild(div);
  scrollToBottom();
}

function removeTyping() {
  const indicator = document.getElementById('typing-indicator');

  if (indicator) {
    indicator.remove();
  }
}

function setWaiting(value) {
  isWaiting = value;
  sendBtn.disabled = value;
  inputEl.disabled = value;

  if (value) {
    showTyping();
  }
}

function scrollToBottom() {
  messagesEl.scrollTop = messagesEl.scrollHeight;
}
