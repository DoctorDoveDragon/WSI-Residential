"use client";

import { Header, Footer, AdmissionsSection } from "@/lib/sections";

export default function Page() {
  return (
    <>
      <Header />
      <main className="flex-1">
        <AdmissionsSection />
      </main>
      <Footer />
    </>
  );
}
