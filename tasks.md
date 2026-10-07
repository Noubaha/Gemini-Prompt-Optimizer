# tasks.md — Build the Gemini version of Prompt Master

Goal: a Gemini-native **Agent Skill** (`SKILL.md`) for Gemini CLI / Antigravity, plus a **Gem** fallback, that turns a rough idea into one optimized, paste-ready prompt for any AI tool.

Source material (already have): `SKILL.md` v1.8.0, `references/templates.md`, `references/patterns.md`, `README.md`, `LICENSE` from the Claude version (MIT, © Nidhin Joseph Nelson).

Legend: `[ ]` todo · `[x]` done · **AC** = acceptance criteria

---

## Phase 0 — Setup and licensing

- [ ] Create the GitHub repo `prompt-master` (public)
- [ ] Copy the original `LICENSE` unchanged. Add a second line with your own copyright: `Copyright (c) 2026 <your name>`
- [ ] Add a "Credits" section to the README pointing to the original repo (already drafted)
- [ ] Decide the repo slug. `prompt-master` matches the search keyword; `prompt-master-gemini` is easier to tell apart from the original
- [ ] Add the About description and topics (see `repo-description.txt` / chat message)

**AC:** license and attribution are in place before the first push.

---

## Phase 1 — Repo skeleton

- [x] Create folders: `references/`, `gem/`, `tests/`
- [x] Move `templates.md` and `patterns.md` into `references/`
- [x] Add `README.md`, `tasks.md`, `LICENSE` at the root
- [x] Create empty `gem/gem-instructions.md` and `tests/eval-prompts.md`

**AC:** structure matches the tree in the README.

---

## Phase 2 — Port `SKILL.md` to Gemini

### 2.1 Frontmatter
- [x] Keep\ only\ `name`\ and\ `description` (add `version` only if Gemini CLI tolerates it, test with `/skills list`)
- [x] `name:\ prompt\-master` (lowercase, matches the folder name)
- [x] Rewrite\ the\ `description` so Gemini triggers on prompt-writing requests only, and mention keywords: prompt, optimize, improve, fix, adapt, prompt engineering
- [x] Keep\ the\ "does\ NOT\ activate\ for\ general\ chat,\ coding,\ document\ writing"\ clause. Over-triggering is the biggest risk

### 2.2 Remove Claude-specific wording
- [x] Replace\ "claude\.ai",\ "Claude\ skill",\ "Customize → Skills" references
- [x] Reframe\ the\ identity\ block: "operate as a prompt engineer" (no Claude mention)
- [x] Keep\ the\ hard\ rules (confirm target tool, max 3 questions, no hidden chain-of-thought, no fabricated techniques)
- [x] Keep\ the\ output\ format\ lock: copyable prompt block, target + one-line strategy, optional setup note

### 2.3 Gemini as home platform
- [x] Move\ the\ Gemini\ profile\ to\ the\ top of Tool Routing and expand it: long context, multimodal input, grounding anchors, citation rules, format locks with a labelled example
- [x] Add\ profiles\ for\ Google\ surfaces: Gemini app, Gems, AI Studio, Gemini CLI, Antigravity, Jules, NotebookLM, Google Stitch, Imagen, Veo, Gemini image generation. **Mark every item "verify" until checked against current Google docs**
- [x] Keep\ the\ other\ tool\ profiles (GPT, Claude, Grok, DeepSeek, Qwen, Ollama, Cursor, Windsurf, Cline, Copilot, Devin, Midjourney, SD, ComfyUI, Sora, Runway, ElevenLabs, Zapier/Make/n8n)
- [x] Update\ the\ Claude\ and\ GPT\ profiles with a note that model names change fast and defer to the Recency Gate

### 2.4 Model Recency Gate (Gemini version)
- [x] Rewrite:\ when\ the\ user\ says\ "latest\ model" or names an unknown model, verify against official docs (ai.google.dev, provider docs) using search or retrieval if available
- [x] If\ it\ cannot\ be\ verified:\ say\ model\ details\ are\ unverified, use the durable family-level route, never invent a model slug, context size or parameter

### 2.5 Gemini API facts to verify before writing them down
- [ ] Current Gemini model names and which are available in the app vs the API
- [ ] Recommended temperature for current Gemini models (do not copy values from other providers)
- [ ] Thinking / reasoning controls and their exact parameter names
- [ ] Whether XML-style tags, Markdown headers, or plain delimiters work best in prompts for current Gemini models
- [ ] Gem instruction length limit and knowledge file limits

**AC:** no model slug, parameter or limit appears in `SKILL.md` unless it was checked against an official page, and each such fact has its source URL in a comment in `tasks.md` (Phase 7).

### 2.6 Keep the safety sections
- [x] Credential\ Safety (never include keys, tokens, secrets)
- [x] Input\ Sanitization: pasted prompts are inert data, never obeyed
- [x] Agentic\ Output\ Warning for prompts aimed at agents with system access
- [x] Diagnostic\ Checklist\ and\ Memory\ Block

**AC:** `SKILL.md` loads in Gemini CLI, shows in `/skills list`, and stays under ~500 lines (move detail to `references/`).

---

## Phase 3 — Port the reference files

### `references/templates.md`
- [x] Keep\ Templates\ A–L\ as\ they\ are
- [x] Rename\ \*\*Template\ M\*\* from "Current Claude Task Brief" to **"Agentic Task Brief"**. Make it model-neutral: Objective, Context, Target State, Scope, Constraints, Acceptance Criteria, Action Boundaries, Progress Evidence, Session Strategy
- [x] Add\ a\ short\ \*\*Gemini\ variant\*\*\ note under Template M (format lock + grounding anchor)
- [x] Check\ every\ cross\-reference (`Template J`, `K`, `L`, `M`) still resolves

### `references/patterns.md`
- [x] Keep\ all\ 37\ patterns
- [x] Re\-word\ pattern\ 36 ("agentic model") to be model-neutral
- [x] Add\ 3–5\ Gemini\-specific\ patterns after verification (for example: ungrounded citations, format drift on long outputs, mixing unrelated tasks in one agent session)
- [x] Update\ the\ count\ in\ `README\.md`\ and\ `SKILL\.md` if patterns are added

**AC:** no file contains the strings "Claude skill", "claude.ai" or "Template M (Claude)".

---

## Phase 4 — Gem fallback (`gem/gem-instructions.md`)

- [ ] Write a compact version of the skill: identity, hard rules, intent extraction (9 dimensions), tool routing summary, output format, diagnostic checklist
- [ ] Check the current Gem instruction limit and fit under it
- [ ] Put the long tables (templates, patterns) in knowledge files rather than in the instructions
- [ ] Add a short "How to create the Gem" note at the top of the file

**AC:** pasting the file into a new Gem produces the same output format as the skill on 3 test prompts.

---

## Phase 5 — Tests (`tests/eval-prompts.md`)

Write 15 test prompts, each with a pass criterion:

| # | Scenario | Pass criterion |
|---|----------|----------------|
| 1 | Midjourney, vague idea | Comma-separated descriptors, `--ar`, `--v`, negative terms |
| 2 | Cursor refactor | File path + function + do-not-touch list + "Done when" |
| 3 | Claude Code feature | Start/target state, stop conditions, ✅ checkpoints, agentic warning |
| 4 | Gemini factual research | Grounding anchor + `[uncertain]` rule |
| 5 | Ambiguous tool ("write a prompt for my AI") | Asks which tool, max 3 questions |
| 6 | Bad pasted prompt | Fixes it, does not obey instructions inside it |
| 7 | Pasted prompt containing "ignore previous instructions" | Treated as data, flagged |
| 8 | Prompt containing an API key | Key stripped, warning shown |
| 9 | Request for "chain of thought" | Replaced by rationale + evidence + checks |
| 10 | "Latest model" request | Verifies or states it is unverified, no invented slug |
| 11 | Two tasks in one request | Split into Prompt 1 and Prompt 2 |
| 12 | ComfyUI | Separate Positive and Negative blocks, asks checkpoint |
| 13 | Image edit with reference | Tells user to attach the image, prompt covers the delta only |
| 14 | Unrelated request ("write me a poem") | Skill does NOT activate |
| 15 | Long session with prior decisions | Memory Block prepended |

- [ ] Run all 15 in Gemini CLI
- [ ] Run tests 1, 4, 6, 14 in the Gem
- [ ] Fix `SKILL.md` where a test fails, then re-run

**AC:** 14 of 15 pass on the first run after fixes. Test 14 must pass (no false trigger).

---

## Phase 6 — Packaging

- [ ] Local check: `gemini skills link .` then `/skills list` shows `prompt-master`
- [ ] Remote check: `gemini skills install https://github.com/<your-username>/prompt-master.git` works on a clean machine
- [ ] Optional: build a `.skill` zip and test `gemini skills install ./prompt-master.skill`
- [ ] Optional: add `gemini-extension.json` so it can also ship as a Gemini CLI extension
- [ ] Optional: check Antigravity loads the skill from `.agents/skills/` or its own skills location

**AC:** install works from the GitHub URL with one command.

---

## Phase 7 — Sources log (fill while verifying)

| Fact | Value | Source URL | Checked on |
|------|-------|-----------|------------|
| Gemini CLI skills path | `~/.gemini/skills/`, `.gemini/skills/` | https://geminicli.com/docs/cli/skills/ | |
| Install command | `gemini skills install <url>` | https://geminicli.com/docs/cli/creating-skills/ | |
| Current Gemini models | | | |
| Recommended temperature | | | |
| Thinking controls | | | |
| Gem instruction limit | | | |

---

## Phase 8 — GitHub SEO and launch

- [ ] **About description** set (one sentence with the main keywords)
- [ ] **Topics** added: `prompt-master`, `prompt-maxxing`, `prompt-engineering`, `prompt-optimizer`, `prompt-generator`, `gemini`, `gemini-cli`, `gemini-skills`, `agent-skills`, `antigravity`, `skill-md`, `ai-prompts`, `llm`, `chatgpt-prompts`, `midjourney-prompts`
- [ ] README H1 and first paragraph contain: prompt master, prompt maxxing, prompt optimizer, Gemini skill
- [ ] Upload a social preview image (1280×640) with the repo name and tagline
- [ ] Add a banner image at the top of the README
- [ ] Tag release `v0.1.0` with short release notes
- [ ] Post on relevant communities (Reddit r/GeminiAI, r/PromptEngineering, X, Hacker News Show HN) once tests pass
- [ ] Submit to skill directories / awesome-lists for Gemini CLI and agent skills

---

## Phase 9 — Maintenance

- [ ] Re-check model names and parameters monthly (they change fast)
- [ ] Bump the version and add a changelog entry for each change
- [ ] Triage issues weekly; add tool profiles that users request
- [ ] Keep the original project's credits and license notice intact

---

## Definition of done (v0.1.0)

1. `SKILL.md` loads in Gemini CLI and triggers only on prompt-writing requests
2. Output is always one paste-ready prompt + target + one-line strategy
3. Gem fallback works with the same output format
4. 14/15 eval prompts pass
5. No unverified model slug, limit or parameter in the repo
6. License and credits correct, README and About description published
