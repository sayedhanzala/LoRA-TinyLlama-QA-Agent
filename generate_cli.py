import os
import json
import re
from pathlib import Path

CLONE_DIR = "tldr"
TARGET_CMDS = [
    "git",
    "bash",
    "tar",
    "gzip",
    "grep",
    "scp",
    "rsync",
    "chmod",
    "chown",
    "curl",
    "wget",
    "venv",
    "pip",
]

# Parse TLDR markdown files
qa_pairs = []
pages_dir = Path("tldr/pages/common/")

# Check if the directory exists
if not pages_dir.exists():
    print(f"Error: Directory {pages_dir} does not exist.")
    exit(1)

# print(f"Files in {pages_dir}:")
# for file in pages_dir.glob("*.md"):
#     print(f"  - {file.name}")

found_commands = []
for cmd in TARGET_CMDS:
    md_file = pages_dir / f"{cmd}.md"
    if not md_file.exists():
        print(f"Command file not found: {md_file}")
        continue

    found_commands.append(cmd)
    print(f"Processing {cmd} command...")

    with open(md_file, encoding="utf-8") as f:
        content = f.read()

    examples = re.findall(r"- (.+?)\n\n`(.+?)`", content, re.DOTALL)

    if not examples:
        print(f"No examples found in {cmd}.md")

    for description, command in examples:
        qa_pairs.append({"question": description.strip(), "answer": command.strip()})

print(f"Found commands: {found_commands}")

if not qa_pairs:
    print(
        "No command files found in common directory. Checking other platform directories..."
    )
    for platform in ["linux", "windows", "osx"]:
        platform_dir = Path(f"tldr/pages/{platform}/")
        if not platform_dir.exists():
            continue

        for cmd in TARGET_CMDS:
            md_file = platform_dir / f"{cmd}.md"
            if not md_file.exists():
                continue

            print(f"Processing {cmd} command from {platform} directory...")

            with open(md_file, encoding="utf-8") as f:
                content = f.read()

            examples = re.findall(r"- (.+?)\n\n`(.+?)`", content, re.DOTALL)

            for description, command in examples:
                qa_pairs.append(
                    {"question": description.strip(), "answer": command.strip()}
                )

# Save to JSON file
os.makedirs("data", exist_ok=True)
with open("data/cli_qa.json", "w", encoding="utf-8") as f:
    json.dump(qa_pairs, f, indent=2)

print(f"Saved {len(qa_pairs)} Q&A pairs to data/cli_qa.json")
