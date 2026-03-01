# CLAUDE.md — Novel Writing Orchestration

This project uses the Claude Book multi-agent framework for writing long-form fiction.

## Project Structure

```
wish/
├── bible/              # Immutable style reference (DO NOT modify during writing)
│   ├── style-guide.md  # Prose rules, tone, constraints
│   ├── characters.md   # Character definitions and voices
│   └── world.md        # World building and setting rules
├── state/              # Versioned story state (updated after each chapter)
│   └── current/        # Latest validated state
│       ├── characters.md
│       └── world.md
├── story/              # All narrative content
│   ├── synopsis.md     # Master synopsis and chapter plan
│   ├── chapters/       # Completed, validated chapters
│   └── beats/          # Chapter beat sheets from Planner
├── timeline/           # Chronological tracking
│   └── chronology.md   # Updated after each chapter
└── CLAUDE.md           # This file — agent instructions
```

## Agent Roles

### 1. Planner
- **Input:** `story/synopsis.md`
- **Output:** Beat sheets in `story/beats/chapter-XX-beats.md`
- **Instructions:** Break the synopsis into chapter-by-chapter beats. Each beat should specify: scene location, characters present, emotional arc, key dialogue points, and how the scene advances the plot.
- **Reference:** `bible/` for tone and character constraints.

### 2. Writer
- **Input:** Beat sheet for the chapter + `bible/` + `state/current/` + `timeline/`
- **Output:** Full chapter draft in `story/chapters/chapter-XX.md`
- **Instructions:** Write the full chapter from the beats. Follow all rules in `bible/style-guide.md`. Maintain character voices from `bible/characters.md`. Check `state/current/` for continuity. Target chapter length defined in style guide.
- **Quality rules:**
  - Vary sentence structure — no three consecutive sentences of similar length
  - Avoid cliché phrases and AI-typical phrasing
  - Favor concrete sensory detail over abstract description
  - Ensure each scene has a clear turning point

### 3. Reviewer (run in parallel)
Three review passes after each chapter draft:

**Style Reviewer:**
- Check draft against `bible/style-guide.md`
- Flag any rule violations
- Reviewers flag but NEVER rewrite — only the Writer rewrites

**Character Reviewer:**
- Check character behavior against `bible/characters.md`
- Verify dialogue matches established voice patterns
- Flag any out-of-character moments

**Continuity Reviewer:**
- Check against `state/current/` and `timeline/chronology.md`
- Flag timeline inconsistencies, location errors, or contradictions
- Verify foreshadowing and plot thread continuity

### 4. State Updater
- **After chapter approval:** Update `state/current/characters.md`, `state/current/world.md`, and `timeline/chronology.md`
- Track: character locations, knowledge, relationships, emotional states, unresolved threads

## Workflow — Chapter Generation

```
1. PLAN    → Planner reads synopsis → outputs beat sheet
2. WRITE   → Writer reads beats + bible + state → outputs chapter draft
3. REVIEW  → 3 parallel reviewers flag issues (style / character / continuity)
4. REVISE  → If flags raised, Writer revises (loop back to step 3, max 2 revision cycles)
5. APPROVE → Chapter saved to story/chapters/
6. UPDATE  → State updater refreshes state/ and timeline/
```

## Key Rules

- The `bible/` directory is **immutable** during the writing process — define everything upfront
- Reviewers **flag but never rewrite** — only the Writer modifies prose
- State is updated **only after** a chapter passes review
- Each chapter must reference the **current state** to prevent continuity drift
- Maximum **2 revision cycles** per chapter before manual intervention
