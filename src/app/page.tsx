"use client";

import { Header, Hero, TrustStrip, StaffBand, Footer } from "@/lib/sections";

export default function HomePage() {
  return (
    <>
      <Header />
      <main className="flex-1">
        <Hero />
        <TrustStrip />
        <section className="py-16 md:py-24" aria-label="Explore our program">
          <div className="mx-auto max-w-6xl px-4 sm:px-6">
            <div className="mx-auto max-w-2xl text-center">
              <p className="mb-3 text-xs font-semibold uppercase tracking-[0.22em] text-primary/80">Explore Our Program</p>
              <h2 className="font-display text-3xl font-semibold tracking-tight sm:text-4xl">Choose where to begin.</h2>
              <p className="mt-4 text-lg leading-relaxed text-muted-foreground">Every page below is a doorway into how we care for children and adolescents at Well Spring. Start wherever feels right.</p>
            </div>
          </div>
        </section>
        <StaffBand />
      </main>
      <Footer />
    </>
  );
}
