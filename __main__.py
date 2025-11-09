import sys, time, shutil, os

# ---------- Speed coefficient ----------
SPEED_COEFFICIENT = 1.0  # lower = faster animations, higher = slower

def sleep(t):
    time.sleep(max(0, t * SPEED_COEFFICIENT))

# ---- optional color support ----
try:
    import colorama
    colorama.just_fix_windows_console()
except Exception:
    pass

def supports_ansi():
    return sys.stdout.isatty()

RESET = "\033[0m" if supports_ansi() else ""
BOLD  = "\033[1m" if supports_ansi() else ""
DIM   = "\033[2m" if supports_ansi() else ""
ITAL  = "\033[3m" if supports_ansi() else ""
GLOW  = "\033[38;5;220m" if supports_ansi() else ""   # warm gold
CYAN  = "\033[36m" if supports_ansi() else ""
MAG   = "\033[35m" if supports_ansi() else ""
GREEN = "\033[32m" if supports_ansi() else ""
RED   = "\033[31m" if supports_ansi() else ""
BLUE  = "\033[34m" if supports_ansi() else ""
YELL  = "\033[33m" if supports_ansi() else ""
WHITE = "\033[97m" if supports_ansi() else ""

# ---- UX helpers ----
def slow_print(text, delay=0.04):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        sleep(delay)
    sys.stdout.write("\n")

def loading_dots(prefix="Processing", cycles=3, dot_delay=0.35):
    for _ in range(cycles):
        for dots in ["", ".", "..", "..."]:
            sys.stdout.write(f"\r{DIM}{prefix}{dots}{RESET}   ")
            sys.stdout.flush()
            sleep(dot_delay)
    sys.stdout.write("\r" + " " * (len(prefix) + 6) + "\r")

def progress_bar(total=30, label="Transmutation"):
    width = max(20, min(40, shutil.get_terminal_size((80, 20)).columns // 3))
    for i in range(total + 1):
        filled = int((i / total) * width)
        bar = f"{GLOW}{'█' * filled}{RESET}{DIM}{'░' * (width - filled)}{RESET}"
        pct = f"{int((i/total)*100):3d}%"
        sys.stdout.write(f"\r{BOLD}{label}:{RESET} [{bar}] {pct}")
        sys.stdout.flush()
        sleep(0.04)
    sys.stdout.write("\n")

def pulse(text, pulses=3, on=0.14, off=0.12):
    line = f"{GLOW}{BOLD}{text}{RESET}"
    for _ in range(pulses):
        sys.stdout.write("\r" + line)
        sys.stdout.flush()
        sleep(on)
        sys.stdout.write("\r" + " " * len(text) + "\r")
        sys.stdout.flush()
        sleep(off)
    print(line)

def stage(title, subtitle=None, wait=0.6):
    print(f"{CYAN}{BOLD}» {title}{RESET}" + (f"  {DIM}{subtitle}{RESET}" if subtitle else ""))
    loading_dots(prefix="   brewing", cycles=1)
    sleep(wait)

def banner():
    cols = shutil.get_terminal_size((80, 20)).columns
    title = " ALCHEMY CONSOLE "
    pad = max(0, (cols - len(title)) // 2)
    print(f"{DIM}{'─'*cols}{RESET}")
    print(" " * pad + f"{BOLD}{title}{RESET}")
    print(f"{DIM}{'─'*cols}{RESET}")

# ---- Shadow (transform) + Light (amplify) ----
RESPONSES = {
    # Shadow Mode
    "pain": [
        (f"{BLUE}Analyzing emotional energy…{RESET}", None),
        (f"{MAG}Stage I: Distill{RESET}", "Extracting the lesson."),
        (f"{MAG}Stage II: Purify{RESET}", "Releasing what isn’t yours."),
        (f"{MAG}Stage III: Transmute{RESET}", "Reframing the story."),
        (f"{MAG}Stage IV: Solidify{RESET}", "Setting a new pattern."),
        (f"{GLOW}{BOLD}🧪 Alchemy initiated… converting pain into purpose ✨{RESET}", None),
        (f"{GREEN}Result:{RESET} Purpose forged from struggle. You carry proof, not scars.", None),
    ],
    "fear": [
        (f"{BLUE}Scanning for threat signals…{RESET}", None),
        (f"{MAG}Breath anchor online{RESET}", "Inhale 4 • Hold 4 • Exhale 6"),
        (f"{GLOW}{BOLD}🔥 Facing the fire — courage is your gold.{RESET}", None),
        (f"{GREEN}Result:{RESET} Do the smallest next brave thing.", None),
    ],
    "doubt": [
        (f"{BLUE}Checking self-talk channel…{RESET}", None),
        (f"{MAG}Reality check{RESET}", "Compare facts vs feelings."),
        (f"{GLOW}{BOLD}💫 Gold doesn’t question its shine. You’ve got this.{RESET}", None),
        (f"{GREEN}Result:{RESET} Replace one “what if” with one “even if.”", None),
    ],
    "anger": [
        (f"{BLUE}Stabilizing heat…{RESET}", None),
        (f"{MAG}Redirect{RESET}", "Channel into focus & boundaries."),
        (f"{GLOW}{BOLD}⚙️ Transmuting fire into focus… clarity achieved.{RESET}", None),
        (f"{GREEN}Result:{RESET} Draft the boundary. Send it when calm.", None),
    ],

    # Light Mode (amplify)
    "joy": [
        (f"{YELL}Detecting radiant frequency…{RESET}", None),
        (f"{MAG}Stage I: Reflect{RESET}", "Savoring this moment."),
        (f"{MAG}Stage II: Amplify{RESET}", "Letting joy ripple outward."),
        (f"{MAG}Stage III: Anchor{RESET}", "Encoding this state in memory."),
        (f"{GLOW}{BOLD}☀️ Alchemy complete — gratitude bottled for later use.{RESET}", None),
        (f"{GREEN}Result:{RESET} Joy stored as creative energy.", None),
    ],
    "love": [
        (f"{YELL}Heart resonance stabilized…{RESET}", None),
        (f"{MAG}Stage I: Expand{RESET}", "Let it fill your chest."),
        (f"{MAG}Stage II: Radiate{RESET}", "Send that energy outward."),
        (f"{MAG}Stage III: Create{RESET}", "Turn connection into action."),
        (f"{GLOW}{BOLD}💗 Love alchemized — connection becomes creation.{RESET}", None),
        (f"{GREEN}Result:{RESET} Art, compassion, and purpose energized.", None),
    ],
    "peace": [
        (f"{YELL}Calm surface detected…{RESET}", None),
        (f"{MAG}Stage I: Settle{RESET}", "Breath softens the water."),
        (f"{MAG}Stage II: Stabilize{RESET}", "Stillness becomes strength."),
        (f"{GLOW}{BOLD}🌊 Peace amplified — clarity expands your field.{RESET}", None),
        (f"{GREEN}Result:{RESET} Focus and presence sustained.", None),
    ],
    "gratitude": [
        (f"{YELL}Counting frequencies of abundance…{RESET}", None),
        (f"{MAG}Stage I: Observe{RESET}", "Recognize the blessings."),
        (f"{MAG}Stage II: Multiply{RESET}", "Gratitude compounds like interest."),
        (f"{GLOW}{BOLD}🌻 Gratitude alchemized — every breath is wealth.{RESET}", None),
        (f"{GREEN}Result:{RESET} Alignment achieved. Energy stabilized.", None),
    ],
    "confidence": [
        (f"{YELL}Certainty signal rising…{RESET}", None),
        (f"{MAG}Stage I: Recall{RESET}", "Remember proven wins."),
        (f"{MAG}Stage II: Crystallize{RESET}", "Belief → small decisive action."),
        (f"{GLOW}{BOLD}⚙️ Confidence forged — momentum engaged.{RESET}", None),
        (f"{GREEN}Result:{RESET} One concrete step identified. Execute.", None),
    ],
    "hope": [
        (f"{YELL}Future-signal detected…{RESET}", None),
        (f"{MAG}Stage I: Envision{RESET}", "Picture a better state."),
        (f"{MAG}Stage II: Bridge{RESET}", "Name one path to get there."),
        (f"{GLOW}{BOLD}🌅 Hope amplified — direction set to sunrise.{RESET}", None),
        (f"{GREEN}Result:{RESET} Next waypoint set. Keep moving.", None),
    ],
}

SHADOW_SET = {"pain", "fear", "doubt", "anger"}
LIGHT_SET  = {"joy", "love", "peace", "gratitude", "confidence", "hope"}

ALIASES = {
    # shadow
    "hurt": "pain", "anxiety": "fear", "anxious": "fear", "afraid": "fear", "worry": "fear",
    "frustration": "anger", "mad": "anger", "rage": "anger", "hesitation": "doubt", "uncertainty": "doubt",
    # light
    "happy": "joy", "bliss": "joy", "delight": "joy",
    "calm": "peace", "serene": "peace", "grounded": "peace",
    "thankful": "gratitude", "appreciation": "gratitude",
    "proud": "confidence", "assured": "confidence",
    "optimism": "hope", "faith": "hope"
}

def normalize_emotion(e):
    e = e.strip().lower()
    return ALIASES.get(e, e)

def mode_banner(emotion):
    if emotion in SHADOW_SET:
        slow_print(f"{WHITE}{BOLD}🌑 Shadow Alchemy initiated — transforming dense emotion…{RESET}", 0.02)
    elif emotion in LIGHT_SET:
        slow_print(f"{YELL}{BOLD}🌞 Light Alchemy initiated — amplifying positive resonance…{RESET}", 0.02)
    else:
        slow_print(f"{GLOW}{BOLD}🌊 Serenity mode — you’re already golden.{RESET}", 0.02)

def run_sequence(emotion):
    mode_banner(emotion)
    slow_print("\nInitializing sequence…", 0.03)
    loading_dots("Attuning", cycles=2, dot_delay=0.25)

    if emotion in RESPONSES:
        script = RESPONSES[emotion]
        for i, (title, sub) in enumerate(script):
            if "Stage" in title:
                stage(title, sub)
                progress_bar(label=title.split(':')[0])
            else:
                if i < len(script) - 1:
                    slow_print(title + (f" {DIM}— {sub}{RESET}" if sub else ""))
                else:
                    pulse(title)
            sleep(0.2)
    else:
        slow_print(f"{GLOW}{BOLD}🌊 You’re already golden — keep flowing in peace.{RESET}")
    print()

def prompt_emotion():
    slow_print(
        f"{ITAL}Type an emotion (pain, fear, doubt, anger | joy, love, peace, gratitude, confidence, hope) "
        f"or a synonym. Commands: {BOLD}[m]{RESET} menu, {BOLD}[q]{RESET} quit.{RESET}", 0.02
    )
    choice = input(f"{BOLD}What are you feeling today? {RESET}").strip().lower()
    if choice in ("q", "quit", "exit"):
        return None
    if choice in ("m", "menu"):
        print(f"\n{BOLD}Select an emotion:{RESET}")
        print("  1) pain      2) fear      3) doubt     4) anger")
        print("  5) joy       6) love      7) peace     8) gratitude")
        print("  9) confidence 10) hope    q) quit")
        sel = input("> ").strip().lower()
        mapping = {
            "1":"pain","2":"fear","3":"doubt","4":"anger",
            "5":"joy","6":"love","7":"peace","8":"gratitude",
            "9":"confidence","10":"hope","q":None
        }
        return mapping.get(sel, "joy")
    return normalize_emotion(choice)

def banner_top():
    os.system("")  # enable ANSI on some Windows setups
    banner()

def main():
    banner_top()
    try:
        while True:
            emotion = prompt_emotion()
            if emotion is None:
                break
            run_sequence(emotion)
            again = input(f"{DIM}Run another transmutation? {RESET}[Enter=yes / q=no]: ").strip().lower()
            if again in ("q", "n", "no", "quit", "exit"):
                break
            print()
    except KeyboardInterrupt:
        print(f"\n{DIM}Session ended by user.{RESET}")

if __name__ == "__main__":
    main()
