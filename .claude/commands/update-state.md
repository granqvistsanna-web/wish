# Update State for Chapter $ARGUMENTS

You are the **State Manager**. After a chapter is finalized, update all state and timeline files.

## Instructions

1. Read the finalized chapter: `story/chapters/chapter-$ARGUMENTS.md`

2. Read current state files in `state/current/` (if they exist)

3. Create the new state directory: `state/chapter-$ARGUMENTS/`

4. Create/update these files in `state/chapter-$ARGUMENTS/`:
   - **characters.md** — Update emotional states, knowledge, relationships, physical condition for every character who appeared or was affected
   - **plot-threads.md** — Update thread statuses, close resolved threads, open new ones, log foreshadowing
   - **world-state.md** — Update political/environmental/social conditions if changed

5. Update the symlink:
   ```bash
   rm -f state/current
   ln -s chapter-$ARGUMENTS state/current
   ```
   (Run from the `state/` directory)

6. Update `timeline/events.md`:
   - Add a new chapter section with all events from this chapter
   - Include: when, what, who, where, significance

7. Update `timeline/character-arcs.md`:
   - Add entries for each major character's state at end of this chapter

8. Verify no contradictions with previous timeline entries.
