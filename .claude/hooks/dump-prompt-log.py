#!/usr/bin/env python3
"""SessionEnd hook: auto-dump this session's verbatim user prompts into prompt-log/.

Format follows prompt-log/README.md: one file per dump, named
YYYY-MM-DD_HHMMSS<_optional-label>.txt, prompts numbered and separated by ---,
with a one-line header. Reads the session transcript (JSONL) rather than
re-typing anything, so the captured text is exactly what was submitted.
"""
import glob
import json
import os
import sys
from datetime import datetime

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROMPT_LOG_DIR = os.path.join(REPO_ROOT, "prompt-log")


def load_stdin_payload():
    try:
        raw = sys.stdin.read()
        return json.loads(raw) if raw.strip() else {}
    except Exception:
        return {}


def find_transcript_path(payload):
    transcript_path = payload.get("transcript_path")
    if transcript_path and os.path.isfile(transcript_path):
        return transcript_path

    # Fallback: newest transcript in this project's session directory.
    sanitized = REPO_ROOT.replace("/", "-")
    project_dir = os.path.expanduser(f"~/.claude/projects/{sanitized}")
    candidates = sorted(
        glob.glob(os.path.join(project_dir, "*.jsonl")),
        key=os.path.getmtime,
    )
    return candidates[-1] if candidates else None


def extract_prompts(transcript_path):
    prompts = []
    with open(transcript_path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except Exception:
                continue
            if entry.get("type") != "user":
                continue
            if entry.get("isMeta") or entry.get("isSidechain"):
                continue
            content = (entry.get("message") or {}).get("content")
            # Verbatim typed prompts are a plain string. Tool results and
            # injected skill/system content come through as a list instead.
            if isinstance(content, str) and content.strip():
                prompts.append(content.strip())
    return prompts


def main():
    payload = load_stdin_payload()
    transcript_path = find_transcript_path(payload)
    if not transcript_path:
        return

    prompts = extract_prompts(transcript_path)
    if not prompts:
        return

    os.makedirs(PROMPT_LOG_DIR, exist_ok=True)

    now = datetime.now()
    session_id = payload.get("session_id", "unknown-session")
    out_path = os.path.join(PROMPT_LOG_DIR, now.strftime("%Y-%m-%d_%H%M%S") + "_session-end.txt")

    header = (
        f"Dump taken {now.strftime('%Y-%m-%d %H:%M:%S')}, auto-captured on session end "
        f"(session {session_id}). Covers all prompts submitted in that session.\n\n"
    )
    body = "\n\n---\n\n".join(f"{i}. {p}" for i, p in enumerate(prompts, start=1))

    with open(out_path, "w", encoding="utf-8") as out:
        out.write(header)
        out.write(body)
        out.write("\n")


if __name__ == "__main__":
    main()
