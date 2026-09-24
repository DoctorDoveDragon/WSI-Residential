import type { Metadata } from "next";
import { Geist, Geist_Mono, Fraunces } from "next/font/google";
import "./globals.css";
import { Toaster } from "@/components/ui/toaster";
import { ContentProvider } from "@/lib/content-provider";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

const fraunces = Fraunces({
  variable: "--font-fraunces",
  subsets: ["latin"],
  display: "swap",
});

export const metadata: Metadata = {
  metadataBase: new URL("https://wellspringintervention.com"),
  title: "Well Spring Intervention · Level III Residential Treatment for Children | Wake County, NC",
  description:
    "A licensed, staff-secure Level III residential treatment facility in Wake County, NC where children ages 6–17 heal, grow, and graduate toward brighter tomorrows. Empowerment · Growth · Freedom · Health · Wholeness · Healing.",
  keywords: [
    "Well Spring Intervention",
    "residential treatment facility",
    "Level III RTF",
    "staff-secure",
    "children's mental health",
    "trauma-informed care",
    "Wake County North Carolina",
    "10A NCAC 27G .1700",
    "out-of-home placement",
    "referral",
  ],
  authors: [{ name: "Well Spring Intervention LLC" }],
  icons: {
    icon: [
      { url: "/favicon.ico", sizes: "any" },
      { url: "/favicon-32x32.png", sizes: "32x32", type: "image/png" },
      { url: "/favicon-16x16.png", sizes: "16x16", type: "image/png" },
    ],
    apple: "/apple-touch-icon.png",
  },
  manifest: "/site.webmanifest",
  openGraph: {
    title: "Well Spring Intervention · Level III Residential Treatment",
    description:
      "Licensed staff-secure Level III residential treatment for children ages 6–17 · Wake County, North Carolina — where children heal, grow, and graduate.",
    siteName: "Well Spring Intervention",
    type: "website",
    images: ["/images/logo-lockup.png"],
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body
        className={`${geistSans.variable} ${geistMono.variable} ${fraunces.variable} antialiased bg-background text-foreground`}
      >
        <ContentProvider>
          {children}
        </ContentProvider>
        <Toaster />
      </body>
    </html>
  );
}
