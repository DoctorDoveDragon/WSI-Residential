// Well Spring Intervention LLC — Brand Logo EDIT v6b
// Take v6 and ONLY fix the family figures — convert from solid silhouettes to hollow outlines
// (matching the rest of the icon's contour style).
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const INPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';
const OUTPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';

const EDIT_PROMPT = `Make ONLY ONE change to this image: convert the three solid-filled human figures (the family of adult woman, adult man, and child beneath the tree) into HOLLOW OUTLINE figures. Each figure should be just a thin walnut-brown outline (small circle outline for head, simple line outline for body, arms, and legs) with the cream background showing through the interior — NOT solid walnut-brown filled silhouettes.

DO NOT change anything else. The wellspring, tree trunk, heart-shaped canopy, leaves/droplets, and overall composition are already correct — leave them as they are. Preserve the warm cream background, the walnut-brown color, and the sleek modern minimalist aesthetic. Preserve the three figures' poses and gestures (the family holding hands in a caring gesture).

NO text, NO letters, NO numbers, NO watermarks.`;

async function main() {
  console.log('Editing logo icon v6 → v6b (hollow figure outlines only)...');
  const buf = fs.readFileSync(INPUT);
  const b64 = buf.toString('base64');
  const dataUrl = `data:image/png;base64,${b64}`;
  const zai = await ZAI.create();
  const response = await zai.images.generations.edit({
    prompt: EDIT_PROMPT,
    images: [{ url: dataUrl }],
    size: '1024x1024',
  });
  const outBuf = Buffer.from(response.data[0].base64, 'base64');
  fs.writeFileSync(OUTPUT, outBuf);
  console.log(`✓ Logo icon v6b saved to ${OUTPUT} (${outBuf.length} bytes)`);
}

main().catch((e) => {
  console.error('❌ Error:', e.message);
  console.error(e.stack);
  process.exit(1);
});
