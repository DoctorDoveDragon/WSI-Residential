// Well Spring Intervention LLC — Brand Logo EDIT v6c
// Take v6b (single-color walnut outline) and:
//  1. ADD MORE COLOR — introduce a multi-color palette while keeping the warm cream bg:
//     - Cool aqua-blue for the wellspring water and droplets
//     - Soft sage/olive green for the tree canopy leaves
//     - Warm terracotta for the family figures (matches brand accent)
//     - Walnut brown retained for the tree trunk and heart canopy outline
//  2. TRANSFORM THE PUDDLE INTO A WELLSPRING — make the water source at the base clearly
//     a wellspring (water actively rising/bubbling up from a source), not just a flat puddle.
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const INPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';
const OUTPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';

const EDIT_PROMPT = `Make TWO changes to this logo icon:

1. ADD MULTI-COLOR PALETTE — Replace the single-color walnut-brown outline with a multi-color palette while keeping the warm cream background:
   - The WELLSPRING WATER and water droplets: cool aqua-blue (about #7aa5b8)
   - The TREE TRUNK and heart-shaped canopy outline: keep warm deep walnut brown (about #6b4d3f)
   - The LEAVES inside the heart canopy: soft sage green (about #7a8c5c)
   - The THREE FAMILY FIGURES (adult woman, adult man, child): warm terracotta (about #ab5125)
   - The wellspring basin/edge: cool grey (about #8a8a8a)
   Keep the outline-only contour line-art style. The colors should be applied as outline strokes (not solid fills) for the trunk, canopy, leaves, and family figures. The water can have small filled aqua droplets for visual emphasis.

2. TRANSFORM THE PUDDLE INTO A WELLSPRING — Make the water source at the base clearly a WELLSPRING (water actively rising/bubbling up from a source), not just a flat puddle or pool. Specifically:
   - Add a small visible stone basin/rim around the water source (cool grey outline) — like a natural well or spring opening
   - Make water clearly RISE UPWARD from the basin — show 3-5 small aqua-blue droplets or short curved lines bubbling upward from the basin, transitioning into the tree trunk
   - The water should look like it's actively emerging from below, not just sitting as a flat puddle

PRESERVE EVERYTHING ELSE:
   - The tree of life trunk rising from the wellspring
   - The heart-shaped canopy at the top
   - The leaves/droplets inside the canopy
   - The three family figures (adult woman, adult man, child) holding hands beneath the tree, as hollow outlines
   - The warm cream background
   - The sleek modern minimalist contour aesthetic
   - Single-weight stroke style
   - NO text, NO letters, NO numbers, NO watermarks

The result should be a more visually rich, multi-color minimalist icon with a clearly active wellspring at the base.`;

async function main() {
  console.log('Editing logo icon v6b → v6c (multi-color + wellspring)...');
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
  console.log(`✓ Logo icon v6c saved to ${OUTPUT} (${outBuf.length} bytes)`);
}

main().catch((e) => {
  console.error('❌ Error:', e.message);
  console.error(e.stack);
  process.exit(1);
});
