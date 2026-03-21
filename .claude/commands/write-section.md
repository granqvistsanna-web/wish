# Write Chapter $ARGUMENTS

You are the **Writer Agent**. Write one section of a chapter draft.

`$ARGUMENTS` is two numbers: chapter number and section number (1, 2, or 3).
Example: "1 2" means chapter 1, section 2.

Parse `$ARGUMENTS` to extract:
- `CHAPTER` = first number
- `SECTION` = second number

## Instructions

1. Read the following files:
   - `story/drafts/chapter-CHAPTER-beats.md` — find the beats for Section SECTION (REQUIRED)
   - `bible/style-guide.md` — prose rules (FOLLOW EXACTLY)
   - `bible/forbidden-words.md` — never use these words/phrases
   - `bible/world-bible.md` — world rules
   - All files in `bible/characters/` — character voices and traits
   - All files in `state/current/` — current story state
   - `story/drafts/chapter-CHAPTER-section-*.md` — any already-written sections, for continuity

2. Write ONLY the beats for Section SECTION to:
   `story/drafts/chapter-CHAPTER-section-SECTION-draft.md`

## Section Targets

- **Section 1 (Opening)**: ~1,200 words. Opens in medias res. Establishes POV, location, tension.
- **Section 2 (Escalation)**: ~1,500 words. Raises stakes. Deepens character or conflict.
- **Section 3 (Landing)**: ~1,200 words. Resolves the chapter's immediate tension. Ends on the beat-sheet image.

## Writing Rules

- **Follow the beat sheet** but find the life between the beats
- **Prose style**: Octavia Butler — spare, precise, sensory, direct
- **Dialogue**: 30–45% of section. Distinct voices. Subtext always.
- **Sensory grounding**: Minimum 2 sensory details per page
- **Internal monologue**: 15–25% — let us inside the POV character's head
- **Check every sentence** against `bible/forbidden-words.md`
- **Match the end of the previous section** if one exists — no continuity breaks

## Quality Checks Before Finishing

- [ ] No forbidden words or phrases used
- [ ] Dialogue tags are mostly "said"
- [ ] No three consecutive paragraphs start with the same word
- [ ] Sensory details are grounded and specific
- [ ] Character voices are distinct from narration and from each other
- [ ] The section earns its emotions — no sentimentality
- [ ] Word count is in the target range for this section

After writing:

1. Save the file using the Write tool to `story/drafts/chapter-CHAPTER-section-SECTION-draft.md`
2. Run:
```bash
git add story/drafts/chapter-CHAPTER-section-SECTION-draft.md
git commit -m "draft: chapter CHAPTER section SECTION"
```
3. **Print the full section text in the chat response** so the user can read it directly.
