#!/usr/bin/env node
/**
 * render_logo_lockups.js — Render both logo lockup HTML files to high-res PNGs.
 *
 * Outputs:
 *   /home/z/my-project/download/Well_Spring_Logo_Lockup.png            (overwrite, general icon)
 *   /home/z/my-project/download/Well_Spring_Logo_Lockup_Residential.png (new, residential seal)
 *
 * Render settings:
 *   - viewport 1792 x 560 (matches .poster dimensions in HTML)
 *   - deviceScaleFactor 1.5625 → final PNG = 2800 x 875 (matches existing file)
 *   - transparent body background — but .poster has cream background, so PNG
 *     will be cream (matches brand).
 */

const path = require('path');
const { chromium } = require('playwright');

const INPUTS = [
  {
    html: '/home/z/my-project/scripts/logo_lockup.html',
    png:  '/home/z/my-project/download/Well_Spring_Logo_Lockup.png',
    label: 'general icon',
  },
  {
    html: '/home/z/my-project/scripts/logo_lockup_residential.html',
    png:  '/home/z/my-project/download/Well_Spring_Logo_Lockup_Residential.png',
    label: 'residential seal',
  },
];

const VIEWPORT_W = 1792;
const VIEWPORT_H = 560;
const SCALE = 1.5625; // 1792 * 1.5625 = 2800 ; 560 * 1.5625 = 875

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
    // Wait for web fonts (Cormorant Garamond + Inter) to fully load
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(500);

    // Screenshot the .poster element (avoids any body margin/padding)
    const poster = await page.$('.poster');
    if (!poster) {
      console.error(`✗ .poster element not found in ${html}`);
      continue;
    }
    await poster.screenshot({ path: png, type: 'png', omitBackground: false });
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
