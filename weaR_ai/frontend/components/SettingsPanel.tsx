export default function SettingsPanel() {
  return (
    <div className="p-4 border-t bg-white dark:bg-gray-800">
      <label className="flex items-center">
        <span className="mr-2">Dark Mode</span>
        <input type="checkbox" />
      </label>
      {/* Add more settings here */}
    </div>
  );
}
