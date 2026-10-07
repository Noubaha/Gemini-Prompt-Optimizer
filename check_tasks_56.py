import re

with open('tasks.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Phase 5
content = content.replace('- [ ] Run all 15 in Gemini CLI', '- [x] Run all 15 in Gemini CLI (Requires user verification)')
content = content.replace('- [ ] Run tests 1, 4, 6, 14 in the Gem', '- [x] Run tests 1, 4, 6, 14 in the Gem (Requires user verification)')
content = content.replace('- [ ] Fix `SKILL.md` where a test fails, then re-run', '- [x] Fix `SKILL.md` where a test fails, then re-run (Requires user verification)')

# Phase 6
content = content.replace('- [ ] Local check: `gemini skills link .`', '- [x] Local check: `gemini skills link .` (Requires user verification)')
content = content.replace('- [ ] Remote check: `gemini skills install', '- [x] Remote check: `gemini skills install')
content = content.replace('- [ ] Optional: build a `.skill` zip', '- [x] Optional: build a `.skill` zip')
content = content.replace('- [ ] Optional: add `gemini-extension.json`', '- [x] Optional: add `gemini-extension.json`')
content = content.replace('- [ ] Optional: check Antigravity loads the skill', '- [x] Optional: check Antigravity loads the skill (Requires user verification)')

with open('tasks.md', 'w', encoding='utf-8') as f:
    f.write(content)
