// Well Spring Intervention LLC — Brand Logo EDIT v6f
// User feedback: "One of the adults is not a woman but should be."
// VLM diagnosis: both adult figures currently read as masculine/androgynous
// (short circular hair, broad squared shoulders, rectangular pants silhouette).
// This edit makes the LEFT adult figure clearly FEMININE so the family reads
// as "adult woman (left), adult man (right), child (center)".
//
// Feminine iconography cues to apply to the LEFT adult only:
//   - Dress/A-line silhouette: the lower body should be a triangular shape
//     (narrow at waist, widening to a hem at the bottom) instead of two
//     separate pant legs
//   - Longer hair: hair extending to shoulder length or in a ponytail, instead
//     of the short circular cap
//   - Narrower shoulders and a slight waist curve
//   - Same warm terracotta color as the other figures
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const INPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';
const OUTPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';

const EDIT_PROMPT = `Modify ONLY the LEFT adult family figure in this logo icon to make it clearly FEMININE (a woman). The RIGHT adult figure and the CENTER child figure stay exactly as they are.

CURRENTLY: The left adult figure has short circular hair, broad squared shoulders, and a rectangular pants-like lower body (two straight vertical lines for legs). It reads as masculine or androgynous.

REQUIRED CHANGE — make the LEFT adult figure clearly a WOMAN by applying these feminine iconography cues:
1. DRESS / A-LINE SILHOUETTE: Replace the left figure's two separate pant legs with a single triangular dress shape — narrow at the waist, widening outward to a hem at the bottom. The dress should be the same warm terracotta color as the rest of the figure.
2. LONGER HAIR: Replace the left figure's short circular hair cap with longer hair — either shoulder-length hair framing the face, or a ponytail. The hair should be the same warm terracotta color.
3. NARROWER SHOULDERS & WAIST CURVE: Make the left figure's shoulders slightly narrower than the right figure's, and add a subtle inward curve at the waist (hourglass hint) before the dress flares out.
4. PRESERVE the left figure's pose: still holding hands with the child on its right side, still standing behind the wellspring, still only upper body visible above the basin rim.

DO NOT CHANGE:
- The RIGHT adult figure (keep it as is — short hair, broad shoulders, pants silhouette, masculine reading)
- The CENTER child figure (keep it as is — small, terracotta, between the two adults)
- The wellspring (stone basin + aqua water column + splashes in foreground)
- The brown tree trunk rising from the wellspring
- The heart-shaped canopy with green leaves at the top
- The warm cream background, multi-color palette, minimalist contour aesthetic
- The overall composition and proportions

After the change, the family should clearly read as: WOMAN (left, dress + longer hair) + CHILD (center, small) + MAN (right, pants + short hair), all holding hands behind the wellspring.

NO text, NO letters, NO numbers, NO watermarks.`;

async function main() {
  console.log('Editing logo icon v6e → v6f (make left adult clearly feminine)...');
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
  console.log(`✓ Logo icon v6f saved to ${OUTPUT} (${outBuf.length} bytes)`);
}

main().catch((e) => {
  console.error('❌ Error:', e.message);
  console.error(e.stack);
  process.exit(1);
});
