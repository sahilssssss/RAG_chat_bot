import { useState } from 'react'
import axios from 'axios'
import ChatWindow from './WhatsAppChat'

function App() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')

  const sendMessage = async (message) => {
    if (!message.trim()) return;
    
    // Add user message immediately
    const updatedMessages = [...messages, { sender: 'user', text: message }];
    setMessages(updatedMessages);
    setInput(''); // Clear input right away
    
    try {
      const res = await axios.post('https://rag-chat-bot-1-3yoa.onrender.com/ask', 
        new URLSearchParams({ query: message }));
      
      // Add bot response
      setMessages([...updatedMessages, { sender: 'bot', text: res.data.answer }]);
    } catch (error) {
      console.error('Error sending message:', error);
      // Add error message
      setMessages([...updatedMessages, { 
        sender: 'bot', 
        text: 'Sorry, I encountered an error. Please try again.' 
      }]);
    }
  }

  return (
    <div className="app-container">
      <ChatWindow 
        messages={messages}
        input={input}
        setInput={setInput}
        sendMessage={sendMessage}
      />
    </div>
  )
}

export default App
