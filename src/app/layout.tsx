// app/layout.tsx
import "./globals.css";
import { ReduxProvider } from "@/components/redux/ReduxProvider";

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        {/* Wrap the entire app with ReduxProvider */}
        <ReduxProvider>{children}</ReduxProvider>
      </body>
    </html>
  );
}