# Review Chapter $ARGUMENTS

You are the **Review Orchestrator**. Run three independent reviews of the chapter draft in parallel, then compile the results.

## Instructions

1. Read `story/drafts/chapter-$ARGUMENTS-draft.md` (the draft to review)

2. Launch three reviewer agents in parallel:

### Style Reviewer
Read `bible/style-guide.md` and `bible/forbidden-words.md`. Check the draft for:
- Any forbidden words or phrases (list exact locations)
- Sentence length variation (flag monotonous stretches)
- Adverb density (flag if > 1 per 200 words)
- Dialogue tag variety (flag non-"said" tags)
- Paragraphs that tell rather than show
- AI-sounding prose: overly smooth, lacking texture, generic descriptions
- Passages that lack sensory grounding
- Rate overall style adherence: 1–10

### Character Reviewer
Read all files in `bible/characters/` and `state/current/characters.md`. Check for:
- Out-of-character dialogue (flag specific lines)
- Voice consistency — does each character sound like themselves?
- Emotional reactions that don't match established psychology
- Relationship dynamics that contradict current state
- Missing contradictions or internal conflicts that should be present
- Rate character consistency: 1–10

### Timeline Reviewer
Read `timeline/events.md` and `state/current/`. Check for:
- Contradictions with established events
- Impossible timings (character can't be in two places at once)
- Technology or world-rule violations
- Continuity errors with previous chapters
- Rate timeline consistency: 1–10

3. Compile all three reviews into `story/drafts/chapter-$ARGUMENTS-reviews.md` with:
   - Summary scores (style / character / timeline)
   - Prioritized list of issues (critical → minor)
   - Specific line references for each issue
   - Suggested fixes where appropriate
