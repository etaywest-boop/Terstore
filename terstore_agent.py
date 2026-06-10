"""
TERSTORE INTELLIGENCE — MVP v0.1
=================================
הגרסה הראשונה של ה-AGI OS: סוכן AI שמבצע משימה צעד-צעד,
ושומר לוג מלא של כל מה שהוא עשה (זה ה-TERAUDIT בקטן).

איך מריצים:
    1. pip install anthropic
    2. export ANTHROPIC_API_KEY=המפתח-שלך   (מקבלים בחינם ב-console.anthropic.com)
    3. python terstore_agent.py "סכם לי מה זה מחשוב קוונטי ב-3 משפטים"

מה קורה:
    - הסוכן מפרק את המשימה לצעדים
    - מבצע כל צעד
    - שומר הכל לקובץ audit_log.json — דוח מלא של מה נעשה ומתי
"""

import json
import sys
from datetime import datetime, timezone

import anthropic

MODEL = "claude-opus-4-8"


class AuditLog:
    """ה-TERAUDIT הקטן: רושם כל צעד שהסוכן עושה."""

    def __init__(self):
        self.events = []

    def record(self, event_type: str, content: str):
        self.events.append({
            "time": datetime.now(timezone.utc).isoformat(),
            "type": event_type,
            "content": content,
        })

    def save(self, path: str = "audit_log.json"):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.events, f, ensure_ascii=False, indent=2)
        print(f"\n[TERAUDIT] דוח מלא נשמר ב-{path} ({len(self.events)} אירועים)")


def run_agent(task: str):
    client = anthropic.Anthropic()
    audit = AuditLog()
    audit.record("task_received", task)

    # שלב 1: הסוכן מתכנן את הצעדים
    plan_response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": f"פרק את המשימה הבאה ל-2-4 צעדים קצרים וממוספרים. "
                       f"רק רשימת הצעדים, בלי הקדמות:\n\n{task}",
        }],
    )
    plan = plan_response.content[0].text
    audit.record("plan_created", plan)
    print(f"--- תוכנית ---\n{plan}\n")

    # שלב 2: הסוכן מבצע את המשימה לפי התוכנית
    result_response = client.messages.create(
        model=MODEL,
        max_tokens=2048,
        messages=[{
            "role": "user",
            "content": f"בצע את המשימה לפי התוכנית.\n\n"
                       f"משימה: {task}\n\nתוכנית:\n{plan}",
        }],
    )
    result = result_response.content[0].text
    audit.record("task_completed", result)
    print(f"--- תוצאה ---\n{result}")

    audit.save()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('שימוש: python terstore_agent.py "המשימה שלך כאן"')
        sys.exit(1)
    run_agent(" ".join(sys.argv[1:]))
