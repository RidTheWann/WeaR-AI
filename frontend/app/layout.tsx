import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
    title: "WeaR Ai - Open Source AGI Assistant",
    description: "An advanced AI assistant with AGI-grade capabilities. Powered by open source models.",
    keywords: ["AI", "assistant", "chatbot", "open source", "AGI", "LLM"],
    authors: [{ name: "WeaR Ai Team" }],
    openGraph: {
        title: "WeaR Ai",
        description: "Open Source AGI-grade Assistant",
        type: "website",
    },
};

export default function RootLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <html lang="en" className="dark">
            <body className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950">
                <div className="fixed inset-0 bg-[url('/grid.svg')] bg-center [mask-image:linear-gradient(180deg,white,rgba(255,255,255,0))]" />
                <main className="relative z-10">
                    {children}
                </main>
            </body>
        </html>
    );
}
