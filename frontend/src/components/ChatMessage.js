import React from 'react';

const ChatMessage = ({ message }) => {
  return (
    <div className={`message ${message.sender}`}>
      {message.text}
    </div>
  );
};

export default ChatMessage;