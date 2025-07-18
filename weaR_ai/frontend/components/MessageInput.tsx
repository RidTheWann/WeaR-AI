import { useState } from 'react';

export default function MessageInput({ onSend, loading }: { onSend: (msg: string) => void, loading: boolean }) {
  const [value, setValue] = useState('');
  return (
    <form
      className="flex mt-2"
      onSubmit={e => {
        e.preventDefault();
        if (value.trim()) {
          onSend(value);
          setValue('');
        }
      }}
    >
      <input
        className="flex-1 px-3 py-2 rounded-l border"
        value={value}
        onChange={e => setValue(e.target.value)}
        placeholder="Type your message..."
        aria-label="Type your message"
        disabled={loading}
      />
      <button className="px-4 py-2 bg-blue-600 text-white rounded-r" type="submit" disabled={loading}>
        {loading ? '...' : 'Send'}
      </button>
    </form>
  );
}
