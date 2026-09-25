import { NextRequest, NextResponse } from "next/server";
import { readFileSync, existsSync } from "fs";
import path from "path";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

const ALLOWED_DOCS = new Set([
  "WSI_CARF_CYS_2026_Conformance_Plans.pdf",
  "WSI_SOP_v2.22_Compliance_Audit_Report.pdf",
  "WSI_SOP_v2.22_Compliance_Audit_Crosswalk.xlsx",
  "WSI_SOP_v2.24_Operational_Audit_Report.pdf",
  "Well_Spring_Intervention_SOP_Manual_LATEST.pdf",
  "Well_Spring_Intervention_SOP_Manual_v2.26_Public-Edition.pdf",
  "Well_Spring_Resident_Handbook_v1.1.pdf",
  "WSI_Form_07_Incident_Report.pdf",
  "WSI_Form_08_Discharge_Planning.pdf",
  "WSI_Form_09_Release_of_Information.pdf",
  "WSI_Form_10_Resident_Rights.pdf",
  "WSI_Form_11_Individualized_Treatment_Plan.pdf",
  "WSI_Form_12_Behavior_Intervention_Plan.pdf",
  "WSI_Form_13_Daily_Progress_Note.pdf",
  "WSI_Form_14_Shift_Change_Log.pdf",
  "WSI_Form_15_Medication_Log.pdf",
  "WSI_Form_16_Emergency_Drill_Log.pdf",
  "WSI_Form_17_Restraint_Debrief.pdf",
  "WSI_Form_18_Family_Team_Meeting.pdf",
  "WSI_Form_19_Staff_Training_Acknowledgment.pdf",
  "WSI_Form_20_Grievance.pdf",
]);

function getExpectedPassword(): string {
  return process.env.WSI_DOCS_PASSWORD || "wellspring2024";
}

function getContentType(filename: string): string {
  if (filename.endsWith(".xlsx")) return "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet";
  if (filename.endsWith(".pdf")) return "application/pdf";
  return "application/octet-stream";
}

function findFile(filename: string): string | null {
  const possiblePaths = [
    path.join(process.cwd(), "private-docs", filename),
    path.join(process.cwd(), ".next", "standalone", "private-docs", filename),
    path.join("/app", "private-docs", filename),
    path.join("/app", ".next", "standalone", "private-docs", filename),
  ];
  for (const p of possiblePaths) {
    if (existsSync(p)) return p;
  }
  return null;
}

export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url);
  const doc = searchParams.get("doc") || "";
  const password = searchParams.get("password") || "";
  if (!ALLOWED_DOCS.has(doc)) return NextResponse.json({ error: "Unknown document." }, { status: 404 });
  if (!password || password !== getExpectedPassword()) return NextResponse.json({ error: "Invalid or missing password." }, { status: 401 });
  try {
    const filePath = findFile(doc);
    if (!filePath) return NextResponse.json({ error: "File not found on server." }, { status: 404 });
    const buffer = readFileSync(filePath);
    return new NextResponse(buffer, {
      status: 200,
      headers: {
        "Content-Type": getContentType(doc),
        "Content-Disposition": `attachment; filename="${doc}"`,
        "Content-Length": buffer.length.toString(),
        "Cache-Control": "no-store",
      },
    });
  } catch {
    return NextResponse.json({ error: "File could not be read." }, { status: 500 });
  }
}
