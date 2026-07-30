// Well Spring Intervention LLC — Brand Logo Generation v5 (icon-only, 1024x1024)
// REDESIGN: OUTLINE-ONLY line-art rendering. Ultra-minimalist modern aesthetic.
// Same core plan: male Aquarius bent over pouring water from his vessel into a stone heart.
// NO plants, NO virtue ribbons, NO text — just the pure essential outline.
// "Sleek modern minimalist" — think modern tech-startup logo line art, NOT engraving.
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const OUTPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';

const PROMPT = `An ultra-minimalist modern logo icon rendered as a single-weight OUTLINE LINE DRAWING ONLY. No fills, no shading, no crosshatching, no gradients. Just clean continuous outlines in one consistent stroke weight. Sleek modern minimalist aesthetic — think modern tech-startup logo or premium wellness brand mark. Generous negative space. Warm cream background.

CENTRAL COMPOSITION (centered, fills frame with generous margin):
- A stylized minimalist OUTLINE of AQUARIUS — a male figure bent over forward at the waist, torso inclined downward. Rendered as a single clean continuous outline line: a curved arc for the bent-over back, a small circle or simple head outline, simple line limbs, a single flowing line suggesting draped fabric. NO internal details, NO muscle definition, NO facial features — just the essential outer silhouette outline.
- Aquarius holds an OUTLINE of a simple vessel (a tilted vase/jug shape rendered as a clean outline) in his hands, tipped forward and downward, pouring water.
- A simple OUTLINE of a stream of water — a few short vertical lines or simple droplet outlines — falling from the vessel spout downward.
- BENEATH: An OUTLINE of a STONE HEART — a simple clean heart outline (two curved lobes meeting at a point at the bottom, with a smooth top). Just the outer outline of the heart shape — no internal shading, no anatomical detail, no texture. The heart sits on the ground below the vessel and receives the water stream.

COLOR: Single-color outline in warm deep walnut brown (#6b4d3f) on warm cream background (#f5ead6). NO other colors. NO aqua-blue water — water is just a few outline lines in the same walnut brown. NO grey for the heart — heart is just an outline in the same walnut brown. Everything is ONE color, ONE stroke weight.

STYLE: Outline-only line art. Single stroke weight throughout. Clean, sleek, modern, minimalist. NOT engraving, NOT crosshatching, NOT vintage, NOT woodcut. Modern pictogram aesthetic. Generous negative space. NO border, NO frame, NO ring. NO text, NO letters, NO numbers, NO words, NO virtue labels, NO plant stems, NO leaves. Just the pure essential outline of: bent-over male figure + tilted vessel + water stream + stone heart.

Square 1024x1024 logo icon.`;

async function main() {
  console.log('Generating Well Spring logo icon v5 (outline-only, sleek modern minimalist)...');
  const zai = await ZAI.create();
  const response = await zai.images.generations.create({
    prompt: PROMPT,
    size: '1024x1024',
  });

  const outB64 = response.data[0].base64;
  const outBuf = Buffer.from(outB64, 'base64');
  fs.writeFileSync(OUTPUT, outBuf);
  console.log(`✓ Logo icon v5 saved to ${OUTPUT} (${outBuf.length} bytes)`);
}

main().catch((e) => {
  console.error('❌ Error:', e.message);
  console.error(e.stack);
  process.exit(1);
});
