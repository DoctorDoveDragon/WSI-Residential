import { defineRailway, preserve, project, service } from "railway/iac";

export default defineRailway(() => {
  const web = service("web", {
    start: "node server.js",
    replicas: { "us-east4-eqdc4a": 1 },
    domains: ["wellspringintervention.com", "www.wellspringintervention.com"],
    env: { HOSTNAME: preserve(), NODE_ENV: preserve(), PORT: preserve(), REFERRAL_EMAIL: preserve(), WSI_ADMIN_PASSWORD: preserve(), WSI_DOCS_PASSWORD: preserve() },
  });

  return project("WSI", {
    resources: [web],
  });
});
