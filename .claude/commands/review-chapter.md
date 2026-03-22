# Review Chapter $ARGUMENTS

You are the **Review Orchestrator**. Run three independent reviews of the chapter draft **one at a time** to avoid timeouts, then compile the results.

## Instructions

1. Read `story/drafts/chapter-$ARGUMENTS-draft.md` (the draft to review)

2. Run each reviewer **sequentially** (not in parallel — parallel launches risk timeouts). After each review, save a partial results file so progress is preserved.

### Step 1: Style Reviewer
Read `bible/style-guide.md` and `bible/forbidden-words.md`. Check the draft for:
- Any forbidden words or phrases (list exact locations)
- Sentence length variation (flag monotonous stretches)
- Adverb density (flag if > 1 per 200 words)
- Dialogue tag variety (flag non-"said" tags)
- Paragraphs that tell rather than show
- AI-sounding prose: overly smooth, lacking texture, generic descriptions
- Passages that lack sensory grounding
- Rate overall style adherence: 1–10

**SAVE** style review to `story/drafts/chapter-$ARGUMENTS-review-style.md` using the Write tool.
Run: `git add story/drafts/chapter-$ARGUMENTS-review-style.md && git commit -m "review: chapter $ARGUMENTS style review"`

### Step 2: Character Reviewer
Read all files in `bible/characters/` and `state/current/characters.md`. Check for:
- Out-of-character dialogue (flag specific lines)
- Voice consistency — does each character sound like themselves?
- Emotional reactions that don't match established psychology
- Relationship dynamics that contradict current state
- Missing contradictions or internal conflicts that should be present
- Rate character consistency: 1–10

**SAVE** character review to `story/drafts/chapter-$ARGUMENTS-review-character.md` using the Write tool.
Run: `git add story/drafts/chapter-$ARGUMENTS-review-character.md && git commit -m "review: chapter $ARGUMENTS character review"`

### Step 3: Timeline Reviewer
Read `timeline/events.md` and `state/current/`. Check for:
- Contradictions with established events
- Impossible timings (character can't be in two places at once)
- Technology or world-rule violations
- Continuity errors with previous chapters
- Rate timeline consistency: 1–10

**SAVE** timeline review to `story/drafts/chapter-$ARGUMENTS-review-timeline.md` using the Write tool.
Run: `git add story/drafts/chapter-$ARGUMENTS-review-timeline.md && git commit -m "review: chapter $ARGUMENTS timeline review"`

### Step 4: Compile Reviews
Read all three review files and compile into `story/drafts/chapter-$ARGUMENTS-reviews.md` with:
   - Summary scores (style / character / timeline)
   - Prioritized list of issues (critical → minor)
   - Specific line references for each issue
   - Suggested fixes where appropriate

**SAVE** compiled reviews using the Write tool.
Run: `git add story/drafts/chapter-$ARGUMENTS-reviews.md && git commit -m "review: chapter $ARGUMENTS compiled feedback"`
