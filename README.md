# Prompt Master for Gemini — Prompt Optimizer Skill (Prompt Maxxing)

> Turn a rough idea into a **production-ready prompt** for any AI tool. One clean, copy-paste prompt. No wasted tokens. No re-prompting.

**Prompt Master for Gemini** is an open-source **Agent Skill** for **Gemini CLI**, **Antigravity** and **Gemini Gems** that acts as a **prompt engineer / prompt optimizer / prompt generator**. It detects the target AI tool, extracts your real intent, fixes the common prompt mistakes, and returns a single optimized prompt, tuned for that exact tool.

**Keywords:** prompt master · prompt maxxing · prompt optimizer · prompt engineering · prompt generator · prompt improver · Gemini skill · Gemini CLI skill · Antigravity skill · Gemini Gem · SKILL.md · agent skills · ChatGPT prompts · Claude prompts · Midjourney prompts · Cursor prompts

**Works with (target tools):** Gemini, Claude, ChatGPT / GPT, Grok, DeepSeek, Qwen, Llama / Ollama, Cursor, Windsurf, Cline, GitHub Copilot, Claude Code, Codex, Antigravity, Bolt, v0, Lovable, Devin, Perplexity, Midjourney, DALL·E, Stable Diffusion, ComfyUI, Sora, Runway, ElevenLabs, Zapier, Make, n8n, and any tool you throw at it.

> ⚠️ Unofficial community project. Not affiliated with or endorsed by Google or Anthropic.

---

## 🔥 The problem

> Write a vague prompt → wrong output → re-prompt → closer → re-prompt → right answer on attempt 4.

That is 3 wasted calls. Multiply by 50 prompts a day.

**Prompt maxxing** means getting the right output on attempt one. The best prompt is not the longest, it is the one where every word is load-bearing.

---

## 🚀 Installation

### Option A — Gemini CLI (recommended)

```bash
gemini skills install https://github.com/<your-username>/prompt-master.git
```

Install for one project only:

```bash
gemini skills install https://github.com/<your-username>/prompt-master.git --scope workspace
```

Then, inside Gemini CLI:

```
/skills list
```

### Option B — Manual copy

```bash
mkdir -p ~/.gemini/skills
git clone https://github.com/<your-username>/prompt-master.git ~/.gemini/skills/prompt-master
```

Project-level skills go in `.gemini/skills/` (the `.agents/skills/` alias also works).

### Option C — Link a local clone (for development)

```bash
gemini skills link /path/to/prompt-master
```

### Option D — Gemini Gem (no CLI needed)

1. Open the Gemini app → **Gems** → **New Gem**
2. Paste the contents of [`gem/gem-instructions.md`](gem/gem-instructions.md) into the instructions field
3. Optionally upload `references/templates.md` and `references/patterns.md` as knowledge files
4. Save and use it like any other Gem

> Gems do not load `SKILL.md` folders. The Gem file is a compact version of the same logic.

---

## 🎯 Usage

Invoke it naturally:

```
Write me a prompt for Cursor to refactor my auth module
```

```
Here's a bad prompt I wrote for GPT, fix it: [paste prompt]
```

```
Generate a Midjourney prompt for a cyberpunk city at night
```

```
Break this prompt down and adapt it for Stable Diffusion
```

```
I need a prompt for Claude Code to build a REST API — ask me what you need to know
```

Or call it by name:

```
/prompt-master
I want to ask Antigravity to build a todo app with React and Supabase
```

---

## ⚙️ How it works

Every request goes through the same pipeline:

1. **Detects the target tool** and routes silently to the right approach
2. **Extracts 9 dimensions of intent**: task, target tool, output format, constraints, input, context, audience, success criteria, examples
3. **Asks at most 3 clarifying questions**, only if critical info is missing
4. **Picks the right template** automatically (never shown to you)
5. **Applies safe techniques only**: role assignment, few-shot examples, grounding anchors, auditable reasoning, memory block
6. **Checks model recency** against official docs when the request depends on "latest"
7. **Runs a token-efficiency audit** and strips every word that changes nothing
8. **Delivers one copyable prompt** plus a one-line strategy note

### Gemini-specific behavior

- Uses **grounding anchors** and citation rules to reduce hallucinated sources
- Adds **explicit format locks with a labelled example** to stop format drift
- Leverages **long-context and multimodal** input when the task is document- or image-heavy
- Never asks for hidden chain-of-thought. It asks for conclusions, assumptions, evidence and checks instead

---

## 📐 13 prompt templates (auto-selected)

| Template | Best for |
|----------|----------|
| RTF | Fast one-shot tasks |
| CO-STAR | Reports, business writing |
| RISEN | Complex multi-step projects |
| CRISPE | Creative work, brand voice |
| Auditable Reasoning | Checkable math, logic, debugging |
| Few-Shot | Consistent structured output |
| File-Scope | Cursor, Windsurf, Copilot, any code editor AI |
| ReAct + Stop Conditions | Autonomous agents |
| Visual Descriptor | Midjourney, DALL·E, Stable Diffusion, Sora |
| Reference Image Editing | Editing an existing image |
| ComfyUI | Node-based image workflows |
| Prompt Decompiler | Breaking down / adapting existing prompts |
| Agentic Task Brief | Complex, multi-step agentic tasks |

Full text: [`references/templates.md`](references/templates.md)

---

## 🚫 37 credit-killing patterns detected

Vague verbs, two tasks in one prompt, no success criteria, missing output format, no scope boundary, no stop condition for agents, hallucination invites, context rot, and more, each with a before/after fix.

Full list: [`references/patterns.md`](references/patterns.md)

---

## 🗂️ Repo structure

```
prompt-master/
├── SKILL.md                 # Skill entry point (loaded by Gemini CLI / Antigravity)
├── README.md
├── LICENSE
├── tasks.md                 # Build plan / roadmap
├── gem/
│   └── gem-instructions.md  # Compact version for Gemini Gems
├── references/
│   ├── templates.md
│   └── patterns.md
└── tests/
    └── eval-prompts.md      # Prompts used to validate the skill
```

---

## 🧪 Testing

Run the prompts in [`tests/eval-prompts.md`](tests/eval-prompts.md) and check each output against its pass criteria. Target: **works on the first try, zero re-prompts**.

---

## 🛣️ Roadmap

See [`tasks.md`](tasks.md).

---

## 🤝 Contributing

Issues and PRs are welcome, especially new tool profiles, new patterns, and corrections when a tool or model changes.

---

## 🙏 Credits

Based on the original **Prompt Master** skill for Claude by [Nidhin Joseph Nelson](https://github.com/nidhinjs/prompt-master) (MIT). This repository adapts its structure and reference material for the Gemini ecosystem.

## 📄 License

MIT — see [LICENSE](LICENSE). The original copyright notice is preserved.
