"use client";

import { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";
import { ArrowRight, ArrowUpRight, CheckCircle2, Download, FileText, Menu, ShieldCheck, X } from "lucide-react";
import {
  BRAND_TAGLINE, BRAND_SERVICES_LINE_1, BRAND_SERVICES_LINE_2, NAV_LINKS, PDFS, PUBLIC_FORMS,
  TRUST_ITEMS, VALUES, PEOPLE_CARDS, SERVICES, MILESTONES, MOMENTS, BRAND_PROMISES,
  ECOSYSTEM_PARTNERS, EXTERNAL_RESOURCES, FadeIn, LogoMark, Wordmark, Eyebrow, linkProps,
} from "./content";
import { useSiteContent } from "./content-provider";

/* ══ Header ══ */
export function Header() {
  const [open, setOpen] = useState(false);
  const pathname = usePathname();
  return (
    <header className="sticky top-0 z-50 border-b border-border/60 bg-background/85 backdrop-blur-md">
      <div className="mx-auto flex h-16 max-w-6xl items-center justify-between gap-3 px-4 sm:px-6">
        <Link href="/" className="flex min-h-11 items-center gap-2.5" aria-label="Well Spring Intervention — home">
          <LogoMark className="h-9 w-9" />
          <Wordmark />
        </Link>
        <nav className="hidden items-center gap-0.5 lg:flex" aria-label="Main navigation">
          {NAV_LINKS.map((link) => {
            const isActive = pathname === link.href;
            return (
              <Link key={link.href} href={link.href} aria-current={isActive ? "page" : undefined}
                className={`rounded-lg px-2.5 py-2 text-sm font-medium transition-colors focus-visible:outline-2 focus-visible:outline-ring ${isActive ? "bg-secondary text-foreground" : "text-muted-foreground hover:bg-secondary hover:text-foreground"}`}>
                {link.label}
              </Link>
            );
          })}
        </nav>
        <div className="hidden lg:block">
          <Button asChild className="h-11 rounded-full px-5">
            <Link href="/admissions">Refer a Child<ArrowRight className="ml-1 h-4 w-4" aria-hidden="true" /></Link>
          </Button>
        </div>
        <button type="button" className="inline-flex h-11 w-11 items-center justify-center rounded-lg text-foreground transition-colors hover:bg-secondary lg:hidden focus-visible:outline-2 focus-visible:outline-ring"
          aria-expanded={open} aria-controls="mobile-nav" aria-label={open ? "Close menu" : "Open menu"} onClick={() => setOpen((v) => !v)}>
          {open ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
        </button>
      </div>
      {open && (
        <div id="mobile-nav" className="border-t border-border/60 bg-background px-4 pb-4 pt-2 lg:hidden">
          <nav className="flex flex-col" aria-label="Mobile navigation">
            {NAV_LINKS.map((link) => {
              const isActive = pathname === link.href;
              return (
                <Link key={link.href} href={link.href} onClick={() => setOpen(false)}
                  className={`rounded-lg px-3 py-3 text-base font-medium transition-colors ${isActive ? "bg-secondary text-foreground" : "text-foreground hover:bg-secondary"}`}>
                  {link.label}
                </Link>
              );
            })}
            <Button asChild className="mt-3 h-11 w-full rounded-full">
              <Link href="/admissions" onClick={() => setOpen(false)}>Refer a Child<ArrowRight className="ml-1 h-4 w-4" aria-hidden="true" /></Link>
            </Button>
          </nav>
        </div>
      )}
    </header>
  );
}

/* ══ Hero ══ */
export function Hero() {
  const { content } = useSiteContent();
  return (
    <section id="top" className="relative overflow-hidden" aria-label="Welcome">
      <div className="pointer-events-none absolute -right-40 -top-40 h-[28rem] w-[28rem] rounded-full bg-secondary/70 blur-3xl" aria-hidden="true" />
      <div className="pointer-events-none absolute -bottom-52 -left-40 h-[26rem] w-[26rem] rounded-full bg-accent/30 blur-3xl" aria-hidden="true" />
      <div className="relative mx-auto grid max-w-6xl items-center gap-10 px-4 pb-16 pt-12 sm:px-6 md:pb-24 md:pt-20 lg:grid-cols-[1.05fr_0.95fr] lg:gap-14">
        <motion.div initial={{ opacity: 0, y: 28 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.7, ease: [0.22, 1, 0.36, 1] }}>
          <p className="mb-4 inline-flex items-center gap-2 rounded-full border border-border bg-card px-4 py-1.5 text-xs font-medium text-muted-foreground">
            <ShieldCheck className="h-3.5 w-3.5 text-[#d05003]" aria-hidden="true" />
            {BRAND_SERVICES_LINE_1} · {content.contact.location}
          </p>
          <h1 className="font-display text-4xl font-semibold leading-[1.08] tracking-tight sm:text-5xl lg:text-6xl">
            A well spring is a source that <span className="italic text-[#d05003]">never stops giving</span>.
          </h1>
          <p className="mt-5 max-w-xl text-lg leading-relaxed text-muted-foreground">{content.hero.body}</p>
          <div className="mt-6 flex flex-wrap gap-x-6 gap-y-2">
            {[{ word: "Steady", gloss: "predictable routines, round-the-clock staff" }, { word: "Clear", gloss: "honest communication, transparent plans" }, { word: "Renewing", gloss: "rest, play, nourishment, growth" }].map((q) => (
              <div key={q.word} className="flex items-baseline gap-2">
                <span className="font-display text-base font-semibold text-[#d05003]">{q.word}.</span>
                <span className="text-sm text-muted-foreground">{q.gloss}</span>
              </div>
            ))}
          </div>
          <p className="mt-5 font-display text-sm font-medium italic text-primary/85 sm:text-base">{content.hero.tagline}</p>
          <div className="mt-7 flex flex-col gap-3 sm:flex-row">
            <Button asChild size="lg" className="h-12 rounded-full bg-[#d05003] px-7 text-base text-[#f5efe7] hover:bg-[#a83802]">
              <Link href="/admissions">Refer a Child<ArrowRight className="ml-1.5 h-5 w-5" aria-hidden="true" /></Link>
            </Button>
            <Button asChild size="lg" variant="outline" className="h-12 rounded-full border-[#d05003]/30 px-7 text-base hover:bg-secondary hover:text-[#d05003]">
              <Link href="/admissions">I&apos;m a Parent</Link>
            </Button>
          </div>
          <ul className="mt-8 flex flex-wrap gap-2" aria-label="Key facts">
            {[{ label: "Ages 6–17", href: "/faq" }, { label: "4–6 Children", href: "/about" }, { label: "Professionals & Teachers Who Care", href: "/people" }, { label: "Trauma-Informed", href: "/promise" }].map((chip) => (
              <li key={chip.label}>
                <Link href={chip.href} className="inline-flex items-center gap-1 rounded-full bg-secondary px-3.5 py-1.5 text-xs font-semibold text-secondary-foreground transition-all hover:bg-[#d05003] hover:text-[#f5efe7] hover:shadow-sm focus-visible:outline-2 focus-visible:outline-ring">
                  {chip.label}
                </Link>
              </li>
            ))}
          </ul>
        </motion.div>
        <motion.div className="relative" initial={{ opacity: 0, scale: 0.97 }} animate={{ opacity: 1, scale: 1 }} transition={{ duration: 0.8, delay: 0.15, ease: [0.22, 1, 0.36, 1] }}>
          <div className="relative flex aspect-square w-full max-w-md flex-col items-center justify-center mx-auto rounded-[2.4rem] bg-gradient-to-br from-[#f5efe7] via-[#f0e0d0] to-[#e8d4c8] p-8 shadow-xl shadow-foreground/10 sm:p-12">
            <div className="pointer-events-none absolute inset-6 rounded-full border-2 border-dashed border-[#d05003]/20" aria-hidden="true" />
            <div className="pointer-events-none absolute inset-10 rounded-full border border-[#d05003]/15" aria-hidden="true" />
            <div className="pointer-events-none absolute inset-14 rounded-full border border-[#d05003]/10" aria-hidden="true" />
            <img src="/images/logo-seal.png?v=3" alt="The official Well Spring Intervention circular seal" className="relative z-10 w-full max-w-[20rem] shrink-0 object-contain drop-shadow-md" loading="eager" />
            <div className="relative z-10 mt-6 text-center">
              <p className="font-display text-xl font-semibold tracking-tight text-[#401000] sm:text-2xl">Well Spring <span className="text-[#d05003]">Intervention</span></p>
              <p className="mt-1 text-[0.6rem] font-semibold uppercase tracking-[0.28em] text-[#604003]/70">Level III Residential Treatment</p>
            </div>
          </div>
          <div className="absolute -bottom-6 left-1/2 flex -translate-x-1/2 items-center gap-2.5 rounded-2xl border border-border bg-card px-4 py-2.5 shadow-lg shadow-foreground/10">
            <ShieldCheck className="h-4 w-4 shrink-0 text-[#d05003]" aria-hidden="true" />
            <span className="text-xs leading-tight">
              <span className="block font-semibold">Staff-Secure Level III RTF</span>
              <span className="block text-muted-foreground">NC 10A NCAC 27G .1700 · DHSR Licensed</span>
            </span>
          </div>
        </motion.div>
      </div>
    </section>
  );
}

/* ══ TrustStrip ══ */
export function TrustStrip() {
  return (
    <section className="bg-[#401000] text-[#f5efe7]" aria-label="Licensing and program facts">
      <div className="mx-auto grid max-w-6xl grid-cols-1 gap-6 px-4 py-10 sm:grid-cols-2 sm:px-6 lg:grid-cols-4 lg:gap-8">
        {TRUST_ITEMS.map((item) => (
          <FadeIn key={item.title} className="flex items-start gap-3.5">
            <item.icon className="mt-0.5 h-6 w-6 shrink-0 text-[#e07020]" aria-hidden="true" />
            <span><span className="block text-sm font-semibold">{item.title}</span><span className="mt-0.5 block text-sm text-[#f5efe7]/75">{item.text}</span></span>
          </FadeIn>
        ))}
      </div>
      <div className="border-t border-[#f5efe7]/10">
        <p className="mx-auto max-w-6xl px-4 py-4 text-center text-[0.65rem] font-semibold uppercase tracking-[0.3em] text-[#f5efe7]/55 sm:px-6">
          {BRAND_SERVICES_LINE_1.toUpperCase().split(" · ").join("  ·  ")}  ·  {BRAND_SERVICES_LINE_2.toUpperCase().split(" · ").join("  ·  ")}
        </p>
      </div>
    </section>
  );
}

/* ══ Section: About ══ */
export function AboutSection() {
  const { content } = useSiteContent();
  return (
    <section id="about" className="py-16 md:py-24" aria-label="About us">
      <div className="mx-auto max-w-6xl px-4 sm:px-6">
        <div className="grid items-center gap-10 lg:grid-cols-[0.95fr_1.05fr] lg:gap-16">
          <FadeIn className="relative order-2 lg:order-1">
            <div className="relative overflow-hidden rounded-[2rem] border border-border/70 bg-gradient-to-br from-[#401000] to-[#503020] p-8 text-center text-[#f5efe7] shadow-lg shadow-foreground/10 sm:p-12">
              <img src="/images/logo-seal.png?v=3" alt="The official Well Spring Intervention circular seal" className="mx-auto h-44 w-44 shrink-0 object-contain opacity-95 sm:h-52 sm:w-52" loading="lazy" />
              <p className="relative mt-6 font-display text-lg font-medium italic leading-relaxed text-[#f5efe7]/90 sm:text-xl">Therapy for children and adolescents, in the shape of a home.</p>
              <p className="relative mt-4 text-xs font-semibold uppercase tracking-[0.18em] text-[#e07020]">Licensed · Staff-Secure · {content.contact.location}</p>
            </div>
          </FadeIn>
          <div className="order-1 lg:order-2">
            <FadeIn>
              <Eyebrow>About Well Spring</Eyebrow>
              <h2 className="font-display text-3xl font-semibold tracking-tight sm:text-4xl">{content.about.heading}</h2>
              <p className="mt-5 text-lg leading-relaxed text-muted-foreground">{content.about.body1}</p>
              <p className="mt-4 text-lg leading-relaxed text-muted-foreground">{content.about.body2}</p>
            </FadeIn>
          </div>
        </div>
        <div className="mt-14 grid gap-5 sm:grid-cols-2 lg:grid-cols-4">
          {VALUES.map((value, i) => {
            const lp = linkProps(value.href);
            return (
              <FadeIn key={value.title} delay={i * 0.08}>
                <Link href={value.href} aria-label={`${value.title} — ${value.cta}`} className="group flex h-full flex-col rounded-2xl border border-border/70 bg-card p-6 transition-all hover:-translate-y-0.5 hover:border-[#d05003]/40 hover:shadow-md hover:shadow-foreground/5 focus-visible:outline-2 focus-visible:outline-ring">
                  <span className="mb-4 flex h-11 w-11 items-center justify-center rounded-xl bg-secondary transition-colors group-hover:bg-accent"><value.icon className="h-5.5 w-5.5 text-primary" aria-hidden="true" /></span>
                  <h3 className="font-display text-lg font-semibold">{value.title}</h3>
                  <p className="mt-2 flex-1 text-sm leading-relaxed text-muted-foreground">{value.text}</p>
                  <span className="mt-4 inline-flex items-center gap-1 text-xs font-semibold uppercase tracking-[0.14em] text-[#d05003]">{value.cta}<ArrowRight className="h-3.5 w-3.5" aria-hidden="true" /></span>
                </Link>
              </FadeIn>
            );
          })}
        </div>
      </div>
    </section>
  );
}

/* ══ Section: Brand Promise ══ */
export function BrandPromiseSection() {
  return (
    <section id="promise" className="relative overflow-hidden py-16 md:py-24" aria-label="Our Brand Promise">
      <div className="pointer-events-none absolute inset-0 bg-gradient-to-b from-secondary/30 via-background to-background" aria-hidden="true" />
      <div className="pointer-events-none absolute -right-32 top-20 h-72 w-72 rounded-full bg-[#d05003]/10 blur-3xl" aria-hidden="true" />
      <div className="pointer-events-none absolute -left-32 bottom-20 h-72 w-72 rounded-full bg-[#e07020]/15 blur-3xl" aria-hidden="true" />
      <div className="relative mx-auto max-w-6xl px-4 sm:px-6">
        <FadeIn className="mx-auto max-w-2xl text-center">
          <Eyebrow>Our Brand Promise</Eyebrow>
          <h2 className="font-display text-3xl font-semibold tracking-tight sm:text-4xl">Five things present in every home, every day.</h2>
          <p className="mt-4 text-lg leading-relaxed text-muted-foreground">
            When a child comes to Well Spring, we promise them more than treatment. We promise them a home where <span className="font-semibold text-[#d05003]">commitment</span>, <span className="font-semibold text-[#d05003]">growth and structure</span>, <span className="font-semibold text-[#d05003]">acceptance</span>, <span className="font-semibold text-[#d05003]">safety</span>, and <span className="font-semibold text-[#d05003]">replenishment</span> are not just words on a wall — they are the lived, daily reality of every child who walks through our door.
          </p>
        </FadeIn>
        <div className="mt-12 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
          {BRAND_PROMISES.map((promise, i) => (
            <FadeIn key={promise.title} delay={i * 0.08}>
              <Link href={promise.href} aria-label={`${promise.title} — ${promise.cta}`} className="group flex h-full flex-col rounded-[1.75rem] border border-border/70 bg-card p-7 transition-all hover:-translate-y-1 hover:border-[#d05003]/40 hover:shadow-lg hover:shadow-foreground/10 focus-visible:outline-2 focus-visible:outline-ring">
                <span className="mb-5 flex h-14 w-14 items-center justify-center rounded-2xl bg-gradient-to-br from-secondary to-[#f5e6dc] transition-transform group-hover:scale-105"><promise.icon className="h-7 w-7 text-[#d05003]" aria-hidden="true" /></span>
                <h3 className="font-display text-xl font-semibold tracking-tight">{promise.title}</h3>
                <p className="mt-3 flex-1 text-sm leading-relaxed text-muted-foreground sm:text-base">{promise.text}</p>
                <span className="mt-5 inline-flex items-center gap-1.5 text-xs font-semibold uppercase tracking-[0.14em] text-[#d05003]">{promise.cta}<ArrowRight className="h-3.5 w-3.5 transition-transform group-hover:translate-x-0.5" aria-hidden="true" /></span>
              </Link>
            </FadeIn>
          ))}
          <FadeIn delay={0.4}>
            <div className="flex h-full flex-col justify-center rounded-[1.75rem] border border-[#d05003]/30 bg-[#401000] p-7 text-[#f5efe7]">
              <span className="mb-4 font-display text-sm font-semibold uppercase tracking-[0.22em] text-[#e07020]">Our Mission</span>
              <p className="font-display text-lg font-medium italic leading-relaxed">&ldquo;Every child deserves a stable, predictable, and nurturing environment in which healing can occur.&rdquo;</p>
              <p className="mt-4 text-xs text-[#f5efe7]/65">— Well Spring Intervention, SOP v2.26 §1.1</p>
              <Link href="/resources" className="mt-6 inline-flex items-center gap-1.5 text-xs font-semibold uppercase tracking-[0.14em] text-[#e07020] transition-colors hover:text-[#f5efe7] focus-visible:outline-2 focus-visible:outline-[#e07020]">View Staff Resources<ArrowUpRight className="h-3.5 w-3.5" aria-hidden="true" /></Link>
            </div>
          </FadeIn>
        </div>
      </div>
    </section>
  );
}

/* ══ Section: People ══ */
export function PeopleSection() {
  return (
    <section id="people" className="bg-secondary/45 py-16 md:py-24" aria-label="Our people">
      <div className="mx-auto max-w-6xl px-4 sm:px-6">
        <FadeIn className="mx-auto max-w-2xl text-center">
          <Eyebrow>Our People</Eyebrow>
          <h2 className="font-display text-3xl font-semibold tracking-tight sm:text-4xl">The adults who show up — and keep showing up.</h2>
          <p className="mt-4 text-lg leading-relaxed text-muted-foreground">Healing happens in relationships. Our campus is small by design, so every child is deeply known — and every professional and teacher has the time to truly know them.</p>
        </FadeIn>
        <div className="mt-12 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
          {PEOPLE_CARDS.map((card, i) => (
            <FadeIn key={card.title} delay={i * 0.08}>
              <Link href={card.href} aria-label={`${card.title} — ${card.cta}`} className="group flex h-full flex-col rounded-2xl border border-border/70 bg-card p-6 transition-all hover:-translate-y-0.5 hover:border-[#d05003]/40 hover:shadow-md hover:shadow-foreground/5 focus-visible:outline-2 focus-visible:outline-ring">
                <span className="mb-4 flex h-11 w-11 items-center justify-center rounded-xl bg-secondary transition-colors group-hover:bg-accent"><card.icon className="h-5.5 w-5.5 text-primary" aria-hidden="true" /></span>
                <h3 className="font-display text-lg font-semibold">{card.title}</h3>
                <p className="mt-2 flex-1 text-sm leading-relaxed text-muted-foreground">{card.text}</p>
                <span className="mt-4 inline-flex items-center gap-1 text-xs font-semibold uppercase tracking-[0.14em] text-[#d05003]">{card.cta}<ArrowRight className="h-3.5 w-3.5" aria-hidden="true" /></span>
              </Link>
            </FadeIn>
          ))}
        </div>
        <FadeIn className="mt-10">
          <div className="relative overflow-hidden rounded-[2rem] border border-[#d05003]/25 bg-gradient-to-br from-[#401000] to-[#503020] p-8 text-[#f5efe7] sm:p-10">
            <img src="/images/logo-seal.png?v=3" alt="" aria-hidden="true" className="pointer-events-none absolute -right-12 -bottom-12 h-56 w-56 opacity-10" />
            <div className="relative max-w-3xl">
              <p className="font-display text-sm font-semibold uppercase tracking-[0.22em] text-[#e07020]">The therapeutic relationship</p>
              <h3 className="mt-3 font-display text-2xl font-semibold leading-tight sm:text-3xl">Trust is built one ordinary moment at a time.</h3>
              <p className="mt-4 text-base leading-relaxed text-[#f5efe7]/85 sm:text-lg">At the breakfast table. On the walk to school. Over homework and bedtime check-ins. Our professionals and teachers turn each day into dozens of small, respectful opportunities for a child to practice coping, connect, and succeed — the kind of therapeutic teaching that only happens inside a real relationship, and the reason residential treatment works when outpatient alone cannot.</p>
            </div>
          </div>
        </FadeIn>
      </div>
    </section>
  );
}

/* ══ Section: Community ══ */
export function CommunitySection() {
  return (
    <section id="community" className="bg-secondary/45 py-16 md:py-24" aria-label="Our place in the community">
      <div className="mx-auto max-w-6xl px-4 sm:px-6">
        <FadeIn className="mx-auto max-w-2xl text-center">
          <Eyebrow>Family, Community &amp; the Care Ecosystem</Eyebrow>
          <h2 className="font-display text-3xl font-semibold tracking-tight sm:text-4xl">Every child belongs to a family, a community, and a system of care.</h2>
          <p className="mt-4 text-lg leading-relaxed text-muted-foreground">A child is never just a placement — they are a son or daughter, a student, a neighbor, a friend. We hold that truth at the center of everything we do, and we know the ecosystem around each child well enough to be a true partner within it.</p>
        </FadeIn>
        <FadeIn delay={0.1}>
          <div className="relative mt-12 overflow-hidden rounded-[2rem] border border-[#d05003]/25 bg-gradient-to-br from-[#401000] to-[#503020] p-8 text-[#f5efe7] sm:p-10">
            <img src="/images/logo-seal.png?v=3" alt="" aria-hidden="true" className="pointer-events-none absolute -right-12 -bottom-12 h-56 w-56 opacity-10" />
            <div className="relative max-w-3xl">
              <p className="font-display text-sm font-semibold uppercase tracking-[0.22em] text-[#e07020]">Why every child matters</p>
              <p className="mt-4 text-base leading-relaxed text-[#f5efe7]/90 sm:text-lg">The children who come to us are not problems to be solved — they are young people who matter deeply to their families, their schools, their congregations, and their neighborhoods. A child&apos;s absence from home is felt in the seat that is empty at the dinner table, the desk that is quiet at school, the pew that is open on Sunday. We never forget that each child here is someone&apos;s son, someone&apos;s daughter, someone&apos;s grandchild, someone&apos;s friend — and that their return home whole is the hope an entire community is holding. Our job is not to replace that community, but to strengthen the child who will re-enter it.</p>
            </div>
          </div>
        </FadeIn>
        <FadeIn delay={0.15}>
          <p className="mt-14 mb-6 text-center font-display text-sm font-semibold uppercase tracking-[0.22em] text-[#d05003]">How we participate in the ecosystem</p>
        </FadeIn>
        <div className="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
          {ECOSYSTEM_PARTNERS.map((partner, i) => (
            <FadeIn key={partner.title} delay={i * 0.06}>
              <div className="h-full rounded-2xl border border-border/70 bg-card p-6 transition-shadow hover:shadow-md hover:shadow-foreground/5">
                <span className="mb-4 flex h-11 w-11 items-center justify-center rounded-xl bg-secondary"><partner.icon className="h-5.5 w-5.5 text-[#d05003]" aria-hidden="true" /></span>
                <h3 className="font-display text-lg font-semibold">{partner.title}</h3>
                <p className="mt-2 text-sm leading-relaxed text-muted-foreground">{partner.text}</p>
              </div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ══ Section: Services ══ */
export function ServicesSection() {
  return (
    <section id="services" className="py-16 md:py-24" aria-label="Our services">
      <div className="mx-auto max-w-6xl px-4 sm:px-6">
        <FadeIn className="mx-auto max-w-2xl text-center">
          <Eyebrow>Our Program</Eyebrow>
          <h2 className="font-display text-3xl font-semibold tracking-tight sm:text-4xl">Everything a child needs, under one roof.</h2>
          <p className="mt-4 text-lg leading-relaxed text-muted-foreground">Clinical care, daily-life coaching, and round-the-clock structure — integrated into one warm residential setting, so treatment never feels like an institution.</p>
        </FadeIn>
        <div className="mt-12 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
          {SERVICES.map((service, i) => (
            <FadeIn key={service.title} delay={i * 0.06}>
              <Link href={service.href} aria-label={`${service.title} — ${service.cta}`} className="group flex h-full flex-col rounded-2xl border border-border/70 bg-card p-6 transition-all hover:-translate-y-0.5 hover:border-[#d05003]/40 hover:shadow-md hover:shadow-foreground/5 focus-visible:outline-2 focus-visible:outline-ring">
                <span className="mb-4 flex h-11 w-11 items-center justify-center rounded-xl bg-secondary transition-colors group-hover:bg-accent"><service.icon className="h-5.5 w-5.5 text-primary" aria-hidden="true" /></span>
                <h3 className="font-display text-lg font-semibold">{service.title}</h3>
                <p className="mt-2 flex-1 text-sm leading-relaxed text-muted-foreground">{service.text}</p>
                <span className="mt-4 inline-flex items-center gap-1 text-xs font-semibold uppercase tracking-[0.14em] text-[#d05003]">{service.cta}<ArrowRight className="h-3.5 w-3.5" aria-hidden="true" /></span>
              </Link>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ══ Section: Growing ══ */
export function GrowingSection() {
  return (
    <section id="growing" className="bg-secondary/45 py-16 md:py-24" aria-label="Growing and graduating">
      <div className="mx-auto max-w-6xl px-4 sm:px-6">
        <FadeIn className="mx-auto max-w-2xl text-center">
          <Eyebrow>Growing &amp; Graduating</Eyebrow>
          <h2 className="font-display text-3xl font-semibold tracking-tight sm:text-4xl">From the first hard day to the day they walk on.</h2>
          <p className="mt-4 text-lg leading-relaxed text-muted-foreground">Every child&apos;s stay is a journey — and every brave step forward is noticed, named, and celebrated. Here is what growing looks like at Well Spring.</p>
        </FadeIn>
        <div className="mt-12 grid items-start gap-10 lg:grid-cols-[0.9fr_1.1fr] lg:gap-14">
          <FadeIn className="relative">
            <div className="relative overflow-hidden rounded-[2rem] border border-[#d05003]/25 bg-gradient-to-br from-[#401000] to-[#503020] p-8 text-[#f5efe7] shadow-lg shadow-foreground/5 sm:p-10">
              <img src="/images/logo-seal.png?v=3" alt="" aria-hidden="true" className="pointer-events-none absolute -right-10 -top-10 h-44 w-44 opacity-10" />
              <p className="relative font-display text-sm font-semibold uppercase tracking-[0.22em] text-[#e07020]">The Treatment Arc</p>
              <h3 className="relative mt-3 font-display text-2xl font-semibold leading-tight sm:text-3xl">Stabilize · Treat · Practice · Transition</h3>
              <p className="relative mt-4 text-sm leading-relaxed text-[#f5efe7]/80 sm:text-base">Every child moves through a clinically supervised arc — from stabilization on arrival, through intensive individualized treatment, to real-world practice and a planned transition home. The goal was never to stay — it&apos;s to leave ready.</p>
              <dl className="relative mt-6 space-y-3 text-sm">
                <div className="flex items-baseline justify-between gap-3 border-b border-[#f5efe7]/10 pb-2"><dt className="font-semibold text-[#f5efe7]">First plan built with family</dt><dd className="text-[#e07020]">Day 1</dd></div>
                <div className="flex items-baseline justify-between gap-3 border-b border-[#f5efe7]/10 pb-2"><dt className="font-semibold text-[#f5efe7]">School re-enrolled</dt><dd className="text-[#e07020]">Within 5 days</dd></div>
                <div className="flex items-baseline justify-between gap-3 border-b border-[#f5efe7]/10 pb-2"><dt className="font-semibold text-[#f5efe7]">Treatment plan reviewed</dt><dd className="text-[#e07020]">Every 30 days</dd></div>
                <div className="flex items-baseline justify-between gap-3"><dt className="font-semibold text-[#f5efe7]">Transition plan finalized</dt><dd className="text-[#e07020]">Before discharge</dd></div>
              </dl>
            </div>
          </FadeIn>
          <FadeIn delay={0.1}>
            <ol className="space-y-3">
              {MILESTONES.map((step, i) => (
                <li key={step.title}>
                  <Link href={step.href} aria-label={`${step.title} — learn more`} className="group flex items-start gap-4 rounded-2xl p-3 -m-3 transition-colors hover:bg-secondary/50 focus-visible:outline-2 focus-visible:outline-ring">
                    <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-full bg-primary text-sm font-semibold text-primary-foreground transition-colors group-hover:bg-[#d05003]">{i + 1}</span>
                    <span className="flex-1">
                      <span className="flex items-center gap-1.5"><span className="block font-display text-lg font-semibold">{step.title}</span><ArrowRight className="h-3.5 w-3.5 text-[#d05003] opacity-0 transition-opacity group-hover:opacity-100" aria-hidden="true" /></span>
                      <span className="mt-1 block text-sm leading-relaxed text-muted-foreground">{step.text}</span>
                    </span>
                  </Link>
                </li>
              ))}
            </ol>
            <div className="mt-8 flex flex-wrap items-center gap-2">
              <span className="inline-flex items-center gap-1.5 text-xs font-semibold uppercase tracking-[0.14em] text-muted-foreground"><span className="text-primary">★</span> Celebrated here:</span>
              {MOMENTS.map((moment) => (
                <Link key={moment} href="/growing" className="rounded-full bg-card px-3 py-1.5 text-xs font-semibold text-secondary-foreground shadow-sm transition-all hover:bg-[#d05003] hover:text-[#f5efe7] focus-visible:outline-2 focus-visible:outline-ring">{moment}</Link>
              ))}
            </div>
          </FadeIn>
        </div>
      </div>
    </section>
  );
}

/* ══ Section: Admissions ══ */
export function AdmissionsSection() {
  return (
    <section id="admissions" className="py-16 md:py-24" aria-label="Admissions and referrals">
      <div className="mx-auto max-w-6xl px-4 sm:px-6">
        <FadeIn className="mx-auto max-w-2xl text-center">
          <Eyebrow>Admissions &amp; Referrals</Eyebrow>
          <h2 className="font-display text-3xl font-semibold tracking-tight sm:text-4xl">Two doors, one warm welcome.</h2>
          <p className="mt-4 text-lg leading-relaxed text-muted-foreground">Whether you coordinate placements for a county agency or you are a parent exploring what comes next for your child — start here.</p>
        </FadeIn>
        <div className="mt-12 grid gap-6 lg:grid-cols-2">
          <FadeIn>
            <div className="flex h-full flex-col rounded-[2rem] border border-border/70 bg-card p-7 sm:p-8">
              <span className="mb-5 flex h-12 w-12 items-center justify-center rounded-2xl bg-secondary"><FileText className="h-6 w-6 text-primary" aria-hidden="true" /></span>
              <h3 className="font-display text-2xl font-semibold">For Referrers &amp; Professionals</h3>
              <p className="mt-3 text-sm leading-relaxed text-muted-foreground sm:text-base">We serve children and adolescents, ages 6–17, placed out of home due to behavioral and mental health needs. Referrals are typically coordinated through county LME/MCOs, departments of social services, and placing agencies — and we move quickly, because children in transition cannot wait.</p>
              <ol className="mt-6 space-y-4">
                {[{ title: "Reach out", text: "Call or email our admissions line with your referral question." }, { title: "Records review", text: "We review the child's history and screen for clinical fit, honestly and promptly." }, { title: "Pre-placement visit", text: "The child and family tour the home and meet the team before anything is decided." }, { title: "Admission & first plan", text: "We welcome the child and build the first 30-day plan together with the family." }].map((step, i) => (
                  <li key={step.title} className="flex gap-4">
                    <span className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-primary text-sm font-semibold text-primary-foreground">{i + 1}</span>
                    <span><span className="block text-sm font-semibold">{step.title}</span><span className="mt-0.5 block text-sm text-muted-foreground">{step.text}</span></span>
                  </li>
                ))}
              </ol>
              <div className="mt-auto pt-7">
                <Button asChild className="h-11 rounded-full px-6"><Link href="/contact">Start a Referral<ArrowRight className="ml-1.5 h-4 w-4" aria-hidden="true" /></Link></Button>
              </div>
            </div>
          </FadeIn>
          <FadeIn delay={0.12}>
            <div id="families" className="relative flex h-full flex-col overflow-hidden rounded-[2rem] border border-border/70 bg-[#401000] p-7 text-[#f5efe7] sm:p-8">
              <img src="/images/logo-seal.png?v=3" alt="" aria-hidden="true" className="pointer-events-none absolute -right-12 -bottom-12 h-56 w-56 opacity-10" />
              <span className="relative mb-5 flex h-12 w-12 items-center justify-center rounded-2xl bg-white/10"><CheckCircle2 className="h-6 w-6 text-[#e07020]" aria-hidden="true" /></span>
              <h3 className="relative font-display text-2xl font-semibold">For Parents &amp; Caregivers</h3>
              <p className="relative mt-3 text-sm leading-relaxed text-[#f5efe7]/80 sm:text-base">If a residential placement has been recommended for your child, you probably have a hundred questions — and you should ask every single one of them. Call us. Tour the home. Meet the team. There is no obligation, and no question is too small.</p>
              <ul className="relative mt-6 space-y-3.5">
                {["You stay part of every plan and every decision", "Visits and phone contact with your child are encouraged", "Planning for home begins on day one, not at discharge"].map((item) => (
                  <li key={item} className="flex items-start gap-3"><CheckCircle2 className="mt-0.5 h-5 w-5 shrink-0 text-[#e07020]" aria-hidden="true" /><span className="text-sm leading-relaxed text-[#f5efe7]/85 sm:text-base">{item}</span></li>
                ))}
              </ul>
              <div className="relative mt-auto pt-7">
                <Button asChild size="lg" className="h-11 rounded-full bg-[#f5efe7] px-6 text-[#401000] hover:bg-white"><Link href="/contact">Talk With Us<ArrowRight className="ml-1.5 h-4 w-4" aria-hidden="true" /></Link></Button>
              </div>
            </div>
          </FadeIn>
        </div>
        {/* Public referral forms — no password needed */}
        <FadeIn delay={0.2}>
          <div className="mt-14">
            <div className="mx-auto mb-8 max-w-2xl text-center">
              <Eyebrow>Referral Forms &amp; Documents</Eyebrow>
              <h3 className="font-display text-2xl font-semibold tracking-tight sm:text-3xl">Download the forms you need.</h3>
              <p className="mt-3 text-base leading-relaxed text-muted-foreground">These forms are available to everyone — no password required. Download, print, complete, and return to us. If you need help, <Link href="/contact" className="font-semibold text-[#d05003] underline-offset-4 hover:underline">contact us</Link>.</p>
            </div>
            <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
              {PUBLIC_FORMS.map((form, i) => (
                <FadeIn key={form.file} delay={i * 0.04}>
                  <a href={`/forms/${form.file}`} download className="group flex h-full flex-col rounded-2xl border border-border/70 bg-card p-5 transition-all hover:-translate-y-0.5 hover:border-[#d05003]/40 hover:shadow-md hover:shadow-foreground/5 focus-visible:outline-2 focus-visible:outline-ring">
                    <span className="mb-3 flex h-10 w-10 items-center justify-center rounded-xl bg-secondary transition-colors group-hover:bg-accent"><Download className="h-5 w-5 text-[#d05003]" aria-hidden="true" /></span>
                    <span className="font-display text-base font-semibold leading-snug">{form.label}</span>
                    <span className="mt-2 flex-1 text-sm leading-relaxed text-muted-foreground">{form.description}</span>
                    <span className="mt-3 inline-flex items-center gap-1 text-xs font-semibold uppercase tracking-[0.14em] text-[#d05003]">Download PDF<ArrowRight className="h-3.5 w-3.5" aria-hidden="true" /></span>
                  </a>
                </FadeIn>
              ))}
            </div>
          </div>
        </FadeIn>
      </div>
    </section>
  );
}

/* ══ Section: FAQ ══ */
export function FaqSection() {
  const { content } = useSiteContent();
  const faqs = content.faqs;
  return (
    <section id="faq" className="bg-secondary/45 py-16 md:py-24" aria-label="Frequently asked questions">
      <div className="mx-auto max-w-3xl px-4 sm:px-6">
        <FadeIn className="text-center">
          <Eyebrow>Questions, Answered Honestly</Eyebrow>
          <h2 className="font-display text-3xl font-semibold tracking-tight sm:text-4xl">Frequently asked questions</h2>
        </FadeIn>
        <FadeIn className="mt-10">
          <Accordion type="single" collapsible className="rounded-[1.75rem] border border-border/70 bg-card px-6 py-2 sm:px-8">
            {faqs.map((faq, i) => (
              <AccordionItem key={i} value={`faq-${i}`}>
                <AccordionTrigger className="py-5 text-left font-display text-base font-semibold sm:text-lg">{faq.q}</AccordionTrigger>
                <AccordionContent className="pb-5 text-sm leading-relaxed text-muted-foreground sm:text-base">{faq.a}</AccordionContent>
              </AccordionItem>
            ))}
          </Accordion>
        </FadeIn>
      </div>
    </section>
  );
}

/* ══ Section: Contact ══ */
export function ContactSection() {
  const { content } = useSiteContent();
  return (
    <section id="contact" className="py-16 md:py-24" aria-label="Contact us">
      <div className="mx-auto max-w-6xl px-4 sm:px-6">
        <FadeIn className="mx-auto max-w-2xl text-center">
          <Eyebrow>Contact</Eyebrow>
          <h2 className="font-display text-3xl font-semibold tracking-tight sm:text-4xl">Start a conversation.</h2>
          <p className="mt-4 text-lg leading-relaxed text-muted-foreground">Referral inquiries and family questions are always welcome — a real person answers, and we do our best to respond within one business day.</p>
        </FadeIn>
        <div className="mt-12 grid gap-5 sm:grid-cols-3">
          <FadeIn>
            <a href={content.contact.phoneHref} className="flex h-full flex-col items-center rounded-[2rem] border border-border/70 bg-card p-8 text-center transition-all hover:-translate-y-0.5 hover:shadow-md hover:shadow-foreground/5 focus-visible:outline-2 focus-visible:outline-ring">
              <span className="mb-4 flex h-12 w-12 items-center justify-center rounded-full bg-secondary"><span className="h-5 w-5 text-[#d05003]" aria-hidden="true">☎</span></span>
              <span className="font-display text-lg font-semibold">Call Us</span>
              <span className="mt-1.5 text-sm text-muted-foreground">{content.contact.phone}</span>
              <span className="mt-1 text-xs text-muted-foreground/70">Admissions &amp; general inquiries</span>
            </a>
          </FadeIn>
          <FadeIn delay={0.08}>
            <a href={`mailto:${content.contact.email}`} className="flex h-full flex-col items-center rounded-[2rem] border border-border/70 bg-card p-8 text-center transition-all hover:-translate-y-0.5 hover:shadow-md hover:shadow-foreground/5 focus-visible:outline-2 focus-visible:outline-ring">
              <span className="mb-4 flex h-12 w-12 items-center justify-center rounded-full bg-secondary"><span className="h-5 w-5 text-[#d05003]" aria-hidden="true">✉</span></span>
              <span className="font-display text-lg font-semibold">Email Us</span>
              <span className="mt-1.5 break-all text-sm text-muted-foreground">{content.contact.email}</span>
              <span className="mt-1 text-xs text-muted-foreground/70">Write any time — we reply within one business day</span>
            </a>
          </FadeIn>
          <FadeIn delay={0.16}>
            <div className="flex h-full flex-col items-center rounded-[2rem] border border-border/70 bg-card p-8 text-center">
              <span className="mb-4 flex h-12 w-12 items-center justify-center rounded-full bg-secondary"><span className="h-5 w-5 text-[#d05003]" aria-hidden="true">⌖</span></span>
              <span className="font-display text-lg font-semibold">Visit — After We Meet</span>
              <span className="mt-1.5 text-sm text-muted-foreground">{content.contact.location}</span>
              <span className="mt-1 text-xs text-muted-foreground/70">For the safety and privacy of our residents, our street address is shared during the referral process</span>
            </div>
          </FadeIn>
        </div>
      </div>
    </section>
  );
}

/* ══ Section: Resources ══ */
export function ResourcesSection() {
  return (
    <section id="resources" className="py-16 md:py-24" aria-label="Forms and resources">
      <div className="mx-auto max-w-6xl px-4 sm:px-6">
        <FadeIn className="mx-auto max-w-2xl text-center">
          <Eyebrow>Forms &amp; Resources</Eyebrow>
          <h2 className="font-display text-3xl font-semibold tracking-tight sm:text-4xl">The forms behind a placement, all in one place.</h2>
          <p className="mt-4 text-lg leading-relaxed text-muted-foreground">Referrals, licensure, enrollment, incident reporting, and clinical policy — these are the official NC DHHS, NC Medicaid, Alliance Health, and NC DPI resources we use every day. Each link opens directly to the source.</p>
        </FadeIn>
        <div className="mt-12 space-y-12">
          {EXTERNAL_RESOURCES.map((group, gi) => (
            <FadeIn key={group.category} delay={gi * 0.05}>
              <div>
                <h3 className="mb-5 flex items-center gap-3 font-display text-xl font-semibold tracking-tight"><span className="h-px flex-1 bg-border" /><span>{group.category}</span><span className="h-px flex-1 bg-border" /></h3>
                <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
                  {group.items.map((item) => {
                    const lp = linkProps(item.url);
                    return (
                      <a key={item.url} href={item.url} {...(lp.external ? { target: lp.target, rel: lp.rel } : {})} className="group flex h-full flex-col rounded-2xl border border-border/70 bg-card p-5 transition-all hover:-translate-y-0.5 hover:border-[#d05003]/40 hover:shadow-md hover:shadow-foreground/5 focus-visible:outline-2 focus-visible:outline-ring">
                        <span className="flex items-start justify-between gap-2"><span className="font-display text-base font-semibold leading-snug">{item.title}</span><ArrowUpRight className="mt-0.5 h-4 w-4 shrink-0 text-[#d05003] transition-transform group-hover:translate-x-0.5 group-hover:-translate-y-0.5" aria-hidden="true" /></span>
                        <p className="mt-2 flex-1 text-sm leading-relaxed text-muted-foreground">{item.description}</p>
                        <span className="mt-3 inline-block truncate text-xs font-medium text-[#d05003]/80">{item.url.replace(/^https?:\/\//, "").replace(/\/$/, "")}</span>
                      </a>
                    );
                  })}
                </div>
              </div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ══ StaffBand — password-gated internal docs ══ */
export function StaffBand() {
  const [password, setPassword] = useState("");
  const [authed, setAuthed] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [downloading, setDownloading] = useState<string | null>(null);

  async function handleUnlock(e: React.FormEvent) {
    e.preventDefault();
    setError(null);
    if (!password.trim()) { setError("Please enter the staff password."); return; }
    try {
      const res = await fetch("/api/verify", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ password }) });
      if (res.ok) setAuthed(true);
      else if (res.status === 401) setError("Incorrect password. Please try again.");
      else setError("Could not verify password. Please try again later.");
    } catch { setError("Network error. Please try again."); }
  }

  async function handleDownload(file: string, label: string) {
    setError(null);
    setDownloading(label);
    try {
      const res = await fetch(`/api/download?doc=${encodeURIComponent(file)}&password=${encodeURIComponent(password)}`);
      if (!res.ok) {
        if (res.status === 401) { setError("Session expired. Please re-enter the password."); setAuthed(false); }
        else setError(`Could not download ${label}.`);
        return;
      }
      const blob = await res.blob();
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url; a.download = file;
      document.body.appendChild(a); a.click(); document.body.removeChild(a);
      URL.revokeObjectURL(url);
    } catch { setError(`Network error downloading ${label}.`); }
    finally { setDownloading(null); }
  }

  return (
    <section className="border-t border-border/60 bg-card/60 py-10" aria-label="For staff and partners">
      <div className="mx-auto max-w-6xl px-4 sm:px-6">
        <div className="flex flex-col gap-4 md:flex-row md:items-start md:justify-between">
          <div>
            <p className="font-display text-sm font-semibold uppercase tracking-[0.18em] text-muted-foreground">For Staff &amp; Partners — Internal Documents</p>
            <p className="mt-1 text-sm text-muted-foreground">Operational documents, treatment plans, and program manuals. Enter the staff password to unlock. Referral forms for families and referrers are available on the <Link href="/admissions" className="font-semibold text-[#d05003] underline-offset-4 hover:underline">Admissions page</Link>.</p>
          </div>
          {!authed ? (
            <form onSubmit={handleUnlock} className="flex flex-col gap-2 sm:flex-row sm:items-center">
              <label htmlFor="staff-password" className="sr-only">Staff password</label>
              <input id="staff-password" type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Staff password" autoComplete="current-password" className="h-11 min-w-[14rem] rounded-full border border-border bg-background px-4 text-sm text-foreground placeholder:text-muted-foreground/70 focus-visible:outline-2 focus-visible:outline-ring" />
              <Button type="submit" className="h-11 rounded-full bg-[#d05003] px-5 text-sm font-semibold text-[#f5efe7] hover:bg-[#a83802]">Unlock</Button>
            </form>
          ) : (
            <ul className="flex flex-wrap gap-2.5">
              {PDFS.map((doc) => (
                <li key={doc.file}>
                  <button type="button" onClick={() => handleDownload(doc.file, doc.label)} disabled={downloading === doc.label} className="inline-flex min-h-11 items-center gap-2 rounded-full border border-border bg-background px-4 py-2.5 text-xs font-medium text-muted-foreground transition-colors hover:bg-secondary hover:text-foreground focus-visible:outline-2 focus-visible:outline-ring disabled:cursor-wait disabled:opacity-60">
                    <FileText className="h-4 w-4 text-primary" aria-hidden="true" />
                    {downloading === doc.label ? "Downloading…" : doc.label}
                    <Download className="h-3.5 w-3.5" aria-hidden="true" />
                  </button>
                </li>
              ))}
            </ul>
          )}
        </div>
        {error && <p className="mt-3 text-sm font-medium text-destructive" role="alert">{error}</p>}
        {authed && <p className="mt-3 text-xs text-muted-foreground">Password accepted. Click any document above to download.</p>}
      </div>
    </section>
  );
}

/* ══ Footer ══ */
export function Footer() {
  const { content } = useSiteContent();
  return (
    <footer className="mt-auto bg-[#401000] text-[#f5efe7]">
      <div className="mx-auto flex max-w-6xl flex-col items-center gap-6 px-4 py-12 text-center sm:px-6 md:flex-row md:items-start md:justify-between md:text-left">
        <div className="max-w-sm">
          <div className="flex items-center justify-center gap-3 md:justify-start">
            <span className="flex h-20 w-20 shrink-0 items-center justify-center overflow-hidden rounded-full bg-[#f5efe7]">
              <img src="/images/logo-seal.png?v=3" alt="Well Spring Intervention official seal" className="h-[4.6rem] w-[4.6rem] object-contain" loading="lazy" />
            </span>
            <span className="flex flex-col leading-none text-left">
              <span className="font-display text-lg font-semibold">Well Spring <span className="text-[#e07020]">Intervention</span></span>
              <span className="text-[0.6rem] font-medium uppercase tracking-[0.28em] text-[#f5efe7]/65">Level III Residential Treatment</span>
            </span>
          </div>
          <p className="mt-4 text-sm leading-relaxed text-[#f5efe7]/75">{content.footer.description}</p>
          <p className="mt-3 font-display text-sm italic text-[#e07020]">{content.hero.tagline}</p>
        </div>
        <div className="text-sm text-[#f5efe7]/75">
          <p className="font-medium text-[#f5efe7]">Licensing</p>
          <p className="mt-2 leading-relaxed">Licensed by the North Carolina Division of Health Service Regulation<br />under 10A NCAC 27G .1700</p>
        </div>
        <nav aria-label="Footer navigation" className="text-sm">
          <p className="font-medium text-[#f5efe7]">Explore</p>
          <ul className="mt-2 space-y-1.5">
            {NAV_LINKS.map((link) => (
              <li key={link.href}><Link href={link.href} className="text-[#f5efe7]/75 transition-colors hover:text-[#e07020] focus-visible:outline-2 focus-visible:outline-[#e07020]/60">{link.label}</Link></li>
            ))}
          </ul>
        </nav>
      </div>
      <div className="border-t border-white/10">
        <p className="mx-auto max-w-6xl px-4 py-5 text-center text-xs text-[#f5efe7]/60 sm:px-6">© {new Date().getFullYear()} Well Spring Intervention LLC. All rights reserved.</p>
      </div>
    </footer>
  );
}
