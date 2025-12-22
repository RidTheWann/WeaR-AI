"use client";

import { Bot, User, Sparkles } from "lucide-react";

interface Message {
    id: string;
    role: "user" | "assistant";
    content: string;
    thinking?: boolean;
    tools?: { name: string; status: "running" | "done" }[];
}

interface MessageBubbleProps {
    message: Message;
}

export default function MessageBubble({ message }: MessageBubbleProps) {
    const isUser = message.role === "user";

    return (
        <div
            className={`flex gap-4 animate-slide-up ${isUser ? "flex-row-reverse" : ""}`}
        >
            {/* Avatar */}
            <div
                className={`flex-shrink-0 flex h-10 w-10 items-center justify-center rounded-xl ${isUser
                        ? "bg-gradient-to-br from-emerald-500 to-emerald-600"
                        : "bg-gradient-to-br from-brand-500 to-brand-600 shadow-glow"
                    }`}
            >
                {isUser ? (
                    <User className="h-5 w-5 text-white" />
                ) : (
                    <Sparkles className="h-5 w-5 text-white" />
                )}
            </div>

            {/* Message Content */}
            <div className={`flex-1 max-w-[80%] ${isUser ? "text-right" : ""}`}>
                <div
                    className={`inline-block px-5 py-3 ${isUser ? "message-user" : "message-ai"
                        }`}
                >
                    {message.thinking ? (
                        <ThinkingIndicator />
                    ) : (
                        <div className="prose prose-invert prose-sm max-w-none">
                            <FormattedContent content={message.content} />
                        </div>
                    )}
                </div>

                {/* Tools used */}
                {message.tools && message.tools.length > 0 && (
                    <div className="mt-2 flex flex-wrap gap-2">
                        {message.tools.map((tool, i) => (
                            <span
                                key={i}
                                className="inline-flex items-center gap-1 px-2 py-1 rounded-md bg-brand-500/20 text-brand-400 text-xs"
                            >
                                {tool.name}
                                {tool.status === "running" && (
                                    <span className="w-1.5 h-1.5 bg-brand-400 rounded-full animate-pulse" />
                                )}
                            </span>
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
}

function ThinkingIndicator() {
    return (
        <div className="flex items-center gap-2">
            <span className="text-sm text-muted-foreground">Thinking</span>
            <div className="thinking-dots">
                <span />
                <span />
                <span />
            </div>
        </div>
    );
}

function FormattedContent({ content }: { content: string }) {
    // Basic markdown-like formatting
    // In production, use a proper markdown parser like react-markdown

    if (!content) return null;

    // Split by code blocks
    const parts = content.split(/(```[\s\S]*?```)/g);

    return (
        <>
            {parts.map((part, i) => {
                if (part.startsWith("```")) {
                    // Code block
                    const match = part.match(/```(\w+)?\n?([\s\S]*?)```/);
                    if (match) {
                        const [, lang, code] = match;
                        return (
                            <pre
                                key={i}
                                className="my-3 p-4 rounded-lg bg-slate-900/50 border border-white/5 overflow-x-auto"
                            >
                                {lang && (
                                    <div className="text-xs text-muted-foreground mb-2 uppercase">
                                        {lang}
                                    </div>
                                )}
                                <code className="text-sm font-mono text-emerald-400">{code}</code>
                            </pre>
                        );
                    }
                }

                // Regular text - handle inline formatting
                return (
                    <span key={i}>
                        {part.split("\n").map((line, j) => (
                            <span key={j}>
                                {j > 0 && <br />}
                                {formatInline(line)}
                            </span>
                        ))}
                    </span>
                );
            })}
        </>
    );
}

function formatInline(text: string): React.ReactNode {
    // Bold: **text**
    const boldRegex = /\*\*(.*?)\*\*/g;
    // Inline code: `code`
    const codeRegex = /`([^`]+)`/g;

    let result: React.ReactNode[] = [];
    let lastIndex = 0;
    let match;

    // Combine patterns
    const combinedRegex = /(\*\*.*?\*\*|`[^`]+`)/g;

    while ((match = combinedRegex.exec(text)) !== null) {
        // Add text before match
        if (match.index > lastIndex) {
            result.push(text.slice(lastIndex, match.index));
        }

        const matched = match[0];
        if (matched.startsWith("**")) {
            result.push(
                <strong key={match.index} className="font-semibold text-foreground">
                    {matched.slice(2, -2)}
                </strong>
            );
        } else if (matched.startsWith("`")) {
            result.push(
                <code
                    key={match.index}
                    className="px-1.5 py-0.5 rounded bg-slate-800 text-brand-400 text-sm font-mono"
                >
                    {matched.slice(1, -1)}
                </code>
            );
        }

        lastIndex = match.index + matched.length;
    }

    // Add remaining text
    if (lastIndex < text.length) {
        result.push(text.slice(lastIndex));
    }

    return result.length > 0 ? result : text;
}
