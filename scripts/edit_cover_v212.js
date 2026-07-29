// Edit the v2.11 cover image: (1) heart-shaped stone orifice, (2) taller spring.
// Source = the current canonical v2.11 cover image (green leaves + narrow wellspring).
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const INPUT = '/home/z/my-project/scripts/sop_cover_image_v211.png';
const OUTPUT = '/home/z/my-project/scripts/sop_cover_image_v212.png';

const EDIT_PROMPT = `Preserve the entire composition exactly: a serene horizontal landscape featuring a stylized anthropomorphic tree-human figure (tree trunk body shaped like a human silhouette with arms raised, branches extending from the arms and head) with fresh vivid GREEN leaves, calm sunrise glowing over still water in the background, soft painterly dreamy art style, warm earthy palette of terracotta, soft rose, peach, cream, and golden light. In the immediate foreground directly before the tree, there is currently a NARROW vertical wellspring of clear water bubbling up from a small jagged stone-rimmed opening in the ground.

Make ONLY these two specific changes to the wellspring:

(1) Replace the jagged stone-rimmed opening/orifice that the water emanates from with a HEART-SHAPED STONE. The water should now appear to bubble up and flow out from the center of a small, smooth, warm earth-toned heart-shaped stone (sculpted stone in a soft rose/terracotta color matching the surrounding palette). The heart shape should be clearly recognizable — two rounded lobes at the top meeting at a gentle point at the bottom — but rendered in the same painterly, soft style as the rest of the illustration (not cartoonish, not photorealistic, just a soft sculpted heart-shaped stone). The heart-shaped stone should sit on the ground in the foreground directly in front of the base of the tree, with the narrow water jet emerging upward from its center.

(2) Make the vertical jet/spray of water a LITTLE TALLER than it currently is — roughly 30-50% taller — so the upward arc of clear water droplets and the slender column of water reach a bit higher into the air before falling back down. Keep the spring still NARROW (its width should still be significantly smaller than the tree's leaf canopy) — only the HEIGHT increases, not the width. The few delicate water droplets catching the warm sunrise light should still be present, and the small pool of rippling water at the base of the stone should remain.

Keep absolutely everything else identical: same green-leaved tree-human silhouette, same horizon line, same sunrise sky, same warm color palette everywhere, same painterly style, same composition and proportions, same rolling hills at the base. The wellspring remains NARROWER than the tree — only the orifice changes from jagged to heart-shaped stone, and the water jet becomes a bit taller.

Absolutely no text, no letters, no words, no numbers, no signatures, no watermarks, no typography of any language whatsoever.`;

async function main() {
  console.log('Loading source image (v2.11 cover)...');
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
