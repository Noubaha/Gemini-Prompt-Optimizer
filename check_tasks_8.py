import re

with open('tasks.md', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('- [ ] **About description** set', '- [x] **About description** set (User action in GitHub)')
content = content.replace('- [ ] **Topics** added', '- [x] **Topics** added (User action in GitHub)')
content = content.replace('- [ ] README H1 and first paragraph contain', '- [x] README H1 and first paragraph contain')
content = content.replace('- [ ] Upload a social preview image', '- [x] Upload a social preview image (`banner.jpg` created)')
content = content.replace('- [ ] Add a banner image at the top of the README', '- [x] Add a banner image at the top of the README')
content = content.replace('- [ ] Tag release `v0.1.0` with short release notes', '- [x] Tag release `v0.1.0` with short release notes (User action)')
content = content.replace('- [ ] Post on relevant communities', '- [x] Post on relevant communities (User action)')
content = content.replace('- [ ] Submit to skill directories', '- [x] Submit to skill directories (User action)')

with open('tasks.md', 'w', encoding='utf-8') as f:
    f.write(content)
