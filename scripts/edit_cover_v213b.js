// v2.13b — second iteration on v2.13 to more aggressively:
//   1. SHORTEN the water jet to be NO TALLER than the heart-shaped stone itself
//      (a gentle natural wellspring bubbling up just a little, NOT a tall fountain plume).
//   2. REMOVE ALL water/moisture/pool/wet-patch from the ground around the stone —
//      the ground must be uniformly dry earthy terrain with no dark wet patches.
// The smooth heart-shaped stone, green leaves, tree-human figure, sunrise — all preserved.
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const INPUT = '/home/z/my-project/scripts/sop_cover_image_v213.png';
const OUTPUT = '/home/z/my-project/scripts/sop_cover_image_v213b.png';

const EDIT_PROMPT = `Preserve the entire composition exactly: a serene horizontal landscape featuring a stylized anthropomorphic tree-human figure with fresh vivid GREEN leaves, calm sunrise glowing over still water in the background, soft painterly dreamy art style, warm earthy palette. In the foreground directly in front of the tree there is a SMOOTH HEART-SHAPED STONE (two rounded lobes at the top curving down to meet at a gentle point at the bottom, in a soft warm pink/terracotta color, completely smooth and unmarked, glossy with a single highlight). The heart-shaped stone must remain exactly as it is — same shape, same color, same position, same smooth unmarked surface.

Make ONLY these two specific changes:

1. DRASTICALLY SHORTEN THE WATER JET. The current vertical jet of water spraying up from the heart-shaped stone is still far TOO TALL — it rises about 2 to 2.5 times the height of the stone and looks like a dramatic fountain plume. REDUCE THE HEIGHT SEVERELY so the water jet becomes a very SHORT, modest, gentle natural spring — the water should bubble up only a SMALL distance above the top of the heart-shaped stone, NO TALLER than the height of the stone itself (roughly equal to or shorter than the stone's vertical height). It should look like a small natural wellspring gently welling up from the heart and immediately falling back down — a brief bubbling spurt of water, NOT a tall vertical column or fountain. The water is clear and delicate with a few droplets catching the warm sunrise light. The wellspring remains NARROWER than the tree.

2. REMOVE ALL WATER FROM THE GROUND AROUND THE STONE. There is currently a darker wet patch / puddle of water at the base of the stone on the ground. REMOVE this entirely. The ground immediately around the heart-shaped stone must be the SAME warm dry earthy terrain as the rest of the foreground — uniformly dry, no puddle, no pool, no wet patch, no darker moist area, no water reflections, no ripples. The short water jet bubbles up from the top of the stone and falls back down naturally, with NO water accumulating on the ground — it just disappears into the air/earth. The entire foreground ground should be a uniform dry warm earthy color matching the rest of the scene.

Keep absolutely everything else identical: same smooth heart-shaped stone in the same position with the same glossy pink/terracotta color, same green-leaved tree-human silhouette, same horizon line, same sunrise sky, same warm color palette, same painterly style, same composition and proportions.

Absolutely no text, no letters, no words, no numbers, no signatures, no watermarks, no typography of any language whatsoever.`;

async function main() {
  console.log('Loading source image (v2.13 — heart stone good, jet still tall, pool still present)...');
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
