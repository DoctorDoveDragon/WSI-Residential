// Well Spring Intervention LLC — Brand Logo Generation v2 (icon-only, 1024x1024)
// REFINE: Aquarius is MALE, bent over the heart pouring his vase onto it.
// Look: sleek professional therapy centered. Engraved vintage style preserved.
// Zero text/letters/numbers/watermarks.
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const OUTPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';

const PROMPT = `A refined engraved vintage logo icon, classical apothecary seal aesthetic. Fine crosshatch intaglio line engraving on warm cream parchment background. Sleek, professional, therapy-centered, inviting. Clean elegant lines with generous negative space.

CENTRAL COMPOSITION (centered, symmetrical, fills frame edge-to-edge with small margin):
- A MALE figure of AQUARIUS — a graceful classical Greek/Roman young man with short curly hair and a short beard, draped in flowing robes. He is BENT OVER at the waist, his torso inclined forward and downward, leaning over a grey stone heart that sits on the ground directly in front of and beneath him. He holds an ornate amphora vessel in both hands, tipped forward and downward, pouring a short clear stream of water directly ONTO the top center of the grey stone heart below. The pose is intimate, focused, gentle — the gesture of offering, blessing, healing therapy.
- The GREY STONE HEART rests on the ground beneath the bent figure — two rounded lobes at top curving down to a gentle point at bottom, cool natural grey weathered granite with subtle crosshatch shading for weight and solidity.
- A single short vertical stream of water falls from the tipped vessel onto the top of the heart, with a few delicate droplets.

PALETTE (warm earthy, refined):
- Warm cream parchment background
- Warm deep walnut brown male figure and vessel, with terracotta accents on vessel ornamentation and robe trim
- Cool grey granite stone heart (medium grey with darker shading)
- Cool aqua-blue water stream

STYLE: Fine crosshatch line engraving throughout, NOT flat fills. Sleek, refined, elegant, balanced. Classical idealized male figure proportions. Clean professional therapy aesthetic. No border, no frame, no circular ring, no ribbon banner.

ABSOLUTELY NO TEXT, NO LETTERS, NO NUMBERS, NO WORDS, NO MONOGRAMS, NO DATES, NO WATERMARKS of any language. Purely pictographic.

Square 1024x1024 logo icon.`;

async function main() {
  console.log('Generating refined Well Spring logo icon v2 (male Aquarius bent over heart)...');
  const zai = await ZAI.create();
  const response = await zai.images.generations.create({
    prompt: PROMPT,
    size: '1024x1024',
  });

  const outB64 = response.data[0].base64;
  const outBuf = Buffer.from(outB64, 'base64');
  fs.writeFileSync(OUTPUT, outBuf);
  console.log(`✓ Logo icon v2 saved to ${OUTPUT} (${outBuf.length} bytes)`);
}

main().catch((e) => {
  console.error('❌ Error:', e.message);
  console.error(e.stack);
  process.exit(1);
});
