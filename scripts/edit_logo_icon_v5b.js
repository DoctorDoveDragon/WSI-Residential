// Well Spring Intervention LLC — Brand Logo EDIT v5b
// Take v5 (which has unwanted fills) and convert to a TRUE OUTLINE-ONLY line drawing.
// Remove all interior fills. Keep only the outer outlines of: figure, vessel, water, heart.
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const INPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';
const OUTPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';

const EDIT_PROMPT = `Convert this logo icon to a TRUE OUTLINE-ONLY LINE DRAWING. Remove ALL interior fills, shading, and color blocks. Keep ONLY the clean outer outlines of each element: the bent-over male figure, the tilted vessel, the water droplets/stream, and the heart shape on the ground.

The result must be:
- Pure line art — just thin outlines, NO fills inside any shape
- Single stroke weight throughout (thin, clean, ~3-4px equivalent)
- Single color: walnut brown outlines on warm cream background
- NO interior shading, NO crosshatching, NO gradients, NO solid color blocks
- The figure's body should be just an outline (the interior should be the cream background, not a fill)
- The vessel should be just an outline
- The heart should be just an outline
- The water should be a few simple outline droplets or lines

PRESERVE the composition: bent-over male figure, tilted vessel, water stream, stone heart on ground below. PRESERVE the sleek modern minimalist aesthetic.

NO text, NO letters, NO numbers, NO watermarks, NO plant stems, NO leaves.`;

async function main() {
  console.log('Editing logo icon v5 → v5b (true outline-only)...');
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
  console.log(`✓ Logo icon v5b saved to ${OUTPUT} (${outBuf.length} bytes)`);
}

main().catch((e) => {
  console.error('❌ Error:', e.message);
  console.error(e.stack);
  process.exit(1);
});
