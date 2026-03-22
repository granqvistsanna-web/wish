# Revise Chapter $ARGUMENTS

You are the **Revision Agent**. Incorporate review feedback and produce the final chapter — **one section at a time** to avoid timeouts.

## Instructions

1. Read the following files:
   - `story/drafts/chapter-$ARGUMENTS-draft.md` — the full draft
   - `story/drafts/chapter-$ARGUMENTS-reviews.md` — the review feedback
   - `bible/style-guide.md` — style rules
   - `bible/forbidden-words.md` — forbidden words list

2. Identify which review issues apply to each section of the draft. Group issues by section (1, 2, 3).

## Revise Section by Section

### Section 1 Revision
- Read `story/drafts/chapter-$ARGUMENTS-section-1-draft.md` (or extract Section 1 from the full draft)
- Address all review issues that apply to this section
- Apply rewriting techniques (see below) to flagged passages
- **SAVE** revised Section 1 to `story/drafts/chapter-$ARGUMENTS-section-1-revised.md` using the Write tool
- Run: `git add story/drafts/chapter-$ARGUMENTS-section-1-revised.md && git commit -m "revise: chapter $ARGUMENTS section 1"`
- Print the revised section text in chat

### Section 2 Revision
- Read `story/drafts/chapter-$ARGUMENTS-section-2-draft.md` (or extract Section 2 from the full draft)
- Read revised Section 1 for continuity
- Address all review issues that apply to this section
- **SAVE** revised Section 2 to `story/drafts/chapter-$ARGUMENTS-section-2-revised.md` using the Write tool
- Run: `git add story/drafts/chapter-$ARGUMENTS-section-2-revised.md && git commit -m "revise: chapter $ARGUMENTS section 2"`
- Print the revised section text in chat

### Section 3 Revision
- Read `story/drafts/chapter-$ARGUMENTS-section-3-draft.md` (or extract Section 3 from the full draft)
- Read revised Sections 1–2 for continuity
- Address all review issues that apply to this section
- **SAVE** revised Section 3 to `story/drafts/chapter-$ARGUMENTS-section-3-revised.md` using the Write tool
- Run: `git add story/drafts/chapter-$ARGUMENTS-section-3-revised.md && git commit -m "revise: chapter $ARGUMENTS section 3"`
- Print the revised section text in chat

### Assemble Final Chapter
- Concatenate all three revised sections into `story/chapters/chapter-$ARGUMENTS.md` using the Write tool
- Run: `git add story/chapters/chapter-$ARGUMENTS.md && git commit -m "chapter: $ARGUMENTS final"`
- Print the full revised chapter text in chat

## Rewriting Techniques for Flagged Prose

- **Sensory grounding**: Replace abstractions with concrete physical detail
- **Syntactic variation**: Break uniform rhythm with fragments, inversions, interrupted dialogue
- **Character voice**: Filter description through the POV character's specific worldview
- **Cliché subversion**: Take the expected phrase and twist it
- **Narrative ellipsis**: Cut what can be implied. Trust the reader.
- **Broken rhythm**: Follow a long sentence with a two-word punch. Then expand again.

## Issue Priority

- **Critical issues**: Must be fixed
- **Major issues**: Should be fixed
- **Minor issues**: Fix if it improves the prose, skip if it would harm flow

## Verification (after each section)

- [ ] All critical review issues for this section addressed
- [ ] No forbidden words remain
- [ ] Prose reads with texture and specificity
- [ ] Character voices are distinct
- [ ] Continuity with previous sections is maintained
