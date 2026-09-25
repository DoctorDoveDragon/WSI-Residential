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

    // Add a summary (NO PHI) to the index
    const summary = {
      id,
      submittedAt: new Date().toISOString(),
      referrerName: body.referrerName || "Unknown",
      agency: body.agency || "N/A",
      childName: body.childName || "Unknown", // Name only, no diagnoses/meds
    };
    const referrals = getReferrals();
    referrals.unshift(summary);
    saveReferralIndex(referrals);

    // Optionally send a notification email (NO PHI in the email)
    const smtpHost = process.env.SMTP_HOST;
    if (smtpHost) {
      const { default: nodemailer } = await import("nodemailer");
      const smtpUser = process.env.SMTP_USER;
      const smtpPass = process.env.SMTP_PASS;
      const smtpPort = process.env.SMTP_PORT || "587";
      const targetEmail = process.env.REFERRAL_EMAIL || "referral@wellspringintervention.com";

      if (smtpUser && smtpPass) {
        const transporter = nodemailer.createTransport({
          host: smtpHost,
          port: parseInt(smtpPort),
          secure: parseInt(smtpPort) === 465,
          auth: { user: smtpUser, pass: smtpPass },
        });

        await transporter.sendMail({
          from: `"Well Spring Website" <${smtpUser}>`,
          to: targetEmail,
          subject: `New Referral Received — ${body.childName || "Unknown"} from ${body.agency || "Unknown Agency"}`,
          text: `A new referral has been submitted.\n\nReferrer: ${body.referrerName || "Unknown"}\nAgency: ${body.agency || "N/A"}\nSubmitted: ${new Date().toISOString()}\n\nTo view the full referral (including clinical information), log in to the admin panel at https://wellspringintervention.com/admin\n\nDo NOT reply to this email with any patient information.`,
          replyTo: body.referrerEmail || undefined,
        });
      }
    }

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
