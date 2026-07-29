// Well Spring Intervention LLC — Brand Logo EDIT v2d
// Take v2c (sleek male bent-over Aquarius) and ONLY fix the symmetry:
// - Move figure to be directly above the heart on the central vertical axis
// - Do NOT touch anything else
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const INPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';
const OUTPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';

const EDIT_PROMPT = `Recompose this logo icon for PERFECT LEFT-RIGHT SYMMETRY. Move the male figure so that he is positioned DIRECTLY ABOVE the heart stone on the SAME central vertical axis. The figure's body, the vessel, the water stream, and the heart stone must all align on the central vertical axis. The figure should straddle the heart with his two feet spaced equally left and right of the center line, his bent torso centered above the heart, and the vessel pouring water straight down onto the heart's top center.

DO NOT change anything else. Keep the male figure, the bent-over pose, the vessel tipped onto the heart, the grey stone heart, the warm cream background, the sleek clean line work, the warm earthy palette. No text, no letters, no numbers, no watermarks.`;

async function main() {
  console.log('Editing logo icon v2c → v2d (perfect symmetry only)...');
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
  console.log(`✓ Logo icon v2d saved to ${OUTPUT} (${outBuf.length} bytes)`);
}

main().catch((e) => {
  console.error('❌ Error:', e.message);
  console.error(e.stack);
  process.exit(1);
});
