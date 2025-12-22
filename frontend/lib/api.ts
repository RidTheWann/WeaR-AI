/**
 * WeaR Ai - API Client
 * Handles communication with the backend API.
 */

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "/api/v1";

export interface ChatRequest {
    message: string;
    conversation_id?: string;
    stream?: boolean;
    use_tools?: boolean;
}

export interface ChatResponse {
    conversation_id: string;
    message: {
        id: string;
        role: "user" | "assistant";
        content: string;
    };
    tool_calls: Array<{
        id: string;
        name: string;
        arguments: Record<string, unknown>;
        result?: string;
    }>;
}

export interface StreamEvent {
    event: "token" | "tool_start" | "tool_end" | "thinking" | "done" | "error";
    data: string | Record<string, unknown>;
}

/**
 * Send a chat message and get a non-streaming response.
 */
export async function sendMessage(request: ChatRequest): Promise<ChatResponse> {
    const response = await fetch(`${API_BASE}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ...request, stream: false }),
    });

    if (!response.ok) {
        throw new Error(`API error: ${response.status}`);
    }

    return response.json();
}

/**
 * Send a chat message and stream the response.
 */
export async function* streamMessage(
    request: ChatRequest
): AsyncGenerator<StreamEvent> {
    const response = await fetch(`${API_BASE}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ...request, stream: true }),
    });

    if (!response.ok) {
        throw new Error(`API error: ${response.status}`);
    }

    const reader = response.body?.getReader();
    if (!reader) {
        throw new Error("No response body");
    }

    const decoder = new TextDecoder();
    let buffer = "";

    while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split("\n\n");
        buffer = lines.pop() || "";

        for (const line of lines) {
            if (line.startsWith("event:")) {
                const eventMatch = line.match(/event: (\w+)/);
                const dataMatch = line.match(/data: (.+)/s);

                if (eventMatch && dataMatch) {
                    const event = eventMatch[1] as StreamEvent["event"];
                    let data: string | Record<string, unknown> = dataMatch[1];

                    try {
                        data = JSON.parse(data as string);
                    } catch {
                        // Keep as string
                    }

                    yield { event, data };
                }
            }
        }
    }
}

/**
 * Check API health status.
 */
export async function checkHealth(): Promise<{
    status: string;
    version: string;
}> {
    const response = await fetch(`${API_BASE}/health`);
    if (!response.ok) {
        throw new Error("Health check failed");
    }
    return response.json();
}

/**
 * Get available models.
 */
export async function getModels(): Promise<{
    current_provider: string;
    current_model: string;
    available_providers: string[];
}> {
    const response = await fetch(`${API_BASE}/models`);
    if (!response.ok) {
        throw new Error("Failed to get models");
    }
    return response.json();
}
