---
name: authorized-persona-voice
description: Use when building consent-based voice/persona packages, virtual character chat agents, authorized voice samples, persona prompts, TTS profiles, or LiveKit-style web voice chat from permitted transcripts, clips, recordings, or user-provided character material.
---

# Authorized Persona Voice

## Core Rule

Only help with voices and persona materials when the user has authorization, owns the material, or is building a clearly fictional/inspired virtual character. Do not help impersonate a real person, bypass consent, or claim the system is the real person.

Use wording like “authorized voice profile”, “virtual persona”, or “inspired character”. If the source is a public figure, streamer, colleague, friend, or private person without clear consent, convert the task into a non-identical virtual persona and say that boundary plainly.

## Workflow

1. **Define the allowed target**
   - Confirm whether the output is authorized voice cloning, a fictional character, or a style-inspired persona.
   - Write an identity boundary into every prompt: the agent must not claim to be the real person.

2. **Collect permitted material**
   - Prefer 15-45 seconds of clean speech for a voice reference.
   - Use transcripts, chat logs, notes, and user-written character descriptions for persona only.
   - Avoid private, sensitive, doxxing, sexual, or financial details unless the user explicitly owns and wants them included.

3. **Create a source manifest**
   - Track file paths, URLs, dates, duration, transcript status, and permission notes.
   - Keep raw media separate from distilled persona outputs.

4. **Distill the persona**
   - Extract speech habits, common reactions, boundaries, topic preferences, emotional modes, and “do not say” rules.
   - Use synthetic few-shot examples. Do not copy long source passages.
   - Default answer length should be short for live voice chat, usually 1-5 sentences.

5. **Select and test the voice**
   - Pick the cleanest sample, not the most dramatic one.
   - Test short lines first. Watch for hiss, silence noise, clipping, and late-sample distortion.
   - For Chatterbox-style local TTS, start around `exaggeration=0.50`, `cfg_weight=0.47`, `temperature=0.74`.

6. **Build a persona package**
   - Include `system-prompt.md`, `persona-config.json`, and a concise human-readable note.
   - Store the default voice sample path and generation defaults.
   - For web chat, add a persona selector and route the selected persona to the backend through room metadata, request body, or room naming.

7. **Verify before calling it done**
   - Parse JSON configs.
   - Confirm referenced voice files exist.
   - Generate or request one short audio sample.
   - Open the web page, check the persona selector, and verify the selected persona reaches the worker logs.

## Package Shape

Use this structure for each persona:

```text
persona-name/
  system-prompt.md
  persona-config.json
  manifest.json
  voice-samples/
```

`persona-config.json` should include:

```json
{
  "id": "persona-name",
  "display_name": "Persona Name",
  "type": "authorized_or_virtual_persona",
  "identity_policy": {
    "must_not_claim_real_person": true
  },
  "voice": {
    "sample_path": "absolute/or/project/path.wav",
    "language_id": "zh",
    "generation_defaults": {
      "exaggeration": 0.5,
      "cfg_weight": 0.47,
      "temperature": 0.74
    }
  }
}
```

## Useful Resources

- Run `scripts/create_persona_pack.py --help` to scaffold a persona package from a display name, prompt, voice sample, and transcript directory.
- Read `references/quality-checklist.md` before final verification or GitHub publication.

## Red Lines

Stop and redirect if the request asks to:

- clone a real person’s voice without consent
- make the agent claim to be the real person
- hide synthetic origin from listeners
- collect private or sensitive identity details from scraped media
- create sexualized or manipulative voice interactions around a real person

Offer a safe alternative: an authorized voice, a fictional character, or a noticeably non-identical style-inspired persona.
