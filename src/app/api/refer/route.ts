import { NextRequest, NextResponse } from "next/server";
import nodemailer from "nodemailer";

export const dynamic = "force-dynamic";

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();

    // Build the email body from the form submission
    const emailBody = `
NEW REFERRAL SUBMISSION — Well Spring Intervention

═══════════════════════════════════════════════════════
 REFERRING PARTY INFORMATION
═══════════════════════════════════════════════════════
Referrer Name:    ${body.referrerName || "N/A"}
Agency:          ${body.agency || "N/A"}
Title / Role:    ${body.title || "N/A"}
Phone:           ${body.referrerPhone || "N/A"}
Email:           ${body.referrerEmail || "N/A"}
Date of Referral: ${body.referralDate || "N/A"}

═══════════════════════════════════════════════════════
 CHILD / ADOLESCENT INFORMATION
═══════════════════════════════════════════════════════
Child's Name:      ${body.childName || "N/A"}
Preferred Name:    ${body.preferredName || "N/A"}
Date of Birth:     ${body.dob || "N/A"}
Age:              ${body.age || "N/A"}
Sex:              ${body.sex || "N/A"}
Gender Identity:   ${body.gender || "N/A"}
Race / Ethnicity:  ${body.race || "N/A"}
Primary Language: ${body.language || "N/A"}
Current Address:  ${body.address || "N/A"}

═══════════════════════════════════════════════════════
 LEGAL / CUSTODY INFORMATION
═══════════════════════════════════════════════════════
Legal Guardian(s): ${body.guardian || "N/A"}
Custody Type:     ${body.custodyType || "N/A"}
DSS Worker:        ${body.dssWorker || "N/A"}
DSS Phone:         ${body.dssPhone || "N/A"}
Court Status:     ${body.courtStatus || "N/A"}
Next Court Date:   ${body.courtDate || "N/A"}

═══════════════════════════════════════════════════════
 CLINICAL SUMMARY
═══════════════════════════════════════════════════════
Primary Diagnoses (DSM-5 / ICD-10):
${body.diagnoses || "N/A"}

Current Medications:
${body.medications || "N/A"}

Behavioral Concerns / Reason for Referral:
${body.behavioralConcerns || "N/A"}

Trauma History (summary):
${body.traumaHistory || "N/A"}

═══════════════════════════════════════════════════════
 CURRENT PLACEMENTS & PROVIDERS
═══════════════════════════════════════════════════════
Current Placement / School: ${body.currentPlacement || "N/A"}
Outpatient Therapist:       ${body.therapist || "N/A"}
Therapist Phone:            ${body.therapistPhone || "N/A"}
Psychiatrist:               ${body.psychiatrist || "N/A"}
Psychiatrist Phone:         ${body.psychPhone || "N/A"}
Primary Care Physician:     ${body.pcp || "N/A"}
PCP Phone:                  ${body.pcpPhone || "N/A"}

═══════════════════════════════════════════════════════
 INSURANCE / FUNDING
═══════════════════════════════════════════════════════
Medicaid ID:        ${body.medicaidId || "N/A"}
Managed Care Plan: ${body.mcp || "N/A"}
LME/MCO:           ${body.lmeMco || "N/A"}
Private Insurance: ${body.privateInsurance || "N/A"}

═══════════════════════════════════════════════════════
 SUBMITTED
═══════════════════════════════════════════════════════
Timestamp: ${new Date().toISOString()}
`;

    // Configure the email transporter
    // Uses environment variables for SMTP credentials
    // Falls back to a simple approach if no SMTP is configured
    const smtpHost = process.env.SMTP_HOST;
    const smtpPort = process.env.SMTP_PORT || "587";
    const smtpUser = process.env.SMTP_USER;
    const smtpPass = process.env.SMTP_PASS;
    const targetEmail = process.env.REFERRAL_EMAIL || "referral@wellspringintervention.com";

    if (!smtpHost || !smtpUser || !smtpPass) {
      // No SMTP configured — log the submission and return success
      // The email body is still available in the response for debugging
      console.log("=== REFERRAL SUBMISSION (no SMTP configured) ===");
      console.log(emailBody);
      return NextResponse.json({
        ok: true,
        message: "Referral submitted. (Note: SMTP not configured — set SMTP_HOST, SMTP_USER, SMTP_PASS env vars to enable email delivery.)",
      });
    }

    const transporter = nodemailer.createTransport({
      host: smtpHost,
      port: parseInt(smtpPort),
      secure: parseInt(smtpPort) === 465,
      auth: { user: smtpUser, pass: smtpPass },
    });

    await transporter.sendMail({
      from: `"Well Spring Website" <${smtpUser}>`,
      to: targetEmail,
      subject: `New Referral: ${body.childName || "Unknown Child"} — ${body.agency || "No Agency"}`,
      text: emailBody,
      replyTo: body.referrerEmail || undefined,
    });

    return NextResponse.json({ ok: true, message: "Referral email sent successfully." });
  } catch (err) {
    console.error("Referral submission error:", err);
    return NextResponse.json(
      { ok: false, error: "Could not submit referral. Please try again or call us directly." },
      { status: 500 }
    );
  }
}
