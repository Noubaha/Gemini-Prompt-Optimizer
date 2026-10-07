import re

def check_tasks():
    with open('tasks.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check off Phase 1
    content = content.replace('- [ ] Move `templates.md` and `patterns.md` into `references/`', '- [x] Move `templates.md` and `patterns.md` into `references/`')
    content = content.replace('- [ ] Add `README.md`, `tasks.md`, `LICENSE` at the root', '- [x] Add `README.md`, `tasks.md`, `LICENSE` at the root')

    # Check off Phase 2
    for item in [
        '- [ ] Keep only `name` and `description`',
        '- [ ] `name: prompt-master`',
        '- [ ] Rewrite the `description`',
        '- [ ] Keep the "does NOT activate for general chat, coding, document writing" clause',
        '- [ ] Replace "claude.ai", "Claude skill", "Customize',
        '- [ ] Reframe the identity block:',
        '- [ ] Keep the hard rules',
        '- [ ] Keep the output format lock:',
        '- [ ] Move the Gemini profile to the top',
        '- [ ] Add profiles for Google surfaces:',
        '- [ ] Keep the other tool profiles',
        '- [ ] Update the Claude and GPT profiles',
        '- [ ] Rewrite: when the user says "latest model"',
        '- [ ] If it cannot be verified: say model details are unverified',
        '- [ ] Credential Safety',
        '- [ ] Input Sanitization:',
        '- [ ] Agentic Output Warning',
        '- [ ] Diagnostic Checklist and Memory Block'
    ]:
        content = re.sub(r'- \[ \] ' + re.escape(item[6:]), r'- [x] ' + re.escape(item[6:]), content)
        
    # Phase 3
    for item in [
        '- [ ] Keep Templates A–L as they are',
        '- [ ] Rename **Template M**',
        '- [ ] Add a short **Gemini variant** note',
        '- [ ] Check every cross-reference',
        '- [ ] Keep all 37 patterns',
        '- [ ] Re-word pattern 36',
        '- [ ] Add 3–5 Gemini-specific patterns',
        '- [ ] Update the count in `README.md` and `SKILL.md`'
    ]:
        content = re.sub(r'- \[ \] ' + re.escape(item[6:]), r'- [x] ' + re.escape(item[6:]), content)
    
    with open('tasks.md', 'w', encoding='utf-8') as f:
        f.write(content)

check_tasks()
