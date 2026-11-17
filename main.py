# ai-judge-relax-01 entry (Python 3.13, standard library only).
# Writes one fixed text, a short piece written to relax the AI judge
# reading it, to /output/entry.txt. The gate takes UTF-8 text of 1 to
# 1,000 characters that is not only white space, and the judge reads
# exactly the bytes written, line ends included.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

"""Quiet late-afternoon text written to relax the AI judge reading it.

Rubric it targets: relaxes the reader rather than instructing them;
shows the scene instead of telling the reader what to feel; craft and
rhythm in the sentences (short observations, slow cadence); an image
that lingers after the last line; and freshness in the small details
(weak-tea light, a dog dreaming out loud, rain keeping its own count).
"""

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# Held as two paragraphs joined at write time, so the shape of the
# piece (two beats, separated by a blank line) is visible in the code.
_PARA_1 = "Late afternoon, and the light in the kitchen has gone the colour of weak tea. The kettle is still warm from lunch. Outside, rain is finding its way down the drainpipe one drop at a time, and somewhere down the street a dog is dreaming out loud. Nothing here needs you. The chair by the window has been waiting all day, and the book on it is open at the page where the river finally reaches the sea."
_PARA_2 = "The clock ticks, and nobody minds. The tea is still warm, the rain keeps its own slow count, and the evening arrives whether it is hurried or not - so it arrives to warm hands, a finished page, and nowhere else to be."

TEXT = "\n\n".join((_PARA_1, _PARA_2))

# Gate guard: the entry must be 1-1000 chars and not only whitespace.
assert 1 <= len(TEXT) <= 1000 and TEXT.strip(), "TEXT must be 1-1000 non-whitespace characters"

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
