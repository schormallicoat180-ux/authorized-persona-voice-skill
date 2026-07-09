#!/usr/bin/env python3
"""Scaffold an authorized virtual persona package."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--id", required=True, help="lowercase persona id, e.g. rabbit")
    parser.add_argument("--display-name", required=True, help="human-readable persona name")
    parser.add_argument("--output-dir", required=True, help="directory that will contain the persona folder")
    parser.add_argument("--voice-sample", required=True, help="authorized voice sample path")
    parser.add_argument("--transcript-dir", default="", help="optional transcript/material directory")
    parser.add_argument("--prompt", default="", help="optional starter system prompt text")
    args = parser.parse_args()

    persona_id = args.id.strip().lower().replace("_", "-")
    if not persona_id or any(ch for ch in persona_id if not (ch.isalnum() or ch == "-")):
        raise SystemExit("--id must contain only lowercase letters, digits, and hyphens")

    root = Path(args.output_dir).expanduser().resolve() / persona_id
    root.mkdir(parents=True, exist_ok=True)
    (root / "voice-samples").mkdir(exist_ok=True)

    voice_path = Path(args.voice_sample).expanduser().resolve()
    transcript_dir = Path(args.transcript_dir).expanduser().resolve() if args.transcript_dir else ""

    prompt = args.prompt.strip() or (
        f"You are {args.display_name}, an authorized or fictional virtual persona. "
        "Do not claim to be any real person. Reply naturally, briefly, and stay within the configured boundaries."
    )
    (root / "system-prompt.md").write_text(prompt + "\n", encoding="utf-8")

    config = {
        "id": persona_id,
        "display_name": args.display_name,
        "type": "authorized_or_virtual_persona",
        "identity_policy": {"must_not_claim_real_person": True},
        "voice": {
            "sample_path": str(voice_path),
            "language_id": "zh",
            "generation_defaults": {
                "exaggeration": 0.5,
                "cfg_weight": 0.47,
                "temperature": 0.74,
            },
        },
        "llm": {
            "system_prompt_file": "system-prompt.md",
            "default_language": "zh",
            "max_reply_sentences": 5,
        },
    }
    (root / "persona-config.json").write_text(
        json.dumps(config, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    manifest = {
        "persona_id": persona_id,
        "display_name": args.display_name,
        "permission_note": "Use only with owned, licensed, authorized, or fictional material.",
        "voice_sample": str(voice_path),
        "transcript_dir": str(transcript_dir) if transcript_dir else "",
        "source_items": [],
    }
    (root / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(root)


if __name__ == "__main__":
    main()
