import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export function middleware(request: NextRequest) {
  // Handle preflight OPTIONS requests for API calls
  if (request.method === "OPTIONS" && request.nextUrl.pathname.startsWith("/api")) {
    const response = new NextResponse(null, { status: 204 });
    response.headers.set("Access-Control-Allow-Origin", "*");
    response.headers.set("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
    response.headers.set("Access-Control-Allow-Headers", "Content-Type");
    return response;
  }

  const response = NextResponse.next();

  // Add CORS headers for API routes
  if (request.nextUrl.pathname.startsWith("/api")) {
    response.headers.set("Access-Control-Allow-Origin", "*");
    response.headers.set("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
    response.headers.set("Access-Control-Allow-Headers", "Content-Type");
    return response;
  }

  // Prevent browser caching of HTML pages so admin edits show immediately
  response.headers.set("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0");
  response.headers.set("Pragma", "no-cache");
  response.headers.set("Expires", "0");

  return response;
}

export const config = {
  matcher: ["/((?!_next/static|_next/image|favicon|images|forms).*)"],
};
