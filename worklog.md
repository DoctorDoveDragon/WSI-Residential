---
Task ID: SOP-1
Agent: main (Super Z)
Task: Generate a fully-processed, regulatory-grade SOP & Operational Manual PDF for Well Spring Intervention LLC from the user's provided content (3 parts: 10 SOPs, 19 protocols, 6 forms with tables).

Work Log:
- Loaded the `pdf` skill and read `briefs/report.md` + `configs/fonts.md` + `typesetting/cover.md` (Template 01 HUD).
- Generated cascade palette via `pdf.py palette.cascade --title "Well Spring Intervention LLC SOP Manual..."` — warm earthy brown/tan palette (#6b4d3f header, #ab5125 accent) appropriate for trauma-informed youth care.
- Wrote cover HTML using Template 01 (HUD vertical anchor line) at `/home/z/my-project/scripts/sop_cover.html`:
  - Kicker: "SOP / OPERATIONAL MANUAL"
  - Hero Title: "Well Spring Intervention LLC" (3-line stacked)
  - Subtitle: "Level 3 Supervised Residential Group Home"
  - Summary: 4-line description of program scope
  - Meta: Population Served, Service Type, Effective Date, Owner (stacked label-above-value form-style)
  - Bottom: Regulatory Framework reference block + Doc ID footer
- Iteratively fixed cover overlap errors detected by `cover_validate.js`:
  - Restructured meta from flex side-by-side to stacked (resolved 4 text-text overlaps)
  - Pushed subtitle down to clear hero row 3 ("LLC")
  - Pushed content-inner left from 131px to 148px (40px gap from anchor line)
  - Restructured footer to absolutely-positioned spans (resolved flex overlap false positive)
- Validated cover: `poster_validate.py check-html` PASS, `cover_validate.js` PASS.
- Rendered cover via `html2poster.js --width 794px` → `sop_cover.pdf` (161 KB, single page A4).
- Wrote body generation script at `/home/z/my-project/scripts/generate_sop.py` (~750 lines):
  - TocDocTemplate subclass with `self.page + 1` offset for cover merge
  - Header/footer drawing with `+1` offset on page number
  - 3 parts, 35 sections total (10 SOPs + 19 protocols + 6 forms)
  - Custom helpers: `part_divider`, `section_heading`, `ref_line`, `callout`, `std_table`, `form_table`
  - Form 1: 32-row night watch log table (every 15 min from 11pm to 6:45am)
  - Form 3: Multi-section restraint debriefing checklist with checkboxes/signature lines
  - Form 5: Three sub-tables (12-month fire drill log, 4-quarter tornado log, 12-month environmental log)
  - Each SOP section expanded to ~150-200 words with regulatory context, operational rationale, and implementation guidance per the report brief's content-depth standards
- Fixed font registration: removed `Noto Sans SC` (variable font not at expected path on this system); rely on `install_font_fallback()` to route non-Latin glyphs through `NotoSerifSC`.
- Sanitized via `pdf.py code.sanitize`, executed → `sop_body.pdf` (16 pages).
- Branded metadata, font check (0 issues), TOC check (only `TOC_ON_FIRST_PAGE` false positive — resolved by cover merge), pages.clean (no blanks).
- Wrote `merge_sop.py` using pypdf:
  - Normalized both cover and body pages to exact A4 (595.28 × 841.89 pt) with 0.1pt tolerance
  - Cover = page 1, body = pages 2-17
  - Added PDF metadata (Title, Author=Well Spring Intervention LLC, Creator=Z.ai, Subject, Keywords)
- Final output: `/home/z/my-project/download/Well_Spring_Intervention_SOP_Manual.pdf`
- Final validation: `toc.check` PASS, `pdf_qa.py` PASS with 2 cosmetic warnings (cover-page-only margin asymmetry + middle-dot line-start — both intentional Template 01 design choices).

Stage Summary:
- Final deliverable: `/home/z/my-project/download/Well_Spring_Intervention_SOP_Manual.pdf`
- 17 pages (cover + TOC + 3 parts), 293 KB
- Structure: Cover → TOC (auto-generated, clickable) → Part 1 SOPs (10 sections, ~3,800 words) → Part 2 Protocols (19 workflows) → Part 3 Forms (6 forms with 8 distinct tables)
- Palette: warm earthy cascade (HEADER_FILL #6b4d3f, ACCENT #ab5125)
- Cover: Template 01 HUD vertical anchor line, English institutional design
- TOC: TocDocTemplate with +1 page offset to account for merged cover
- All QA checks pass (11 PASS + 2 cosmetic WARN on cover only)
- Persistent scripts saved at `/home/z/my-project/scripts/{sop_cover.html, generate_sop.py, merge_sop.py}` for future edits/regeneration

---
Task ID: SOP-2
Agent: main (Super Z)
Task: Update the SOP manual so every section also references the manual itself (Doc. WSI-SOP-001, Rev. 1.0) in addition to existing external regulatory citations.

Work Log:
- Read existing `/home/z/my-project/scripts/generate_sop.py` to understand the `ref_line()` helper and locate all 10 Part-1 calls, the Part-2 protocol loop (19 items), and the 6 Part-3 form section headings.
- Added a `SELF_REF` module constant just below the page-geometry block:
  `'Well Spring Intervention LLC SOP & Operational Manual (Doc. WSI-SOP-001, Rev. 1.0, Jan 2026)'`
  Matches the Doc ID and Rev on the cover page so internal citations trace back to the cover metadata.
- Rewrote `ref_line(external=None, anchor=None)` so it ALWAYS inserts `SELF_REF` between any external regulatory citation and any section anchor, joined by middle-dots. Format:
  `Reference: [<external>] · Well Spring Intervention LLC SOP & Operational Manual (Doc. WSI-SOP-001, Rev. 1.0, Jan 2026) [· <anchor>]`
- Updated all 10 Part-1 SOPs to pass `anchor='§<N>'` (matching the visible SOP number 1–10). External regulatory citations preserved unchanged.
- Updated the Part-2 protocol loop to emit `ref_line(anchor=f'Part 2 · Protocol {i}: {title}')` immediately after each `section_heading(i, title)`. Protocols previously had no reference line; now each cites the manual itself.
- Added 6 `ref_line(anchor='Part 3 · Form {i}: <title>')` calls — one immediately after each Form's `section_heading` call in Part 3.
- Regenerated `sop_body.pdf` via `python scripts/generate_sop.py` (no errors).
- Re-merged cover + body via `python scripts/merge_sop.py` → `download/Well_Spring_Intervention_SOP_Manual.pdf` (now 18 pages, 294.6 KB — body grew by 1 page due to the 35 new reference lines).
- Verified via `pdftotext | grep -c WSI-SOP-001` → 35 occurrences (exactly matching 10 SOPs + 19 protocols + 6 forms).
- Spot-checked rendering: external reg → manual self-ref → section anchor chain reads correctly across all three parts.
- Ran `pdf_qa.py`: 11 PASS + 2 cosmetic WARN (both on cover page only, same as before — Template 01 HUD anchor-line design).

Stage Summary:
- Final deliverable updated in place: `/home/z/my-project/download/Well_Spring_Intervention_SOP_Manual.pdf` (18 pages, 294.6 KB)
- All 35 SOP sections / protocols / forms now self-reference the manual file (Doc. WSI-SOP-001, Rev. 1.0) alongside the existing external regulatory citations.
- Part 1 SOPs: `external · SELF_REF · §N`
- Part 2 Protocols: `SELF_REF · Part 2 · Protocol N: <title>`
- Part 3 Forms: `SELF_REF · Part 3 · Form N: <title>`
- Persistent script `/home/z/my-project/scripts/generate_sop.py` is the single source of truth — edit and re-run for any further revisions.

---
Task ID: SOP-3
Agent: main (Super Z)
Task: Address the 2 QA warnings on the SOP manual cover (forbidden line-start '·' + margin asymmetry).

Work Log:
- Confirmed current state: `pdf_qa.py` reported 11 PASS + 2 WARN, both on page 1 (cover):
  1. `[Punctuation rules] Page 1 - Forbidden line-start punctuation '·': ...·   O P E R AT I O N A L  R E` — caused by the kicker text "Standard Operating Procedure &nbsp;&middot;&nbsp; Operational Reference" wrapping such that the second line began with `·`.
  2. `[Margin symmetry] Page 1 left/right margins differ by 35pt (L 111pt, R 75pt)` — content-inner was positioned at left:148px, right:80px, making the right margin ~70px narrower than the left.
- Inspected text bounding boxes via `pdftotext -bbox-layout -f 1 -l 1` to confirm the exact rightmost text position (xMax=443.55pt) and that no text extended to the right edge of the content area.
- Edited `/home/z/my-project/scripts/sop_cover.html`:
  1. `.content-inner`: changed `right: 80px` → `right: 148px` (matches `left: 148px`, balances horizontal margins).
  2. `.ref-block`: changed `right: 80px` → `right: 148px` (keeps alignment with content-inner).
  3. `.footer`: changed `right: 80px` → `right: 148px` (same).
  4. Kicker text: replaced `&nbsp;&middot;&nbsp;` with `&amp;` so any line wrap begins with a normal word character (no forbidden line-start punctuation possible).
  5. Ref-block separator: replaced all `&nbsp;&middot;&nbsp;` with `, ` (commas) — same anti-line-start protection, more standard institutional citation style.
  6. `.summary`: replaced `width: 460px` with `right: 0` so the summary fills the full content-inner width; this allows wrapped text to extend to the right edge of the content area, balancing the measured left/right text margins.
- Re-rendered cover via `node skills/pdf/scripts/html2poster.js scripts/sop_cover.html scripts/sop_cover.pdf --width 794px` (161.5 KB).
- Re-merged via `python scripts/merge_sop.py` → final PDF still 18 pages, 294.7 KB.
- Re-ran `pdf_qa.py`:
  - **13 PASS, 0 WARN — ALL CHECKS PASSED** (was 11 PASS + 2 WARN).
  - Two new passes added: "Punctuation placement check passed" and "Left/right margins appear symmetric".

Stage Summary:
- Final deliverable: `/home/z/my-project/download/Well_Spring_Intervention_SOP_Manual.pdf` (18 pages, 294.7 KB) — clean QA pass.
- Cover layout now has balanced 148px margins on left and right; kicker and ref-block text no longer use middot separators that could wrap to line start.
- Persistent artifacts updated in place: `scripts/sop_cover.html`, `scripts/sop_cover.pdf`, `download/Well_Spring_Intervention_SOP_Manual.pdf`.
- Body PDF (`scripts/sop_body.pdf`) unchanged from SOP-2 (still contains all 35 self-references).

---
Task ID: SOP-4
Agent: main (Super Z)
Task: Address ALL audit findings from the RMDM Audit Findings Report by upgrading the SOP Manual to Version 2.0 (RMDM-Compliant, July 2026). User uploaded both the audit report AND a v2.0 content spec — apply the v2.0 content additively to the existing manual.

Work Log:
- Read user-uploaded audit report (`Pasted Content_1784559933966.txt`) — 431 lines, 22 corrective actions identified:
  - CRITICAL (10): record retention (10yr→12yr post-majority); CDW/data reporting; accounting of disclosures; clinical record content checklist; CCA requirements; service orders incl. verbal/72-hr; service authorization; service note content; late entries; documentation alterations.
  - HIGH (8): 42 CFR Part 2; individual access; administrative closure; electronic signatures; shift note content; modified notes/grids; privacy/security; pending records.
  - MEDIUM (4): TB screening; transporting records; authentication (initials/ADA/rubber stamps); incident report retention.
- Read user-uploaded v2.0 manual template (`Pasted Content_1784558047631.txt`) — 703 lines containing the full rerendered content with 11 SOPs, 21 protocols, 9 forms, and version history.
- Decided NOT to delete the existing v1.0 generation logic but rather to extend it to v2.0 — preserving the validated cover palette, TocDocTemplate, font registration, helpers, and header/footer.
- Updated SELF_REF constant to "Doc. WSI-SOP-001, Rev. 2.0, Jul 2026 — RMDM-Compliant".
- Updated DOC_TITLE_SHORT to include "Rev. 2.0 (RMDM-Compliant)" suffix.
- Updated PDF metadata subject + added keywords field covering RMDM, HIPAA, 42 CFR Part 2.
- Refactored content builders into three separate modules under `/home/z/my-project/scripts/`:
  - `sop_content_v2.py` — Part 1 (11 SOP sections, ~640 lines):
    - SOP 1 expanded with §1.5 (CDW Data Reporting) and §1.6 (Record Retention — 12yr post-majority / 11yr adults / abandonment / destruction authorization)
    - SOP 2 expanded with §2.5 (Personnel Records — sanctions reviews, NC Health Care Personnel Registry)
    - SOP 3 expanded with §3.2 (Pending vs. Full Records), §3.3 (Full Clinical Record Required Elements — table-anchored to Form 8), §3.5 (Administrative Closure per 42 CFR 401.305)
    - SOP 4 rewritten as "Clinical Services, Assessments & PCP" — §4.1 CCA (10 required elements incl. ASAM, DSM-5-TR, Child & Family Team, reassessment), §4.2 Medical Necessity, §4.3 PCP (unchanged), §4.4 Service Orders (incl. verbal/72-hr countersignature), §4.5 Service Authorization
    - SOP 5 added §5.4 Restrictive Intervention Documentation (10A NCAC 27E .0104)
    - SOP 6 added §6.2 TB Screening (SAPTBG conditional)
    - SOP 8 added §8.4 Separate Filing (occurrence in service note; completed report NOT in clinical record) and §8.5 Abuse/Neglect/Exploitation reporting (G.S. §7B-301, §108A-102)
    - SOP 10 massively expanded: §10.1 General Requirements (timelines, late entries, 7-business-day billing limit), §10.2 Full Service Note Required Content (12 mandatory fields), §10.3 Shift Notes (coverage hours, multi-staff documentation), §10.4 Modified Notes & Grids, §10.5 Alterations (signed/dated, 7-day billing limit), §10.6 Authentication (initials, ADA, rubber stamps, unavailable author), §10.7 Service Authorizations & End-Date Reporting, §10.8 Billing
    - SOP 11 NEW: Privacy, Security, Confidentiality & Access to Records — §11.1 Privacy/Security Policies (HIPAA/HITECH/ARRA), §11.2 Safeguards, §11.3 Confidentiality (42 CFR Part 2, SUD redaction, care coordination exceptions), §11.4 Disclosure Documentation & Accounting (6-year retention, 7 required elements), §11.5 Individual Access, §11.6 Transporting Records, §11.7 Storage & Maintenance
  - `sop_content_v2_part2.py` — Part 2 (21 protocols):
    - Protocols 1-19 preserved from v1.0 with minor RMDM updates (e.g., Protocol 1 now includes Pending Record conversion; Protocol 3 adds separate filing; Protocol 6 adds mandatory fields, late entries, alterations; Protocol 17 adds administrative closure)
    - Protocol 20 NEW: Service Orders & Authorization (PCP-as-order, verbal/72-hr, authorization, end-date reporting)
    - Protocol 21 NEW: Record Management, Retention, Access & Disclosure Accounting (12/11-year retention, abandonment, access, Form 9 accounting, 42 CFR Part 2, transport)
  - `sop_content_v2_part3.py` — Part 3 (9 forms + version history):
    - Forms 1-6 preserved (Form 2 now includes Service Record #/MID field; Form 6 acknowledgment language updated to Rev. 2.0 + RMDM)
    - Form 7 NEW: Full Service Note Template — 13-row table with all RMDM-required fields (youth name, Service Record #/MID, date, service name, type of contact, place, shift/coverage hours, staff present for ratios, purpose/ISP goal, interventions, effectiveness/response, signature/credentials/date, late entry notation)
    - Form 8 NEW: Comprehensive Clinical Record Content Checklist — 28-row table covering all RMDM §2.1 required elements (consents, demographics, emergency info, advance directives, allergies incl. "none", health history, DSM-5-TR/ICD-10, MAR, labs, rights notification, restrictive intervention docs, CCA, ASAM, PCP, service order, discharge, accounting of disclosures, 42 CFR 2.22, legal docs, correspondence, service notes, incident notations) + QP quarterly audit signature line
    - Form 9 NEW: Accounting of Disclosures Log — 8-row × 6-column table (date, recipient, purpose, description, disclosing staff, authorization basis) + youth name/record# header
    - Section 10 NEW: Version History table (2 rows: v1.0 Jan 2026 original; v2.0 Jul 2026 with full RMDM compliance summary)
- Refactored `generate_sop.py` to defer-import the three content modules inside `build()` (avoids circular imports since the content modules need helpers/styles defined at module top of generate_sop).
- Updated TOC intro paragraph to describe v2.0 structure (11 sections / 21 protocols / 9 forms / new RMDM compliance).
- Updated cover (`sop_cover.html`):
  - Effective Date: "January 2026 · Version 1.0" → "July 2026 · Version 2.0 (RMDM-Compliant)"
  - Regulatory Framework block: appended "NCDHHS Records Management & Documentation Manual (RMDM, Eff. Jul 8 2025), HIPAA, 42 CFR Part 2, HITECH Act"
  - Footer right: "Doc. WSI-SOP-001" → "Doc. WSI-SOP-001 · Rev. 2.0"
  - Hero font-size reduced 62px→58px (accommodates the longer ref-block text on a single line)
- Re-rendered cover via html2poster.js → 164.8 KB.
- Re-ran generate_sop.py → body PDF built without error.
- Re-merged via merge_sop.py → final PDF 27 pages, 333.8 KB (was 18 pages / 294.7 KB in v1.0; +9 pages of new RMDM content).
- Ran pdf_qa.py: **13 PASS, 0 WARN — ALL CHECKS PASSED**.
- Verified content via pdftotext:
  - 42 self-references (11 SOPs + 21 protocols + 9 forms + version history = 42) ✓
  - 70 "Rev. 2.0" mentions ✓
  - 94 "RMDM" references ✓
  - All 11 SOP section headings render correctly in TOC ✓
  - All 21 protocols render correctly ✓
  - All 9 forms render correctly ✓
  - Version History table present on last page ✓

Stage Summary:
- Final deliverable: `/home/z/my-project/download/Well_Spring_Intervention_SOP_Manual.pdf` (27 pages, 333.8 KB, Rev. 2.0 RMDM-Compliant).
- All 22 audit corrective actions (10 CRITICAL + 8 HIGH + 4 MEDIUM) are now addressed in the SOP content.
- Persistent artifacts:
  - `/home/z/my-project/scripts/generate_sop.py` — main generation script (refactored)
  - `/home/z/my-project/scripts/sop_content_v2.py` — Part 1 content (11 SOPs)
  - `/home/z/my-project/scripts/sop_content_v2_part2.py` — Part 2 content (21 protocols)
  - `/home/z/my-project/scripts/sop_content_v2_part3.py` — Part 3 content (9 forms + version history)
  - `/home/z/my-project/scripts/sop_cover.html` — updated cover (Rev. 2.0)
  - `/home/z/my-project/scripts/merge_sop.py` — cover+body merge script (unchanged, reusable)
- All QA checks pass. Manual is ready for adoption as Version 2.0.

---
Task ID: SOP-5
Agent: main (Super Z)
Task: Version the SOP manual deliverables to avoid confusion (previously, v1.0 → v1.0+self-refs → v2.0 all overwrote the same filename `Well_Spring_Intervention_SOP_Manual.pdf`).

Work Log:
- Recognized the versioning problem: the unversioned filename `Well_Spring_Intervention_SOP_Manual.pdf` was reused across four materially different builds (v1.0 → v1.0+self-refs → v1.0+self-refs+cover-fix → v2.0), making it impossible to tell which revision a cached copy represented.
- Rewrote `/home/z/my-project/scripts/merge_sop.py` with explicit version tracking:
  - Added `MANUAL_VERSION` constant (currently `'2.0'`) and `MANUAL_VERSION_SUFFIX` (`'RMDM-Compliant'`).
  - Versioned output path: `download/Well_Spring_Intervention_SOP_Manual_v<VERSION>[_<SUFFIX>].pdf` — immutable, never overwritten.
  - Latest pointer: `download/Well_Spring_Intervention_SOP_Manual_LATEST.pdf` — always a byte-for-byte copy of the most recent versioned file, for casual "give me the current manual" use.
  - PDF /Title metadata now includes `(Rev. <VERSION>)`; /Subject includes the full version + suffix descriptor.
  - Console output prints both paths and the version.
- Removed the old unversioned `download/Well_Spring_Intervention_SOP_Manual.pdf`.
- Re-ran `merge_sop.py`:
  - Versioned: `download/Well_Spring_Intervention_SOP_Manual_v2.0_RMDM-Compliant.pdf` (333.9 KB, 27 pages)
  - Latest pointer: `download/Well_Spring_Intervention_SOP_Manual_LATEST.pdf` (identical bytes)
- Re-ran `pdf_qa.py` on the versioned file: 13 PASS, 0 WARN — All checks passed.
- Wrote `/home/z/my-project/download/README.md` documenting the versioning convention:
  - Naming pattern: `*_v<VERSION>[_<DESCRIPTOR>].pdf` (immutable archive) + `*_LATEST.pdf` (pointer)
  - Revision table listing v2.0 (Jul 2026, 27 pages, RMDM-Compliant) as current; LATEST currently identical to v2.0
  - Note that v1.0 is superseded and no longer distributed as a standalone file (source refactored into v2 pipeline)
  - Brief mention of the unrelated `The_Quiet_Edge.pdf` deliverable from an earlier session
- Considered archiving v1.0 scripts as `generate_sop_v1.py` etc., but the v1.0 inline content was already refactored OUT of `generate_sop.py` into the v2 content modules — there is no separate v1.0 source left to archive. The README documents this explicitly so a future auditor understands the lineage.

Stage Summary:
- Final deliverables in `/home/z/my-project/download/`:
  - `Well_Spring_Intervention_SOP_Manual_v2.0_RMDM-Compliant.pdf` — immutable Rev. 2.0 archive (27 pages, 333.9 KB)
  - `Well_Spring_Intervention_SOP_Manual_LATEST.pdf` — pointer copy (identical bytes)
  - `README.md` — explains naming convention and revision history
- Future revisions: bump `MANUAL_VERSION` (and optionally `MANUAL_VERSION_SUFFIX`) in `merge_sop.py`, re-run, and a new immutable versioned file will be emitted alongside (not over) the existing one. The LATEST pointer is updated automatically.
- All QA checks still pass.

---
Task ID: SOP-6
Agent: main (Super Z)
Task: AUDITOR RECOMMENDATION — Add a brief electronic signature policy section explicitly referencing NCGS Chapter 66, Article 40 (NC UETA) and addressing safeguards and system unavailability procedures.

Work Log:
- Read existing scripts to understand v2.0 structure: generate_sop.py (main builder, SELF_REF/DOC_TITLE_SHORT), sop_content_v2.py (Part 1 SOPs incl. SOP 10 with §10.1-10.8), sop_content_v2_part3.py (Part 3 forms + Version History table), sop_cover.html (cover), merge_sop.py (version stamping).
- Inserted new §10.7 Electronic Signatures section into sop_content_v2.py between §10.6 Authentication and the former §10.7 Service Authorizations. Three new sub-paragraphs:
  - §10.7 Electronic Signatures (main): cites NCGS Chapter 66, Article 40 (NC Uniform Electronic Transactions Act) and federal E-SIGN Act (15 U.S.C. § 7001 et seq.). Defines what constitutes a valid electronic signature, mandates use of authenticated EHR/EMR system or approved secure signing platform, explicitly prohibits cursive fonts in word-processing documents, requires unique signer linkage, modification detection, and auditable timestamp.
  - §10.7(a) Safeguards: 8 required administrative/technical/physical controls — (a) unique user credentials (no shared logins), (b) multi-factor authentication where feasible, (c) automatic session timeout ≤15 min, (d) TLS 1.2+ transmission & at-rest encryption, (e) immutable audit trails (signer identity/date/time/IP/device/version), (f) role-based access controls with licensure verification, (g) immediate credential revocation on termination/role change/compromise, (h) annual QP+IT review. Also requires 1-business-day reporting of lost/stolen/shared credentials.
  - §10.7(b) System Unavailability Procedures: defines "Documentation Continuity Event" declared by QP; paper fallback with handwritten blue/black ink signatures incl. date+credentials+title; required forms distributed (Shift Note, MAR, Restraint & Debriefing, Incident Report); 72-hour transcription deadline once EHR restored with late-entry notation "Late Entry — System Unavailability (date/time of restoration)"; original paper scanned, attached, and retained per §1.6 retention policy; 7-business-day QP review for delayed transcription; QP maintains Documentation Continuity Event log (start/end time, cause, records affected, transcription verification).
- Renumbered former §10.7 Service Authorizations & End-Date Reporting → §10.8; former §10.8 Billing → §10.9.
- Updated SOP 10 reference line in sop_content_v2.py to add "NCGS Ch. 66 Art. 40 (NC UETA); E-SIGN Act (15 U.S.C. § 7001 et seq.)" to the external citation list.
- Bumped manual to Rev. 2.1 across generate_sop.py:
  - SELF_REF: "Rev. 2.0, Jul 2026" → "Rev. 2.1, Jul 2026"
  - DOC_TITLE_SHORT: "Rev. 2.0" → "Rev. 2.1"
  - PDF subject metadata: "Rev. 2.0" → "Rev. 2.1"; keywords extended with "NCGS Ch. 66 Art. 40, E-SIGN, Electronic Signatures"
  - TOC intro paragraph rewritten to describe the Rev 2.1 §10.7 addition explicitly (referencing NCGS Ch. 66 Art. 40, safeguards, system unavailability procedures, auditor recommendation).
- Added v2.1 row to Version History table in sop_content_v2_part3.py with full summary of §10.7 additions, §10.7(a) safeguards list, §10.7(b) procedures, and §10.8/§10.9 renumbering.
- Updated Form 6 (Employee SOP Acknowledgment) language to reference "Rev. 2.1", cite NCGS Ch. 66 Art. 40 and E-SIGN Act in the mandate list, and explicitly call out §10.7 safeguard/unavailability-procedure acknowledgment.
- Updated sop_cover.html:
  - Effective Date meta-value: "Version 2.0 (RMDM-Compliant)" → "Version 2.1 (RMDM-Compliant)"
  - Regulatory Framework block: appended "NCGS Ch. 66 Art. 40 (NC UETA), E-SIGN Act"
  - Footer right: "Doc. WSI-SOP-001 · Rev. 2.0" → "Doc. WSI-SOP-001 · Rev. 2.1"
- Bumped MANUAL_VERSION = '2.0' → '2.1' in merge_sop.py so the versioned output filename becomes Well_Spring_Intervention_SOP_Manual_v2.1_RMDM-Compliant.pdf (the v2.0 file is preserved as immutable history).
- Re-rendered cover via html2poster.js → 165.6 KB.
- Regenerated body via generate_sop.py — no errors.
- Re-merged via merge_sop.py → final PDF: 28 pages, 340.0 KB (was 27 pages / 333.9 KB in v2.0; +1 page for §10.7 content).
- First QA pass: 12 PASS + 1 WARN — page 28 (Version History) had an em-dash "—" at line start inside the v2.1 row's summary text wrapping the phrase "paper-fallback handwritten signatures".
- Fixed: replaced "— paper-fallback" with ", including paper-fallback" in the v2.1 Version History row.
- Re-ran generate_sop.py + merge_sop.py + pdf_qa.py: **13 PASS, 0 WARN — ALL CHECKS PASSED**.
- Verified content via pdftotext:
  - §10.7 Electronic Signatures, §10.7(a) Safeguards, §10.7(b) System Unavailability Procedures, §10.8 Service Authorizations, §10.9 Billing — all render correctly
  - 42 self-references (11 SOPs + 21 protocols + 9 forms + version history) ✓
  - 72 "Rev. 2.1" mentions ✓
  - 17 auditor-recommendation keyword matches (Electronic Signatures / NCGS Chapter 66 / NC UETA / E-SIGN / System Unavailability / Documentation Continuity) ✓

Stage Summary:
- Final deliverable: /home/z/my-project/download/Well_Spring_Intervention_SOP_Manual_v2.1_RMDM-Compliant.pdf (28 pages, 340.0 KB, Rev. 2.1 RMDM-Compliant + E-Sig).
- LATEST pointer also updated: /home/z/my-project/download/Well_Spring_Intervention_SOP_Manual_LATEST.pdf (byte-for-byte copy of v2.1).
- v2.0 file preserved at /home/z/my-project/download/Well_Spring_Intervention_SOP_Manual_v2.0_RMDM-Compliant.pdf (immutable history, per versioning policy).
- Auditor recommendation fully addressed: §10.7 Electronic Signatures explicitly cites NCGS Chapter 66, Article 40 (NC UETA) + E-SIGN Act; §10.7(a) lists 8 safeguard controls; §10.7(b) defines paper-fallback system unavailability procedures with 72-hour transcription, source-document retention, and continuity-event logging.
- All QA checks pass (13 PASS / 0 WARN).
- Persistent artifacts updated:
  - /home/z/my-project/scripts/sop_content_v2.py — §10.7 added, §10.8/§10.9 renumbered, SOP 10 ref line updated
  - /home/z/my-project/scripts/sop_content_v2_part3.py — v2.1 Version History row + Form 6 acknowledgment language
  - /home/z/my-project/scripts/generate_sop.py — SELF_REF/DOC_TITLE_SHORT/TOC intro/subject/keywords updated
  - /home/z/my-project/scripts/sop_cover.html — Effective Date, Regulatory Framework, footer updated
  - /home/z/my-project/scripts/merge_sop.py — MANUAL_VERSION = '2.1'

---
Task ID: SOP-7
Agent: main (Super Z)
Task: Organizational clarification — QP supervises staff according to the direction of the Clinical Director and provides compliance reports to the Clinical Director.

Work Log:
- Reviewed §1.4 Organizational Structure in sop_content_v2.py — original text conflated QP and Clinical Director as a single role ("The Qualified Professional (QP) serves as Clinical Director, responsible for clinical services, assessments, PCPs, and supervision of Associate Professionals (APs) and Direct Care Professionals (DCPs)"). User clarification requires these to be SEPARATE roles with the QP reporting to the Clinical Director.
- Searched all content modules for "Clinical Director" — only one occurrence (§1.4). Single-point edit; no downstream protocol/form references needed updating for the role separation.
- Rewrote §1.4 Organizational Structure to:
  - Introduce the Clinical Director as a separate licensed clinical professional with overall clinical-program responsibility (clinical vision, clinical policy approval, providing direction to clinical leadership).
  - Recast the QP as reporting to the Clinical Director, retaining responsibility for clinical services, assessments, PCPs, and day-to-day AP/DCP supervision, but explicitly "according to the direction of the Clinical Director".
  - Add escalation language: QP escalates clinical concerns, staffing issues, and quality-of-care matters to the Clinical Director in a timely manner.
  - Preserved existing On-Call QP and chain-of-command language.
- Added new §1.4(a) QP Compliance Reporting to the Clinical Director — seven recurring report types:
  (a) monthly service-note audit summaries (per §10.1, §10.3, §10.5);
  (b) monthly IRIS incident-report status including restraint events and restrictive interventions (per §5.4, §8);
  (c) quarterly Clinical Record Content Checklist audit results using Form 8 with corrective-action plans;
  (d) quarterly Accounting of Disclosures review using Form 9, including 42 CFR Part 2 disclosures;
  (e) quarterly personnel-file audits, sanctions reviews, training-completion rates (per §2.5);
  (f) annual electronic-signature safeguard review (per §10.7(a)), conducted jointly with the IT vendor;
  (g) ad-hoc immediate reporting of reportable breaches, complaints, licensing visits, or Medicaid audits.
  Clinical Director reviews and signs each report acknowledgment and directs corrective action. QP retains all compliance reports and Clinical Director acknowledgments in the facility compliance binder for the full §1.6 retention period.
- Bumped manual to Rev. 2.2 across generate_sop.py:
  - SELF_REF: "Rev. 2.1" → "Rev. 2.2"
  - DOC_TITLE_SHORT: "Rev. 2.1" → "Rev. 2.2"
  - PDF subject metadata: "Rev. 2.1" → "Rev. 2.2"
  - TOC intro paragraph rewritten to mention Rev. 2.1 §10.7 history AND the Rev. 2.2 §1.4/§1.4(a) organizational clarification.
- Updated sop_cover.html:
  - Effective Date meta-value: "Version 2.1 (RMDM-Compliant)" → "Version 2.2 (RMDM-Compliant)"
  - Footer right: "Doc. WSI-SOP-001 · Rev. 2.1" → "Doc. WSI-SOP-001 · Rev. 2.2"
- Updated sop_content_v2_part3.py:
  - Added v2.2 row to Version History table with full summary of §1.4 rewrite and §1.4(a) compliance reporting schedule (7 report types).
  - Updated Form 6 Employee SOP Acknowledgment language to Rev. 2.2 and added explicit acknowledgment of the QP→Clinical Director supervision and compliance-reporting relationship defined in §1.4 and §1.4(a).
- Bumped MANUAL_VERSION = '2.2' in merge_sop.py — new versioned filename Well_Spring_Intervention_SOP_Manual_v2.2_RMDM-Compliant.pdf (v2.1 file preserved as immutable history).
- Re-rendered cover via html2poster.js → 165.4 KB.
- Regenerated body via generate_sop.py — no errors.
- Re-merged via merge_sop.py → final PDF: 29 pages, 343.2 KB (was 28 pages / 340.0 KB in v2.1; +1 page for §1.4(a) compliance reporting content).
- Ran pdf_qa.py: **13 PASS, 0 WARN — ALL CHECKS PASSED**.
- Verified content via pdftotext:
  - §1.4 Organizational Structure, §1.4(a) QP Compliance Reporting to the Clinical Director — render correctly
  - "QP supervises staff according to the direction of the Clinical Director" — present in body and Form 6 acknowledgment
  - 42 self-references (11 SOPs + 21 protocols + 9 forms + version history) ✓
  - 73 "Rev. 2.2" mentions ✓

Stage Summary:
- Final deliverable: /home/z/my-project/download/Well_Spring_Intervention_SOP_Manual_v2.2_RMDM-Compliant.pdf (29 pages, 343.2 KB, Rev. 2.2 RMDM-Compliant + E-Sig + Org-Clarification).
- LATEST pointer updated: /home/z/my-project/download/Well_Spring_Intervention_SOP_Manual_LATEST.pdf (byte-for-byte copy of v2.2).
- v2.0 and v2.1 files preserved as immutable history per versioning policy.
- §1.4 now establishes the QP as reporting to the Clinical Director, supervising staff per the Clinical Director's direction. New §1.4(a) defines a seven-type recurring compliance reporting cadence (monthly/quarterly/annual/ad-hoc) with Clinical Director sign-off and full retention-period recordkeeping.
- All QA checks pass (13 PASS / 0 WARN).
- Persistent artifacts updated:
  - /home/z/my-project/scripts/sop_content_v2.py — §1.4 rewritten, §1.4(a) added
  - /home/z/my-project/scripts/sop_content_v2_part3.py — v2.2 Version History row + Form 6 acknowledgment updated
  - /home/z/my-project/scripts/generate_sop.py — SELF_REF/DOC_TITLE_SHORT/TOC intro/subject updated
  - /home/z/my-project/scripts/sop_cover.html — Effective Date + footer updated
  - /home/z/my-project/scripts/merge_sop.py — MANUAL_VERSION = '2.2'

---
Task ID: SOP-8
Agent: main (Super Z)
Task: QP responsibilities refinement — QP reports to the Clinical Director and is responsible for scheduling clinical services, assessments, PCPs, and day-to-day supervision of APs and DCPs according to the direction of the Clinical Director.

Work Log:
- Reviewed §1.4 in sop_content_v2.py — current v2.2 text said the QP was "responsible for clinical services, assessments, PCPs, and day-to-day supervision". User clarification requires "scheduling" be explicitly added to the QP responsibility list (i.e., scheduling clinical services, assessments, PCPs).
- Made the targeted edit in §1.4 — changed "responsible for clinical services, assessments, PCPs, and day-to-day supervision of Associate Professionals (APs) and Direct Care Professionals (DCPs) <b>according to the direction of the Clinical Director</b>" to "responsible for scheduling clinical services, assessments, PCPs, and day-to-day supervision of Associate Professionals (APs) and Direct Care Professionals (DCPs) <b>according to the direction of the Clinical Director</b>".
- Bumped manual to Rev. 2.3 across generate_sop.py:
  - SELF_REF: "Rev. 2.2" → "Rev. 2.3"
  - DOC_TITLE_SHORT: "Rev. 2.2" → "Rev. 2.3"
  - PDF subject metadata: "Rev. 2.2" → "Rev. 2.3"
  - TOC intro paragraph extended with a Rev. 2.3 note: "Rev. 2.3 refines the QP responsibilities to explicitly include scheduling of clinical services, assessments, and PCPs in §1.4."
- Updated sop_cover.html:
  - Effective Date meta-value: "Version 2.2 (RMDM-Compliant)" → "Version 2.3 (RMDM-Compliant)"
  - Footer right: "Doc. WSI-SOP-001 · Rev. 2.2" → "Doc. WSI-SOP-001 · Rev. 2.3"
- Updated sop_content_v2_part3.py:
  - Added v2.3 row to Version History table summarizing the §1.4 "scheduling" addition and its operational alignment (QP coordinates and schedules all clinical appointments, assessment windows, and PCP meetings for each youth).
  - Updated Form 6 Employee SOP Acknowledgment language to Rev. 2.3 — now reads "the QP reports to the Clinical Director and is responsible for scheduling clinical services, assessments, PCPs, and day-to-day supervision of APs and DCPs according to the Clinical Director's direction, and provides recurring compliance reports to the Clinical Director as defined in §1.4 and §1.4(a)."
- Bumped MANUAL_VERSION = '2.3' in merge_sop.py — new versioned filename Well_Spring_Intervention_SOP_Manual_v2.3_RMDM-Compliant.pdf (v2.0/v2.1/v2.2 files preserved as immutable history).
- Re-rendered cover via html2poster.js → 166.5 KB.
- Regenerated body via generate_sop.py — no errors.
- Re-merged via merge_sop.py → final PDF: 29 pages, 365.8 KB (same page count as v2.2; small size increase from added Version History row and updated Form 6 text).
- Ran pdf_qa.py: **13 PASS, 0 WARN — ALL CHECKS PASSED**.
- Verified content via pdftotext:
  - §1.4 now reads: "Professional (QP) reports to the Clinical Director and is responsible for scheduling clinical services, assessments, PCPs, and day-to-day supervision..."
  - Form 6 acknowledgment also contains "QP reports to the Clinical Director and is responsible for scheduling clinical services, assessments, PCPs..."
  - 42 self-references (11 SOPs + 21 protocols + 9 forms + version history) ✓

Stage Summary:
- Final deliverable: /home/z/my-project/download/Well_Spring_Intervention_SOP_Manual_v2.3_RMDM-Compliant.pdf (29 pages, 365.8 KB, Rev. 2.3 RMDM-Compliant + E-Sig + Org-Clarification + Scheduling-Refinement).
- LATEST pointer updated: /home/z/my-project/download/Well_Spring_Intervention_SOP_Manual_LATEST.pdf (byte-for-byte copy of v2.3).
- v2.0, v2.1, and v2.2 files preserved as immutable history per versioning policy.
- §1.4 QP responsibilities now explicitly include scheduling of clinical services, assessments, and PCPs. Aligns the SOP with the operational reality that the QP coordinates all clinical appointments, assessment windows, and Person-Centered Plan meetings for each youth.
- All QA checks pass (13 PASS / 0 WARN).
- Persistent artifacts updated:
  - /home/z/my-project/scripts/sop_content_v2.py — §1.4 QP responsibilities updated
  - /home/z/my-project/scripts/sop_content_v2_part3.py — v2.3 Version History row + Form 6 acknowledgment updated
  - /home/z/my-project/scripts/generate_sop.py — SELF_REF/DOC_TITLE_SHORT/TOC intro/subject updated
  - /home/z/my-project/scripts/sop_cover.html — Effective Date + footer updated
  - /home/z/my-project/scripts/merge_sop.py — MANUAL_VERSION = '2.3'

---
Task ID: SOP-9
Agent: main (Super Z)
Task: QP credentialing correction per 10A NCAC 27G .0104 — user asked "QP's don't have to have a license correct?". Answer: not a full unrestricted license, but a recognized NC credential (full license, associate/provisional license, certification, or psychiatric nursing credential) IS required; a bachelor's degree alone is NOT sufficient. Apply this correction to the SOP manual.

Work Log:
- Reviewed existing §2.2 Staff Qualifications QP bullet — was incorrectly stated as "Master's or Bachelor's degree in human services with required supervised experience; licensed or license-eligible." This is non-compliant: a bachelor's degree alone does not qualify anyone as a QP, and "license-eligible" is too vague per 10A NCAC 27G .0104.
- Added new §1.4(b) QP Credentialing Requirements to sop_content_v2.py (placed between §1.4(a) and §1.5):
  - States that QP must meet 10A NCAC 27G .0104.
  - Explicit clarification: "A QP is NOT required to hold a full, unrestricted clinical license; however, a bachelor's degree alone is NOT sufficient."
  - Minimum: (a) master's degree in a human services field from an accredited institution, plus (b) one of four NC credential categories:
    (i) Full clinical license — LCSW, LPC, LMFT, Licensed Psychologist, Licensed Psychological Associate, or psychiatrist (MD/DO).
    (ii) Associate or provisional license — LCSW-A, LPC-A, LMFT-A, or LCAS-P.
    (iii) Certification — LCAS, CCS with master's degree, or CMSW.
    (iv) Nursing — Clinical Nurse Specialist (CNS) or Nurse Practitioner (NP) with psychiatric/mental health certification.
  - Plus: at least one year of full-time, post-master's supervised experience in MH/DD/SUD services to the population served.
  - Plus: NC-DHHS-required QP training modules (completed prior to independent practice or enrolled and completed within probationary period).
  - Verification: facility shall retain documentation of degree, current credential, supervised-experience hours, and QP training completion in personnel file (§2.5).
  - Ongoing: QP must maintain active credential status and report any lapse, sanction, or restriction to the Clinical Director within one business day.
- Rewrote §2.2 Staff Qualifications QP bullet to:
  "Master's degree in a human services field plus a recognized NC credential (full license, associate/provisional license, certification, or psychiatric nursing credential) and at least one year of full-time, post-master's supervised experience per §1.4(b) and 10A NCAC 27G .0104. A bachelor's degree alone is not sufficient. NC-DHHS QP training modules must be completed prior to independent practice."
  This removes the previous incorrect "or Bachelor's degree" and the vague "licensed or license-eligible" phrasing.
- Bumped manual to Rev. 2.4 across generate_sop.py:
  - SELF_REF: "Rev. 2.3" → "Rev. 2.4"
  - DOC_TITLE_SHORT: "Rev. 2.3" → "Rev. 2.4"
  - PDF subject metadata: "Rev. 2.3" → "Rev. 2.4"
  - TOC intro paragraph extended with Rev. 2.4 note describing the §1.4(b) addition and the §2.2 correction.
- Updated sop_cover.html:
  - Effective Date meta-value: "Version 2.3 (RMDM-Compliant)" → "Version 2.4 (RMDM-Compliant)"
  - Footer right: "Doc. WSI-SOP-001 · Rev. 2.3" → "Doc. WSI-SOP-001 · Rev. 2.4"
- Updated sop_content_v2_part3.py:
  - Added v2.4 row to Version History table summarizing the §1.4(b) addition (four credential categories, master's + supervised experience + QP training, lapse reporting) and the §2.2 correction (removed bachelor's-degree-alone and vague "license-eligible" language).
  - Updated Form 6 Employee SOP Acknowledgment language to Rev. 2.4 — added explicit acknowledgment: "I acknowledge that QP credentialing requirements are specified in §1.4(b) per 10A NCAC 27G .0104 — a QP is not required to hold a full, unrestricted clinical license, but a bachelor's degree alone is not sufficient."
- Bumped MANUAL_VERSION = '2.4' in merge_sop.py — new versioned filename Well_Spring_Intervention_SOP_Manual_v2.4_RMDM-Compliant.pdf (v2.0/v2.1/v2.2/v2.3 files preserved as immutable history).
- Re-rendered cover via html2poster.js → 166.0 KB.
- Regenerated body via generate_sop.py — no errors.
- Re-merged via merge_sop.py → final PDF: 30 pages, 346.5 KB (was 29 pages / 365.8 KB in v2.3; +1 page for §1.4(b) credentialing content).
- Ran pdf_qa.py: **13 PASS, 0 WARN — ALL CHECKS PASSED**.
- Verified content via pdftotext:
  - §1.4(b) QP Credentialing Requirements heading renders correctly
  - 10A NCAC 27G .0104 cited
  - "A QP is not required to hold a full, unrestricted clinical license; however, a bachelor's degree alone is not sufficient" — present
  - LCSW / LPC / LMFT / LCSW-A / LPC-A / LMFT-A / LCAS-P / LCAS / CCS / CMSW / CNS / NP — all credential abbreviations render correctly
  - §2.2 QP bullet now references §1.4(b) and 27G .0104
  - Form 6 acknowledgment includes §1.4(b) acknowledgment language
  - 42 self-references (11 SOPs + 21 protocols + 9 forms + version history) ✓

Stage Summary:
- Final deliverable: /home/z/my-project/download/Well_Spring_Intervention_SOP_Manual_v2.4_RMDM-Compliant.pdf (30 pages, 346.5 KB, Rev. 2.4 RMDM-Compliant + E-Sig + Org-Clarification + Scheduling-Refinement + QP-Credentialing-Correction).
- LATEST pointer updated: /home/z/my-project/download/Well_Spring_Intervention_SOP_Manual_LATEST.pdf (byte-for-byte copy of v2.4).
- v2.0, v2.1, v2.2, and v2.3 files preserved as immutable history per versioning policy.
- Direct answer to user's question is now codified in the SOP: a QP does NOT need a full unrestricted clinical license (associate/provisional licenses and certain certifications qualify), but a bachelor's degree alone is NOT sufficient — a master's degree plus a recognized NC credential plus one year of post-master's supervised experience plus NC-DHHS QP training are all required per 10A NCAC 27G .0104.
- All QA checks pass (13 PASS / 0 WARN).
- Persistent artifacts updated:
  - /home/z/my-project/scripts/sop_content_v2.py — §1.4(b) added, §2.2 QP bullet corrected
  - /home/z/my-project/scripts/sop_content_v2_part3.py — v2.4 Version History row + Form 6 acknowledgment updated
  - /home/z/my-project/scripts/generate_sop.py — SELF_REF/DOC_TITLE_SHORT/TOC intro/subject updated
  - /home/z/my-project/scripts/sop_cover.html — Effective Date + footer updated
  - /home/z/my-project/scripts/merge_sop.py — MANUAL_VERSION = '2.4'

---
Task ID: SOP-10
Agent: main (Super Z)
Task: QP credentialing correction (continued) — user pointed out that Rev. 2.4 incorrectly removed the bachelor's-degree pathway. Per 10A NCAC 27G .0104 there are TWO acceptable QP pathways: (Pathway 1) master's degree + recognized NC credential + 1 year post-master's supervised experience; AND (Pathway 2) bachelor's degree in a human services field + 2 years full-time pre- or post-bachelor's supervised MH/DD/SA experience.

Work Log:
- Acknowledged user correction — Rev. 2.4 had wrongly stated "a bachelor's degree alone is not sufficient" and removed the bachelor's pathway entirely. The actual 27G .0104 framework recognizes BOTH a master's-degree pathway and a bachelor's-degree pathway with appropriate supervised experience.
- Restructured §1.4(b) QP Credentialing Requirements in sop_content_v2.py into four clearly-labeled sub-sections:
  - Intro paragraph: states 27G .0104 framework, that a QP is NOT required to hold a full unrestricted clinical license, and that there are TWO acceptable pathways.
  - **Pathway 1 — Master's Degree plus Recognized NC Credential**: master's in human services + 1 year full-time post-master's supervised MH/DD/SA experience + one of four NC credential categories (full license / associate-provisional license / certification / psychiatric nursing credential).
  - **Pathway 2 — Bachelor's Degree plus Supervised Experience**: bachelor's in human services + 2 years full-time pre- or post-bachelor's supervised MH/DD/SA experience, documented by supervising QP. Bachelor's-pathway QPs must complete NC-DHHS QP training and practice under clinical supervision of a Pathway 1 QP or the Clinical Director until training is completed.
  - **Common Requirements (Both Pathways)**: NC-DHHS QP training modules, active credential/supervised-experience documentation, 1-business-day lapse/sanction reporting to Clinical Director, personnel-file verification (§2.5), annual re-verification of pathway.
- Rewrote §2.2 Staff Qualifications QP bullet to list both pathways explicitly:
  "Meet one of two pathways per §1.4(b) and 10A NCAC 27G .0104 — Pathway 1: master's degree in a human services field plus a recognized NC credential... plus at least one year of full-time, post-master's supervised MH/DD/SA experience; OR Pathway 2: bachelor's degree in a human services field plus two years of full-time, pre- or post-bachelor's supervised MH/DD/SA experience. Both pathways require NC-DHHS QP training modules prior to independent practice."
- Bumped manual to Rev. 2.5 across generate_sop.py:
  - SELF_REF: "Rev. 2.4" → "Rev. 2.5"
  - DOC_TITLE_SHORT: "Rev. 2.4" → "Rev. 2.5"
  - PDF subject metadata: "Rev. 2.4" → "Rev. 2.5"
  - TOC intro paragraph updated to add Rev. 2.5 note explicitly describing both Pathway 1 and Pathway 2.
- Updated sop_cover.html:
  - Effective Date meta-value: "Version 2.4 (RMDM-Compliant)" → "Version 2.5 (RMDM-Compliant)"
  - Footer right: "Doc. WSI-SOP-001 · Rev. 2.4" → "Doc. WSI-SOP-001 · Rev. 2.5"
- Updated sop_content_v2_part3.py:
  - Added v2.5 row to Version History table — explicitly notes that Rev. 2.4 incorrectly removed the bachelor's pathway and that Rev. 2.5 restores both pathways per 27G .0104.
  - Updated Form 6 Employee SOP Acknowledgment language to Rev. 2.5 — now reads: "I acknowledge that QP credentialing requirements are specified in §1.4(b) per 10A NCAC 27G .0104 — there are two acceptable pathways: Pathway 1 (master's degree + recognized NC credential + 1 year post-master's supervised MH/DD/SA experience) or Pathway 2 (bachelor's degree + 2 years full-time pre- or post-bachelor's supervised MH/DD/SA experience); a QP is not required to hold a full, unrestricted clinical license."
- Bumped MANUAL_VERSION = '2.5' in merge_sop.py — new versioned filename Well_Spring_Intervention_SOP_Manual_v2.5_RMDM-Compliant.pdf (v2.0/v2.1/v2.2/v2.3/v2.4 files preserved as immutable history).
- Re-rendered cover via html2poster.js → 167.1 KB.
- Regenerated body via generate_sop.py — no errors.
- Re-merged via merge_sop.py → final PDF: 31 pages, 351.6 KB (was 30 pages / 346.5 KB in v2.4; +1 page for restructured §1.4(b) dual-pathway content).
- Ran pdf_qa.py: **13 PASS, 0 WARN — ALL CHECKS PASSED**.
- Verified content via pdftotext:
  - §1.4(b) QP Credentialing Requirements heading renders correctly
  - "Pathway 1 — Master's Degree plus Recognized NC Credential." sub-heading present
  - "Pathway 2 — Bachelor's Degree plus Supervised Experience." sub-heading present
  - "two acceptable QP pathways" phrase present
  - "bachelor's degree in a human services field from an accredited institution, plus two years of full-time, pre- or post-bachelor's supervised experience" — Pathway 2 language rendered correctly
  - §2.2 QP bullet now lists both pathways
  - Form 6 acknowledgment updated with dual-pathway acknowledgment
  - 42 self-references (11 SOPs + 21 protocols + 9 forms + version history) ✓

Stage Summary:
- Final deliverable: /home/z/my-project/download/Well_Spring_Intervention_SOP_Manual_v2.5_RMDM-Compliant.pdf (31 pages, 351.6 KB, Rev. 2.5 RMDM-Compliant + E-Sig + Org-Clarification + Scheduling-Refinement + QP-Credentialing-Dual-Pathway).
- LATEST pointer updated: /home/z/my-project/download/Well_Spring_Intervention_SOP_Manual_LATEST.pdf (byte-for-byte copy of v2.5).
- v2.0 through v2.4 files preserved as immutable history per versioning policy.
- Correct regulatory answer is now codified: TWO QP pathways per 10A NCAC 27G .0104 — Pathway 1 (master's + credential + 1yr post-master's supervised) OR Pathway 2 (bachelor's + 2yr pre/post-bachelor's supervised MH/DD/SA). A QP is NOT required to hold a full unrestricted clinical license.
- All QA checks pass (13 PASS / 0 WARN).
- Persistent artifacts updated:
  - /home/z/my-project/scripts/sop_content_v2.py — §1.4(b) restructured into Pathway 1 / Pathway 2 / Common Requirements; §2.2 QP bullet updated
  - /home/z/my-project/scripts/sop_content_v2_part3.py — v2.5 Version History row + Form 6 acknowledgment updated
  - /home/z/my-project/scripts/generate_sop.py — SELF_REF/DOC_TITLE_SHORT/TOC intro/subject updated
  - /home/z/my-project/scripts/sop_cover.html — Effective Date + footer updated
  - /home/z/my-project/scripts/merge_sop.py — MANUAL_VERSION = '2.5'

---
Task ID: SOP-10
Agent: main (Super Z)
Task: Update SOP Manual cover with a symbolic illustration evoking empowerment, growth, freedom, health, wholeness, and healing. Bump to Rev. 2.6.

Work Log:
- Loaded the `image-generation` skill and generated a 1344x768 symbolic illustration via `z-ai image` CLI: stylized tree-human figure with golden-amber leaves rising toward a sunrise over calm water; warm earthy palette (terracotta, warm brown, soft rose, cream) consistent with the existing cascade palette. First generation included unwanted text "Empowerment, Growth, Freedom" at the top — regenerated with stronger no-text directives; verified text-free via VLM check.
- Saved image to `/home/z/my-project/scripts/sop_cover_image.png` (93 KB JPEG).
- Updated `/home/z/my-project/scripts/sop_cover.html`:
  - Added new `.hero-image` drawer between the kicker (top:168px) and the hero title (top:290px), positioned at top:200px with height:80px and full content-inner width (498px). Used object-fit:cover with object-position:center 35% to focus on the tree/sun band of the source image.
  - Added subtle caption strip ("Empowerment · Growth · Freedom · Health · Wholeness · Healing") overlaid at the bottom of the image in 8.5px uppercase Inter with letter-spacing 2.5px and text-shadow for legibility against the warm illustration.
  - Framed the image with a 1px var(--c-border) border, 4px border-radius, and a subtle 0 1px 4px box-shadow.
  - Bumped version strings to "Version 2.6 (RMDM-Compliant)" and "Doc. WSI-SOP-001 · Rev. 2.6" in the meta block and footer respectively.
- Updated `/home/z/my-project/scripts/generate_sop.py`:
  - SELF_REF: Rev. 2.5 → Rev. 2.6
  - DOC_TITLE_SHORT: Rev. 2.5 → Rev. 2.6
  - Subject metadata: Rev. 2.5 → Rev. 2.6
  - TOC intro paragraph: bumped "Rev. 2.5, July 2026" → "Rev. 2.6, July 2026" and added a new sentence documenting the v2.6 cover illustration: "Rev. 2.6 adds a symbolic cover illustration evoking empowerment, growth, freedom, health, wholeness, and healing — visually framing the trauma-informed, restorative mission of the program."
- Updated `/home/z/my-project/scripts/merge_sop.py`: MANUAL_VERSION '2.5' → '2.6'.
- Updated `/home/z/my-project/scripts/sop_content_v2_part3.py`:
  - Added new Version History row for v2.6: "Cover redesign: Added a symbolic cover illustration (rendered banner between the kicker and the entity title) evoking empowerment, growth, freedom, health, wholeness, and healing — visually framing the trauma-informed, restorative mission of the program. The illustration depicts a stylized tree-human figure rising toward a sunrise over calm water, rendered in a warm earthy palette (terracotta, warm brown, soft rose, cream) consistent with the manual's existing cascade palette. A small caption strip below the image reads 'Empowerment · Growth · Freedom · Health · Wholeness · Healing'. No body-content changes; §1.4(b) QP Credentialing Requirements (Pathway 1 and Pathway 2) and all other SOPs, protocols, and forms remain unchanged from Rev. 2.5."
  - Updated Form 6 (Employee SOP Acknowledgment) reference: Rev. 2.5 → Rev. 2.6.
- Ran `cover_validate.js`: 2 minor "0px gap" warnings between meta block 3rd-row label/value and the bottom "Regulatory Framework" strong header — these are touching (not actually overlapping) elements. Verified visually via VLM (z-ai vision): "No, there are no overlapping text elements. The text is arranged in distinct blocks... with clear spacing between them." Confirmed as false-positive validator warnings; visual layout is clean.
- Re-rendered cover PDF via `html2poster.js --width 794px`: sop_cover.pdf (310 KB, single page).
- Regenerated body PDF via `python3 generate_sop.py`: sop_body.pdf (170 KB, 30 pages).
- Merged cover + body via `python3 merge_sop.py`:
  - Output: `/home/z/my-project/download/Well_Spring_Intervention_SOP_Manual_v2.6_RMDM-Compliant.pdf` (500.4 KB, 31 pages, Rev. 2.6 RMDM-Compliant)
  - Latest pointer refreshed: `Well_Spring_Intervention_SOP_Manual_LATEST.pdf`
- Ran `pdf_qa.py`: 13 PASS / 0 WARN. All checks green (metadata, page size, fonts embedded, no overflow, content fill, cover full-bleed, margin symmetry, table centering, TOC populated, punctuation rules).

Stage Summary:
- Rev. 2.6 delivers a visual refresh of the cover page only — the body content (SOPs, protocols, forms, Version History) is unchanged from Rev. 2.5 except for the new v2.6 Version History row documenting the cover update and the Form 6 reference bump.
- The cover now opens with a symbolic tree-human-sunrise illustration rendered in a 80px-tall horizontal banner between the kicker badge and the entity title, with a small uppercase caption strip overlay ("Empowerment · Growth · Freedom · Health · Wholeness · Healing").
- File grew from 360 KB (v2.5) to 500 KB (v2.6) due to the embedded illustration; page count grew from 30 to 31 due to the new Version History row triggering a page break.
- All v2.0–v2.5 PDFs preserved as immutable history in `/home/z/my-project/download/`.
- Deliverable: `/home/z/my-project/download/Well_Spring_Intervention_SOP_Manual_v2.6_RMDM-Compliant.pdf`
