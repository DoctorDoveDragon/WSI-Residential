import { NextRequest, NextResponse } from "next/server";
import { readFileSync, writeFileSync } from "fs";
import path from "path";

const CONTENT_FILE = path.join(process.cwd(), "data", "site-content.json");

function getExpectedPassword(): string {
  return process.env.WSI_ADMIN_PASSWORD || process.env.WSI_DOCS_PASSWORD || "wellspring2024";
}

function readContent(): Record<string, unknown> {
  try { return JSON.parse(readFileSync(CONTENT_FILE, "utf-8")); } catch { return {}; }
}

export async function GET() {
  try {
    return NextResponse.json(readContent(), { headers: { "Cache-Control": "no-store" } });
  } catch { return NextResponse.json({ error: "Could not read content." }, { status: 500 }); }
}

export async function POST(request: NextRequest) {
  let body: Record<string, unknown>;
  try { body = await request.json(); } catch { return NextResponse.json({ error: "Invalid JSON." }, { status: 400 }); }
  const password = body.password as string;
  const verifyOnly = body.verify === true;
  if (!password || password !== getExpectedPassword()) return NextResponse.json({ error: "Invalid or missing password." }, { status: 401 });
  if (verifyOnly) return NextResponse.json({ ok: true });
  const content = body.content;
  if (!content || typeof content !== "object") return NextResponse.json({ error: "Missing 'content' field." }, { status: 400 });
  try {
    writeFileSync(CONTENT_FILE, JSON.stringify(content, null, 2), "utf-8");
    return NextResponse.json({ ok: true });
  } catch { return NextResponse.json({ error: "Could not save content." }, { status: 500 }); }
}
