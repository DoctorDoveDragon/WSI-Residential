// Well Spring Intervention LLC — Brand Logo EDIT v5c
// Take v5b and ONLY fix the head — make it a hollow circle outline, not a solid fill.
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const INPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';
const OUTPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';

const EDIT_PROMPT = `Make ONLY ONE change to this image: convert the solid-filled head circle into a HOLLOW OUTLINE circle. The head should be just a thin walnut-brown outline circle with the cream background showing through the interior — NOT a solid walnut-brown filled circle.

DO NOT change anything else. The body, vessel, water, and heart are already correct outlines — leave them as they are. Preserve the composition, the warm cream background, the walnut-brown color, and the sleek modern minimalist aesthetic.

NO text, NO letters, NO numbers, NO watermarks.`;

async function main() {
  console.log('Editing logo icon v5b → v5c (hollow head outline only)...');
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
  console.log(`✓ Logo icon v5c saved to ${OUTPUT} (${outBuf.length} bytes)`);
}

main().catch((e) => {
  console.error('❌ Error:', e.message);
  console.error(e.stack);
  process.exit(1);
});
