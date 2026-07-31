// Well Spring Intervention LLC — Brand Logo EDIT v6e
// Take v6d (multi-color + wellspring + 3 terracotta family figures currently standing
// IN the wellspring water at the base of the tree) and reposition the family figures
// so they stand BEHIND the wellspring — i.e., the wellspring (stone basin + rising
// water column) is in the FOREGROUND and the three family figures are arranged behind
// it, no longer submerged in / standing in the water.
//
// Visual goal:
//   - The wellspring (stone basin + aqua-blue water rising up + splashes) remains at
//     the base of the tree trunk as before, in the FOREGROUND.
//   - The three terracotta family figures (adult woman, adult man, child — same warm
//     terracotta color, holding hands) are moved BEHIND the wellspring so that the
//     wellspring basin and water column partially overlap / pass in front of them.
//     The figures should appear to stand on the ground BEHIND the wellspring, with
//     the lower portion of their bodies (below about knee height) hidden behind the
//     stone basin and rising water — i.e., the wellspring is between the viewer and
//     the family. The figures' upper bodies (torso, heads, raised holding-hands
//     arms) should remain visible above and behind the wellspring.
//   - The tree trunk continues to rise from the wellspring as before.
//   - The heart-shaped canopy with green leaves remains at the top.
//   - All other elements (colors, palette, style, composition) unchanged.
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const INPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';
const OUTPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';

const EDIT_PROMPT = `Reposition the three family figures in this logo icon so they stand BEHIND the wellspring, NOT in it.

CURRENTLY: The three terracotta family figures (adult woman, adult man, child holding hands) are standing IN the wellspring water at the base of the tree — their feet/bodies are submerged in or standing directly on top of the wellspring basin and water.

DESIRED CHANGE: Move the three family figures BEHIND the wellspring so they are no longer standing in the water. Specifically:
- The wellspring (stone basin + aqua-blue water column rising up + splash droplets) stays in the FOREGROUND at the base of the tree trunk, exactly as it is now.
- The three terracotta family figures are repositioned BEHIND the wellspring — they stand on the ground behind/behind-and-above the stone basin. The wellspring (basin + rising water) should be visually IN FRONT of the lower portion of the figures, partially overlapping/obscuring their legs/lower bodies. The figures' upper bodies (torsos, heads, arms holding hands) should remain visible above and behind the wellspring.
- The figures remain the same warm terracotta color, the same relative sizes (woman + man taller, child shorter), and the same holding-hands caring pose.
- The figures should appear to be standing together as a family on the far side of the wellspring, looking forward, with the wellspring between them and the viewer.

PRESERVE EVERYTHING ELSE EXACTLY:
- The wellspring (stone basin, aqua-blue rising water column, splash droplets) — unchanged in foreground
- The brown tree trunk rising from the wellspring — unchanged
- The heart-shaped canopy outline at the top — unchanged
- The green leaves and small accent dots inside the canopy — unchanged
- The warm cream background — unchanged
- The multi-color palette — unchanged
- The sleek modern minimalist contour aesthetic — unchanged
- The composition's overall balance and proportions — unchanged (just the family figures shift to behind the wellspring)

NO text, NO letters, NO numbers, NO watermarks.`;

async function main() {
  console.log('Editing logo icon v6d → v6e (family behind wellspring)...');
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
  console.log(`✓ Logo icon v6e saved to ${OUTPUT} (${outBuf.length} bytes)`);
}

main().catch((e) => {
  console.error('❌ Error:', e.message);
  console.error(e.stack);
  process.exit(1);
});
