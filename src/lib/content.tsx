"use client";

import {
  ArrowRight, ArrowUpRight, BedDouble, BookOpen, CheckCircle2, ClipboardList,
  Download, Droplets, FileText, GraduationCap, Heart, HeartHandshake, HeartPulse,
  Home, Mail, MapPin, Menu, MoonStar, Network, PartyPopper, Phone, ShieldCheck,
  Sprout, Users, UsersRound, X,
} from "lucide-react";

export {
  ArrowRight, ArrowUpRight, BedDouble, BookOpen, CheckCircle2, ClipboardList,
  Download, Droplets, FileText, GraduationCap, Heart, HeartHandshake, HeartPulse,
  Home, Mail, MapPin, Menu, MoonStar, Network, PartyPopper, Phone, ShieldCheck,
  Sprout, Users, UsersRound, X,
};

export const BRAND_TAGLINE = "Empowerment · Growth · Freedom · Health · Wholeness · Healing";
export const BRAND_SERVICES_LINE_1 = "Level III Residential Treatment Facility · Staff-Secure";
export const BRAND_SERVICES_LINE_2 = "Outpatient Therapy · Case Management · Psychosocial Rehabilitation";
export const REFERRAL_EMAIL = "referral@wellspringintervention.com";

export const NAV_LINKS: { href: string; label: string }[] = [
  { href: "/about", label: "About" },
  { href: "/promise", label: "Our Promise" },
  { href: "/people", label: "Our People" },
  { href: "/community", label: "Community" },
  { href: "/services", label: "Services" },
  { href: "/growing", label: "Growing" },
  { href: "/admissions", label: "Admissions" },
  { href: "/faq", label: "FAQ" },
  { href: "/resources", label: "Forms & Resources" },
  { href: "/contact", label: "Contact" },
];

/* Client-facing forms (public, no password) */
export const PUBLIC_FORMS = [
  { file: "WSI_Form_01_Referral_Intake.pdf", label: "Referral & Intake Request", description: "For referring professionals, LME/MCOs, and county DSS — start a referral." },
  { file: "WSI_Form_02_PrePlacement_Screening.pdf", label: "Pre-Placement Screening", description: "Clinical fit assessment — completed by WSI staff during screening." },
  { file: "WSI_Form_03_Admission_Application.pdf", label: "Admission Application", description: "Application for residential treatment placement — guardian + WSI." },
  { file: "WSI_Form_04_Medical_Consent.pdf", label: "Medical Consent", description: "Consent for routine and emergency medical care." },
  { file: "WSI_Form_05_Medication_Consent.pdf", label: "Medication Consent", description: "Consent for psychiatric and prescribed medication management." },
  { file: "WSI_Form_06_Visitation_Authorization.pdf", label: "Visitation Authorization", description: "Approved contacts and visitation preferences for your child." },
  { file: "WSI_Form_09_Release_of_Information.pdf", label: "Release of Information (ROI)", description: "Authorization to release / obtain protected health information." },
  { file: "WSI_Form_10_Resident_Rights.pdf", label: "Resident Rights", description: "Review and acknowledgment of resident rights." },
  { file: "WSI_Form_20_Grievance.pdf", label: "Grievance / Complaint", description: "For children, families, staff, and community members." },
];

/* Password-gated internal documents */
export const PDFS = [
  { file: "WSI_Form_07_Incident_Report.pdf", label: "F07 · Incident Report" },
  { file: "WSI_Form_08_Discharge_Planning.pdf", label: "F08 · Discharge Planning" },
  { file: "WSI_Form_11_Individualized_Treatment_Plan.pdf", label: "F11 · Individualized Treatment Plan" },
  { file: "WSI_Form_12_Behavior_Intervention_Plan.pdf", label: "F12 · Behavioral Intervention Plan" },
  { file: "WSI_Form_13_Daily_Progress_Note.pdf", label: "F13 · Daily Progress Note" },
  { file: "WSI_Form_14_Shift_Change_Log.pdf", label: "F14 · Shift Change / Night Watch Log" },
  { file: "WSI_Form_15_Medication_Log.pdf", label: "F15 · Medication Administration Record (MAR)" },
  { file: "WSI_Form_16_Emergency_Drill_Log.pdf", label: "F16 · Emergency Drill & Safety Log" },
  { file: "WSI_Form_17_Restraint_Debrief.pdf", label: "F17 · Restraint & Debriefing Checklist" },
  { file: "WSI_Form_18_Family_Team_Meeting.pdf", label: "F18 · Family Team (CFT) Meeting Notes" },
  { file: "WSI_Form_19_Staff_Training_Acknowledgment.pdf", label: "F19 · Staff SOP & Training Record" },
  { file: "Well_Spring_Intervention_SOP_Manual_v2.26_Public-Edition.pdf", label: "SOP Manual v2.26" },
  { file: "WSI_CARF_CYS_2026_Conformance_Plans.pdf", label: "CARF CYS 2026 Plans" },
  { file: "WSI_SOP_v2.24_Operational_Audit_Report.pdf", label: "Operational Audit Report" },
];

export const TRUST_ITEMS = [
  { icon: ShieldCheck, title: "Licensed by NC DHSR", text: "10A NCAC 27G .1700 residential treatment" },
  { icon: BedDouble, title: "Staff-Secure Level III", text: "Structured 24-hour residential treatment" },
  { icon: Users, title: "Small by Design", text: "A 4–6 child home where every child is truly known" },
  { icon: MoonStar, title: "Awake Supervision", text: "Trained staff on duty around the clock" },
];

export const VALUES = [
  { icon: ShieldCheck, title: "Safety Comes First", text: "Structured, predictable, and closely supervised — children do their bravest growing when they feel safe. Our environment, routines, and staffing are built around physical and emotional safety, the foundation for every therapeutic intervention.", href: "/resources", cta: "View Staff Resources" },
  { icon: HeartHandshake, title: "Therapeutic Relationships Heal", text: "Children grow best beside adults who keep showing up. Our licensed clinicians and trained professionals are chosen for warmth as much as skill — building the trusting therapeutic relationships that make real clinical work possible.", href: "/people", cta: "Meet Our People" },
  { icon: UsersRound, title: "Families Are Partners", text: "You know your child best. Parents and caregivers stay at the center of every treatment plan — with visits, calls, family therapy sessions, and a genuine voice in every clinical decision we make together.", href: "/admissions", cta: "For Parents & Caregivers" },
  { icon: GraduationCap, title: "Growing Toward Graduation", text: "Every school day, every new coping skill, every brave step builds toward the day a child walks out our door — and across their next graduation stage — emotionally regulated, therapeutically supported, and ready for what comes next.", href: "/growing", cta: "See the Growing Journey" },
];

export const PEOPLE_CARDS = [
  { icon: HeartHandshake, title: "A Therapist in Their Corner", text: "Every child has a primary licensed therapist who checks in daily, listens hard, and celebrates loudly — building the trusting therapeutic relationship that makes real clinical work possible.", href: "/contact", cta: "Reach Out to Us" },
  { icon: MoonStar, title: "Trained Professionals Around the Clock", text: "Two awake, trained direct care professionals for every one to four children — at breakfast, at homework time, through the night. Emotional support and safety, 24/7.", href: "/people", cta: "Meet Our People" },
  { icon: BookOpen, title: "Teachers Who Keep Them Moving", text: "Our education liaison enrolls every child in community school within days, attends every IEP meeting, and our staff provide homework support each evening — so credits keep counting, friendships keep growing, and graduations stay on schedule.", href: "/growing", cta: "See the Growing Journey" },
];

export const SERVICES = [
  { icon: MoonStar, title: "24/7 Supervised Living", text: "Awake, trained staff are present around the clock in a calm, home-like residence designed for both safety and everyday comfort — the stable container where therapeutic work can happen.", href: "/services", cta: "Explore Our Program" },
  { icon: ClipboardList, title: "Individualized Treatment", text: "Every child builds their own treatment plan with their licensed therapist — clinical goals alongside personal ones, like making a friend, catching up in math, or learning to regulate big emotions.", href: "/admissions", cta: "Start a Referral" },
  { icon: HeartPulse, title: "Clinical & Behavioral Support", text: "Individual therapy, group therapy, psychiatric medication management, and positive behavior support are woven into daily routines by licensed clinicians who know each child well.", href: "/resources", cta: "View Staff Resources" },
  { icon: Sprout, title: "Life Skills & Independence", text: "From morning routines to cooking, chores, and community outings, children practice coping skills, self-regulation, and daily living skills they will carry home.", href: "/growing", cta: "See the Growing Journey" },
  { icon: UsersRound, title: "Family Therapy & Engagement", text: "Visits, phone contact, and family therapy sessions keep parents and caregivers connected and central to their child's treatment — healing happens in families, not just in sessions.", href: "/admissions", cta: "For Parents & Caregivers" },
  { icon: GraduationCap, title: "School & Community Ties", text: "We enroll children in community schools, follow each child's IEP, coordinate transportation, and provide academic support — because therapeutic growth and educational progress go hand in hand.", href: "/growing", cta: "See the Growing Journey" },
];

export const MILESTONES = [
  { title: "Arrive & belong", text: "A warm welcome, a predictable routine, and a professional who is already on their side.", href: "/admissions" },
  { title: "Learn & grow", text: "Enrolled in community school within days, homework support every evening, and at least 14 hours a week of planned group activities.", href: "/growing" },
  { title: "Build & practice", text: "Cooking, chores, coping skills, and confidence — real skills for real life, practiced with professionals and teachers who care about them.", href: "/growing" },
  { title: "Graduate & celebrate", text: "Report cards, birthdays, and graduation ceremonies are celebrated loudly here. Every milestone matters.", href: "/growing" },
  { title: "Head home ready", text: "Planning for home begins on day one — so when the day comes, the family, the aftercare, and the next chapter are already prepared.", href: "/contact" },
];

export const MOMENTS = ["Birthdays", "Game nights", "Report-card wins", "Moving-on ceremonies", "Cooking night", "Garden days"];

export const BRAND_PROMISES = [
  { icon: Heart, title: "Commitment", text: "Children are held by a steady commitment here — not as a clinical outcome, but as a daily practice. Warmth at the breakfast table, a hand on a shoulder, a professional who remembers the small things. Commitment is the quietest, strongest thing we offer.", href: "/people", cta: "Meet the People Who Show Up" },
  { icon: Sprout, title: "Growth and Structure", text: "Every child is growing — academically, emotionally, socially, spiritually — and every child needs structure to do it safely. We name growth when we see it, we celebrate it loudly, and we wrap it in predictable routines and clear expectations.", href: "/growing", cta: "See the Growing & Graduating Journey" },
  { icon: Users, title: "Acceptance", text: "Children arrive exactly as they are — diagnoses, histories, hard days and all — and they are met with belonging, not conditions. Acceptance here is not passive; it is the active choice to welcome a child before we ever ask them to change.", href: "/about", cta: "Learn About Well Spring" },
  { icon: ShieldCheck, title: "Safety", text: "Physical and emotional safety is the ground everything else grows from. Structured routines, awake supervision, trauma-informed staff, and a home designed to feel like one — because children do their bravest healing only when they feel safe.", href: "/resources", cta: "View Staff Resources" },
  { icon: Droplets, title: "Replenishment", text: "A well spring is a source that never stops giving — and that is what we promise to be for every child. Steady, clear, quietly renewing. When a child gives all they have to healing, we give back twice over: rest, play, nourishment, and the simple joy of being a kid.", href: "/about", cta: "Return to the Well Spring" },
];

export const ECOSYSTEM_PARTNERS = [
  { icon: Network, title: "Alliance Health & LME/MCOs", text: "We are an in-network provider with Alliance Health and coordinate closely with Local Management Entities/Managed Care Organizations across the region. We understand the Tailored Plan system, Medicaid eligibility, and the care-coordination pathway." },
  { icon: Users, title: "Departments of Social Services", text: "Many of the children we serve arrive through county DSS placements. We partner with social workers at every step — from initial screening through discharge — sharing documentation, attending court reviews, and keeping the placing agency fully informed." },
  { icon: GraduationCap, title: "Local Schools & LEAs", text: "Our education liaison enrolls every child in a community school within days of arrival, attends every IEP meeting, and maintains written agreements with the local education authority." },
  { icon: HeartPulse, title: "Outpatient & Medical Providers", text: "We are one chapter in a child's larger care story. We coordinate with existing outpatient therapists, psychiatric providers, primary care physicians, and any specialist already involved — and we hand off cleanly at discharge." },
  { icon: Home, title: "Families & Caregivers", text: "Families are not visitors here — they are partners. We keep parents and guardians at the center of every plan, with visits, calls, and a genuine voice in every decision." },
  { icon: MapPin, title: "The Wake County Community", text: "Our children are part of this community. They attend local schools, visit local libraries, worship alongside neighbors, and give back through service projects. A child's stay here is not a withdrawal from life — it is a deeper participation in it." },
];

export const EXTERNAL_RESOURCES = [
  {
    category: "Referral & Placement",
    items: [
      { title: "NC DSS Child Welfare Services", description: "County Departments of Social Services coordinate out-of-home placements for children.", url: "https://www.ncdhhs.gov/divisions/social-services/child-welfare-services/requests-information" },
      { title: "NC DSS Social Services Forms (English)", description: "The full catalog of NC DSS forms — including the DSS-1700 Application Worksheet, placement agreements, consent forms, and incident report forms.", url: "https://policies.ncdhhs.gov/divisional-n-z/social-services/ss-forms/forms-in-english/" },
      { title: "NC LME/MCO Directory", description: "Find your county's LME/MCO for referral coordination and care management.", url: "https://www.ncdhhs.gov/providers/lme-mco-directory" },
    ],
  },
  {
    category: "Clinical & Coverage Policy",
    items: [
      { title: "NC Medicaid Clinical Coverage Policies", description: "Program-specific clinical coverage policies, including the residential treatment facility service definition and HCPCS coding requirements.", url: "https://medicaid.ncdhhs.gov/providers/program-specific-clinical-coverage-policies" },
      { title: "NC Medicaid Managed Care Playbook", description: "The provider playbook for NC Medicaid Managed Care and Tailored Plans — explains the billing, authorization, and care-coordination pathways.", url: "https://medicaid.ncdhhs.gov/providers/provider-playbook-nc-medicaid-managed-care" },
      { title: "NC Medicaid Tailored Care Management", description: "Information for providers participating in Tailored Care Management.", url: "https://medicaid.ncdhhs.gov/tailored-care-management/for-providers" },
    ],
  },
  {
    category: "Education & Special Populations",
    items: [
      { title: "NC DPI Exceptional Children", description: "The NC Department of Public Instruction oversees special education. IEP forms, DEC-series documents, and placement committee resources.", url: "https://www.dpi.nc.gov/districts-schools/classroom-support/exceptional-children" },
      { title: "NC DHHS Notice of Nondiscrimination", description: "The official notice informing individuals about nondiscrimination and accessibility requirements for DHHS programs and services.", url: "https://www.ncdhhs.gov/assistance/notice-informing-individuals-about-nondiscrimination-and-accessibility-requirements" },
    ],
  },
];

/* Helper components */
import { motion } from "framer-motion";

export function FadeIn({ children, delay = 0, className }: { children: React.ReactNode; delay?: number; className?: string }) {
  return (
    <motion.div className={className} initial={{ opacity: 0, y: 24 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true, margin: "-60px" }} transition={{ duration: 0.6, delay, ease: [0.22, 1, 0.36, 1] }}>
      {children}
    </motion.div>
  );
}

export function LogoMark({ className = "h-10 w-10" }: { className?: string }) {
  return <img src="/images/logo-icon.png?v=3" alt="" aria-hidden="true" className={className} />;
}

export function Wordmark() {
  return (
    <span className="flex flex-col leading-none">
      <span className="font-display text-lg font-semibold tracking-tight sm:text-xl">
        Well Spring <span className="text-[#d05003]">Intervention</span>
      </span>
      <span className="text-[0.6rem] font-medium uppercase tracking-[0.28em] text-muted-foreground">Level III Residential Treatment</span>
    </span>
  );
}

export function Eyebrow({ children }: { children: React.ReactNode }) {
  return <p className="mb-3 text-xs font-semibold uppercase tracking-[0.22em] text-primary/80">{children}</p>;
}

export function linkProps(href: string) {
  if (href.startsWith("/")) return { href, external: false };
  return { href, external: true, target: "_blank" as const, rel: "noopener noreferrer" };
}
