// Well Spring Intervention LLC — Brand Logo Generation v6 (icon-only, 1024x1024)
// KEYWORD-DRIVEN REDESIGN:
//   minimalist, sleek contours, abstract, therapy, healing, growth, children,
//   emotions, care, renewal, rebirth, self realization, family, wellspring,
//   tree of life, empowerment
//
// CONCEPT: A unified emblem that merges all keywords into one symbol:
//   - WELLSRING at the base: water bubbling up from below (renewal, rebirth)
//   - TREE OF LIFE rising from the wellspring: trunk grows upward (growth)
//   - HEART-SHAPED CANOPY: branches curve into a heart at the top (emotions, care, healing, therapy)
//   - LEAVES/DROPLETS: small dots within the heart canopy (dual symbol: leaves = growth, droplets = wellspring)
//   - FAMILY FIGURES: small abstract adult + child figures sheltered beneath the tree (family, children, care, empowerment)
//   - The whole rendered as sleek contour abstract line art (minimalist, sleek contours, abstract)
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const OUTPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';

const PROMPT = `A minimalist abstract logo icon rendered as sleek contour line art. Single-weight outline only, no fills, no shading. Modern wellness brand aesthetic. Generous negative space. Warm cream background.

CENTRAL COMPOSITION (centered, fills frame with margin) — a unified emblem merging wellspring, tree of life, heart, and family:

- BASE: A simple curved basin line at the bottom representing a WELLSPRING — a small pool or source from which water rises. A few simple curved lines or small droplet outlines rising upward from the wellspring suggest water bubbling up (renewal, rebirth).

- TRUNK: The rising water transitions into the trunk of a TREE OF LIFE — a single flowing vertical contour line rising from the wellspring, slightly organic and curved (not rigidly straight). The trunk represents growth and the connection between water and life.

- CANOPY: At the top, the trunk branches out into a few simple flowing branch contours that curve upward and outward to form a HEART shape — the canopy of the tree IS a heart outline (two curved lobes meeting at a point at the bottom, with the branches filling the heart silhouette). The heart canopy represents emotions, care, healing, and therapy.

- LEAVES/DROPLETS: Within the heart canopy, scatter a few small simple shapes (small circles, ovals, or teardrops) that serve as BOTH leaves of the tree AND water droplets from the wellspring — a dual symbol of growth and renewal.

- FAMILY FIGURES: Beneath the tree canopy, on either side of the trunk, stand TWO small abstract human figures rendered as simple outline stick-figures (small circle for head, single line for body, simple line arms and legs). One figure is slightly TALLER (the adult/caregiver) and one is slightly SHORTER (the child). The taller figure's arm gently reaches toward or over the shorter figure in a protective caring gesture. These represent family, children, care, and empowerment.

COLOR: Single-color outline in warm deep walnut brown on warm cream background. Everything (wellspring, water, trunk, branches, heart canopy, leaves/droplets, family figures) in the same walnut brown, same stroke weight. NO other colors.

STYLE: Sleek contour abstract line art. Single stroke weight throughout. Clean, organic, flowing contours. Generous negative space. Modern wellness brand mark. NOT engraving, NOT crosshatching, NOT vintage. NO border, NO frame, NO ring.

ABSOLUTELY NO TEXT, NO LETTERS, NO NUMBERS, NO WORDS, NO WATERMARKS. Purely pictographic.

Square 1024x1024 logo icon.`;

async function main() {
  console.log('Generating Well Spring logo icon v6 (wellspring + tree of life + heart + family)...');
  const zai = await ZAI.create();
  const response = await zai.images.generations.create({
    prompt: PROMPT,
    size: '1024x1024',
  });

  const outB64 = response.data[0].base64;
  const outBuf = Buffer.from(outB64, 'base64');
  fs.writeFileSync(OUTPUT, outBuf);
  console.log(`✓ Logo icon v6 saved to ${OUTPUT} (${outBuf.length} bytes)`);
}

main().catch((e) => {
  console.error('❌ Error:', e.message);
  console.error(e.stack);
  process.exit(1);
});
