import re

def process_skill():
    with open('SKILL.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # 2.1 Frontmatter
    content = re.sub(
        r'description: Generates optimized prompts.*?\.',
        'description: Acts as a prompt engineer to optimize, improve, fix, adapt or write prompts. Triggers only when the user explicitly asks to write, fix, improve, or adapt a prompt for a specific AI tool.',
        content,
        flags=re.DOTALL
    )
    content = content.replace('Does not activate for general conversation, coding tasks, document writing, or other non-prompt-engineering work.', 'Does NOT activate for general chat, coding, document writing, or non-prompt-engineering work.')

    # 2.2 Claude specific wording - nothing to replace as seen, but we will make sure.
    content = content.replace('Template M (Claude)', 'Template M')
    content = content.replace('claude.ai', 'Claude web')
    content = content.replace('Claude skill', 'Agent skill')

    # 2.4 Model Recency Gate (Gemini version)
    recency_gate_new = """### Model Recency Gate

Model names, defaults, controls, and availability change quickly. When the user asks for the "latest" model, names a model not covered below, or needs exact API settings:

1. Verify the current model and supported controls in the provider's official documentation (e.g. ai.google.dev or provider docs) using search or retrieval if available.
2. If current documentation cannot be checked, say that model-specific details are unverified and use the closest durable family-level route. Never invent a model slug, context size, or parameter."""
    content = re.sub(r'### Model Recency Gate.*?---', recency_gate_new + '\n\n---', content, flags=re.DOTALL)

    # 2.3 Gemini as home platform & Google surfaces
    gemini_profile = """**Gemini (Gemini 2.x / Gemini 3 Pro / Gemini App / API)**
- [verify] Strong at long-context and multimodal — leverage its large context window for document-heavy prompts.
- [verify] Uses grounding anchors and citation rules to reduce hallucinated sources ("Cite only sources you are certain of. If uncertain, say [uncertain].").
- [verify] Use explicit format locks with a labelled example to stop format drift on long outputs.
- [verify] For grounded tasks add "Base your response only on the provided context. Do not extrapolate."

**Google Surfaces (Gems, AI Studio, Gemini CLI, Antigravity, Jules, NotebookLM, Google Stitch, Imagen, Veo)**
- [verify] **Gems**: Compact instructions needed due to limits; use knowledge files for large context.
- [verify] **AI Studio**: Recommend current Gemini models. Adjust temperature based on task (low for code, higher for creative).
- [verify] **Gemini CLI & Antigravity**: Task-based prompting. Ask for Artifacts before execution. Use built-in browser automation.
- [verify] **Jules & NotebookLM**: Focus on document synthesis and grounded extraction.
- [verify] **Google Stitch**: Prompt-to-UI focused. Describe interface goal, add "match Material Design 3 guidelines".
- [verify] **Imagen / Veo / Gemini image gen**: Use visual descriptors, subject first, then style, mood, lighting.
"""
    
    # Remove old Gemini profile
    content = re.sub(r'\*\*Gemini 2\.x / Gemini 3 Pro\*\*.*?\n---\n', '', content, flags=re.DOTALL)
    
    # Insert Gemini profile at the top of Tool Routing (after Recency Gate)
    content = content.replace(recency_gate_new + '\n\n---', recency_gate_new + '\n\n---\n\n' + gemini_profile + '\n---\n')

    # Update Claude and GPT profiles with note
    content = content.replace('**Claude (Claude web, Claude API, Claude 5 / current Claude models)**', '**Claude (Claude web, Claude API, Claude 5 / current Claude models)**\n*(Note: Model names change fast, defer to Model Recency Gate if asked for "latest")*')
    content = content.replace('**ChatGPT / GPT-5.6 / OpenAI GPT models**', '**ChatGPT / GPT-5.6 / OpenAI GPT models**\n*(Note: Model names change fast, defer to Model Recency Gate if asked for "latest")*')

    with open('SKILL.md', 'w', encoding='utf-8') as f:
        f.write(content)

def process_templates():
    with open('references/templates.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('Template M: Current Claude Task Brief', 'Template M: Agentic Task Brief')
    content = content.replace('Claude Task Brief', 'Agentic Task Brief')
    
    gemini_variant = """
*(Gemini Variant: For Gemini agents like Antigravity, add a format lock and grounding anchor to the above template: "Output the final plan as an Artifact. Base all steps on the provided workspace context without hallucinating unsupported dependencies.")*
"""
    content = content.replace('### Template M', '### Template M\n' + gemini_variant)
    
    with open('references/templates.md', 'w', encoding='utf-8') as f:
        f.write(content)

def process_patterns():
    with open('references/patterns.md', 'r', encoding='utf-8') as f:
        content = f.read()
        
    content = content.replace('agentic model', 'autonomous agent')
    
    gemini_patterns = """
### 38. Ungrounded Citations (Gemini-specific)
**Pattern:** Asking Gemini for research without anchoring.
**Fix:** Add "Cite only sources you are certain of. If uncertain, say [uncertain]."

### 39. Format Drift (Gemini-specific)
**Pattern:** Asking for a long structured output without a lock.
**Fix:** Provide an explicit format lock with a labelled example showing the exact syntax required.

### 40. Mixing Unrelated Tasks (Gemini-specific)
**Pattern:** Giving an agent multiple unrelated deliverables in one session.
**Fix:** Split into one deliverable per session.
"""
    content += gemini_patterns
    
    with open('references/patterns.md', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    process_skill()
    process_templates()
    process_patterns()
