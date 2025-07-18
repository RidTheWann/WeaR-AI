export default function Sidebar() {
  return (
    <aside className="w-64 bg-white dark:bg-gray-800 border-r p-4">
      <h2 className="font-bold mb-4">Conversations</h2>
      {/* List of conversations */}
      <ul>
        <li className="mb-2">Chat 1</li>
        <li className="mb-2">Chat 2</li>
      </ul>
    </aside>
  );
}
