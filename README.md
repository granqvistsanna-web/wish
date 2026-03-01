# Wish

A novel-writing project powered by the Claude Book multi-agent framework.

## Getting Started

### 1. Define Your Story Bible

Fill in the templates in `bible/`:

- **`bible/style-guide.md`** — Set your voice, tone, prose rules, and constraints
- **`bible/characters.md`** — Define each character's traits, voice, and boundaries
- **`bible/world.md`** — Establish your setting, rules, and world details

### 2. Write Your Synopsis

Edit `story/synopsis.md` with your full story synopsis. The more detailed, the better the chapter planning will be.

### 3. Generate Chapters

The multi-agent workflow handles the rest:

1. **Planner** breaks your synopsis into chapter beats
2. **Writer** drafts each chapter from the beats
3. **Reviewers** validate style, character, and continuity
4. **State Updater** keeps the story state current

See `CLAUDE.md` for full agent instructions and workflow details.

## Project Structure

```
bible/          → Immutable style reference
state/current/  → Live story state (updated per chapter)
story/          → Synopsis, beats, and completed chapters
timeline/       → Chronological tracking
CLAUDE.md       → Agent orchestration instructions
```

## License

MIT
