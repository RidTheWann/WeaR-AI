"use client";

import { useState } from "react";
import ChatInterface from "@/components/chat-interface";
import { Sparkles, Github, Menu } from "lucide-react";

export default function Home() {
    const [sidebarOpen, setSidebarOpen] = useState(false);

    return (
        <div className="flex h-screen overflow-hidden">
            {/* Sidebar */}
            <aside
                className={`${sidebarOpen ? "translate-x-0" : "-translate-x-full"
                    } fixed inset-y-0 left-0 z-50 w-72 glass border-r border-white/10 transition-transform duration-300 lg:translate-x-0 lg:static`}
            >
                <div className="flex h-full flex-col">
                    {/* Logo */}
                    <div className="flex items-center gap-3 p-6 border-b border-white/10">
                        <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-gradient-to-br from-brand-500 to-brand-600 shadow-glow">
                            <Sparkles className="h-5 w-5 text-white" />
                        </div>
                        <div>
                            <h1 className="text-xl font-bold gradient-text">WeaR Ai</h1>
                            <p className="text-xs text-muted-foreground">AGI Assistant</p>
                        </div>
                    </div>

                    {/* New Chat Button */}
                    <div className="p-4">
                        <button className="w-full flex items-center gap-2 px-4 py-3 rounded-xl bg-brand-600 hover:bg-brand-500 text-white font-medium transition-all hover:shadow-glow focus-ring">
                            <span className="text-lg">+</span>
                            New Chat
                        </button>
                    </div>

                    {/* Chat History */}
                    <div className="flex-1 overflow-y-auto custom-scrollbar p-4 space-y-2">
                        <p className="text-xs font-medium text-muted-foreground uppercase tracking-wider mb-3">
                            Recent Chats
                        </p>
                        {/* Placeholder chat items */}
                        {["Research on quantum computing", "Python code review", "Travel planning ideas"].map(
                            (title, i) => (
                                <button
                                    key={i}
                                    className="w-full text-left px-4 py-3 rounded-xl hover:bg-white/5 text-sm text-muted-foreground hover:text-foreground transition-colors truncate"
                                >
                                    {title}
                                </button>
                            )
                        )}
                    </div>

                    {/* Footer */}
                    <div className="p-4 border-t border-white/10">
                        <a
                            href="https://github.com/RidTheWann/WeaR-AI"
                            target="_blank"
                            rel="noopener noreferrer"
                            className="flex items-center gap-2 px-4 py-2 rounded-lg hover:bg-white/5 text-sm text-muted-foreground hover:text-foreground transition-colors"
                        >
                            <Github className="h-4 w-4" />
                            View on GitHub
                        </a>
                    </div>
                </div>
            </aside>

            {/* Main Content */}
            <div className="flex flex-1 flex-col overflow-hidden">
                {/* Mobile Header */}
                <header className="flex items-center gap-4 p-4 border-b border-white/10 lg:hidden">
                    <button
                        onClick={() => setSidebarOpen(!sidebarOpen)}
                        className="p-2 rounded-lg hover:bg-white/5"
                    >
                        <Menu className="h-5 w-5" />
                    </button>
                    <div className="flex items-center gap-2">
                        <Sparkles className="h-5 w-5 text-brand-500" />
                        <span className="font-semibold">WeaR Ai</span>
                    </div>
                </header>

                {/* Chat Interface */}
                <ChatInterface />
            </div>

            {/* Mobile Overlay */}
            {sidebarOpen && (
                <div
                    className="fixed inset-0 z-40 bg-black/50 lg:hidden"
                    onClick={() => setSidebarOpen(false)}
                />
            )}
        </div>
    );
}
