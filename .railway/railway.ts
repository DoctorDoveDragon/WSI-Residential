import { defineRailway, preserve, project, service } from "railway/iac";

export default defineRailway(() => {
  const web = service("web", {
    start: "node .next/standalone/server.js",
    build: "npm run build",
    replicas: { "us-east4-eqdc4a": 1 },
    env: { PORT: "3000", HOSTNAME: "0.0.0.0", NODE_ENV: "production" },
  });

  return project("WSI", {
    resources: [web],
  });
});
