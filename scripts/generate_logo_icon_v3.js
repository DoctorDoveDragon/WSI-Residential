// Well Spring Intervention LLC — Brand Logo Generation v3 (icon-only, 1024x1024)
// REDESIGN:
//  - The heart is now a stone heart-shaped VASE (a sculptural planter, NOT an anatomical heart)
//  - Three plant stems grow upward from the soil in the heart vase
//  - Each stem bears a small ribbon banner with a virtue word: PEACE, HONOR, FIDELITY
//  - Aquarius' ornate vessel is clearly visible (not hidden by the bent pose)
//  - Male Aquarius, bent over, pouring water from vessel into the heart vase
//  - Sleek clean line engraving, warm earthy palette, zero watermark
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const OUTPUT = '/home/z/my-project/download/Well_Spring_Logo_Icon.png';

const PROMPT = `A refined engraved vintage logo icon, classical apothecary seal aesthetic. Sleek, professional, therapy-centered, inviting. Clean elegant line engraving with generous negative space — sparse, minimal, modern-wellness aesthetic. NO dense crosshatching.

CENTRAL COMPOSITION (centered, fills frame with small margin):
- A MALE figure of AQUARIUS — young Greek/Roman man, short curly hair, short beard, athletic build, draped in flowing robes — is BENT OVER at the waist, leaning forward and downward. His ornate amphora VESSEL is held in both hands at chest height, clearly visible, tipped forward and downward, pouring a short clear stream of water. The vessel is prominently depicted — its ornate form, two handles, and spout are all clearly visible to the viewer, NOT hidden behind the figure's body.
- BENEATH THE VESSEL, on the ground, sits a STONE HEART-SHAPED VASE — a sculptural planter vessel shaped like a heart (two rounded lobes at top curving down to a gentle point at bottom, with a wide hollow opening at the top center where the soil and plants are). The vase is made of cool grey weathered granite stone, NOT an anatomical heart — it is clearly a sculptural vessel/planter with visible stone walls and a hollow opening at the top. The water stream from Aquarius's vessel falls into the opening of the heart vase.
- THREE PLANT STEMS grow upward out of the soil in the heart vase opening. Each stem is a slender green plant stalk rising vertically. Each stem bears a small ribbon banner with a single virtue word engraved on it: PEACE on the left stem, HONOR on the center stem, FIDELITY on the right stem. The ribbons are small and elegant, the words in clean uppercase serif lettering. Each stem also bears a few small green leaves.

PALETTE (warm earthy):
- Warm cream parchment background
- Warm deep walnut brown male figure, terracotta accents on vessel and robe trim
- Cool grey granite heart vase
- Cool aqua-blue water stream
- Soft natural green plant stems and leaves
- Subtle terracotta/gold ribbon banners with dark engraved lettering

STYLE: Sleek clean line engraving, sparse, refined, elegant. Minimal shading. Generous negative space. NO dense crosshatching. NO border, NO frame, NO ring, NO outer banner. Square 1024x1024.`;

async function main() {
  console.log('Generating Well Spring logo icon v3 (stone heart vase + 3 virtue stems)...');
  const zai = await ZAI.create();
  const response = await zai.images.generations.create({
    prompt: PROMPT,
    size: '1024x1024',
  });

  const outB64 = response.data[0].base64;
  const outBuf = Buffer.from(outB64, 'base64');
  fs.writeFileSync(OUTPUT, outBuf);
  console.log(`✓ Logo icon v3 saved to ${OUTPUT} (${outBuf.length} bytes)`);
}

main().catch((e) => {
  console.error('❌ Error:', e.message);
  console.error(e.stack);
  process.exit(1);
});
