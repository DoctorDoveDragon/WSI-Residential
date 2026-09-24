"use client";

import { Header, Footer, GrowingSection } from "@/lib/sections";

export default function Page() {
  return (
    <>
      <Header />
      <main className="flex-1">
        <GrowingSection />
      </main>
      <Footer />
    </>
  );
}
