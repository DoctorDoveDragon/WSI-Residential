"use client";

import { Header, Footer, ContactSection } from "@/lib/sections";

export default function Page() {
  return (
    <>
      <Header />
      <main className="flex-1">
        <ContactSection />
      </main>
      <Footer />
    </>
  );
}
