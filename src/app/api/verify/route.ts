import { NextRequest, NextResponse } from "next/server";

function getExpectedPassword(): string {
  return process.env.WSI_DOCS_PASSWORD || process.env.WSI_ADMIN_PASSWORD || "wellspring2024";
}

export async function POST(request: NextRequest) {
  let body: { password?: string };
  try { body = await request.json(); } catch { return NextResponse.json({ error: "Invalid JSON." }, { status: 400 }); }
  const password = body.password || "";
  if (!password) return NextResponse.json({ error: "Password required." }, { status: 400 });
  if (password !== getExpectedPassword()) return NextResponse.json({ error: "Incorrect password." }, { status: 401 });
  return NextResponse.json({ ok: true }, { headers: { "Cache-Control": "no-store" } });
}
