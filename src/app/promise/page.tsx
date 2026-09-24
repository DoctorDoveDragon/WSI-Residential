"use client";

import { Header, Footer, BrandPromiseSection } from "@/lib/sections";

export default function Page() {
  return (
    <>
      <Header />
      <main className="flex-1">
        <BrandPromiseSection />
      </main>
      <Footer />
    </>
  );
}
