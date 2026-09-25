import type { Metadata } from "next";
import { Inter, Lora } from "next/font/google";
import "./globals.css";
import { Toaster } from "@/components/ui/toaster";
import { ContentProvider, DEFAULT_CONTENT, SiteContent } from "@/lib/content-provider";
import { readFileSync } from "fs";
import path from "path";
import { headers } from "next/headers";

// Force all pages to be dynamically rendered (reads content file on each request)
export const dynamic = "force-dynamic";
export const revalidate = 0;

// Set cache-control headers to prevent browser caching of page content
export async function generateHeaders() {
  return {
    "Cache-Control": "no-store, no-cache, must-revalidate, max-age=0",
    "Pragma": "no-cache",
    "Expires": "0",
  };
}

const inter = Inter({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const lora = Lora({
  variable: "--font-fraunces",
  subsets: ["latin"],
  display: "swap",
  weight: ["400", "500", "600", "700"],
  style: ["normal", "italic"],
});

function getContent(): SiteContent {
  try {
    const possiblePaths = [
      path.join(process.cwd(), "data", "site-content.json"),
      path.join(process.cwd(), ".next", "standalone", "data", "site-content.json"),
      "/app/data/site-content.json",
    ];
    for (const p of possiblePaths) {
      try {
        const raw = readFileSync(p, "utf-8");
        const data = JSON.parse(raw);
        return {
          ...DEFAULT_CONTENT,
          ...data,
          contact: { ...DEFAULT_CONTENT.contact, ...(data.contact || {}) },
          hero: { ...DEFAULT_CONTENT.hero, ...(data.hero || {}) },
          footer: { ...DEFAULT_CONTENT.footer, ...(data.footer || {}) },
          about: { ...DEFAULT_CONTENT.about, ...(data.about || {}) },
          faqs: Array.isArray(data.faqs) && data.faqs.length > 0 ? data.faqs : DEFAULT_CONTENT.faqs,
        } as SiteContent;
      } catch { continue; }
    }
  } catch { /* use defaults */ }
  return DEFAULT_CONTENT;
}

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

export default async function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  // Read content from the file system on EVERY request (server-side)
  const content = getContent();

  // Set cache-control headers to prevent browser caching
  const headerList = await headers();
  // Headers are set via the dynamic export above

  return (
    <html lang="en" suppressHydrationWarning>
      <body
        className={`${inter.variable} ${lora.variable} antialiased bg-background text-foreground`}
      >
        <ContentProvider initialContent={content}>
          {children}
        </ContentProvider>
        <Toaster />
      </body>
    </html>
  );
}
