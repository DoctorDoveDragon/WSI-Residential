// v2.13 cover refinement.
// User feedback on v2.12: "the fountain is too tall on this one. the pool is still there as well.
//   we want to see a stone with a heart shaped likeness with the fountain spring flowing from it."
//
// Two targeted edits on the v2.12b image (which already has the smooth heart-shaped stone + TALL jet + pool):
//   1. SHORTEN the vertical water jet — back to a modest natural-spring height (NOT a tall fountain plume).
//   2. REMOVE the pool of water at the base entirely — water springs directly from the heart-shaped stone
//      with no pooling/rippling water around it on the ground.
// The smooth heart-shaped stone, green leaves, tree-human figure, sunrise, painterly style, warm palette,
// 1344×768 horizontal, zero text — all preserved exactly.
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const INPUT = '/home/z/my-project/scripts/sop_cover_image_v212b.png';
const OUTPUT = '/home/z/my-project/scripts/sop_cover_image_v213.png';

const EDIT_PROMPT = `Preserve the entire composition exactly: a serene horizontal landscape featuring a stylized anthropomorphic tree-human figure with fresh vivid GREEN leaves, calm sunrise glowing over still water in the background, soft painterly dreamy art style, warm earthy palette. In the foreground directly in front of the tree there is a SMOOTH HEART-SHAPED STONE (two rounded lobes at the top curving down to meet at a gentle point at the bottom, in a soft warm earth-toned color, completely smooth and unmarked — no eyes, no mouth, no facial features, no carvings, no patterns, no texture lines). The heart-shaped stone itself must remain exactly as it is.

Make ONLY these two specific changes:

1. SHORTEN THE WATER JET. The current vertical jet of water spraying up from the heart-shaped stone is TOO TALL — it looks like a tall fountain plume. REDUCE its height significantly so it becomes a modest, gentle, natural spring — a SHORT slender vertical spurt of clear water bubbling gently upward only a small distance above the heart-shaped stone (roughly the height of the stone itself, or only slightly taller — maybe 1 to 1.5x the height of the stone). It should look like a small natural wellspring gently welling up, NOT a tall dramatic fountain. Keep the water clear and delicate with a few droplets catching the warm sunrise light. The wellspring remains NARROWER than the tree (only the HEIGHT is reduced; width stays the same).

2. REMOVE THE POOL ENTIRELY. There is currently a small pool of rippling/pooling water at the base of the wellspring on the ground. REMOVE this pool completely — there should be NO pooling water, NO puddle, NO ripples on the ground around the heart-shaped stone. The heart-shaped stone sits directly on the dry earthy ground (or on a few small pebbles), and the short slender jet of water bubbles up from the top/center of the stone and falls back down naturally without forming any pool at the base. The ground around the stone should be the same warm earthy terrain as the rest of the foreground — no water, no wetness, no reflections.

Keep absolutely everything else identical: same smooth heart-shaped stone in the same position, same green-leaved tree-human silhouette, same horizon line, same sunrise sky, same warm color palette, same painterly style, same composition and proportions.

Absolutely no text, no letters, no words, no numbers, no signatures, no watermarks, no typography of any language whatsoever.`;

async function main() {
  console.log('Loading source image (v2.12b cover with heart stone + tall jet + pool)...');
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
