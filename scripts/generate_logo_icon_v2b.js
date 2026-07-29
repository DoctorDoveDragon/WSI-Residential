// Well Spring Intervention LLC — Brand Logo Generation v2b (icon-only, 1024x1024)
// REFINE iteration b: enforce centered symmetry + sleek clean lines.
// Aquarius male, bent over heart, pouring vessel onto heart.
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const OUTPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';

const PROMPT = `A refined engraved vintage logo icon, classical apothecary seal aesthetic. Sleek, professional, therapy-centered, inviting. Clean elegant line engraving with generous negative space — NOT dense crosshatching, NOT a busy medieval woodcut. Sparse, minimal, modern-wellness aesthetic.

PERFECTLY CENTERED SYMMETRICAL COMPOSITION (everything aligned on the central vertical axis, fills frame with small margin):
- The MALE figure of AQUARIUS — young Greek/Roman man, short curly hair, short beard — is BENT OVER at the waist, his torso inclined forward and downward. He is positioned DIRECTLY ABOVE the grey stone heart on the central vertical axis. His two feet are spaced equally left and right of the center line. He holds an ornate amphora vessel in both hands, tipped forward and downward, pouring a short clear stream of water straight down onto the top center of the grey stone heart directly beneath him.
- The GREY STONE HEART rests on the ground DIRECTLY BELOW the bent figure, centered on the central vertical axis — two rounded lobes at top curving to a gentle point at bottom, cool grey weathered granite with minimal sparse shading.
- A short vertical stream of water falls from the vessel directly onto the heart's top center, on the central vertical axis.

CENTERED RULE: The figure, the vessel, the water stream, and the heart stone are ALL on the same central vertical axis. The composition is perfectly left-right symmetric.

PALETTE (warm earthy):
- Warm cream parchment background
- Warm deep walnut brown male figure and vessel, terracotta accents
- Cool grey granite stone heart
- Cool aqua-blue water stream

STYLE: Clean elegant line engraving — sparse, sleek, refined. Minimal shading. Generous negative space. Classical idealized male figure. NO dense crosshatching. NO busy textures. NO border, NO frame, NO ring, NO banner.

ABSOLUTELY NO TEXT, NO LETTERS, NO NUMBERS, NO WORDS, NO MONOGRAMS, NO DATES, NO WATERMARKS. Purely pictographic.

Square 1024x1024 logo icon.`;

async function main() {
  console.log('Generating refined Well Spring logo icon v2b (centered + sleek)...');
  const zai = await ZAI.create();
  const response = await zai.images.generations.create({
    prompt: PROMPT,
    size: '1024x1024',
  });

  const outB64 = response.data[0].base64;
  const outBuf = Buffer.from(outB64, 'base64');
  fs.writeFileSync(OUTPUT, outBuf);
  console.log(`✓ Logo icon v2b saved to ${OUTPUT} (${outBuf.length} bytes)`);
}

main().catch((e) => {
  console.error('❌ Error:', e.message);
  console.error(e.stack);
  process.exit(1);
});
