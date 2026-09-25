"use client";

import { useState } from "react";
import { Header, Footer } from "@/lib/sections";
import { Button } from "@/components/ui/button";
import { ArrowRight, CheckCircle2, ShieldCheck } from "lucide-react";

export default function ReferPage() {
  const [submitting, setSubmitting] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setSubmitting(true);
    setError(null);

    const formData = new FormData(e.currentTarget);
    const data: Record<string, string> = {};
    formData.forEach((value, key) => {
      data[key] = value as string;
    });

    try {
      const res = await fetch("/api/refer", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });
      const result = await res.json();
      if (result.ok) {
        setSubmitted(true);
        window.scrollTo({ top: 0, behavior: "smooth" });
      } else {
        setError(result.error || "Submission failed. Please try again.");
      }
    } catch {
      setError("Network error. Please try again or call us directly.");
    } finally {
      setSubmitting(false);
    }
  }

  if (submitted) {
    return (
      <>
        <Header />
        <main className="flex-1">
          <div className="mx-auto max-w-2xl px-4 py-24 text-center sm:px-6">
            <div className="mx-auto mb-6 flex h-16 w-16 items-center justify-center rounded-full bg-green-100">
              <CheckCircle2 className="h-8 w-8 text-green-600" aria-hidden="true" />
            </div>
            <h1 className="font-display text-3xl font-semibold tracking-tight sm:text-4xl">
              Referral Submitted.
            </h1>
            <p className="mt-4 text-lg leading-relaxed text-muted-foreground">
              Thank you. Your referral has been sent to our admissions team at
              referral@wellspringintervention.com. We will review it promptly and
              contact you within one business day. If you need immediate
              assistance, please call us directly.
            </p>
            <div className="mt-8 flex flex-col gap-3 sm:flex-row sm:justify-center">
              <Button asChild className="h-12 rounded-full bg-[#d05003] px-7 text-[#f5efe7] hover:bg-[#a83802]">
                <a href="/">Return to Home</a>
              </Button>
              <Button asChild variant="outline" className="h-12 rounded-full px-7">
                <a href="/admissions">Back to Admissions</a>
              </Button>
            </div>
          </div>
        </main>
        <Footer />
      </>
    );
  }

  return (
    <>
      <Header />
      <main className="flex-1">
        <div className="mx-auto max-w-3xl px-4 py-12 sm:px-6 md:py-16">
          <div className="mb-8 text-center">
            <p className="mb-3 inline-flex items-center gap-2 rounded-full border border-border bg-card px-4 py-1.5 text-xs font-medium text-muted-foreground">
              <ShieldCheck className="h-3.5 w-3.5 text-[#d05003]" aria-hidden="true" />
              Secure Online Referral Form
            </p>
            <h1 className="font-display text-3xl font-semibold tracking-tight sm:text-4xl">
              Refer a Child
            </h1>
            <p className="mt-4 text-lg leading-relaxed text-muted-foreground">
              Complete the form below and submit it securely. Your referral
              will be sent directly to our admissions team at
              referral@wellspringintervention.com. We respond within one
              business day.
            </p>
          </div>

          {error && (
            <div className="mb-6 rounded-xl border border-red-200 bg-red-50 p-4 text-sm text-red-800" role="alert">
              {error}
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-8">
            {/* Referring Party */}
            <FormSection title="Referring Party Information">
              <FieldRow>
                <FormField label="Referrer Name" name="referrerName" required />
                <FormField label="Agency" name="agency" />
              </FieldRow>
              <FieldRow>
                <FormField label="Title / Role" name="title" />
                <FormField label="Phone" name="referrerPhone" type="tel" required />
              </FieldRow>
              <FieldRow>
                <FormField label="Email" name="referrerEmail" type="email" required />
                <FormField label="Date of Referral" name="referralDate" type="date" />
              </FieldRow>
            </FormSection>

            {/* Child Information */}
            <FormSection title="Child / Adolescent Information">
              <FieldRow>
                <FormField label="Child's Name" name="childName" required />
                <FormField label="Preferred Name" name="preferredName" />
              </FieldRow>
              <FieldRow>
                <FormField label="Date of Birth" name="dob" type="date" required />
                <FormField label="Age" name="age" />
              </FieldRow>
              <FieldRow>
                <FormField label="Sex" name="sex" />
                <FormField label="Gender Identity" name="gender" />
              </FieldRow>
              <FieldRow>
                <FormField label="Race / Ethnicity" name="race" />
                <FormField label="Primary Language" name="language" />
              </FieldRow>
              <FormField label="Current Address" name="address" full />
            </FormSection>

            {/* Legal / Custody */}
            <FormSection title="Legal / Custody Information">
              <FieldRow>
                <FormField label="Legal Guardian(s)" name="guardian" />
                <FormField label="Custody Type" name="custodyType" />
              </FieldRow>
              <FieldRow>
                <FormField label="DSS Worker" name="dssWorker" />
                <FormField label="DSS Phone" name="dssPhone" type="tel" />
              </FieldRow>
              <FieldRow>
                <FormField label="Court Status" name="courtStatus" />
                <FormField label="Next Court Date" name="courtDate" type="date" />
              </FieldRow>
            </FormSection>

            {/* Clinical Summary */}
            <FormSection title="Clinical Summary">
              <TextAreaField label="Primary Diagnoses (DSM-5 / ICD-10)" name="diagnoses" rows={3} />
              <TextAreaField label="Current Medications" name="medications" rows={3} />
              <TextAreaField label="Behavioral Concerns / Reason for Referral" name="behavioralConcerns" rows={4} required />
              <TextAreaField label="Trauma History (summary)" name="traumaHistory" rows={4} />
            </FormSection>

            {/* Current Providers */}
            <FormSection title="Current Placements & Providers">
              <FormField label="Current Placement / School" name="currentPlacement" full />
              <FieldRow>
                <FormField label="Outpatient Therapist" name="therapist" />
                <FormField label="Therapist Phone" name="therapistPhone" type="tel" />
              </FieldRow>
              <FieldRow>
                <FormField label="Psychiatrist" name="psychiatrist" />
                <FormField label="Psychiatrist Phone" name="psychPhone" type="tel" />
              </FieldRow>
              <FieldRow>
                <FormField label="Primary Care Physician" name="pcp" />
                <FormField label="PCP Phone" name="pcpPhone" type="tel" />
              </FieldRow>
            </FormSection>

            {/* Insurance */}
            <FormSection title="Insurance / Funding">
              <FieldRow>
                <FormField label="Medicaid ID" name="medicaidId" />
                <FormField label="Managed Care Plan" name="mcp" />
              </FieldRow>
              <FieldRow>
                <FormField label="LME/MCO" name="lmeMco" />
                <FormField label="Private Insurance" name="privateInsurance" />
              </FieldRow>
            </FormSection>

            {/* Submit */}
            <div className="flex flex-col gap-3 border-t border-border pt-6 sm:flex-row sm:justify-end">
              <Button
                type="submit"
                disabled={submitting}
                className="h-12 rounded-full bg-[#d05003] px-8 text-base text-[#f5efe7] hover:bg-[#a83802] disabled:opacity-60"
              >
                {submitting ? "Submitting…" : "Submit Referral"}
                <ArrowRight className="ml-2 h-5 w-5" aria-hidden="true" />
              </Button>
            </div>
            <p className="text-center text-xs text-muted-foreground">
              Your submission is sent securely to referral@wellspringintervention.com.
              We respond within one business day.
            </p>
          </form>
        </div>
      </main>
      <Footer />
    </>
  );
}

function FormSection({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <section className="rounded-2xl border border-border/70 bg-card p-6 sm:p-8">
      <h2 className="mb-5 font-display text-lg font-semibold text-[#401000]">{title}</h2>
      <div className="space-y-4">{children}</div>
    </section>
  );
}

function FieldRow({ children }: { children: React.ReactNode }) {
  return <div className="grid gap-4 sm:grid-cols-2">{children}</div>;
}

function FormField({
  label,
  name,
  type = "text",
  required = false,
  full = false,
}: {
  label: string;
  name: string;
  type?: string;
  required?: boolean;
  full?: boolean;
}) {
  return (
    <div className={full ? "" : ""}>
      <label htmlFor={name} className="mb-1.5 block text-sm font-semibold text-foreground">
        {label} {required && <span className="text-[#d05003]">*</span>}
      </label>
      <input
        id={name}
        name={name}
        type={type}
        required={required}
        className="h-11 w-full rounded-lg border border-border bg-background px-4 text-sm focus-visible:outline-2 focus-visible:outline-ring"
      />
    </div>
  );
}

function TextAreaField({
  label,
  name,
  rows = 3,
  required = false,
}: {
  label: string;
  name: string;
  rows?: number;
  required?: boolean;
}) {
  return (
    <div>
      <label htmlFor={name} className="mb-1.5 block text-sm font-semibold text-foreground">
        {label} {required && <span className="text-[#d05003]">*</span>}
      </label>
      <textarea
        id={name}
        name={name}
        rows={rows}
        required={required}
        className="w-full rounded-lg border border-border bg-background p-4 text-sm leading-relaxed focus-visible:outline-2 focus-visible:outline-ring"
      />
    </div>
  );
}
