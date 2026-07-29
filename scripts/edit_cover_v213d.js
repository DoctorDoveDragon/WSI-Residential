// v2.13d — final cleanup pass on v2.13b. v2.13b has the correct SHORT jet but a subtle
// moist patch at the base. v2.13c failed because it disturbed the jet height.
// This pass uses STRICT preservation language for the jet and ONLY touches the ground.
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const INPUT = '/home/z/my-project/scripts/sop_cover_image_v213b.png';
const OUTPUT = '/home/z/my-project/scripts/sop_cover_image_v213d.png';

const EDIT_PROMPT = `CRITICAL PRESERVATION RULE: The vertical jet of water on top of the heart-shaped stone is already at the CORRECT short height (about 1/4 to 1/3 the height of the stone itself, like a gentle bubbling spring). DO NOT change the water jet in any way — do NOT make it taller, do NOT make it shorter, do NOT change its shape, do NOT change its position. The water jet MUST remain exactly as it currently is. Also DO NOT change the heart-shaped stone itself — same shape, same color, same position, same smooth unmarked glossy surface. Also DO NOT change the tree, the leaves, the sky, the sunrise, the horizon, or the painterly style. The ONLY thing that should change is the ground immediately around the base of the heart-shaped stone.

THE ONLY CHANGE TO MAKE: There is currently a subtle darker moist-looking patch or wet shadow on the ground immediately surrounding the base of the heart-shaped stone. Repaint that patch of ground so it matches the surrounding dry earthy terrain exactly — the same warm tan/orange/brown earthy color, the same texture, the same brightness. The ground immediately around and behind the heart-shaped stone should look identical to the dry earthy ground in the rest of the foreground. No darker patch, no puddle, no pool, no moist shadow, no water reflection, no ripples. The heart-shaped stone simply sits on dry warm earthy ground.

To be absolutely clear: the ONLY pixels that should change are the darker wet-looking pixels on the ground immediately around the base of the stone. Everything else — the stone, the water jet, the tree, the leaves, the sky, the sunrise, the horizon — must remain pixel-for-pixel identical.

Absolutely no text, no letters, no words, no numbers, no signatures, no watermarks, no typography of any language whatsoever.`;

async function main() {
  console.log('Loading source image (v2.13b — short jet correct, subtle wet patch to remove)...');
  const buf = fs.readFileSync(INPUT);
  const b64 = buf.toString('base64');
  const dataUrl = `data:image/png;base64,${b64}`;
  console.log(`Source: ${INPUT} (${buf.length} bytes)`);

  console.log('Calling image edit API (size=1344x768)...');
  const zai = await ZAI.create();
  const response = await zai.images.generations.edit({
    prompt: EDIT_PROMPT,
    images: [{ url: dataUrl }],
    size: '1344x768',
  });

  const outB64 = response.data[0].base64;
  const outBuf = Buffer.from(outB64, 'base64');
  fs.writeFileSync(OUTPUT, outBuf);
  console.log(`✓ Edited image saved to ${OUTPUT} (${outBuf.length} bytes)`);
}

main().catch((e) => {
  console.error('❌ Error:', e.message);
  process.exit(1);
});
