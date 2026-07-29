// Edit existing cover image: add green leaves + wellspring fountain in front of tree
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const INPUT = '/home/z/my-project/scripts/sop_cover_image.png';
const OUTPUT = '/home/z/my-project/scripts/sop_cover_image_v2.png';

const EDIT_PROMPT = `Preserve the entire composition exactly: a serene horizontal landscape featuring a stylized anthropomorphic tree-human figure (tree trunk body with branches uplifted like arms) standing on a small rise, calm sunrise glowing over still water in the background, soft painterly dreamy art style, warm earthy palette of terracotta, soft rose, peach, cream, and golden light.

Make ONLY these two specific changes:
(1) Change ALL the foliage and leaves on the tree branches from golden-amber to fresh vivid GREEN leaves (emerald and spring green, symbolizing growth, renewal, vitality, flourishing).
(2) Add a small gentle wellspring — a fountain of clear water bubbling up from the ground — positioned in the immediate foreground, slightly in front of the base of the tree-human figure, with soft rippling water, a few delicate droplets catching the warm sunrise light, and a subtle stone rim around the spring.

Keep absolutely everything else identical: same tree-human silhouette, same horizon line, same sunrise sky, same warm color palette everywhere except the leaves, same painterly style, same composition and proportions.

Absolutely no text, no letters, no words, no numbers, no signatures, no watermarks, no typography of any language whatsoever.`;

async function main() {
  console.log('Loading source image...');
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
