"use client";

import { Search, Code, FileText, Loader2, CheckCircle2 } from "lucide-react";

interface ToolIndicatorProps {
    name: string;
    status: "running" | "done";
    result?: string;
}

const TOOL_ICONS: Record<string, React.ElementType> = {
    web_search: Search,
    code_executor: Code,
    file_analyzer: FileText,
};

export default function ToolIndicator({ name, status, result }: ToolIndicatorProps) {
    const Icon = TOOL_ICONS[name] || Code;
    const isRunning = status === "running";

    return (
        <div
            className={`flex items-center gap-3 p-3 rounded-xl border transition-all ${isRunning
                    ? "bg-brand-500/10 border-brand-500/30 animate-pulse-soft"
                    : "bg-emerald-500/10 border-emerald-500/30"
                }`}
        >
            <div
                className={`flex h-8 w-8 items-center justify-center rounded-lg ${isRunning ? "bg-brand-500/20" : "bg-emerald-500/20"
                    }`}
            >
                {isRunning ? (
                    <Loader2 className="h-4 w-4 text-brand-400 animate-spin" />
                ) : (
                    <CheckCircle2 className="h-4 w-4 text-emerald-400" />
                )}
            </div>

            <div className="flex-1 min-w-0">
                <div className="flex items-center gap-2">
                    <Icon className={`h-4 w-4 ${isRunning ? "text-brand-400" : "text-emerald-400"}`} />
                    <span className="text-sm font-medium capitalize">
                        {name.replace(/_/g, " ")}
                    </span>
                </div>
                {result && (
                    <p className="text-xs text-muted-foreground mt-1 truncate">{result}</p>
                )}
            </div>

            {isRunning && (
                <span className="text-xs text-brand-400 font-medium">Running...</span>
            )}
        </div>
    );
}
