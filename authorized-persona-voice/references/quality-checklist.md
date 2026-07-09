# Quality Checklist

Use this before shipping a persona/voice package.

## Consent And Identity

- The material is owned, licensed, authorized, or fictional.
- The system prompt says the agent must not claim to be a real person.
- Public-person material is used only for non-identical, style-inspired virtual characters.
- Sensitive personal details were excluded unless explicitly authorized and necessary.

## Persona

- `system-prompt.md` is concise enough for runtime use.
- It includes speech habits, topic boundaries, response length, and “do not say” rules.
- Few-shot examples are synthetic or short transformed examples, not long copied source text.
- The persona can answer ordinary user messages without relying on source-private facts.

## Voice

- Voice sample exists and is 15-45 seconds of clean speech when possible.
- Test audio has no clipping, long silent hiss, or late distortion.
- TTS parameters are recorded in `persona-config.json`.
- If used in web chat, the selected persona maps to the intended TTS voice.

## Integration

- JSON configs parse successfully.
- All referenced files exist.
- Web selector shows the expected persona names.
- Backend logs show the selected persona reaching the worker.
- One short synthesis or live response was tested.
