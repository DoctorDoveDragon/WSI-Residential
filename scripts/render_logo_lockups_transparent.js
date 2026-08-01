#!/usr/bin/env node
/**
 * render_logo_lockups_transparent.js — Render the two transparent-background
 * lockup HTML files to high-res PNGs with alpha.
 *
 * Outputs (all 2800x875 RGBA PNG, transparent background):
 *   /home/z/my-project/download/Well_Spring_Logo_Lockup_Transparent.png
 *   /home/z/my-project/download/Well_Spring_Logo_Lockup_Residential_Transparent.png
 *
 * Render settings:
 *   - viewport 1792 x 560 (matches .poster dimensions in HTML)
 *   - deviceScaleFactor 1.5625 → final PNG = 2800 x 875
 *   - .poster has transparent background; screenshot uses omitBackground:true
 *     so the resulting PNG has alpha channel.
 */

const path = require('path');
const { chromium } = require('playwright');

const INPUTS = [
  {
    html: '/home/z/my-project/scripts/logo_lockup_transparent.html',
    png:  '/home/z/my-project/download/Well_Spring_Logo_Lockup_Transparent.png',
    label: 'general icon (transparent)',
  },
  {
    html: '/home/z/my-project/scripts/logo_lockup_residential_transparent.html',
    png:  '/home/z/my-project/download/Well_Spring_Logo_Lockup_Residential_Transparent.png',
    label: 'residential seal (transparent)',
  },
];

const VIEWPORT_W = 1792;
const VIEWPORT_H = 560;
const SCALE = 1.5625;

(async () => {
  const browser = await chromium.launch({ args: ['--font-render-hinting=none'] });
  const context = await browser.newContext({
    viewport: { width: VIEWPORT_W, height: VIEWPORT_H },
    deviceScaleFactor: SCALE,
  });
  const page = await context.newPage();

  for (const { html, png, label } of INPUTS) {
    const fileUrl = 'file://' + html;
    console.log(`→ Rendering ${label}: ${html}`);
    await page.goto(fileUrl, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(500);

    const poster = await page.$('.poster');
    if (!poster) {
      console.error(`✗ .poster element not found in ${html}`);
      continue;
    }
    // omitBackground:true → PNG has alpha channel
    await poster.screenshot({ path: png, type: 'png', omitBackground: true });
    const fs = require('fs');
    const stat = fs.statSync(png);
    console.log(`  ✓ wrote ${png} (${(stat.size / 1024).toFixed(1)} KB)`);
  }

  await browser.close();
  console.log('Done.');
})().catch(err => {
  console.error('Fatal:', err);
  process.exit(1);
});
