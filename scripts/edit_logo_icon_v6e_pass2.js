// Well Spring Intervention LLC — Brand Logo EDIT v6e (pass 2)
// The first v6e edit pass did not achieve the desired repositioning — the family
// figures are still standing IN the wellspring water. This pass uses stronger, more
// explicit spatial language to force the model to physically relocate the figures
// behind the wellspring.
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const INPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';
const OUTPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';

const EDIT_PROMPT = `CRITICAL SPATIAL REPOSITIONING of the three family figures.

CURRENTLY (the problem): The three terracotta family figures are standing INSIDE the round stone wellspring basin — their feet and legs are submerged in the aqua-blue water, with the stone basin ringing around them and the rising water column between them.

REQUIRED CHANGE: Physically MOVE the three family figures to a position BEHIND the wellspring. They must no longer be inside, on, or touching the wellspring basin or water. Instead:

- The wellspring (round stone basin + aqua-blue water column rising up + splash droplets) stays exactly where it is — in the FOREGROUND at the base of the tree, partially obscuring whatever is behind it.
- The three terracotta family figures are relocated to stand BEHIND the wellspring, on the ground on the FAR SIDE of the basin. The wellspring basin + rising water column pass IN FRONT of the figures' lower bodies, so the figures' legs and feet are HIDDEN BEHIND the stone basin and water. Only the figures' UPPER BODIES (waist up — torso, heads, and their holding-hands arms) should be visible, appearing to rise up above and behind the wellspring.
- The figures should NOT be inside the basin, NOT standing in the water, NOT in front of the basin. They are BEHIND it — at a slightly greater distance from the viewer than the basin.

Think of it like a family standing on the far shore of a small round well or spring, with the well opening between them and the camera. We see their upper bodies above the well rim; their lower bodies are hidden behind the well.

The three figures remain the same warm terracotta color, same relative sizes (woman + man taller, child shorter), same holding-hands caring pose — just relocated behind the wellspring so the wellspring is in the foreground.

PRESERVE EXACTLY: the wellspring (stone basin + aqua water column + splashes), the brown tree trunk rising from the wellspring center, the heart-shaped canopy outline, the green leaves + accent dots inside the canopy, the warm cream background, the multi-color palette, the minimalist contour aesthetic.

NO text, NO letters, NO numbers, NO watermarks.`;

async function main() {
  console.log('Editing logo icon v6e pass 2 (stronger behind-wellspring language)...');
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
  console.log(`✓ Logo icon v6e pass 2 saved to ${OUTPUT} (${outBuf.length} bytes)`);
}

main().catch((e) => {
  console.error('❌ Error:', e.message);
  console.error(e.stack);
  process.exit(1);
});
