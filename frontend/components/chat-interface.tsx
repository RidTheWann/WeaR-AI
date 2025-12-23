"use client";

import { useState, useRef, useEffect, FormEvent } from "react";
import { Send, Loader2, Bot, User, Sparkles, RefreshCw } from "lucide-react";
import MessageBubble from "./message-bubble";
import ToolIndicator from "./tool-indicator";

interface Message {
    id: string;
    role: "user" | "assistant";
    content: string;
    thinking?: boolean;
    tools?: { name: string; status: "running" | "done" }[];
}

export default function ChatInterface() {
    const [messages, setMessages] = useState<Message[]>([]);
    const [input, setInput] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const messagesEndRef = useRef<HTMLDivElement>(null);
    const inputRef = useRef<HTMLTextAreaElement>(null);

    // Auto-scroll to bottom
    useEffect(() => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    }, [messages]);

    // Auto-resize textarea
    useEffect(() => {
        if (inputRef.current) {
            inputRef.current.style.height = "auto";
            inputRef.current.style.height = `${Math.min(inputRef.current.scrollHeight, 200)}px`;
        }
    }, [input]);

    const handleSubmit = async (e: FormEvent) => {
        e.preventDefault();
        if (!input.trim() || isLoading) return;

        const userMessage: Message = {
            id: Date.now().toString(),
            role: "user",
            content: input.trim(),
        };

        setMessages((prev) => [...prev, userMessage]);
        setInput("");
        setIsLoading(true);

        // Add thinking placeholder
        const thinkingId = (Date.now() + 1).toString();
        setMessages((prev) => [
            ...prev,
            { id: thinkingId, role: "assistant", content: "", thinking: true },
        ]);

        try {
            // Call the local AI API (non-streaming)
            const response = await fetch("http://localhost:8000/api/v1/chat/local", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: input.trim() }),
            });

            if (!response.ok) throw new Error("Failed to get response");

            const data = await response.json();

            // Update the message with the response
            setMessages((prev) =>
                prev.map((m) =>
                    m.id === thinkingId
                        ? { ...m, content: data.response || "No response received", thinking: false }
                        : m
                )
            );
        } catch (error) {
            console.error("Chat error:", error);
            setMessages((prev) =>
                prev.map((m) =>
                    m.id === thinkingId
                        ? {
                            ...m,
                            content: "Maaf, terjadi error. Pastikan backend berjalan di http://localhost:8000",
                            thinking: false,
                        }
                        : m
                )
            );
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="flex flex-1 flex-col overflow-hidden">
            {/* Messages Area */}
            <div className="flex-1 overflow-y-auto custom-scrollbar">
                {messages.length === 0 ? (
                    <WelcomeScreen onExampleClick={setInput} />
                ) : (
                    <div className="max-w-3xl mx-auto py-8 px-4 space-y-6">
                        {messages.map((message) => (
                            <MessageBubble key={message.id} message={message} />
                        ))}
                        <div ref={messagesEndRef} />
                    </div>
                )}
            </div>

            {/* Input Area */}
            <div className="border-t border-white/10 p-4 bg-gradient-to-t from-slate-950 to-transparent">
                <form onSubmit={handleSubmit} className="max-w-3xl mx-auto">
                    <div className="relative flex items-end gap-2 p-2 rounded-2xl glass border border-white/10 focus-within:border-brand-500/50 focus-within:shadow-glow transition-all">
                        <textarea
                            ref={inputRef}
                            value={input}
                            onChange={(e) => setInput(e.target.value)}
                            onKeyDown={(e) => {
                                if (e.key === "Enter" && !e.shiftKey) {
                                    e.preventDefault();
                                    handleSubmit(e);
                                }
                            }}
                            placeholder="Message WeaR Ai..."
                            rows={1}
                            className="flex-1 bg-transparent resize-none px-4 py-3 text-foreground placeholder:text-muted-foreground focus:outline-none max-h-[200px]"
                            disabled={isLoading}
                        />
                        <button
                            type="submit"
                            disabled={!input.trim() || isLoading}
                            className="flex-shrink-0 p-3 rounded-xl bg-brand-600 hover:bg-brand-500 disabled:opacity-50 disabled:hover:bg-brand-600 text-white transition-all hover:shadow-glow focus-ring"
                        >
                            {isLoading ? (
                                <Loader2 className="h-5 w-5 animate-spin" />
                            ) : (
                                <Send className="h-5 w-5" />
                            )}
                        </button>
                    </div>
                    <p className="text-xs text-center text-muted-foreground mt-3">
                        WeaR Ai can make mistakes. Consider checking important information.
                    </p>
                </form>
            </div>
        </div>
    );
}

function WelcomeScreen({ onExampleClick }: { onExampleClick: (text: string) => void }) {
    const examples = [
        {
            title: "Explain quantum computing",
            subtitle: "in simple terms anyone can understand",
        },
        {
            title: "Write a Python function",
            subtitle: "to find the nth Fibonacci number",
        },
        {
            title: "Search the web for",
            subtitle: "the latest AI research news",
        },
        {
            title: "Help me brainstorm",
            subtitle: "startup ideas for 2025",
        },
    ];

    return (
        <div className="flex flex-col items-center justify-center min-h-full py-12 px-4">
            <div className="flex items-center gap-4 mb-8">
                <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-gradient-to-br from-brand-500 to-brand-600 shadow-glow-lg animate-pulse-soft">
                    <Sparkles className="h-8 w-8 text-white" />
                </div>
            </div>

            <h2 className="text-3xl font-bold text-center mb-2 gradient-text">
                Welcome to WeaR Ai
            </h2>
            <p className="text-muted-foreground text-center mb-12 max-w-md">
                Your open-source AGI assistant. I can search the web, run code, analyze files, and help you with complex tasks.
            </p>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 w-full max-w-2xl">
                {examples.map((example, i) => (
                    <button
                        key={i}
                        onClick={() => onExampleClick(`${example.title} ${example.subtitle}`)}
                        className="group p-4 rounded-xl glass border border-white/10 hover:border-brand-500/50 text-left transition-all hover:shadow-glow animate-fade-in"
                        style={{ animationDelay: `${i * 100}ms` }}
                    >
                        <p className="font-medium text-foreground group-hover:text-brand-400 transition-colors">
                            {example.title}
                        </p>
                        <p className="text-sm text-muted-foreground">{example.subtitle}</p>
                    </button>
                ))}
            </div>
        </div>
    );
}
