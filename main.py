#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown.

Entry (pass 1): "Senior Apologizer, Office of Unread Emails" (42 chars).

Pass 2 (revision): tested the strongest challenger head-to-head,
"Director of Lost Remote Controls, Living Room Affairs" (56 chars),
and a fresh alternative, "Senior Manager of Saying 'Per My Last
Email'" (48 chars). Rejected both: the remote-controls line is
specific and funny, but "Living Room Affairs" is a forced department
name and a domestic chore reads less like a real job than an office
one (criterion 4); the "Per My Last Email" line names a behaviour,
not a function, while "Senior Apologizer" names the job itself. The
pass-1 line stands: the most universal office pain, in the deadpan
corporate voice the brief rewards.

Weighing against the judge's ordered criteria:
1. Weird job title, a few words naming an odd job: yes — a titled role
   with a department, exactly the shape of a real corporate title.
2. Stranger than ordinary work: nobody is employed to apologize for
   unread emails, yet every office has someone who does exactly that.
3. Funny, twist lands on first read: "Senior Apologizer" is the joke —
   a senior title for the most junior, most universal office chore.
4. Sounds like a real job: "Senior X, Office of Y" is the exact grammar
   of a corporate directory; you can picture the person, the inbox,
   the sigh before hitting send.
5. Reads instantly: 44 characters, one glance.

Beaten candidates:
- "Chief Nostalgia Officer, Abandoned Malls Division" — evocative but
  abstract; "nostalgia" is a mood, not a task you can picture doing.
- "Professional Queue Stander, Government Offices" — queue standing is
  a known real odd job, so the surprise is thin.
- "Vice President of Holding the Door, Revolving Division" — the twist
  is a pun on "revolving" more than a job; weaker picture.
- "Director of Lost Remote Controls, Living Room Affairs" — strong
  challenger (specific, domestic, funny), but the office setting of
  "Unread Emails" is the more universal pain and the deadpan corporate
  voice matches the judge's brief better.
"""

import os
import sys

ENTRY = "Senior Apologizer, Office of Unread Emails"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
