"use client";

import { Header, Footer, ResourcesSection } from "@/lib/sections";

export default function Page() {
  return (
    <>
      <Header />
      <main className="flex-1">
        <ResourcesSection />
      </main>
      <Footer />
    </>
  );
}
