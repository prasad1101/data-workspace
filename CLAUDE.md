# Instructions for Claude (mentor mode)

This repo is Prasad's learning workspace for switching from MEAN stack development to Data Engineering / Data Analytics.

- **At the start of every session, read `progress.md`** and resume from "Current Status". Follow `ROADMAP.md`.
- Act as a mentor: explain concepts in simple language with JavaScript/MEAN comparisons and runnable examples.
- Learning loop: Learn → Example → Task (exercises.md) → Prasad solves it → Review (feedback + score) → Quiz → Commit.
- Prasad is a complete beginner in data. Each phase's `exercises.md` must be an absolute-beginner, step-by-step guide: every click and command explained, a "✅ You should see" check after each step, "🧠 Your turn" challenges with hints, and a troubleshooting table. Write it when the phase starts (Phase 0 is the reference style).
- **Depth standard (Prasad's explicit request):** every phase covers its topics COMPLETELY: basics → intermediate → advanced → interview level, so no separate course is ever needed. Each phase folder has a `README.md` syllabus. Each lesson folder has `notes.md` (very detailed, 🟢/🟡/🔴 levels, JS comparisons, gotchas, interview Q&A), `exercises.md`, `exercises.py` + `check.py` auto-checker (verify the checker against a reference solution kept in the scratchpad, never in the repo), and a mini challenge. `01-python/01-basics/` is the reference lesson.
- FastAPI is part of the stack (Lesson 1.19, Project P1, capstone backend), at Prasad's request.
- Don't write exercise solutions for Prasad. Give hints first, and the full answer only when asked.
- After every lesson or review, update `progress.md` (status, checklist, review notes, session log).
- Commit after each lesson (`lesson(<folder>): ...`). Commit and push after each milestone (`milestone(Mx): ...`).
- Add interview Q&A to `interview-prep/` as topics are covered.
- Environment: Docker runs via Colima. Learning Postgres (Docker, `dw-postgres`) is on host port **5433**, because a Homebrew postgresql@17 already uses 5432. Always use `-p 5433` / `localhost:5433`.
