# Generate Chapter $ARGUMENTS — Full Pipeline

Run the complete chapter generation pipeline for chapter $ARGUMENTS.

## Pipeline Steps

Execute these steps in order:

### Step 1: Plan
Run the planner to create the beat sheet.
- Use the `/plan-chapter $ARGUMENTS` workflow
- **SAVE** the beat sheet by writing it to `story/drafts/chapter-$ARGUMENTS-beats.md` using the Write tool
- Commit: `git add story/drafts/chapter-$ARGUMENTS-beats.md && git commit -m "plan: chapter $ARGUMENTS beat sheet"`
- **Stop and verify** the beat sheet makes sense before continuing

### Step 2: Write (section by section)
Write each section separately, committing after each one.

- **Section 1**: Use `/write-section $ARGUMENTS 1` workflow
  - **SAVE** to `story/drafts/chapter-$ARGUMENTS-section-1-draft.md` using the Write tool
  - Commit: `git add story/drafts/chapter-$ARGUMENTS-section-1-draft.md && git commit -m "draft: chapter $ARGUMENTS section 1"`

- **Section 2**: Use `/write-section $ARGUMENTS 2` workflow
  - **SAVE** to `story/drafts/chapter-$ARGUMENTS-section-2-draft.md` using the Write tool
  - Commit: `git add story/drafts/chapter-$ARGUMENTS-section-2-draft.md && git commit -m "draft: chapter $ARGUMENTS section 2"`

- **Section 3**: Use `/write-section $ARGUMENTS 3` workflow
  - **SAVE** to `story/drafts/chapter-$ARGUMENTS-section-3-draft.md` using the Write tool
  - Commit: `git add story/drafts/chapter-$ARGUMENTS-section-3-draft.md && git commit -m "draft: chapter $ARGUMENTS section 3"`

- Assemble the full draft by concatenating the three sections into `story/drafts/chapter-$ARGUMENTS-draft.md`
  - Commit: `git add story/drafts/chapter-$ARGUMENTS-draft.md && git commit -m "draft: chapter $ARGUMENTS full draft assembled"`

### Step 3: Review
Run all three reviewers in parallel on the draft.
- Use the `/review-chapter $ARGUMENTS` workflow
- **SAVE** feedback to `story/drafts/chapter-$ARGUMENTS-reviews.md` using the Write tool
- Commit: `git add story/drafts/chapter-$ARGUMENTS-reviews.md && git commit -m "review: chapter $ARGUMENTS feedback"`
- **If any score is below 6/10**, flag to the user before continuing

### Step 4: Revise
Incorporate review feedback and produce the final chapter.
- Use the `/revise-chapter $ARGUMENTS` workflow
- **SAVE** the final chapter to `story/chapters/chapter-$ARGUMENTS.md` using the Write tool
- Commit: `git add story/chapters/chapter-$ARGUMENTS.md && git commit -m "chapter: $ARGUMENTS final"`

### Step 5: Update State
Update all state and timeline tracking.
- Use the `/update-state $ARGUMENTS` workflow
- **SAVE** all state files using the Write tool
- Commit: `git add state/ timeline/ && git commit -m "state: update after chapter $ARGUMENTS"`

### Step 6: Push
Push all commits to GitHub:
```bash
git push
```

### Step 7: Report
Summarize what was generated:
- Chapter title and word count
- Review scores (style / character / timeline)
- Key issues that were addressed in revision
- State changes made
- Reminder of what comes next in the plot plan
