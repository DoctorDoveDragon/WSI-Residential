"use client";

import { Header, Footer, CommunitySection } from "@/lib/sections";

export default function Page() {
  return (
    <>
      <Header />
      <main className="flex-1">
        <CommunitySection />
      </main>
      <Footer />
    </>
  );
}
