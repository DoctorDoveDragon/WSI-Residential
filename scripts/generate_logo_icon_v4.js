// Well Spring Intervention LLC — Brand Logo Generation v4 (icon-only, 1024x1024)
// REDESIGN: Same conceptual plan as v3, but rendered in an ABSTRACT style:
//  - Male Aquarius bent over pouring water from a visible vessel
//  - Stone heart-shaped vase (NOT anatomical)
//  - 3 plant stems growing from vase, each bearing a virtue ribbon: PEACE, HONOR, FIDELITY
//  - BUT rendered as abstract modern geometric art, not literal engraved illustration
//  - Sleek professional therapy-centered, modern wellness brand aesthetic
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const OUTPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';

const PROMPT = `An abstract modern logo icon in a sleek geometric minimalist style — NOT a literal engraved illustration, NOT a vintage woodcut, NOT a classical painting. Think modern wellness brand mark, Bauhaus-inspired clean geometric forms, mid-century pictogram aesthetic. Solid color shapes with clean edges. Generous negative space. Warm earthy palette on warm cream background.

ABSTRACT COMPOSITION (centered, fills frame with margin):
- UPPER: An abstract stylized figure of Aquarius — rendered as a few simple geometric shapes (a curved arc for the bent-over torso, a small circle for the head, simple rectangular or trapezoidal forms for the limbs and robe). The figure is bent over forward and downward. The figure holds an abstract vessel form (a simple trapezoid or curved goblet shape) tipped forward, pouring water downward. The vessel is clearly identifiable as a vase/jug shape, prominently depicted, NOT hidden.
- CENTER: A short vertical stream of water — rendered as a simple vertical line or three small teardrop/droplet shapes falling from the vessel toward the heart vase below.
- LOWER CENTER: A STONE HEART-SHAPED VASE — an abstract geometric heart form (two semicircles meeting at a point at the bottom, with a flat or slightly recessed top opening). Rendered as a solid cool grey shape suggesting a stone planter/vase with a hollow opening at the top where plants grow. NOT an anatomical heart — clearly a stylized vessel/planter form.
- RISING FROM THE VASE OPENING: Three slender vertical green plant stems rising upward (simple thin vertical lines or thin tapered shapes). Each stem bears a small abstract ribbon banner — a small horizontal curved-rectangle shape — with a single virtue word in clean modern sans-serif uppercase: PEACE on the left stem, HONOR on the center stem, FIDELITY on the right stem. The stems each have a few simple leaf shapes (small ovals or teardrops).

PALETTE (warm earthy, modern):
- Warm cream parchment background
- Warm walnut brown abstract figure and vessel, with terracotta accent
- Cool grey granite heart vase (solid shape, minimal shading)
- Cool aqua-blue water droplets/stream
- Soft natural green plant stems and leaves
- Subtle gold or terracotta ribbon banners with dark uppercase sans-serif lettering

STYLE: Abstract modern, geometric, minimalist, sleek. Solid color shapes with clean edges. Generous negative space. Modern wellness brand aesthetic. NOT literal engraving, NOT vintage crosshatch, NOT classical illustration. NO border, NO frame, NO ring, NO outer banner. Square 1024x1024.`;

async function main() {
  console.log('Generating Well Spring logo icon v4 (abstract style)...');
  const zai = await ZAI.create();
  const response = await zai.images.generations.create({
    prompt: PROMPT,
    size: '1024x1024',
  });

  const outB64 = response.data[0].base64;
  const outBuf = Buffer.from(outB64, 'base64');
  fs.writeFileSync(OUTPUT, outBuf);
  console.log(`✓ Logo icon v4 saved to ${OUTPUT} (${outBuf.length} bytes)`);
}

main().catch((e) => {
  console.error('❌ Error:', e.message);
  console.error(e.stack);
  process.exit(1);
});
