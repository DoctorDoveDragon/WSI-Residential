import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export function middleware(request: NextRequest) {
  // Skip middleware entirely for API routes — let them handle their own headers
  if (request.nextUrl.pathname.startsWith("/api")) {
    return NextResponse.next();
  }

  // Prevent browser caching of HTML pages so admin edits show immediately
  const response = NextResponse.next();
  response.headers.set("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0");
  response.headers.set("Pragma", "no-cache");
  response.headers.set("Expires", "0");

  return response;
}

// Only run middleware on page routes, NOT API routes
export const config = {
  matcher: ["/((?!_next/static|_next/image|favicon|images|forms|api).*)"],
};
