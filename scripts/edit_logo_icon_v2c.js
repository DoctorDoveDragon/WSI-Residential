// Well Spring Intervention LLC — Brand Logo EDIT v2c
// Take v2b icon (male Aquarius bent over heart) and recompose:
// - Move figure to be DIRECTLY ABOVE the heart on the central vertical axis (perfect symmetry)
// - Reduce crosshatch density to sleeker, sparser, more elegant lines
// - Keep everything else (male figure, bent-over pose, vessel tipped onto heart, grey stone heart, warm cream bg, palette)
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const INPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';
const OUTPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';

const EDIT_PROMPT = `Refine this engraved vintage logo icon with the following changes ONLY:

1. RECOMPOSE FOR PERFECT CENTRAL SYMMETRY: Move the male Aquarius figure so that he is positioned DIRECTLY ABOVE the grey stone heart on the SAME central vertical axis. The figure's body, the vessel, the water stream, and the heart stone must ALL align on the central vertical axis. The figure should straddle the heart with his two feet spaced equally left and right of the center line, his bent torso centered above the heart, and the vessel pouring water straight down onto the heart's top center. The composition must be perfectly left-right symmetric.

2. MAKE THE LINE WORK SLEEKER: Reduce the density of the crosshatching. Replace heavy/busy crosshatch with sparser, cleaner, more elegant line engraving. Use minimal shading — only essential lines to define form. Increase the negative space. The aesthetic should be sleek, refined, modern-wellness, professional therapy-centered — NOT a dense medieval woodcut.

PRESERVE EXACTLY (do not change):
- The male figure (young Greek/Roman man, short curly hair, short beard, athletic build, draped in flowing robes)
- The bent-over pose at the waist, torso inclined forward and downward
- The vessel held in both hands, tipped forward and downward, pouring water onto the heart
- The grey stone heart (cool grey weathered granite, two lobes at top curving to point at bottom)
- The short vertical water stream from vessel onto heart
- The warm cream parchment background
- The warm earthy palette (walnut brown figure, terracotta accents, grey heart, aqua-blue water)
- No text, no letters, no numbers, no watermarks of any language
- Square 1024x1024 format`;

async function main() {
  console.log('Editing logo icon v2b → v2c (centered symmetry + sleeker lines)...');
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
  console.log(`✓ Logo icon v2c saved to ${OUTPUT} (${outBuf.length} bytes)`);
}

main().catch((e) => {
  console.error('❌ Error:', e.message);
  console.error(e.stack);
  process.exit(1);
});
