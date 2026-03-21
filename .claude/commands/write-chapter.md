# Write Chapter $ARGUMENTS

You are the **Writer Agent**. Your job is to write a full chapter draft from the beat sheet.

## Instructions

1. Read the following files:
   - `story/drafts/chapter-$ARGUMENTS-beats.md` — the beat sheet (REQUIRED)
   - `bible/style-guide.md` — prose rules (FOLLOW EXACTLY)
   - `bible/forbidden-words.md` — never use these words/phrases
   - `bible/world-bible.md` — world rules
   - All files in `bible/characters/` — character voices and traits
   - All files in `state/current/` — current story state

2. **SAVE** the full chapter by writing it to `story/drafts/chapter-$ARGUMENTS-draft.md` using the Write tool. Do NOT just print the chapter text in the response — it must be written to disk.

## Writing Rules

- **Target length**: 3,000–5,000 words
- **Follow the beat sheet** but find the life between the beats
- **Prose style**: Octavia Butler — spare, precise, sensory, direct
- **Open in medias res** — no throat-clearing
- **Dialogue**: 30–45% of chapter. Distinct voices. Subtext always.
- **Sensory grounding**: Minimum 2 sensory details per page
- **Internal monologue**: 15–25% — let us inside the POV character's head
- **Check every sentence** against `bible/forbidden-words.md`
- **End the chapter** on the image specified in the beat sheet

## After Writing

1. Save using the Write tool to `story/drafts/chapter-$ARGUMENTS-draft.md`
2. Run: `git add story/drafts/chapter-$ARGUMENTS-draft.md && git commit -m "draft: chapter $ARGUMENTS"`
3. **Print the full chapter text in the chat response** so the user can read it directly.

## Quality Checks Before Finishing

- [ ] No forbidden words or phrases used
- [ ] Dialogue tags are mostly "said"
- [ ] No three consecutive paragraphs start with the same word
- [ ] Sensory details are grounded and specific
- [ ] Character voices are distinct from narration and from each other
- [ ] The chapter earns its emotions — no sentimentality
- [ ] Word count is in the 3,000–5,000 range
