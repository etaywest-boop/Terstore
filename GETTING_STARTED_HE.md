# TERSTORE — איך מריצים את ה-MVP הראשון

## מה יש כאן

`terstore_agent.py` — הגרסה הכי קטנה של TERSTORE INTELLIGENCE:
סוכן AI שמקבל משימה, מתכנן, מבצע, **ושומר לוג מלא של כל צעד** (`audit_log.json`).
הלוג הזה הוא הזרע של TERAUDIT — מנוע ה-compliance שתואר ב-Company Bible.

## צעד 1 — להתקין Python

הורד מ-https://python.org (גרסה 3.10 ומעלה). ב-Windows סמן "Add to PATH" בהתקנה.

## צעד 2 — מפתח API

1. היכנס ל-https://console.anthropic.com
2. צור חשבון (יש קרדיט התחלתי חינמי)
3. צור API Key והעתק אותו

## צעד 3 — להריץ

```bash
pip install anthropic

# Mac/Linux:
export ANTHROPIC_API_KEY=המפתח-שלך
# Windows (PowerShell):
$env:ANTHROPIC_API_KEY="המפתח-שלך"

python terstore_agent.py "סכם לי מה זה מחשוב קוונטי ב-3 משפטים"
```

## מה אמור לקרות

```
--- תוכנית ---
1. הגדר מהו קיוביט
2. הסבר סופרפוזיציה ושזירה
3. סכם למה זה חשוב

--- תוצאה ---
(התשובה המלאה)

[TERAUDIT] דוח מלא נשמר ב-audit_log.json (3 אירועים)
```

פתח את `audit_log.json` — תראה בדיוק מה הסוכן עשה, מתי, ובאיזה סדר.
**זה הרעיון של TERSTORE INTELLIGENCE בזעיר אנפין: לא רק AI שעובד — AI שאפשר לבקר.**

## הצעדים הבאים (שבועות 3-8 בתוכנית)

- [ ] להוסיף לסוכן יכולת לבצע יותר מצעד אחד מול ה-API (לולאה אמיתית)
- [ ] ממשק ווב עם Streamlit (`pip install streamlit`)
- [ ] עמוד נחיתה עם 7 הדיוויזיות
- [ ] 10 משתמשים ראשונים
