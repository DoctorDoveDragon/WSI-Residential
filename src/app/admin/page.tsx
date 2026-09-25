"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { Button } from "@/components/ui/button";
import { useSiteContent, DEFAULT_CONTENT } from "@/lib/content-provider";
import { ArrowRight, Check, FileText, Lock, RefreshCw } from "lucide-react";

type ContentState = typeof DEFAULT_CONTENT;

type ReferralSummary = {
  id: string;
  submittedAt: string;
};

export default function AdminPage() {
  const { content, loading, refresh } = useSiteContent();
  const [password, setPassword] = useState("");
  const [authed, setAuthed] = useState(false);
  const [draft, setDraft] = useState<ContentState | null>(null);
  const [saving, setSaving] = useState(false);
  const [message, setMessage] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [referrals, setReferrals] = useState<ReferralSummary[]>([]);
  const [viewingReferral, setViewingReferral] = useState<Record<string, string> | null>(null);

  async function loadReferrals() {
    try {
      const res = await fetch(`/api/refer?password=${encodeURIComponent(password)}`, { cache: "no-store" });
      if (res.ok) {
        const data = await res.json();
        setReferrals(data.referrals || []);
      }
    } catch { /* ignore */ }
  }

  async function viewReferral(id: string) {
    try {
      const res = await fetch(`/api/refer?password=${encodeURIComponent(password)}&id=${id}`, { cache: "no-store" });
      if (res.ok) {
        const data = await res.json();
        setViewingReferral(data);
      }
    } catch { /* ignore */ }
  }

  useEffect(() => {
    if (authed) loadReferrals();
  }, [authed]);

  useEffect(() => {
    if (content && !draft) setDraft(JSON.parse(JSON.stringify(content)));
  }, [content, draft]);

  async function handleLogin(e: React.FormEvent) {
    e.preventDefault();
    setError(null);
    if (!password.trim()) { setError("Please enter the admin password."); return; }
    try {
      const res = await fetch("/api/content", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ password, verify: true }) });
      if (res.ok) setAuthed(true);
      else if (res.status === 401) setError("Incorrect password.");
      else setError("Login failed.");
    } catch { setError("Network error."); }
  }

  function updateField(path: string, value: string) {
    if (!draft) return;
    const keys = path.split(".");
    const newDraft = JSON.parse(JSON.stringify(draft));
    let obj = newDraft;
    for (let i = 0; i < keys.length - 1; i++) obj = obj[keys[i]];
    obj[keys[keys.length - 1]] = value;
    setDraft(newDraft);
  }

  function updateFaq(index: number, field: "q" | "a", value: string) {
    if (!draft) return;
    const newDraft = JSON.parse(JSON.stringify(draft));
    newDraft.faqs[index][field] = value;
    setDraft(newDraft);
  }

  function addFaq() {
    if (!draft) return;
    const newDraft = JSON.parse(JSON.stringify(draft));
    newDraft.faqs.push({ q: "New question?", a: "New answer." });
    setDraft(newDraft);
  }

  function removeFaq(index: number) {
    if (!draft) return;
    const newDraft = JSON.parse(JSON.stringify(draft));
    newDraft.faqs.splice(index, 1);
    setDraft(newDraft);
  }

  async function handleSave() {
    if (!draft) return;
    setSaving(true); setError(null); setMessage(null);
    try {
      const res = await fetch("/api/content", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ password, content: draft }) });
      if (res.ok) { setMessage("Saved! Changes are now live."); refresh(); }
      else if (res.status === 401) { setError("Session expired. Reload and log in again."); setAuthed(false); }
      else setError("Save failed.");
    } catch { setError("Network error."); }
    finally { setSaving(false); }
  }

  if (!authed) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-background px-4">
        <div className="w-full max-w-md rounded-[2rem] border border-border/70 bg-card p-8 shadow-lg sm:p-10">
          <div className="mb-6 text-center">
            <img src="/images/logo-seal.png?v=4" alt="Well Spring Intervention seal" className="mx-auto mb-4 h-16 w-16 object-contain" />
            <h1 className="font-display text-2xl font-semibold">Staff Login</h1>
            <p className="mt-2 text-sm text-muted-foreground">Edit your website content — phone, email, text, and FAQs.</p>
          </div>
          <form onSubmit={handleLogin} className="space-y-4">
            <div>
              <label htmlFor="admin-password" className="mb-1.5 block text-sm font-semibold">Password</label>
              <input id="admin-password" type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Enter the staff password" autoComplete="current-password" className="h-11 w-full rounded-lg border border-border bg-background px-4 text-sm focus-visible:outline-2 focus-visible:outline-ring" />
            </div>
            {error && <p className="text-sm font-medium text-destructive" role="alert">{error}</p>}
            <Button type="submit" className="h-11 w-full rounded-full bg-[#d05003] text-[#f5efe7] hover:bg-[#a83802]">Log In<ArrowRight className="ml-1.5 h-4 w-4" aria-hidden="true" /></Button>
          </form>
          <div className="mt-6 rounded-lg bg-secondary/50 p-4 text-center text-xs text-muted-foreground">
            <p className="font-semibold text-foreground">How to use this page:</p>
            <p className="mt-1">1. Enter the staff password and click Log In.<br />2. Edit any text fields (phone, email, headlines, FAQs).<br />3. Click &ldquo;Save Changes&rdquo; — updates go live instantly.</p>
            <p className="mt-2">Default password: <code className="rounded bg-secondary px-1.5 py-0.5 font-mono text-[#d05003]">wellspring2024</code></p>
          </div>
        </div>
      </div>
    );
  }

  if (loading || !draft) {
    return <div className="flex min-h-screen items-center justify-center bg-background"><RefreshCw className="h-8 w-8 animate-spin text-[#d05003]" aria-hidden="true" /></div>;
  }

  return (
    <div className="min-h-screen bg-background">
      <div className="sticky top-0 z-50 border-b border-border bg-card/95 backdrop-blur-md">
        <div className="mx-auto flex max-w-4xl items-center justify-between px-4 py-3 sm:px-6">
          <div><h1 className="font-display text-lg font-semibold">Content Editor</h1><p className="text-xs text-muted-foreground">Edit your site content — changes go live instantly</p></div>
          <div className="flex items-center gap-2">
            <Link href="/" className="inline-flex h-9 items-center rounded-full border border-border px-4 text-xs font-medium text-muted-foreground transition-colors hover:bg-secondary hover:text-foreground">← View Site</Link>
            <Button type="button" variant="outline" onClick={() => setDraft(JSON.parse(JSON.stringify(DEFAULT_CONTENT)))} className="h-9 rounded-full text-xs">Reset</Button>
            <Button type="button" onClick={handleSave} disabled={saving} className="h-9 rounded-full bg-[#d05003] text-[#f5efe7] hover:bg-[#a83802] disabled:opacity-60">{saving ? "Saving…" : "Save Changes"}<Check className="ml-1.5 h-4 w-4" aria-hidden="true" /></Button>
          </div>
        </div>
      </div>
      <div className="mx-auto max-w-4xl px-4 py-8 sm:px-6">
        {message && <div className="mb-6 rounded-xl border border-green-200 bg-green-50 p-4 text-sm text-green-800" role="status">{message}</div>}
        {error && <div className="mb-6 rounded-xl border border-red-200 bg-red-50 p-4 text-sm text-red-800" role="alert">{error}</div>}
        <Section title="Contact Information">
          <Field label="Phone Number (display)" value={draft.contact.phone} onChange={(v) => updateField("contact.phone", v)} />
          <Field label="Phone Link (tel: format)" value={draft.contact.phoneHref} onChange={(v) => updateField("contact.phoneHref", v)} help="Must start with tel:" />
          <Field label="Email Address" value={draft.contact.email} onChange={(v) => updateField("contact.email", v)} />
          <Field label="Location" value={draft.contact.location} onChange={(v) => updateField("contact.location", v)} />
        </Section>
        <Section title="Home Page Hero">
          <Field label="Headline" value={draft.hero.headline} onChange={(v) => updateField("hero.headline", v)} />
          <TextArea label="Body Text" value={draft.hero.body} onChange={(v) => updateField("hero.body", v)} rows={4} />
          <Field label="Tagline" value={draft.hero.tagline} onChange={(v) => updateField("hero.tagline", v)} />
        </Section>
        <Section title="About Page">
          <Field label="Heading" value={draft.about.heading} onChange={(v) => updateField("about.heading", v)} />
          <TextArea label="Body Paragraph 1" value={draft.about.body1} onChange={(v) => updateField("about.body1", v)} rows={4} />
          <TextArea label="Body Paragraph 2" value={draft.about.body2} onChange={(v) => updateField("about.body2", v)} rows={4} />
        </Section>
        <Section title="Footer">
          <TextArea label="Footer Description" value={draft.footer.description} onChange={(v) => updateField("footer.description", v)} rows={3} />
        </Section>
        <Section title="Frequently Asked Questions">
          <p className="mb-4 text-sm text-muted-foreground">Add, edit, or remove FAQ entries.</p>
          {draft.faqs.map((faq, i) => (
            <div key={i} className="mb-4 rounded-xl border border-border bg-background p-4">
              <div className="mb-2 flex items-center justify-between"><span className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">Question {i + 1}</span><button type="button" onClick={() => removeFaq(i)} className="text-xs font-medium text-destructive hover:underline">Remove</button></div>
              <Field label="Question" value={faq.q} onChange={(v) => updateFaq(i, "q", v)} />
              <TextArea label="Answer" value={faq.a} onChange={(v) => updateFaq(i, "a", v)} rows={3} />
            </div>
          ))}
          <Button type="button" variant="outline" onClick={addFaq} className="h-9 rounded-full text-xs">+ Add FAQ</Button>
        </Section>

        {/* Secure Referrals */}
        <section className="mb-8 rounded-2xl border border-[#d05003]/30 bg-card p-6 sm:p-8">
          <div className="mb-5 flex items-center gap-3">
            <FileText className="h-6 w-6 text-[#d05003]" aria-hidden="true" />
            <div>
              <h2 className="font-display text-xl font-semibold tracking-tight text-[#401000]">Secure Referrals</h2>
              <p className="text-xs text-muted-foreground">Online referral submissions from the /refer form. Contains PHI — view behind password only.</p>
            </div>
          </div>

          {viewingReferral ? (
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <h3 className="font-display text-lg font-semibold">Referral: {viewingReferral.childName || "Unknown"}</h3>
                <Button type="button" variant="outline" onClick={() => setViewingReferral(null)} className="h-9 rounded-full text-xs">← Back to List</Button>
              </div>
              <div className="rounded-xl border border-border bg-background p-6">
                <dl className="grid gap-4 sm:grid-cols-2">
                  {Object.entries(viewingReferral)
                    .filter(([key]) => key !== "id")
                    .map(([key, val]) => (
                      <div key={key} className={val && String(val).length > 60 ? "sm:col-span-2" : ""}>
                        <dt className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">{key.replace(/([A-Z])/g, " $1").replace(/^./, (c) => c.toUpperCase())}</dt>
                        <dd className="mt-1 text-sm leading-relaxed text-foreground">{String(val || "—")}</dd>
                      </div>
                    ))}
                </dl>
              </div>
            </div>
          ) : referrals.length === 0 ? (
            <p className="text-sm text-muted-foreground">No referrals submitted yet.</p>
          ) : (
            <div className="space-y-3">
              {referrals.map((r) => (
                <button
                  key={r.id}
                  type="button"
                  onClick={() => viewReferral(r.id)}
                  className="flex w-full items-center justify-between rounded-xl border border-border bg-background p-4 text-left transition-colors hover:bg-secondary/50 focus-visible:outline-2 focus-visible:outline-ring"
                >
                  <div>
                    <p className="font-semibold text-foreground">New Referral</p>
                    <p className="text-sm text-muted-foreground">{new Date(r.submittedAt).toLocaleString()}</p>
                  </div>
                  <div className="text-right">
                    <p className="text-xs font-medium text-[#d05003]">View →</p>
                  </div>
                </button>
              ))}
            </div>
          )}
        </section>

        <div className="mt-8 flex flex-col gap-3 border-t border-border pt-6 sm:flex-row sm:justify-between sm:items-center">
          <Link href="/" className="inline-flex h-11 items-center justify-center rounded-full border border-border px-6 text-sm font-medium text-muted-foreground transition-colors hover:bg-secondary hover:text-foreground">← Back to Website</Link>
          <Button type="button" onClick={handleSave} disabled={saving} className="h-11 rounded-full bg-[#d05003] text-[#f5efe7] hover:bg-[#a83802] disabled:opacity-60">{saving ? "Saving…" : "Save All Changes"}<Check className="ml-1.5 h-4 w-4" aria-hidden="true" /></Button>
        </div>
      </div>
    </div>
  );
}

function Section({ title, children }: { title: string; children: React.ReactNode }) {
  return <section className="mb-8 rounded-2xl border border-border/70 bg-card p-6 sm:p-8"><h2 className="mb-5 font-display text-xl font-semibold tracking-tight text-[#401000]">{title}</h2><div className="space-y-4">{children}</div></section>;
}

function Field({ label, value, onChange, placeholder, help }: { label: string; value: string; onChange: (v: string) => void; placeholder?: string; help?: string }) {
  return <div><label className="mb-1.5 block text-sm font-semibold text-foreground">{label}</label><input type="text" value={value} onChange={(e) => onChange(e.target.value)} placeholder={placeholder} className="h-11 w-full rounded-lg border border-border bg-background px-4 text-sm focus-visible:outline-2 focus-visible:outline-ring" />{help && <p className="mt-1 text-xs text-muted-foreground">{help}</p>}</div>;
}

function TextArea({ label, value, onChange, rows = 3 }: { label: string; value: string; onChange: (v: string) => void; rows?: number }) {
  return <div><label className="mb-1.5 block text-sm font-semibold text-foreground">{label}</label><textarea value={value} onChange={(e) => onChange(e.target.value)} rows={rows} className="w-full rounded-lg border border-border bg-background p-4 text-sm leading-relaxed focus-visible:outline-2 focus-visible:outline-ring" /></div>;
}
