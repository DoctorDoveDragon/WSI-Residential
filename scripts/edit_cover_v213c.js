// v2.13c — final cleanup pass on v2.13b. The jet height is now correct (short bubbling spring),
// but there is still a subtle darker moist-looking patch on the ground at the base of the stone.
// This pass removes that patch so the ground is uniformly dry earthy terrain.
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const INPUT = '/home/z/my-project/scripts/sop_cover_image_v213b.png';
const OUTPUT = '/home/z/my-project/scripts/sop_cover_image_v213c.png';

const EDIT_PROMPT = `Preserve the entire composition exactly: a serene horizontal landscape featuring a stylized anthropomorphic tree-human figure with fresh vivid GREEN leaves, calm sunrise glowing over still water in the background, soft painterly dreamy art style, warm earthy palette. In the foreground directly in front of the tree there is a SMOOTH HEART-SHAPED STONE (two rounded lobes at the top curving down to meet at a gentle point at the bottom, in a soft warm pink/terracotta color, completely smooth and unmarked, glossy with a single highlight). A SHORT, modest, gentle natural spring of clear water bubbles up from the top of the heart-shaped stone (only about 1/4 to 1/3 the height of the stone itself) and immediately falls back down.

Make ONLY this one specific change:

There is currently a subtle darker moist-looking patch or wet shadow on the ground immediately around the base of the heart-shaped stone, suggesting pooled water or wetness. REMOVE this darker patch completely so the ground around the stone is uniformly dry. The ground immediately around and behind the heart-shaped stone must be the SAME warm earthy tan/orange color and texture as the rest of the dry foreground terrain — no darker wet patch, no puddle, no pool, no moist shadow, no water reflection, no ripples. The heart-shaped stone simply sits on dry warm earthy ground, and the short spring of water bubbles up from its top and falls back down naturally without any water accumulating on the ground at all. The entire foreground ground should be a uniform dry warm earthy color matching the rest of the scene, with no wet or dark patches anywhere near the stone.

Keep absolutely everything else identical: same smooth heart-shaped stone in the same position with the same glossy pink/terracotta color, same SHORT gentle bubbling water spring on top of the stone (do NOT change the jet height — keep it short), same green-leaved tree-human silhouette, same horizon line, same sunrise sky, same warm color palette, same painterly style, same composition and proportions.

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
