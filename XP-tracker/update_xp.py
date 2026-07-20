# XP-tracker/update_xp.py
import re
import sys
from pathlib import Path

README_PATH = Path(__file__).resolve().parent.parent / "README.md"

def calculate_cumulative_xp(weeks, xp_per_week=3500):
    return [week * xp_per_week for week in range(1, weeks + 1)]

def update_readme(weeks=7, xp_per_week=3500):
    # Read README
    content = README_PATH.read_text(encoding="utf-8")

    # Build scoreboard text
    scoreboard_lines = []
    cumulative_xp = calculate_cumulative_xp(weeks, xp_per_week)
    for i, xp in enumerate(cumulative_xp, start=1):
        scoreboard_lines.append(f"Week-{i}: {xp} XP")

    scoreboard_text = "\n".join(scoreboard_lines)

    # Replace old scoreboard section
    new_content = re.sub(
        r"(Azure Mastery XP Scoreboard[\s\S]*?)(?=\n##|\Z)",
        f"Azure Mastery XP Scoreboard\n{scoreboard_text}\n",
        content,
    )

    # Write updated README
    README_PATH.write_text(new_content, encoding="utf-8")
    print("✅ README updated with latest XP scoreboard!")

if __name__ == "__main__":
    # Default: 7 weeks, 3500 XP each
    weeks = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    update_readme(weeks)
