// Well Spring Intervention LLC — Brand Logo EDIT v6f (pass 2)
// Pass 1 successfully made the LEFT adult feminine (ponytail + A-line dress), but
// the model ALSO applied the same feminine cues to the RIGHT adult (which was
// supposed to remain masculine). The user wanted only ONE adult to be a woman.
// This pass reverts the RIGHT adult back to clearly MASCULINE while keeping the
// LEFT adult as the woman.
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const INPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';
const OUTPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';

const EDIT_PROMPT = `Modify ONLY the RIGHT adult family figure in this logo icon to make it clearly MASCULINE (a man). The LEFT adult figure (a woman with ponytail + dress) and the CENTER child figure stay exactly as they are.

CURRENTLY: The right adult figure has long hair and a triangular A-line dress-like lower body — it reads as feminine (same as the left figure). This is wrong.

REQUIRED CHANGE — make the RIGHT adult figure clearly a MAN by applying these masculine iconography cues:
1. PANTS / RECTANGULAR SILHOUETTE: Replace the right figure's triangular dress with TWO SEPARATE STRAIGHT PANT LEGS — two parallel vertical rectangles forming a rectangular lower-body shape (not a flared triangle). The pants should be the same warm terracotta color.
2. SHORT HAIR: Replace the right figure's long hair with SHORT hair — a simple rounded cap or short-cropped hair on top of the head only, no hair extending to the shoulders or back.
3. BROADER SHOULDERS: Make the right figure's shoulders slightly broader/more squared than the left figure's, with no waist curve — a straight rectangular torso from shoulders to hips.
4. PRESERVE the right figure's pose: still holding hands with the child on its left side, still standing behind the wellspring, still only upper body visible above the basin rim.

DO NOT CHANGE:
- The LEFT adult figure (keep it as is — woman with ponytail + A-line dress + narrower shoulders + waist curve)
- The CENTER child figure (keep it as is — small, terracotta, between the two adults)
- The wellspring (stone basin + aqua water column + splashes in foreground)
- The brown tree trunk rising from the wellspring
- The heart-shaped canopy with green leaves at the top
- The warm cream background, multi-color palette, minimalist contour aesthetic
- The overall composition and proportions

After the change, the family should clearly read as: WOMAN (left, ponytail + dress) + CHILD (center, small) + MAN (right, short hair + pants), all holding hands behind the wellspring.

NO text, NO letters, NO numbers, NO watermarks.`;

async function main() {
  console.log('Editing logo icon v6f pass 2 (revert right adult to masculine)...');
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
  console.log(`✓ Logo icon v6f pass 2 saved to ${OUTPUT} (${outBuf.length} bytes)`);
}

main().catch((e) => {
  console.error('❌ Error:', e.message);
  console.error(e.stack);
  process.exit(1);
});
