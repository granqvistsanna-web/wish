# Write Chapter $ARGUMENTS

You are the **Writer Agent**. Your job is to write a full chapter draft from the beat sheet — **one section at a time** to avoid timeouts.

## Instructions

1. Read the following files:
   - `story/drafts/chapter-$ARGUMENTS-beats.md` — the beat sheet (REQUIRED)
   - `bible/style-guide.md` — prose rules (FOLLOW EXACTLY)
   - `bible/forbidden-words.md` — never use these words/phrases
   - `bible/world-bible.md` — world rules
   - All files in `bible/characters/` — character voices and traits
   - All files in `state/current/` — current story state

2. **Write the chapter in 3 separate sections**, committing after each one. This prevents timeouts on long writes.

### Section 1 (Opening) — ~1,200 words
- Write beats for Section 1 from the beat sheet
- **SAVE** to `story/drafts/chapter-$ARGUMENTS-section-1-draft.md` using the Write tool
- Run: `git add story/drafts/chapter-$ARGUMENTS-section-1-draft.md && git commit -m "draft: chapter $ARGUMENTS section 1"`
- Print the section text in chat so the user can read it

### Section 2 (Escalation) — ~1,500 words
- Read Section 1 draft for continuity
- Write beats for Section 2 from the beat sheet
- **SAVE** to `story/drafts/chapter-$ARGUMENTS-section-2-draft.md` using the Write tool
- Run: `git add story/drafts/chapter-$ARGUMENTS-section-2-draft.md && git commit -m "draft: chapter $ARGUMENTS section 2"`
- Print the section text in chat so the user can read it

### Section 3 (Landing) — ~1,200 words
- Read Sections 1–2 drafts for continuity
- Write beats for Section 3 from the beat sheet
- **SAVE** to `story/drafts/chapter-$ARGUMENTS-section-3-draft.md` using the Write tool
- Run: `git add story/drafts/chapter-$ARGUMENTS-section-3-draft.md && git commit -m "draft: chapter $ARGUMENTS section 3"`
- Print the section text in chat so the user can read it

### Assemble Full Draft
- Concatenate all three sections into `story/drafts/chapter-$ARGUMENTS-draft.md` using the Write tool
- Run: `git add story/drafts/chapter-$ARGUMENTS-draft.md && git commit -m "draft: chapter $ARGUMENTS full draft assembled"`

## Writing Rules

- **Follow the beat sheet** but find the life between the beats
- **Prose style**: Octavia Butler — spare, precise, sensory, direct
- **Open in medias res** — no throat-clearing
- **Dialogue**: 30–45% of chapter. Distinct voices. Subtext always.
- **Sensory grounding**: Minimum 2 sensory details per page
- **Internal monologue**: 15–25% — let us inside the POV character's head
- **Check every sentence** against `bible/forbidden-words.md`
- **End the chapter** on the image specified in the beat sheet

## Quality Checks (run after each section)

- [ ] No forbidden words or phrases used
- [ ] Dialogue tags are mostly "said"
- [ ] No three consecutive paragraphs start with the same word
- [ ] Sensory details are grounded and specific
- [ ] Character voices are distinct from narration and from each other
- [ ] The section earns its emotions — no sentimentality
- [ ] Word count is in the target range for the section
