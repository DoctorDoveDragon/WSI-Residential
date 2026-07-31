// Well Spring Intervention LLC — Brand Logo EDIT v6e (pass 4)
// Pass 3 restored the child figure, but introduced two regressions:
//   1. The child is now a lighter peach/skin-tone color instead of the warm
//      terracotta of the two adults.
//   2. The wellspring basin shifted DOWN, so the figures' lower bodies (legs)
//      are now fully visible again — they should be hidden behind the basin rim.
// This pass fixes both: (a) unify all three figures to the same warm terracotta
// color, and (b) raise the wellspring basin back up so it passes in front of the
// figures' lower bodies (only their upper bodies visible above the basin rim).
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const INPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';
const OUTPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';

const EDIT_PROMPT = `Two clean-up fixes to this logo icon:

1. UNIFY THE CHILD FIGURE'S COLOR — The small child figure in the center (between the two adults) is currently a lighter peach/skin-tone color. Change the child to the SAME warm terracotta color as the two adult figures flanking it. All three family figures (adult woman on left, child in center, adult man on right) must be the same warm terracotta color. No skin-tone, no peach, no lighter shade — same terracotta as the adults.

2. RAISE THE WELLSPRING BASIN — The round stone wellspring basin has shifted downward, exposing the figures' legs and lower bodies. Raise the basin back up so it sits in front of the figures' LOWER BODIES. The basin rim should pass horizontally across the figures at about waist/hip height, hiding their legs and feet behind the stone basin + rising water column. Only the figures' UPPER BODIES (torso, heads, holding-hands arms) should be visible above the basin rim. The wellspring basin remains in the FOREGROUND, between the viewer and the family figures.

PRESERVE EXACTLY: the three family figures (now all terracotta, holding hands, behind the wellspring), the brown tree trunk rising from the wellspring, the heart-shaped canopy with green leaves at the top, the warm cream background, the multi-color palette, the minimalist contour aesthetic, the overall composition.

NO text, NO letters, NO numbers, NO watermarks.`;

async function main() {
  console.log('Editing logo icon v6e pass 4 (unify child color + raise basin)...');
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
  console.log(`✓ Logo icon v6e pass 4 saved to ${OUTPUT} (${outBuf.length} bytes)`);
}

main().catch((e) => {
  console.error('❌ Error:', e.message);
  console.error(e.stack);
  process.exit(1);
});
