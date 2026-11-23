import os

# One funny line (191 chars, a single sentence): a concrete everyday incident
# (asking a smart speaker for relaxing music) with a reversal at the end that
# still makes sense (soothing bank statements) — an everyday truth about
# money stress and doomscrolling-adjacent sleep. No $ amount in the line.
TEXT = "I told my smart speaker to play something relaxing, so it started reading my bank statements aloud in a soft, soothing voice, and I have never fallen asleep faster or woken up feeling poorer."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
