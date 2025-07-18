import { useState } from 'react';
import MessageInput from './MessageInput';

export default function ChatWindow() {
  const [messages, setMessages] = useState<{role: string, content: string}[]>([
    { role: 'assistant', content: 'Welcome to weaR AI!' }
  ]);
  const [loading, setLoading] = useState(false);

  const handleSend = async (msg: string) => {
    setMessages([...messages, { role: 'user', content: msg }]);
    setLoading(true);
    try {
      const res = await fetch('http://localhost:8000/v1/chat/completions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer my-secret-token'
        },
        body: JSON.stringify({ messages: [msg], stream: false })
      });
      const data = await res.json();
      setMessages(m => [...m, { role: 'assistant', content: data.choices[0].message }]);
    } catch (e) {
      setMessages(m => [...m, { role: 'assistant', content: 'Error connecting to API' }]);
    }
    setLoading(false);
  };

  return (
    <div className="flex flex-col h-full p-4 overflow-y-auto">
      {messages.map((m, i) => (
        <div key={i} className={`mb-2 ${m.role === 'user' ? 'text-right' : 'text-left'}`}>
          <span className={`inline-block px-4 py-2 rounded ${m.role === 'user' ? 'bg-blue-500 text-white' : 'bg-gray-200 dark:bg-gray-700 dark:text-white'}`}>{m.content}</span>
        </div>
      ))}
      <MessageInput onSend={handleSend} loading={loading} />
    </div>
  );
}
