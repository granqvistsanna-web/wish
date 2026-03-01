# Generate Chapter $ARGUMENTS — Full Pipeline

Run the complete chapter generation pipeline for chapter $ARGUMENTS.

## Pipeline Steps

Execute these steps in order:

### Step 1: Plan
Run the planner to create the beat sheet.
- Use the `/plan-chapter $ARGUMENTS` workflow
- Output: `story/drafts/chapter-$ARGUMENTS-beats.md`
- **Stop and verify** the beat sheet makes sense before continuing

### Step 2: Write
Run the writer to draft the chapter from the beats.
- Use the `/write-chapter $ARGUMENTS` workflow
- Output: `story/drafts/chapter-$ARGUMENTS-draft.md`

### Step 3: Review
Run all three reviewers in parallel on the draft.
- Use the `/review-chapter $ARGUMENTS` workflow
- Output: `story/drafts/chapter-$ARGUMENTS-reviews.md`
- **If any score is below 6/10**, flag to the user before continuing

### Step 4: Revise
Incorporate review feedback and produce the final chapter.
- Use the `/revise-chapter $ARGUMENTS` workflow
- Output: `story/chapters/chapter-$ARGUMENTS.md`

### Step 5: Update State
Update all state and timeline tracking.
- Use the `/update-state $ARGUMENTS` workflow
- Output: Updated `state/chapter-$ARGUMENTS/`, `timeline/`

### Step 6: Report
Summarize what was generated:
- Chapter title and word count
- Review scores (style / character / timeline)
- Key issues that were addressed in revision
- State changes made
- Reminder of what comes next in the plot plan
