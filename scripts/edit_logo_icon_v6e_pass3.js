// Well Spring Intervention LLC — Brand Logo EDIT v6e (pass 3)
// Pass 2 successfully moved the family figures behind the wellspring (lower bodies
// now hidden by the basin rim), BUT the model lost the third figure — only TWO
// figures (the adults) are visible; the child is missing. This pass restores the
// child while preserving the behind-wellspring positioning.
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const INPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';
const OUTPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';

const EDIT_PROMPT = `RESTORE THE THIRD FAMILY FIGURE (the child) behind the wellspring.

CURRENTLY: Behind the wellspring basin, only TWO terracotta family figures are visible (the adult woman and adult man). The CHILD figure is missing.

REQUIRED CHANGE: Add back the third figure — a smaller CHILD — so that all THREE family members (adult woman, adult man, child) stand together behind the wellspring. Specifically:
- Keep the two existing adult terracotta figures exactly where they are (behind the wellspring, upper bodies visible above the basin rim, lower bodies hidden by the basin).
- Add a SMALLER THIRD figure (the child) between or beside the two adults, also behind the wellspring, also terracotta colored, also with only upper body visible above the basin rim.
- All three figures should be holding hands in a caring family pose — the child between or beside the two adults, holding hands with them.
- The child should be visibly shorter than the two adults (head height roughly at the adults' shoulder/chest height).
- Same warm terracotta color as the adults.

PRESERVE EXACTLY: the wellspring basin + rising aqua water + splashes in the foreground, the brown tree trunk, the heart-shaped canopy with green leaves, the warm cream background, the multi-color palette, the minimalist contour aesthetic, the overall composition.

NO text, NO letters, NO numbers, NO watermarks.`;

async function main() {
  console.log('Editing logo icon v6e pass 3 (restore child figure)...');
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
  console.log(`✓ Logo icon v6e pass 3 saved to ${OUTPUT} (${outBuf.length} bytes)`);
}

main().catch((e) => {
  console.error('❌ Error:', e.message);
  console.error(e.stack);
  process.exit(1);
});
