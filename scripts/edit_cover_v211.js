// Edit the v2.8 cover image: (1) green leaves, (2) narrow wellspring in foreground
// NOT wider than the tree.
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const INPUT = '/home/z/my-project/scripts/sop_cover_image_v28_source.png';
const OUTPUT = '/home/z/my-project/scripts/sop_cover_image_v211.png';

const EDIT_PROMPT = `Preserve the entire composition exactly: a serene horizontal landscape featuring a stylized anthropomorphic tree-human figure (tree trunk body shaped like a human silhouette with arms raised, branches extending from the arms and head) standing on rolling hills, calm sunrise glowing over still water in the background, soft painterly dreamy art style, warm earthy palette of terracotta, soft rose, peach, cream, and golden light. Currently the foliage on the tree branches is orange/amber.

Make ONLY these two specific changes:

(1) Change ALL the foliage and leaves on the tree branches from orange/amber to fresh vivid GREEN leaves (emerald and spring green, symbolizing growth, renewal, vitality, flourishing). The leaf clusters should keep their same shape, density, and placement on the branches — only the color changes from warm orange to lush green.

(2) Add a SMALL, NARROW wellspring in the immediate foreground, directly in front of the base of the tree-human figure. The wellspring MUST be NARROWER than the tree itself (its width should be roughly one-third to one-half the width of the tree's leaf canopy). It should appear as a small vertical fountain of clear water bubbling gently upward from a narrow crack or small stone-rimmed opening in the ground, with a few delicate water droplets catching the warm sunrise light and a small pool of rippling water at its base. The wellspring should be subtle and modest in scale, NOT a large circular basin or pool — it is a narrow vertical jet of water from the earth, evoking the literal "well spring" of the company name.

Keep absolutely everything else identical: same tree-human silhouette, same horizon line, same sunrise sky, same warm color palette everywhere except the leaves, same painterly style, same composition and proportions, same rolling hills at the base.

Absolutely no text, no letters, no words, no numbers, no signatures, no watermarks, no typography of any language whatsoever.`;

async function main() {
  console.log('Loading source image (v2.8 cover)...');
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
