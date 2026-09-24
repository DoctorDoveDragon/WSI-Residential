# Well Spring Intervention — Website

A licensed, staff-secure Level III residential treatment facility website for
Wake County, North Carolina.

## Deploy to Railway

### Option A: Railway CLI (fastest)

```bash
# 1. Install Railway CLI (if not already installed)
npm install -g @railway/cli

# 2. Log in to Railway (opens browser)
railway login

# 3. Link this project to your Railway project
railway link

# 4. Add environment variables
railway variables set WSI_DOCS_PASSWORD=your_docs_password
railway variables set WSI_ADMIN_PASSWORD=your_admin_password

# 5. Deploy!
railway up
```

### Option B: GitHub + Railway Dashboard

1. Push this code to a GitHub repository
2. Go to [railway.app](https://railway.app) → New Project → Deploy from GitHub repo
3. Select this repo
4. Add environment variables in the Railway dashboard:
   - `WSI_DOCS_PASSWORD` — password for staff document downloads
   - `WSI_ADMIN_PASSWORD` — password for the admin content editor
5. Railway builds and deploys automatically

### Connect Your Domain (wellspringintervention.com)

1. In Railway: Settings → Networking → Custom Domains → Add `wellspringintervention.com`
2. Railway gives you a CNAME target
3. At Porkbun (your domain registrar), add:
   - CNAME record: `@` → Railway's CNAME target
   - CNAME record: `www` → Railway's CNAME target
4. Wait for DNS propagation (15 min – 24 hours)
5. Railway provisions HTTPS automatically

## Admin Panel

- **URL**: `https://wellspringintervention.com/admin`
- **Password**: Set via `WSI_ADMIN_PASSWORD` env var (defaults to `wellspring2024`)
- **What it does**: Edit phone, email, hero text, about text, footer, and FAQs
  without touching code. Changes go live instantly.

## Staff Document Downloads

- **Location**: Bottom of every page ("For Staff & Partners")
- **Password**: Set via `WSI_DOCS_PASSWORD` env var (defaults to `wellspring2024`)
- **Contents**: 14 internal documents (incident reports, treatment plans,
  shift logs, medication records, etc.) + 3 program documents (SOP Manual,
  CARF Plans, Audit Report)

## Public Referral Forms

- **Location**: `/admissions` page (no password needed)
- **Contents**: 9 downloadable PDF forms (referral, screening, admission,
  medical consent, medication consent, visitation, ROI, resident rights,
  grievance)

## Key Files

| File | Purpose |
|---|---|
| `src/lib/content.tsx` | All site content (text, data arrays, helpers) |
| `src/lib/sections.tsx` | All visual components (Header, Hero, sections, Footer) |
| `src/lib/content-provider.tsx` | Editable content context (feeds admin changes) |
| `src/app/admin/page.tsx` | Admin content editor |
| `src/app/api/download/route.ts` | Password-gated PDF downloads |
| `src/app/api/content/route.ts` | Content store (read/save) |
| `src/app/api/verify/route.ts` | Password verification endpoint |
| `src/app/globals.css` | Brand color palette (canonical seal colors) |
| `data/site-content.json` | Editable content store |
| `private-docs/` | Password-gated PDFs (23 files) |
| `public/forms/` | Public referral forms (9 PDFs) |
| `public/images/` | Logo assets (seal, icon, lockup, favicons) |
| `railway.json` | Railway deployment config |

## Tech Stack

- **Framework**: Next.js 16 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS 4 + shadcn/ui
- **Fonts**: Lora (display/headings) + Inter (body)
- **Animations**: Framer Motion
- **Icons**: Lucide React
- **PDF Generation**: ReportLab (Python)

## Local Development

```bash
npm install
npm run dev
# Visit http://localhost:3000
```

## Regenerate Branded Forms

```bash
pip install reportlab
python3 scripts/generate_branded_forms.py
```

This regenerates all 20 branded PDFs with the official Well Spring letterhead.
