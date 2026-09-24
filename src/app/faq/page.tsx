"use client";

import { Header, Footer, FaqSection } from "@/lib/sections";

export default function Page() {
  return (
    <>
      <Header />
      <main className="flex-1">
        <FaqSection />
      </main>
      <Footer />
    </>
  );
}
