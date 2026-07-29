// Re-edit v2.12 image to remove any "eyes"/face from the heart-shaped stone.
// Source = the v2.12 image (heart-shaped stone + taller spring).
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const INPUT = '/home/z/my-project/scripts/sop_cover_image_v212.png';
const OUTPUT = '/home/z/my-project/scripts/sop_cover_image_v212b.png';

const EDIT_PROMPT = `Preserve the entire composition exactly: a serene horizontal landscape featuring a stylized anthropomorphic tree-human figure with fresh vivid GREEN leaves, calm sunrise glowing over still water in the background, soft painterly dreamy art style, warm earthy palette. In the foreground directly in front of the tree there is a NARROW vertical wellspring of clear water bubbling up from a smooth heart-shaped stone (two rounded lobes at top meeting at a point at the bottom).

Make ONLY this one specific change:

The heart-shaped stone at the base of the wellspring currently appears to have two circular indentations that resemble eyes, making it look like a face. REMOVE those indentations completely. The heart-shaped stone should be completely SMOOTH and UNMARKED — a plain, polished, sculpted stone in a soft warm earth-toned color (terracotta or soft rose), with a clean heart silhouette (two rounded lobes at the top curving down to a gentle point at the bottom). No eyes, no mouth, no facial features, no carvings, no markings, no patterns, no texture lines on its surface — just a smooth plain heart-shaped stone. The narrow vertical jet of clear water continues to bubble up from the center/top of the smooth heart-shaped stone, reaching a TALL slender column into the air, with a few delicate droplets catching the warm sunrise light and a small pool of rippling water at the base.

Keep absolutely everything else identical: same green-leaved tree-human silhouette, same horizon line, same sunrise sky, same warm color palette, same painterly style, same composition and proportions, same wellspring height and narrowness. Only the surface of the heart-shaped stone changes — remove any face/eyes/markings so it is a clean smooth sculpted stone.

Absolutely no text, no letters, no words, no numbers, no signatures, no watermarks, no typography of any language whatsoever.`;

async function main() {
  console.log('Loading source image (v2.12 cover with possible face on heart)...');
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
