"use client";

import { Header, Footer, PeopleSection } from "@/lib/sections";

export default function Page() {
  return (
    <>
      <Header />
      <main className="flex-1">
        <PeopleSection />
      </main>
      <Footer />
    </>
  );
}
