import React, { useEffect, useRef, useState } from 'react';
import './ChatWindow.css';

const ChatWindow = ({ messages = [], input, setInput, sendMessage }) => {
  const chatBodyRef = useRef(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleSend = async () => {
    if (input.trim() !== '') {
      setIsLoading(true);
      await sendMessage(input);
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      handleSend();
    }
  };

  // Auto-scroll to bottom when new messages arrive or loading state changes
  useEffect(() => {
    if (chatBodyRef.current) {
      chatBodyRef.current.scrollTop = chatBodyRef.current.scrollHeight;
    }
  }, [messages, isLoading]);

  // Generate timestamp for messages
  const getTimeStamp = () => {
    return new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  };

  return (
    <div className="whatsapp-chat-window">
      {/* Header */}
      <div className="chat-header">
        <div className="header-user">
          <div className="avatar">A</div>
          <div className="user-info">
            <div className="user-name">RAG Support ChatBot</div>
            <div className="user-status">Online</div>
          </div>
        </div>
        <button className="close-button">X</button>
      </div>

      {/* Chat body */}
      <div ref={chatBodyRef} className="chat-body">
        {messages.length === 0 && (
          <div className="welcome-message bot-message">
            <div className="message-text">Hello! How can I help you today?</div>
            <div className="message-time">{getTimeStamp()}</div>
          </div>
        )}
        
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`chat-message ${msg.sender === 'user' ? 'user-message' : 'bot-message'}`}
          >
            <div className="message-text">{msg.text}</div>
            <div className="message-time">{getTimeStamp()}</div>
          </div>
        ))}

        {/* Typing indicator when loading */}
        {isLoading && (
          <div className="typing-indicator">
            <div className="typing-dot"></div>
            <div className="typing-dot"></div>
            <div className="typing-dot"></div>
          </div>
        )}
      </div>

      {/* Input area */}
      <div className="chat-input-container">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={handleKeyPress}
          className="chat-input"
          placeholder="Type a message..."
          disabled={isLoading}
        />
        <button 
          onClick={handleSend}
          disabled={!input.trim() || isLoading}
          className={`send-button ${(!input.trim() || isLoading) ? 'disabled' : ''}`}
        >
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <line x1="22" y1="2" x2="11" y2="13"></line>
            <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
          </svg>
        </button>
      </div>
    </div>
  );
};

export default ChatWindow;