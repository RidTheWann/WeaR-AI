// Main chat interface for weaR AI
import ChatWindow from '../components/ChatWindow';
import Sidebar from '../components/Sidebar';
import SettingsPanel from '../components/SettingsPanel';

export default function Home() {
  return (
    <div className="flex h-screen bg-gray-100 dark:bg-gray-900">
      <Sidebar />
      <main className="flex-1 flex flex-col">
        <ChatWindow />
        <SettingsPanel />
      </main>
    </div>
  );
}
