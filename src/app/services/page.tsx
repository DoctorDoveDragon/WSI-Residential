"use client";

import { Header, Footer, ServicesSection } from "@/lib/sections";

export default function Page() {
  return (
    <>
      <Header />
      <main className="flex-1">
        <ServicesSection />
      </main>
      <Footer />
    </>
  );
}
