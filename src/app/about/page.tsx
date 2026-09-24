"use client";

import { Header, Footer, AboutSection } from "@/lib/sections";

export default function Page() {
  return (
    <>
      <Header />
      <main className="flex-1">
        <AboutSection />
      </main>
      <Footer />
    </>
  );
}
