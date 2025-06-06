import React, { useState, useRef, useEffect } from 'react';
import './App.css';
import ChatMessage from './components/ChatMessage';
import BuddyInfo from './components/BuddyInfo';

function App() {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  // Add a welcome message when the app loads
  useEffect(() => {
    setMessages([
      {
        text: "Yo, what's up? I'm your buddy! Hit me up with whatever's on your mind, and let's chat!",
        sender: 'buddy'
      }
    ]);
  }, []);

  const sendMessage = async (e) => {
    e.preventDefault();
    
    if (input.trim() === '') return;
    
    // Add user message to chat
    const userMessage = { text: input, sender: 'user' };
    setMessages([...messages, userMessage]);
    
    // Clear input field
    setInput('');
    
    // Set loading state
    setLoading(true);
    
    try {
      // Send request to backend
      const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: input }),
      });
      
      const data = await response.json();
      
      // Add buddy's response to chat
      setMessages(prevMessages => [...prevMessages, { text: data.response, sender: 'buddy' }]);
    } catch (error) {
      console.error('Error:', error);
      setMessages(prevMessages => [...prevMessages, { 
        text: "Yo, something's messed up with my brain right now. Can you try again?", 
        sender: 'buddy' 
      }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Your Buddy</h1>
        <p>Chat with your friendly AI buddy!</p>
      </header>
      
      <div className="chat-container">
        <div className="sidebar">
          <BuddyInfo />
        </div>
        
        <div className="chat-box">
          <div className="messages">
            {messages.map((message, index) => (
              <ChatMessage key={index} message={message} />
            ))}
            {loading && <div className="loading-indicator">Buddy is typing...</div>}
            <div ref={messagesEndRef} />
          </div>
          
          <form className="input-form" onSubmit={sendMessage}>
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Type your message here..."
              disabled={loading}
            />
            <button type="submit" disabled={loading || input.trim() === ''}>
              Send
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default App;