// v2.14 — restart from v2.10 cover image (green leaves + tree-human + sunrise + wide circular stone basin + tall vertical jet + pool).
// Per the user's new direction:
//   "ok we are starting with 2.10 again. the heart stone has a grey stone look.
//    A small crack in the stone has the spring rising about belly high to the tree in the back ground.
//    there is no hole or pool."
//
// Translation into edit instructions:
//   1. REMOVE the entire existing wide circular stone basin AND the tall vertical jet of water AND the circular pool of water at the base — replace all of that foreground wellspring structure with a SINGLE GREY HEART-SHAPED STONE.
//   2. The heart-shaped stone should be GREY (a natural grey river-stone / granite color, NOT pink, NOT terracotta, NOT rose — a cool grey stone with subtle natural stony texture, like weathered granite).
//   3. The heart-shaped stone should have a SMALL CRACK running across its surface (a thin irregular fissure, natural stone crack, not a smooth cut — the kind of crack an old weathered stone would develop).
//   4. The water spring rises FROM THE CRACK in the heart-shaped stone — clear water emerges from the crack and rises vertically into the air. The water reaches about BELLY-HIGH of the tree in the background (i.e. roughly the lower third of the tree trunk, around 1/3 to 1/2 the height of the tree trunk before the branches/leaves begin — significantly TALLER than the heart-shaped stone itself, but shorter than the tree's full height).
//   5. There is NO HOLE on the ground (no opening, no orifice in the earth — the water comes from the crack in the stone, not from the ground).
//   6. There is NO POOL of water at the base — the heart-shaped stone sits directly on dry warm earthy terrain, and the water that rises from the crack falls back down naturally without forming any pool, puddle, or wet patch on the ground.
//
// PRESERVE EXACTLY from v2.10: the stylized tree-human figure, the fresh vivid green leaves, the horizon line, the calm sunrise sky, the warm earthy palette, the soft painterly dreamy art style, the 1344x768 horizontal aspect ratio.
// Zero text/letters/numbers/watermarks of any language.
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const INPUT = '/home/z/my-project/scripts/sop_cover_image_v210_source.png';
const OUTPUT = '/home/z/my-project/scripts/sop_cover_image_v214.png';

const EDIT_PROMPT = `Preserve the entire background composition exactly: a serene horizontal landscape featuring a stylized anthropomorphic tree-human figure with fresh vivid GREEN leaves, calm sunrise glowing over still water in the background, soft painterly dreamy art style, warm earthy palette. The tree, leaves, horizon line, sunrise sky, color palette, and painterly style must all remain IDENTICAL to the source image.

Make these SPECIFIC changes to the FOREGROUND wellspring area only (currently a wide circular stone basin with a tall narrow vertical jet of water and a circular pool of water at the base):

1. REMOVE the entire wide circular stone basin. REMOVE the entire tall narrow vertical jet of water shooting up from the basin. REMOVE the entire circular pool of water. All of these foreground wellspring elements from the source image must be GONE.

2. REPLACE all of that with a SINGLE GREY HEART-SHAPED STONE sitting on the ground directly in front of the tree, in the immediate foreground. The heart-shaped stone should be:
   - GREY in color — a natural cool grey stone color, like weathered granite or river stone. NOT pink, NOT terracotta, NOT rose, NOT brown. A medium grey with subtle natural stony texture (very faint mineral speckling or grain, like real granite).
   - Shaped like a heart: two rounded lobes at the top curving down to meet at a gentle point at the bottom.
   - Modest in size — about the size of a large river stone or a small boulder, sitting directly on the dry earthy ground in the foreground directly before the tree.
   - The stone surface is mostly smooth (natural weathered stone surface) — NOT glossy, NOT polished. It looks like real natural grey stone.
   - Completely free of any facial features — no eyes, no mouth, no carvings, no patterns, no inscriptions, no decorative markings. Just a plain natural grey heart-shaped stone.

3. Add a SMALL CRACK on the surface of the heart-shaped stone — a thin, irregular, natural stone fissure running across the front face of the stone (the kind of crack an old weathered stone would naturally develop over time). The crack should be a thin dark grey line, slightly irregular, NOT a smooth straight cut — it looks like a natural geological crack.

4. The WATER SPRING rises FROM THE CRACK in the heart-shaped stone. Clear water emerges from the crack and rises VERTICALLY into the air as a slender column of water with a few delicate droplets catching the warm sunrise light. The water reaches about BELLY-HIGH of the tree in the background — meaning roughly the lower third of the tree trunk, around one-third to one-half the height of the visible tree trunk BEFORE the branches and leaves begin. The water column is TALLER than the heart-shaped stone itself (it rises well above the stone) but is SHORTER than the tree's full height. The water spring is NARROWER than the tree's canopy.

5. There must be NO HOLE on the ground. The water does NOT come from any opening or orifice in the earth — it comes ONLY from the crack in the heart-shaped stone. The ground around the stone is solid dry earthy terrain.

6. There must be NO POOL of water at the base — no puddle, no wet patch, no rippling water, no dark moist area, no water reflection on the ground. The heart-shaped stone sits directly on the same dry warm earthy tan/orange terrain as the rest of the foreground. The water that rises from the crack simply falls back down naturally and disappears without accumulating.

Keep absolutely everything else identical to the source: same green-leaved tree-human silhouette, same horizon line, same sunrise sky, same warm color palette, same painterly style, same composition proportions.

Absolutely no text, no letters, no words, no numbers, no signatures, no watermarks, no typography of any language whatsoever.`;

async function main() {
  console.log('Loading source image (v2.10 cover with wide basin + tall jet + pool)...');
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
