import { NextRequest, NextResponse } from "next/server";
import { readFileSync, writeFileSync, mkdirSync } from "fs";
import path from "path";

export const dynamic = "force-dynamic";

/*
  Secure referral submission endpoint.

  PHI (Protected Health Information) is NEVER sent via email.
  Instead:
  1. The full referral is saved to /data/referrals/ on the server
  2. A notification email (containing NO PHI) is optionally sent
     via SMTP to alert staff that a new referral is waiting
  3. Staff log in to /admin to view the full referral securely

  This is the HIPAA-compliant pattern: PHI stays on the server,
  behind the password gate. The email only says "new referral received."
*/

const REFERRALS_DIR = path.join(process.cwd(), "data", "referrals");

function saveReferral(data: Record<string, string>): string {
  mkdirSync(REFERRALS_DIR, { recursive: true });
  const id = `ref_${Date.now()}_${Math.random().toString(36).slice(2, 8)}`;
  const filepath = path.join(REFERRALS_DIR, `${id}.json`);
  const record = {
    id,
    submittedAt: new Date().toISOString(),
    ...data,
  };
  writeFileSync(filepath, JSON.stringify(record, null, 2), "utf-8");
  return id;
}

function getReferrals() {
  try {
    mkdirSync(REFERRALS_DIR, { recursive: true });
    const files = readFileSync(path.join(REFERRALS_DIR, "index.json"), "utf-8");
    return JSON.parse(files);
  } catch {
    return [];
  }
}

function saveReferralIndex(referrals: unknown[]) {
  mkdirSync(REFERRALS_DIR, { recursive: true });
  writeFileSync(
    path.join(REFERRALS_DIR, "index.json"),
    JSON.stringify(referrals, null, 2),
    "utf-8"
  );
}

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();

    // Save the full referral (with PHI) to the server
    const id = saveReferral(body);

    // Add ONLY the submission ID and timestamp to the index — NO PHI
    // (child name, referrer name, agency are all PHI in the context of
    // a behavioral health referral)
    const summary = {
      id,
      submittedAt: new Date().toISOString(),
    };
    const referrals = getReferrals();
    referrals.unshift(summary);
    saveReferralIndex(referrals);

    // NO email notification — all referral data (including child's name)
    // is PHI and stays on the server behind the password gate.
    // Staff must check the admin panel at /admin to view new referrals.

    return NextResponse.json({ ok: true, id });
  } catch (err) {
    console.error("Referral submission error:", err);
    return NextResponse.json(
      { ok: false, error: "Could not submit referral. Please try again or call us directly." },
      { status: 500 }
    );
  }
}

// GET endpoint to list referrals (password-protected, used by admin)
export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url);
  const password = searchParams.get("password") || "";
  const expectedPassword = process.env.WSI_ADMIN_PASSWORD || process.env.WSI_DOCS_PASSWORD || "wellspring2024";

  if (password !== expectedPassword) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const referralId = searchParams.get("id");
  if (referralId) {
    // Return a specific referral (full PHI)
    try {
      const filepath = path.join(REFERRALS_DIR, `${referralId}.json`);
      const data = readFileSync(filepath, "utf-8");
      return NextResponse.json(JSON.parse(data), {
        headers: { "Cache-Control": "no-store" },
      });
    } catch {
      return NextResponse.json({ error: "Referral not found" }, { status: 404 });
    }
  }

  // Return the index (summaries only, no PHI)
  const referrals = getReferrals();
  return NextResponse.json({ referrals }, {
    headers: { "Cache-Control": "no-store" },
  });
}
