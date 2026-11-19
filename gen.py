import math
import os
import random

OUT = "assets"
os.makedirs(OUT, exist_ok=True)

# Color Palette (Deep Navy / Cyber-Chic)
NAVY = "#0F1E33"
ROAD = "#22385A"
ROAD2 = "#2E4A73"
TEXT = "#F2F5F9"
MUTED = "#8FA3BF"
SAFFRON = "#FFB020"
CYAN = "#3FD0C9"
PINK = "#F0648C"
PURPLE = "#8B9CFF"
WHITE = "#FFFFFF"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def wrap(text, width_chars):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width_chars:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    lines.append(cur)
    return lines


# -------------------------------------------------------------
# 1. HERO SVG: Multi-Agent Network Simulation
# -------------------------------------------------------------
def hero():
    random.seed(42)
    Wd, Ht = 1200, 420

    # Layout for Multi-Agent Supervisor Graph on the right side
    # Supervisor at center (cx, cy)
    scx, scy = 930, 205

    # Worker agents positioned in an orbit
    agents = [
        ("Shadow Critic", 740, 105, CYAN, "Evaluator"),
        ("Panel Interviewer", 870, 75, PINK, "Voice Agent"),
        ("Code Sandbox", 1080, 105, SAFFRON, "Judge0 CE"),
        ("Roadmap DAG", 1120, 260, PURPLE, "Skill Graph"),
        ("BKT Engine", 970, 345, CYAN, "Mastery"),
        ("Resume Doctor", 760, 310, PINK, "Parser"),
    ]

    # Background grid lines & decorative circuits
    grid_lines = []
    for x in range(650, 1200, 50):
        grid_lines.append(
            f'<line x1="{x}" y1="20" x2="{x}" y2="400" stroke="{ROAD}" stroke-width="0.8" stroke-dasharray="2 6" stroke-opacity="0.4"/>'
        )
    for y in range(40, 400, 45):
        grid_lines.append(
            f'<line x1="650" y1="{y}" x2="1180" y2="{y}" stroke="{ROAD}" stroke-width="0.8" stroke-dasharray="2 6" stroke-opacity="0.4"/>'
        )

    # Edge links between Supervisor and Workers with animated pulses
    edge_svg = []
    pulse_svg = []
    for i, (name, ax, ay, col, role) in enumerate(agents):
        # Line from Supervisor to Worker
        L = math.dist((scx, scy), (ax, ay))
        edge_svg.append(
            f'<line x1="{scx}" y1="{scy}" x2="{ax}" y2="{ay}" stroke="{ROAD2}" stroke-width="2"/>'
        )
        edge_svg.append(
            f'<line class="pulse-line p{i}" x1="{scx}" y1="{scy}" x2="{ax}" y2="{ay}" stroke="{col}" stroke-width="2.5" stroke-linecap="round" style="--len:{L:.0f};stroke-dasharray:{L*0.25:.0f} {L:.0f};stroke-dashoffset:{L:.0f}"/>'
        )

        # Worker Node circles and labels
        edge_svg.append(
            f'<circle cx="{ax}" cy="{ay}" r="16" fill="{NAVY}" stroke="{col}" stroke-width="2.5"/>'
        )
        edge_svg.append(
            f'<circle cx="{ax}" cy="{ay}" r="5" fill="{col}"/>'
        )
        # Small role badge
        edge_svg.append(
            f'<text x="{ax}" y="{ay + 32}" font-family="{MONO}" font-size="11" fill="{MUTED}" text-anchor="middle">{esc(name)}</text>'
        )

    # Cross connections between workers (e.g. Critic -> Sandbox, BKT -> Roadmap)
    cross_pairs = [(0, 1), (1, 2), (3, 4), (4, 5), (5, 0)]
    for a, b in cross_pairs:
        x1, y1 = agents[a][1], agents[a][2]
        x2, y2 = agents[b][1], agents[b][2]
        edge_svg.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{ROAD}" stroke-width="1.2" stroke-dasharray="3 4"/>'
        )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {Wd} {Ht}" width="{Wd}" height="{Ht}" role="img" aria-label="Dhruv Chaudhary. Full-Stack AI and Autonomous Systems Engineer.">
<title>Dhruv Chaudhary</title>
<style>
  .pulse-line {{ animation: pulseFlow 4s linear infinite; }}
  .p0 {{ animation-delay: 0s; }}
  .p1 {{ animation-delay: 0.6s; }}
  .p2 {{ animation-delay: 1.2s; }}
  .p3 {{ animation-delay: 1.8s; }}
  .p4 {{ animation-delay: 2.4s; }}
  .p5 {{ animation-delay: 3.0s; }}
  @keyframes pulseFlow {{
    0% {{ stroke-dashoffset: var(--len); opacity: 0; }}
    20% {{ opacity: 1; }}
    80% {{ opacity: 1; }}
    100% {{ stroke-dashoffset: 0; opacity: 0; }}
  }}
  .sup-pulse {{
    animation: supRing 2.4s ease-out infinite;
  }}
  @keyframes supRing {{
    0% {{ r: 24; opacity: 0.9; }}
    100% {{ r: 52; opacity: 0; }}
  }}
  @media (prefers-reduced-motion: reduce) {{
    .pulse-line {{ animation: none; stroke-dashoffset: 0; opacity: 0.6; }}
    .sup-pulse {{ animation: none; opacity: 0; }}
  }}
</style>
<defs>
  <linearGradient id="fade" x1="0" x2="1">
    <stop offset="0" stop-color="{NAVY}" stop-opacity="1"/>
    <stop offset=".44" stop-color="{NAVY}" stop-opacity="1"/>
    <stop offset=".66" stop-color="{NAVY}" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="supGrad" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="{CYAN}"/>
    <stop offset="100%" stop-color="{PURPLE}"/>
  </linearGradient>
</defs>

<!-- Card Base -->
<rect width="{Wd}" height="{Ht}" rx="14" fill="{NAVY}"/>

<!-- Decorative Grid on Right -->
{''.join(grid_lines)}

<!-- Multi-Agent Supervisor Links -->
{''.join(edge_svg)}

<!-- Center Supervisor Node -->
<circle class="sup-pulse" cx="{scx}" cy="{scy}" r="24" fill="none" stroke="{CYAN}" stroke-width="2"/>
<circle cx="{scx}" cy="{scy}" r="26" fill="{NAVY}" stroke="url(#supGrad)" stroke-width="3.5"/>
<circle cx="{scx}" cy="{scy}" r="11" fill="url(#supGrad)"/>
<rect x="{scx - 72}" y="{scy + 36}" width="144" height="22" rx="4" fill="{NAVY}" stroke="{ROAD2}"/>
<text x="{scx}" y="{scy + 51}" font-family="{MONO}" font-size="11.5" font-weight="700" fill="{TEXT}" text-anchor="middle">SUPERVISOR AGENT</text>

<!-- Left Fade Gradient to ensure crisp text contrast -->
<rect width="{Wd}" height="{Ht}" rx="14" fill="url(#fade)" pointer-events="none"/>

<!-- Identity & Thesis on Left -->
<text x="56" y="148" font-family="{SANS}" font-size="60" font-weight="800" fill="{TEXT}" letter-spacing="-1.5">Dhruv Chaudhary</text>
<text x="58" y="198" font-family="{SANS}" font-size="22" font-weight="600" fill="{TEXT}">I build autonomous multi-agent systems,</text>
<text x="58" y="228" font-family="{SANS}" font-size="22" font-weight="600" fill="{TEXT}">and the deterministic engines that keep them honest.</text>

<text x="58" y="278" font-family="{SANS}" font-size="15" fill="{MUTED}">Full-Stack AI &amp; Systems Engineer • Machine Learning • Distributed Architectures</text>

<g font-family="{SANS}" font-size="13" fill="{MUTED}">
  <circle cx="64" cy="336" r="5" fill="{CYAN}"/>
  <circle cx="80" cy="336" r="5" fill="{SAFFRON}"/>
  <circle cx="96" cy="336" r="5" fill="{PINK}"/>
  <circle cx="112" cy="336" r="5" fill="{PURPLE}"/>
  <text x="128" y="340.5">Multi-agent loops, sandboxed code execution, demand forecasting &amp; EVM contracts.</text>
</g>
</svg>"""
    with open(f"{OUT}/hero.svg", "w", encoding="utf-8") as f:
        f.write(svg)


# -------------------------------------------------------------
# 2. GLYPHS FOR PROJECT CARDS
# -------------------------------------------------------------
def glyph_supervisor(col):
    # Multi-agent Supervisor dispatching to workers
    nodes = [(32, 70), (75, 30), (120, 48), (120, 92), (75, 110)]
    s = f'<g stroke="{ROAD2}" stroke-width="1.6" fill="none">'
    for i in range(1, len(nodes)):
        s += f'<path d="M{nodes[0][0]},{nodes[0][1]} L{nodes[i][0]},{nodes[i][1]}"/>'
    s += f'<path d="M{nodes[1][0]},{nodes[1][1]} L{nodes[2][0]},{nodes[2][1]} L{nodes[3][0]},{nodes[3][1]} L{nodes[4][0]},{nodes[4][1]}"/>'
    s += "</g>"
    # Supervisor
    s += f'<circle cx="{nodes[0][0]}" cy="{nodes[0][1]}" r="10" fill="{col}"/>'
    s += f'<circle cx="{nodes[0][0]}" cy="{nodes[0][1]}" r="14" fill="none" stroke="{col}" stroke-opacity="0.4"/>'
    # Workers
    for i in range(1, len(nodes)):
        s += f'<circle cx="{nodes[i][0]}" cy="{nodes[i][1]}" r="6" fill="{WHITE if i==1 else ROAD2}"/>'
    return s


def glyph_forecasting(col):
    # Real sales data curve vs forecasting models
    s = f'<g stroke="{ROAD2}" stroke-width="1" fill="none">'
    for x in range(20, 140, 20):
        s += f'<line x1="{x}" y1="20" x2="{x}" y2="120"/>'
    for y in range(30, 120, 25):
        s += f'<line x1="20" y1="{y}" x2="140" y2="{y}"/>'
    s += "</g>"
    # Moving average historical baseline (muted)
    s += f'<path d="M22,100 Q45,70 70,85 T110,50 T138,40" stroke="{ROAD2}" stroke-width="2" fill="none" stroke-dasharray="3 3"/>'
    # LightGBM forecast curve (accent)
    s += f'<path d="M22,95 Q48,60 74,78 T112,42 T138,32" stroke="{col}" stroke-width="2.6" fill="none" stroke-linecap="round"/>'
    s += f'<circle cx="138" cy="32" r="4.5" fill="{WHITE}"/>'
    return s


def glyph_radar(col):
    # KrishiAI: N-P-K nutrient & yield polygon
    cx, cy, r = 78, 70, 48
    s = f'<g stroke="{ROAD2}" stroke-width="1.2" fill="none">'
    for rad in [18, 34, 48]:
        s += f'<polygon points="{cx},{cy-rad} {cx+rad*0.95:.1f},{cy-rad*0.31:.1f} {cx+rad*0.59:.1f},{cy+rad*0.81:.1f} {cx-rad*0.59:.1f},{cy+rad*0.81:.1f} {cx-rad*0.95:.1f},{cy-rad*0.31:.1f}"/>'
    s += "</g>"
    # Actual crop profile polygon
    pts = f"{cx},{cy-42} {cx+38},{cy-12} {cx+28},{cy+35} {cx-35},{cy+25} {cx-28},{cy-10}"
    s += f'<polygon points="{pts}" fill="{col}" fill-opacity="0.25" stroke="{col}" stroke-width="2.2"/>'
    s += f'<circle cx="{cx}" cy="{cy-42}" r="3.5" fill="{WHITE}"/>'
    return s


def glyph_blockchain(col):
    # Tourist Safety: Decentralized blocks & cryptographic hashes
    blocks = [(26, 46), (68, 46), (110, 46)]
    s = ""
    # Links between blocks
    s += f'<line x1="48" y1="58" x2="68" y2="58" stroke="{col}" stroke-width="2"/>'
    s += f'<line x1="90" y1="58" x2="110" y2="58" stroke="{col}" stroke-width="2"/>'
    # Broadcast alert wave on block 3
    s += f'<path d="M110,34 Q124,20 138,34" stroke="{WHITE}" stroke-width="1.5" fill="none"/>'
    s += f'<path d="M106,28 Q124,10 142,28" stroke="{col}" stroke-width="1.5" fill="none"/>'
    for x, y in blocks:
        s += f'<rect x="{x}" y="{y}" width="22" height="24" rx="4" fill="{NAVY}" stroke="{ROAD2}" stroke-width="1.5"/>'
        s += f'<circle cx="{x+11}" cy="{y+12}" r="3.5" fill="{col}"/>'
    # ID Hash fingerprint icon below
    s += f'<path d="M50,96 Q78,82 106,96" stroke="{col}" stroke-width="1.8" fill="none"/>'
    s += f'<path d="M58,104 Q78,92 98,104" stroke="{ROAD2}" stroke-width="1.8" fill="none"/>'
    s += f'<path d="M66,112 Q78,102 90,112" stroke="{ROAD2}" stroke-width="1.8" fill="none"/>'
    return s


# -------------------------------------------------------------
# 3. PROJECT CARD GENERATOR
# -------------------------------------------------------------
CARDS = [
    (
        "placement-mentor",
        "Placement Mentor",
        "Live System",
        CYAN,
        glyph_supervisor,
        "Supervisor agent coordinates five specialist subagents for voice mock interviews, dynamic DAG skill solving, and automated resume diagnostics.",
        "Judge0 sandbox execution + Bayesian Knowledge Tracing",
        "Gemini 2.5 / Next.js 15 / FastAPI / ElevenLabs / PostgreSQL",
    ),
    (
        "retail-insight",
        "Retail Demand & VOC Engine",
        "Shipped",
        SAFFRON,
        glyph_forecasting,
        "End-to-end data pipeline over 913,000+ transaction records. Benchmarks SARIMAX, Prophet, and LightGBM with customer review sentiment mining.",
        "913k Kaggle rows across 10 stores & 50 items • SQL analytics",
        "Python / LightGBM / SARIMAX / Prophet / SQLite / NLP",
    ),
    (
        "krishai",
        "KrishiAI Precision Engine",
        "Shipped",
        PINK,
        glyph_radar,
        "Precision agriculture ML model predicting crop yield and potential revenue from soil chemistry (N-P-K), climate metrics, and historical market volatility.",
        "Optimized XGBoost Regressor with R² = 0.939 • sub-100ms API",
        "XGBoost / Scikit-learn / Flask / Pandas / NumPy",
    ),
    (
        "tourist-safety",
        "Tourist Safety Registry",
        "Contract Shipped",
        PURPLE,
        glyph_blockchain,
        "Decentralized identity and incident response registry on Ethereum. Cryptographically hashes IDs for zero PII leakage with instant emergency alert broadcast.",
        "Solidity ^0.8.20 + Foundry test harness • zero PII leakage",
        "Solidity / Foundry (Forge/Cast) / EVM / JavaScript",
    ),
]


def card(slug, title, status, col, glyph, desc, proof, stack):
    Wd, Ht = 600, 250
    lines = wrap(desc, 48)
    desc_svg = "".join(
        f'<text x="196" y="{94 + i * 21}" font-family="{SANS}" font-size="14.5" fill="{TEXT}">{esc(l)}</text>'
        for i, l in enumerate(lines)
    )
    y_proof = 94 + len(lines) * 21 + 10
    pw = len(status) * 7.4 + 22
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {Wd} {Ht}" width="{Wd}" height="{Ht}" role="img" aria-label="{esc(title)}: {esc(desc)}">
<title>{esc(title)}</title>
<defs><clipPath id="c-{slug}"><rect width="{Wd}" height="{Ht}" rx="12"/></clipPath></defs>
<g clip-path="url(#c-{slug})">
  <rect width="{Wd}" height="{Ht}" fill="{NAVY}"/>
  <rect x="0" y="0" width="6" height="{Ht}" fill="{col}"/>
</g>
<g transform="translate(24,34)">{glyph(col)}</g>
<text x="196" y="56" font-family="{SANS}" font-size="23" font-weight="700" fill="{TEXT}">{esc(title)}</text>
<rect x="{96 - pw / 2}" y="{Ht - 42}" width="{pw}" height="24" rx="12" fill="none" stroke="{col}" stroke-width="1.2"/>
<text x="96" y="{Ht - 25.5}" font-family="{SANS}" font-size="12" fill="{col}" text-anchor="middle">{esc(status)}</text>
{desc_svg}
<text x="196" y="{y_proof}" font-family="{SANS}" font-size="13" font-weight="600" fill="{col}">{esc(proof)}</text>
<line x1="196" y1="{Ht - 44}" x2="{Wd - 20}" y2="{Ht - 44}" stroke="{ROAD}"/>
<text x="196" y="{Ht - 20}" font-family="{MONO}" font-size="12.5" fill="{MUTED}">{esc(stack)}</text>
</svg>"""
    with open(f"{OUT}/card-{slug}.svg", "w", encoding="utf-8") as f:
        f.write(svg)


# -------------------------------------------------------------
# 4. TIMELINE SVG ("The Route So Far")
# -------------------------------------------------------------
def route():
    Wd, Ht = 1200, 200
    stations = [
        (
            "Foundations",
            "C++, Python & Algorithm Design",
            SAFFRON,
        ),
        (
            "Full-Stack Architectures",
            "Next.js 15, FastAPI & DB Systems",
            CYAN,
        ),
        (
            "Predictive ML & Forecasting",
            "XGBoost R²=0.939, LightGBM, 913k rows",
            PINK,
        ),
        (
            "Web3 & Smart Contracts",
            "Solidity ^0.8.20, Foundry Test Suites",
            PURPLE,
        ),
        (
            "Autonomous Agent Systems",
            "Supervisor Multi-Agent & Sandboxes",
            CYAN,
        ),
    ]
    x0, x1, y = 120, 950, 100
    step = (x1 - x0) / (len(stations) - 1)
    s = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {Wd} {Ht}" width="{Wd}" height="{Ht}" role="img" aria-label="Milestones: Foundations in C++ and Python; Full-Stack Architectures; Predictive ML with XGBoost R²=0.939; Web3 and Solidity; Multi-Agent Systems; Open to 2026-2027 SDE and AI/ML roles.">
<title>The route so far</title>
<rect width="{Wd}" height="{Ht}" rx="14" fill="{NAVY}"/>
<defs>
  <linearGradient id="line" x1="0" x2="1">
    <stop offset="0" stop-color="{SAFFRON}"/>
    <stop offset=".35" stop-color="{CYAN}"/>
    <stop offset=".7" stop-color="{PINK}"/>
    <stop offset="1" stop-color="{PURPLE}"/>
  </linearGradient>
</defs>
<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="url(#line)" stroke-width="8" stroke-linecap="round"/>
<line x1="{x1}" y1="{y}" x2="1080" y2="{y}" stroke="{CYAN}" stroke-width="8" stroke-dasharray="2 14" stroke-linecap="round"/>
"""
    for i, (name, sub, col) in enumerate(stations):
        x = x0 + i * step
        up = i % 2 == 0
        ty = y - 52 if up else y + 48
        s += f'<circle cx="{x:.1f}" cy="{y}" r="11" fill="{NAVY}" stroke="{col}" stroke-width="5"/>'
        s += f'<line x1="{x:.1f}" y1="{y + (-14 if up else 14)}" x2="{x:.1f}" y2="{y + (-30 if up else 28)}" stroke="{ROAD2}" stroke-width="1.5"/>'
        s += f'<text x="{x:.1f}" y="{ty}" font-family="{SANS}" font-size="14.5" font-weight="700" fill="{TEXT}" text-anchor="middle">{esc(name)}</text>'
        s += f'<text x="{x:.1f}" y="{ty + 19}" font-family="{SANS}" font-size="12" fill="{MUTED}" text-anchor="middle">{esc(sub)}</text>'

    s += f"""<circle cx="1090" cy="{y}" r="15" fill="#fff"><animate attributeName="r" values="13;16;13" dur="2.4s" repeatCount="indefinite"/></circle>
<text x="1090" y="{y - 52}" font-family="{SANS}" font-size="15" font-weight="700" fill="{TEXT}" text-anchor="middle">Next stop</text>
<text x="1090" y="{y - 33}" font-family="{SANS}" font-size="12.5" fill="{MUTED}" text-anchor="middle">SDE / AI-ML Roles</text>
</svg>"""
    with open(f"{OUT}/route-so-far.svg", "w", encoding="utf-8") as f:
        f.write(s)


# -------------------------------------------------------------
# 5. TECH STACK CHIP GRID SVG
# -------------------------------------------------------------
def stack():
    Wd = 1200
    groups = [
        ("Languages", SAFFRON, ["Python", "TypeScript", "JavaScript", "SQL", "Solidity", "C++"]),
        (
            "AI & Agentic Systems",
            CYAN,
            [
                "Gemini 2.5 Interactions API",
                "Supervisor Architectures",
                "Shadow Critics",
                "ElevenLabs Neural TTS",
                "Bayesian Knowledge Tracing (BKT)",
                "Prompt Orchestration",
            ],
        ),
        (
            "Full-Stack & Systems",
            PINK,
            [
                "Next.js 15 (App Router)",
                "React",
                "FastAPI",
                "Pydantic",
                "PostgreSQL",
                "Judge0 CE Sandbox",
                "Monaco Editor",
                "Tailwind CSS",
            ],
        ),
        (
            "Data Science & ML",
            PURPLE,
            [
                "XGBoost",
                "LightGBM",
                "Scikit-learn",
                "Pandas",
                "NumPy",
                "Prophet",
                "SARIMAX",
                "NLP & Sentiment Mining",
            ],
        ),
        (
            "Tools & Web3",
            "#38bdf8",
            [
                "Foundry (Forge, Cast, Anvil)",
                "EVM Smart Contracts",
                "Git & GitHub Actions",
                "Docker",
                "Linux / Bash",
                "REST APIs",
            ],
        ),
    ]
    label_w = 170
    pad_l, pad_r = label_w + 34, 30
    row_gap, chip_gap, chip_h = 36, 8, 27
    avail = Wd - pad_l - pad_r

    def chip_w(t):
        return len(t) * 7.5 + 34

    rows_svg = []
    y = 52
    for gi, (label, col, items) in enumerate(groups):
        lines, cur, curw = [], [], 0
        for it in items:
            w = chip_w(it)
            if cur and curw + chip_gap + w > avail:
                lines.append(cur)
                cur, curw = [], 0
            cur.append((it, w))
            curw += (chip_gap if curw else 0) + w
        if cur:
            lines.append(cur)
        block_h = len(lines) * (chip_h + 10) - 10
        rows_svg.append(
            f'<text x="34" y="{y + block_h / 2 + 5}" font-family="{SANS}" font-size="14.5" font-weight="700" fill="{TEXT}">{esc(label)}</text>'
        )
        cy = y
        for line in lines:
            cx = pad_l
            for it, w in line:
                rows_svg.append(
                    f'<rect x="{cx:.1f}" y="{cy}" width="{w:.1f}" height="{chip_h}" rx="{chip_h/2:.1f}" fill="none" stroke="{col}" stroke-width="1.3"/>'
                )
                rows_svg.append(
                    f'<circle cx="{cx + 14:.1f}" cy="{cy + chip_h/2:.1f}" r="3" fill="{col}"/>'
                )
                rows_svg.append(
                    f'<text x="{cx + 24:.1f}" y="{cy + chip_h/2 + 4.5:.1f}" font-family="{MONO}" font-size="12.2" fill="{TEXT}">{esc(it)}</text>'
                )
                cx += w + chip_gap
            cy += chip_h + 10
        y += block_h + row_gap
        if gi < len(groups) - 1:
            rows_svg.append(
                f'<line x1="34" y1="{y - row_gap/2:.1f}" x2="{Wd-30}" y2="{y - row_gap/2:.1f}" stroke="{ROAD}"/>'
            )
    Ht = y - row_gap + 26
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {Wd} {Ht:.0f}" width="{Wd}" height="{Ht:.0f}" role="img" '
        f'aria-label="Dhruv Chaudhary Stack: Python, TypeScript, JavaScript, SQL, Solidity, C++; Gemini 2.5, Supervisor multi-agent, ElevenLabs; Next.js 15, FastAPI, Judge0; XGBoost, LightGBM; Foundry, EVM.">'
        f"<title>Stack</title>"
        f'<rect width="{Wd}" height="{Ht:.0f}" rx="14" fill="{NAVY}"/>'
        + "".join(rows_svg)
        + "</svg>"
    )
    with open(f"{OUT}/stack.svg", "w", encoding="utf-8") as f:
        f.write(svg)


if __name__ == "__main__":
    print("Generating portfolio SVG assets...")
    hero()
    for c in CARDS:
        card(*c)
    route()
    stack()
    print("Generated successfully in assets/:", sorted(os.listdir(OUT)))
