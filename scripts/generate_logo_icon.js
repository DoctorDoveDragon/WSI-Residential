// Well Spring Intervention LLC — Brand Logo Generation (icon-only, 1024x1024)
// Style: engraved vintage (classical apothecary seal / university medal aesthetic)
// Composition: full-figure Aquarius pouring water from a vessel into a grey stone heart
// Palette: warm earthy (cream bg, warm brown figure, terracotta accents, grey heart, aqua water)
// Concept: health therapy, renewal. Look: sleek, professional, inviting.
// Zero text/letters/numbers/watermarks.
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const OUTPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';

const PROMPT = `A refined engraved vintage logo icon in the style of a classical apothecary seal or university medal. Fine crosshatch intaglio line engraving on a warm cream parchment background. Sleek, professional, inviting — heritage craftsmanship reimagined for a modern wellness brand. Generous negative space, NOT a dense medieval woodcut.

CENTRAL COMPOSITION (centered, symmetrical, fills the frame edge-to-edge with a small margin):
- UPPER HALF: A standing figure of AQUARIUS (the water bearer) — a graceful classical Greek/Roman figure rendered in engraved crosshatch lines, draped in flowing robes, standing upright and centered. The figure holds and tilts an ornate amphora vessel with both hands, pouring water from the vessel in a graceful arc downward.
- LOWER HALF: A single smooth GREY STONE HEART resting on the ground — two rounded lobes at the top curving down to meet at a gentle point at the bottom, rendered as cool natural grey weathered granite with subtle engraved shading suggesting weight and solidity.
- BETWEEN THEM: A single clear stream of water flows in a graceful vertical arc from the tilted vessel in Aquarius's hands downward into the top center of the grey stone heart. The water is rendered with fine engraved lines suggesting flowing liquid, with a few delicate droplets catching the light.

PALETTE (warm earthy, refined):
- Warm cream background (parchment off-white #f5ead6)
- Warm brown figure and vessel (#6b4d3f deep walnut, with #ab5125 terracotta accents on the vessel ornamentation and robe trim)
- Soft rose / peach highlights (#ffd9a7) on drapery folds and vessel rim
- Cool grey stone heart (#8a8a8a medium grey with #5a5a5a darker shading)
- Cool aqua-blue (#7aa5b8) for the water stream, to distinguish it from the warm earthy surroundings

STYLE: Fine crosshatch line engraving throughout — NOT flat fills. Refined, elegant, balanced. Classical idealized figure proportions. No border, no frame, no circular ring, no ribbon banner.

ABSOLUTELY NO TEXT, NO LETTERS, NO NUMBERS, NO WORDS, NO MONOGRAMS, NO DATES, NO WATERMARKS of any language. The icon is purely pictographic.

Square 1024x1024 logo icon, suitable for use as a brand mark on websites, letterheads, business cards, signage, embroidery, and favicon.`;

async function main() {
  console.log('Generating Well Spring logo icon (1024x1024, engraved vintage)...');
  const zai = await ZAI.create();
  const response = await zai.images.generations.create({
    prompt: PROMPT,
    size: '1024x1024',
  });

  const outB64 = response.data[0].base64;
  const outBuf = Buffer.from(outB64, 'base64');
  fs.writeFileSync(OUTPUT, outBuf);
  console.log(`✓ Logo icon saved to ${OUTPUT} (${outBuf.length} bytes)`);
}

main().catch((e) => {
  console.error('❌ Error:', e.message);
  console.error(e.stack);
  process.exit(1);
});
