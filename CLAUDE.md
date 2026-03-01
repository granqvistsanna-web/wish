# Claude Book — Multi-Agent Novel Framework

## Project Overview

This is a **sci-fi romance novel** written in the style of **Octavia Butler**. The framework uses a multi-agent pipeline to plan, write, review, and refine each chapter.

## Genre & Style

- **Genre**: Science fiction + romance
- **Style inspiration**: Octavia Butler — spare, powerful prose; unflinching themes of power, identity, otherness, and intimacy; grounded worldbuilding; complex characters who make difficult choices
- **Tone**: Direct, visceral, emotionally honest. Never sentimental. Tenderness exists alongside brutality.

## Directory Structure

```
bible/          — Style rules, character sheets, world bible. NEVER modified during generation.
state/          — Versioned chapter snapshots. state/current/ symlinks to latest.
  template/     — Blank state file templates
  current/      — Symlink → latest validated chapter state
  chapter-NN/   — Per-chapter state snapshots
story/          — Synopsis, plot plan, and finished chapters.
  chapters/     — Final validated chapters
  drafts/       — In-progress chapter drafts
timeline/       — Chronological event records, updated per chapter.
.claude/        — Agent skill definitions
```

## Multi-Agent Workflow

Each chapter follows this pipeline:

### 1. PLAN (Planner Agent)
- Read `story/synopsis.md` and `story/plot-plan.md`
- Read `state/current/` for where the story left off
- Read `bible/` for all constraints
- Output: `story/drafts/chapter-NN-beats.md` — a beat sheet for the chapter

### 2. WRITE (Writer Agent)
- Read the beat sheet + `bible/` + `state/current/`
- Write the full chapter draft to `story/drafts/chapter-NN-draft.md`
- Target: 3,000–5,000 words per chapter

### 3. REVIEW (Reviewer Agents — run in parallel)
Three independent reviewers check the draft:
- **Style Reviewer**: Does it match the bible/style-guide.md? Flag AI-sounding prose.
- **Character Reviewer**: Are characters consistent with bible/characters/? Do voices ring true?
- **Timeline Reviewer**: Do events align with timeline/? Any contradictions?
- Output: `story/drafts/chapter-NN-reviews.md`

### 4. REVISE (Writer Agent)
- Incorporate review feedback
- Rewrite flagged passages using techniques: sensory grounding, syntactic variation, cliché subversion, character voice
- Output: `story/chapters/chapter-NN.md` (final)

### 5. UPDATE STATE
- Update `state/chapter-NN/` with new character states, relationship changes, plot threads
- Update `timeline/events.md` with chapter events
- Repoint `state/current/` symlink → `state/chapter-NN/`

## Rules for All Agents

1. **Always read `bible/` before writing.** The bible is law.
2. **Never contradict established timeline events.**
3. **Characters must evolve** — track emotional arcs in state files.
4. **Show, don't tell.** Butler's prose earns emotion through concrete detail.
5. **Dialogue must be distinct per character.** Each voice is recognizable.
6. **No forbidden words** — see `bible/forbidden-words.md`.
7. **Embrace discomfort.** Butler never shied from difficult truths about power and desire.

## Commands

- **Plan a chapter**: "Plan chapter N" → runs the Planner agent
- **Write a chapter**: "Write chapter N" → runs the Writer agent
- **Review a chapter**: "Review chapter N" → runs all three reviewers in parallel
- **Revise a chapter**: "Revise chapter N" → incorporates feedback and finalizes
- **Full pipeline**: "Generate chapter N" → runs plan → write → review → revise → update state
