// Well Spring Intervention LLC — Brand Logo EDIT v6d
// Take v6c (multi-color + wellspring — good) and clean up two regressions:
//  1. Make all three family figures the SAME warm terracotta color, as HOLLOW OUTLINES
//     (not solid silhouettes, not three different colors)
//  2. Remove the extra decorative side leaves/motifs flanking the family
// Keep everything else (multi-color palette, wellspring, tree, heart canopy) as is.
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const INPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';
const OUTPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';

const EDIT_PROMPT = `Make TWO clean-up changes to this logo icon:

1. UNIFY THE FAMILY FIGURES — Make all three family figures (adult woman, adult man, child) the SAME warm terracotta color, rendered as HOLLOW OUTLINES (not solid filled silhouettes). Currently they are three different colors (orange, blue, red) and solid filled — change them all to thin terracotta-colored outlines with the cream background showing through the interior. Keep their poses (holding hands in a caring gesture) and their relative sizes (woman and man taller, child shorter).

2. REMOVE THE EXTRA DECORATIVE SIDE LEAVES — Remove the decorative leaf-shaped motifs that flank the family on either side (the yellow/gold and green floating leaf shapes beside the figures). Keep only the leaves INSIDE the heart-shaped canopy at the top. The area beside the family figures should be clean cream background.

DO NOT CHANGE ANYTHING ELSE. Specifically preserve:
- The wellspring at the base (stone basin with rising water and splashes)
- The aqua-blue water color
- The brown tree trunk
- The heart-shaped canopy outline
- The green leaves inside the canopy
- The small accent dots inside the canopy
- The warm cream background
- The multi-color palette overall
- The composition and layout

NO text, NO letters, NO numbers, NO watermarks.`;

async function main() {
  console.log('Editing logo icon v6c → v6d (unify figures + remove side leaves)...');
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
  console.log(`✓ Logo icon v6d saved to ${OUTPUT} (${outBuf.length} bytes)`);
}

main().catch((e) => {
  console.error('❌ Error:', e.message);
  console.error(e.stack);
  process.exit(1);
});
