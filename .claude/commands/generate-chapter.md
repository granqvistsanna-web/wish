# Generate Chapter $ARGUMENTS — Full Pipeline

Run the complete chapter generation pipeline for chapter $ARGUMENTS.

**IMPORTANT — Timeout Prevention**: Each step below is designed to be a self-contained unit of work. Complete and commit each step before moving to the next. If a step involves multiple sub-parts (e.g., writing 3 sections), complete and commit each sub-part individually. This ensures progress is saved even if a timeout occurs.

## Pipeline Steps

Execute these steps in order. **Commit after every sub-step** so no work is lost.

### Step 1: Plan
Run the planner to create the beat sheet.
- Read `story/synopsis.md`, `story/plot-plan.md`, `bible/`, `state/current/`, `timeline/events.md`
- **SAVE** the beat sheet by writing it to `story/drafts/chapter-$ARGUMENTS-beats.md` using the Write tool
- Commit: `git add story/drafts/chapter-$ARGUMENTS-beats.md && git commit -m "plan: chapter $ARGUMENTS beat sheet"`
- **Stop and verify** the beat sheet makes sense before continuing

### Step 2: Write Section 1
- Read the beat sheet + `bible/` + `state/current/`
- Write Section 1 (Opening, ~1,200 words)
- **SAVE** to `story/drafts/chapter-$ARGUMENTS-section-1-draft.md` using the Write tool
- Commit: `git add story/drafts/chapter-$ARGUMENTS-section-1-draft.md && git commit -m "draft: chapter $ARGUMENTS section 1"`

### Step 3: Write Section 2
- Read Section 1 draft for continuity
- Write Section 2 (Escalation, ~1,500 words)
- **SAVE** to `story/drafts/chapter-$ARGUMENTS-section-2-draft.md` using the Write tool
- Commit: `git add story/drafts/chapter-$ARGUMENTS-section-2-draft.md && git commit -m "draft: chapter $ARGUMENTS section 2"`

### Step 4: Write Section 3
- Read Sections 1–2 for continuity
- Write Section 3 (Landing, ~1,200 words)
- **SAVE** to `story/drafts/chapter-$ARGUMENTS-section-3-draft.md` using the Write tool
- Commit: `git add story/drafts/chapter-$ARGUMENTS-section-3-draft.md && git commit -m "draft: chapter $ARGUMENTS section 3"`

### Step 5: Assemble Draft
- Concatenate all three sections into `story/drafts/chapter-$ARGUMENTS-draft.md`
- Commit: `git add story/drafts/chapter-$ARGUMENTS-draft.md && git commit -m "draft: chapter $ARGUMENTS full draft assembled"`

### Step 6: Style Review
- Read `bible/style-guide.md`, `bible/forbidden-words.md`, and the draft
- Check for forbidden words, sentence variation, adverb density, show-don't-tell, AI-sounding prose
- **SAVE** to `story/drafts/chapter-$ARGUMENTS-review-style.md`
- Commit: `git add story/drafts/chapter-$ARGUMENTS-review-style.md && git commit -m "review: chapter $ARGUMENTS style"`

### Step 7: Character Review
- Read `bible/characters/` and `state/current/characters.md`
- Check for out-of-character dialogue, voice consistency, emotional accuracy
- **SAVE** to `story/drafts/chapter-$ARGUMENTS-review-character.md`
- Commit: `git add story/drafts/chapter-$ARGUMENTS-review-character.md && git commit -m "review: chapter $ARGUMENTS character"`

### Step 8: Timeline Review
- Read `timeline/events.md` and `state/current/`
- Check for contradictions, impossible timings, continuity errors
- **SAVE** to `story/drafts/chapter-$ARGUMENTS-review-timeline.md`
- Commit: `git add story/drafts/chapter-$ARGUMENTS-review-timeline.md && git commit -m "review: chapter $ARGUMENTS timeline"`

### Step 9: Compile Reviews
- Combine all three reviews into `story/drafts/chapter-$ARGUMENTS-reviews.md`
- Include: summary scores, prioritized issues, specific line references, suggested fixes
- Commit: `git add story/drafts/chapter-$ARGUMENTS-reviews.md && git commit -m "review: chapter $ARGUMENTS compiled feedback"`
- **If any score is below 6/10**, flag to the user before continuing

### Step 10: Revise Section 1
- Read review feedback relevant to Section 1
- Apply rewriting techniques to flagged passages
- **SAVE** to `story/drafts/chapter-$ARGUMENTS-section-1-revised.md`
- Commit: `git add story/drafts/chapter-$ARGUMENTS-section-1-revised.md && git commit -m "revise: chapter $ARGUMENTS section 1"`

### Step 11: Revise Section 2
- Read revised Section 1 for continuity
- Apply rewriting techniques to flagged passages
- **SAVE** to `story/drafts/chapter-$ARGUMENTS-section-2-revised.md`
- Commit: `git add story/drafts/chapter-$ARGUMENTS-section-2-revised.md && git commit -m "revise: chapter $ARGUMENTS section 2"`

### Step 12: Revise Section 3
- Read revised Sections 1–2 for continuity
- Apply rewriting techniques to flagged passages
- **SAVE** to `story/drafts/chapter-$ARGUMENTS-section-3-revised.md`
- Commit: `git add story/drafts/chapter-$ARGUMENTS-section-3-revised.md && git commit -m "revise: chapter $ARGUMENTS section 3"`

### Step 13: Assemble Final Chapter
- Concatenate all three revised sections into `story/chapters/chapter-$ARGUMENTS.md`
- Commit: `git add story/chapters/chapter-$ARGUMENTS.md && git commit -m "chapter: $ARGUMENTS final"`

### Step 14: Update State
Update all state and timeline tracking.
- Create `state/chapter-$ARGUMENTS/` with updated characters.md, plot-threads.md, world-state.md
- Update `timeline/events.md` and `timeline/character-arcs.md`
- Repoint `state/current` symlink
- Commit: `git add state/ timeline/ && git commit -m "state: update after chapter $ARGUMENTS"`

### Step 15: Push
Push all commits to GitHub:
```bash
git push
```

### Step 16: Report
Summarize what was generated:
- Chapter title and word count
- Review scores (style / character / timeline)
- Key issues that were addressed in revision
- State changes made
- Reminder of what comes next in the plot plan
