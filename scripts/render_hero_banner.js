#!/usr/bin/env node
/**
 * render_hero_banner.js — Render the homepage hero banner to a high-res PNG.
 *
 * Output:
 *   /home/z/my-project/download/Well_Spring_Hero_Banner.png  (1920x800 PNG)
 *
 * Render settings:
 *   - viewport 1920 x 800 (matches .poster dimensions in HTML)
 *   - deviceScaleFactor 1.0 → final PNG = 1920 x 800 (already web-resolution)
 *   - The .poster has a background image (brand image) + dark overlay gradient,
 *     so we screenshot the .poster element directly (NOT omitBackground — we
 *     WANT the background image and overlay to be captured).
 */
const path = require('path');
const { chromium } = require('playwright');

const HTML = '/home/z/my-project/scripts/hero_banner.html';
const PNG  = '/home/z/my-project/download/Well_Spring_Hero_Banner.png';

const VIEWPORT_W = 1920;
const VIEWPORT_H = 800;
const SCALE = 1.0;

(async () => {
  const browser = await chromium.launch({ args: ['--font-render-hinting=none'] });
  const context = await browser.newContext({
    viewport: { width: VIEWPORT_W, height: VIEWPORT_H },
    deviceScaleFactor: SCALE,
  });
  const page = await context.newPage();

  const fileUrl = 'file://' + HTML;
  console.log(`→ Rendering hero banner: ${HTML}`);
  await page.goto(fileUrl, { waitUntil: 'networkidle' });
  // Wait for web fonts + background image to load
  await page.evaluate(() => {
    return Promise.all([
      document.fonts.ready,
      // Wait for the background image (loaded via CSS) — Image object trick
      new Promise((resolve) => {
        const url = getComputedStyle(document.querySelector('.poster')).backgroundImage;
        const m = url.match(/url\(["']?(.+?)["']?\)/);
        if (m) {
          const img = new Image();
          img.onload = resolve;
          img.onerror = resolve;
          img.src = m[1].replace(/^file:\/\//, '');
          setTimeout(resolve, 3000); // hard timeout
        } else { resolve(); }
      }),
      // Wait for the seal <img>
      ...Array.from(document.images).map(img =>
        img.complete ? Promise.resolve() :
          new Promise(r => { img.onload = r; img.onerror = r; })
      ),
    ]);
  });
  await page.waitForTimeout(800);

  const poster = await page.$('.poster');
  if (!poster) {
    console.error('✗ .poster element not found');
    process.exit(1);
  }
  await poster.screenshot({ path: PNG, type: 'png', omitBackground: false });
  const fs = require('fs');
  const stat = fs.statSync(PNG);
  console.log(`  ✓ wrote ${PNG} (${(stat.size / 1024).toFixed(1)} KB)`);

  await browser.close();
  console.log('Done.');
})().catch(err => {
  console.error('Fatal:', err);
  process.exit(1);
});
