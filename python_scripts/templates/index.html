<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>SpamScan — Message Spam Detector</title>
  <link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet" />
  <style>
    /* ── Reset & Variables ─────────────────────────── */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg:        #0a0a0f;
      --surface:   #111118;
      --border:    #1e1e2e;
      --text:      #e8e8f0;
      --muted:     #5a5a78;
      --accent:    #ff4d6d;
      --safe:      #00e5a0;
      --warn:      #ff4d6d;
      --yellow:    #ffd166;
      --glow-r:    rgba(255, 77, 109, 0.18);
      --glow-g:    rgba(0, 229, 160, 0.18);
      --radius:    14px;
      --font-main: 'Syne', sans-serif;
      --font-mono: 'DM Mono', monospace;
    }

    html { scroll-behavior: smooth; }

    body {
      background: var(--bg);
      color: var(--text);
      font-family: var(--font-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      overflow-x: hidden;
    }

    /* ── Background grid ───────────────────────────── */
    body::before {
      content: '';
      position: fixed; inset: 0;
      background-image:
        linear-gradient(rgba(255,77,109,.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,77,109,.04) 1px, transparent 1px);
      background-size: 48px 48px;
      pointer-events: none;
      z-index: 0;
    }

    /* ── Header ────────────────────────────────────── */
    header {
      width: 100%;
      max-width: 780px;
      padding: 60px 24px 32px;
      text-align: center;
      position: relative;
      z-index: 1;
      animation: fadeDown .7s ease both;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      gap: 7px;
      background: rgba(255,77,109,.12);
      border: 1px solid rgba(255,77,109,.3);
      color: var(--accent);
      font-family: var(--font-mono);
      font-size: 11px;
      letter-spacing: .12em;
      text-transform: uppercase;
      padding: 5px 14px;
      border-radius: 999px;
      margin-bottom: 22px;
    }
    .badge .dot {
      width: 6px; height: 6px;
      background: var(--accent);
      border-radius: 50%;
      animation: pulse 1.6s ease infinite;
    }

    h1 {
      font-size: clamp(2.4rem, 6vw, 4rem);
      font-weight: 800;
      letter-spacing: -.03em;
      line-height: 1.1;
      margin-bottom: 14px;
    }

    h1 span {
      background: linear-gradient(135deg, var(--accent), var(--yellow));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    .subtitle {
      color: var(--muted);
      font-size: .95rem;
      font-weight: 400;
      letter-spacing: .01em;
      max-width: 420px;
      margin: 0 auto;
    }

    /* ── Main card ─────────────────────────────────── */
    main {
      width: 100%;
      max-width: 780px;
      padding: 0 24px 80px;
      position: relative;
      z-index: 1;
      animation: fadeUp .7s .15s ease both;
    }

    .card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 32px;
      margin-bottom: 20px;
      transition: border-color .3s;
    }

    /* ── Textarea ──────────────────────────────────── */
    .textarea-wrap { position: relative; }

    textarea {
      width: 100%;
      min-height: 160px;
      background: var(--bg);
      border: 1.5px solid var(--border);
      border-radius: 10px;
      color: var(--text);
      font-family: var(--font-mono);
      font-size: .9rem;
      line-height: 1.65;
      padding: 18px 20px;
      resize: vertical;
      outline: none;
      transition: border-color .25s, box-shadow .25s;
    }

    textarea::placeholder { color: var(--muted); }
    textarea:focus {
      border-color: rgba(255,77,109,.5);
      box-shadow: 0 0 0 3px rgba(255,77,109,.08);
    }

    .char-count {
      position: absolute;
      bottom: 12px; right: 14px;
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--muted);
      pointer-events: none;
    }

    /* ── Actions row ───────────────────────────────── */
    .actions {
      display: flex;
      gap: 12px;
      margin-top: 16px;
      flex-wrap: wrap;
    }

    .btn {
      font-family: var(--font-main);
      font-size: .9rem;
      font-weight: 700;
      letter-spacing: .02em;
      border: none;
      border-radius: 9px;
      cursor: pointer;
      padding: 13px 28px;
      transition: transform .15s, box-shadow .15s, opacity .15s;
    }
    .btn:active { transform: scale(.97); }

    .btn-primary {
      background: linear-gradient(135deg, var(--accent), #ff6b35);
      color: #fff;
      box-shadow: 0 4px 20px rgba(255,77,109,.35);
      flex: 1;
      min-width: 140px;
    }
    .btn-primary:hover { box-shadow: 0 6px 28px rgba(255,77,109,.5); }
    .btn-primary:disabled { opacity: .5; cursor: not-allowed; }

    .btn-ghost {
      background: transparent;
      border: 1.5px solid var(--border);
      color: var(--muted);
    }
    .btn-ghost:hover { border-color: var(--muted); color: var(--text); }

    /* ── Result panel ──────────────────────────────── */
    #result-panel {
      display: none;
      animation: fadeUp .4s ease both;
    }
    #result-panel.visible { display: block; }

    .result-inner {
      display: flex;
      align-items: flex-start;
      gap: 24px;
      flex-wrap: wrap;
    }

    .verdict-badge {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 8px;
      min-width: 120px;
      padding: 24px 20px;
      border-radius: 12px;
      border: 2px solid;
      text-align: center;
      flex-shrink: 0;
    }
    .verdict-badge.spam {
      background: rgba(255,77,109,.08);
      border-color: rgba(255,77,109,.4);
      color: var(--accent);
    }
    .verdict-badge.ham {
      background: rgba(0,229,160,.08);
      border-color: rgba(0,229,160,.4);
      color: var(--safe);
    }

    .verdict-icon { font-size: 2.2rem; line-height: 1; }
    .verdict-label {
      font-size: .7rem;
      font-family: var(--font-mono);
      letter-spacing: .14em;
      text-transform: uppercase;
      opacity: .75;
    }
    .verdict-word { font-size: 1.35rem; font-weight: 800; }

    .verdict-details { flex: 1; min-width: 200px; }
    .verdict-details h3 {
      font-size: 1.05rem;
      font-weight: 700;
      margin-bottom: 4px;
    }
    .verdict-details p {
      font-size: .85rem;
      color: var(--muted);
      margin-bottom: 20px;
    }

    /* ── Probability bars ──────────────────────────── */
    .prob-bars { display: flex; flex-direction: column; gap: 10px; }

    .prob-row { display: flex; flex-direction: column; gap: 5px; }
    .prob-meta {
      display: flex;
      justify-content: space-between;
      font-size: .8rem;
    }
    .prob-meta .label { font-family: var(--font-mono); color: var(--muted); }
    .prob-meta .val   { font-family: var(--font-mono); font-weight: 500; }

    .bar-track {
      height: 7px;
      background: var(--border);
      border-radius: 99px;
      overflow: hidden;
    }
    .bar-fill {
      height: 100%;
      border-radius: 99px;
      transition: width 1s cubic-bezier(.22,1,.36,1);
      width: 0;
    }
    .bar-fill.spam-bar { background: linear-gradient(90deg, #ff4d6d, #ff6b35); }
    .bar-fill.ham-bar  { background: linear-gradient(90deg, #00e5a0, #00b4d8); }

    /* ── Examples section ──────────────────────────── */
    .section-title {
      font-size: .7rem;
      font-family: var(--font-mono);
      letter-spacing: .14em;
      text-transform: uppercase;
      color: var(--muted);
      margin-bottom: 14px;
    }

    .examples-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 12px;
    }

    .example-chip {
      background: var(--bg);
      border: 1.5px solid var(--border);
      border-radius: 10px;
      padding: 14px 16px;
      cursor: pointer;
      transition: border-color .2s, transform .15s;
      text-align: left;
    }
    .example-chip:hover {
      border-color: rgba(255,77,109,.4);
      transform: translateY(-2px);
    }
    .example-chip .chip-label {
      font-family: var(--font-mono);
      font-size: 10px;
      letter-spacing: .1em;
      text-transform: uppercase;
      margin-bottom: 6px;
    }
    .example-chip .chip-label.spam { color: var(--accent); }
    .example-chip .chip-label.ham  { color: var(--safe); }
    .example-chip .chip-text {
      font-size: .82rem;
      color: var(--muted);
      line-height: 1.5;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    /* ── Spinner ───────────────────────────────────── */
    .spinner {
      display: inline-block;
      width: 18px; height: 18px;
      border: 2.5px solid rgba(255,255,255,.25);
      border-top-color: #fff;
      border-radius: 50%;
      animation: spin .65s linear infinite;
      vertical-align: middle;
      margin-right: 8px;
    }

    /* ── Animations ────────────────────────────────── */
    @keyframes fadeDown {
      from { opacity:0; transform: translateY(-20px); }
      to   { opacity:1; transform: translateY(0); }
    }
    @keyframes fadeUp {
      from { opacity:0; transform: translateY(16px); }
      to   { opacity:1; transform: translateY(0); }
    }
    @keyframes pulse {
      0%,100% { opacity:1; transform: scale(1); }
      50%      { opacity:.5; transform: scale(.8); }
    }
    @keyframes spin { to { transform: rotate(360deg); } }

    /* ── Footer ────────────────────────────────────── */
    footer {
      position: relative; z-index:1;
      padding: 24px;
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--muted);
      text-align: center;
    }

    /* ── Responsive ────────────────────────────────── */
    @media (max-width: 520px) {
      .card { padding: 22px 18px; }
      .result-inner { flex-direction: column; }
      .verdict-badge { flex-direction: row; min-width: unset; padding: 16px; }
    }
  </style>
</head>
<body>

<!-- ── Header ───────────────────────────────────────── -->
<header>
  <div class="badge">
    <span class="dot"></span>
    ML-Powered · Naive Bayes · TF-IDF
  </div>
  <h1>Detect <span>Spam</span><br>Instantly</h1>
  <p class="subtitle">Paste any SMS or email message and our trained classifier will analyse it in milliseconds.</p>
</header>

<!-- ── Main ─────────────────────────────────────────── -->
<main>

  <!-- Input Card -->
  <div class="card">
    <div class="textarea-wrap">
      <textarea
        id="msg-input"
        placeholder="Paste your message here… e.g. 'Congratulations! You've won a FREE iPhone. Click now to claim!'"
        maxlength="1000"
      ></textarea>
      <span class="char-count" id="char-count">0 / 1000</span>
    </div>
    <div class="actions">
      <button class="btn btn-primary" id="scan-btn" onclick="scan()">
        Scan Message
      </button>
      <button class="btn btn-ghost" onclick="clearAll()">Clear</button>
    </div>
  </div>

  <!-- Result Panel -->
  <div class="card" id="result-panel">
    <div class="result-inner">
      <div class="verdict-badge" id="verdict-badge">
        <div class="verdict-icon" id="verdict-icon"></div>
        <div class="verdict-label">verdict</div>
        <div class="verdict-word" id="verdict-word"></div>
      </div>
      <div class="verdict-details">
        <h3 id="verdict-headline"></h3>
        <p id="verdict-sub"></p>
        <div class="prob-bars">
          <div class="prob-row">
            <div class="prob-meta">
              <span class="label">SPAM probability</span>
              <span class="val" id="spam-val">—</span>
            </div>
            <div class="bar-track"><div class="bar-fill spam-bar" id="spam-bar"></div></div>
          </div>
          <div class="prob-row">
            <div class="prob-meta">
              <span class="label">HAM probability</span>
              <span class="val" id="ham-val">—</span>
            </div>
            <div class="bar-track"><div class="bar-fill ham-bar" id="ham-bar"></div></div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Examples Card -->
  <div class="card" id="examples-card">
    <p class="section-title">Try an example</p>
    <div class="examples-grid" id="examples-grid">
      <p style="color:var(--muted);font-size:.85rem">Loading examples…</p>
    </div>
  </div>

</main>

<footer>SpamScan · Flask + scikit-learn · Naive Bayes Classifier</footer>

<!-- ── JavaScript ────────────────────────────────────── -->
<script>
  const input   = document.getElementById('msg-input');
  const counter = document.getElementById('char-count');
  const scanBtn = document.getElementById('scan-btn');

  // Character counter
  input.addEventListener('input', () => {
    counter.textContent = `${input.value.length} / 1000`;
  });

  // ── Scan ────────────────────────────────────────────
  async function scan() {
    const msg = input.value.trim();
    if (!msg) { input.focus(); return; }

    scanBtn.disabled = true;
    scanBtn.innerHTML = '<span class="spinner"></span>Analysing…';

    try {
      const res  = await fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: msg })
      });
      const data = await res.json();

      if (data.error) { alert(data.error); return; }
      showResult(data);
    } catch (e) {
      alert('⚠️ Could not connect to the server. Make sure app.py is running.');
    } finally {
      scanBtn.disabled = false;
      scanBtn.innerHTML = 'Scan Message';
    }
  }

  // ── Show result ─────────────────────────────────────
  function showResult({ label, confidence, spam_prob, ham_prob }) {
    const isSpam   = label === 'spam';
    const panel    = document.getElementById('result-panel');
    const badge    = document.getElementById('verdict-badge');
    const icon     = document.getElementById('verdict-icon');
    const word     = document.getElementById('verdict-word');
    const headline = document.getElementById('verdict-headline');
    const sub      = document.getElementById('verdict-sub');
    const spamVal  = document.getElementById('spam-val');
    const hamVal   = document.getElementById('ham-val');
    const spamBar  = document.getElementById('spam-bar');
    const hamBar   = document.getElementById('ham-bar');

    badge.className = `verdict-badge ${label}`;
    icon.textContent  = isSpam ? '🚨' : '✅';
    word.textContent  = label.toUpperCase();
    headline.textContent = isSpam
      ? `High spam likelihood — ${confidence}% confidence`
      : `Looks legitimate — ${confidence}% confidence`;
    sub.textContent = isSpam
      ? 'This message contains patterns commonly associated with unsolicited spam.'
      : 'This message does not appear to contain spam indicators.';

    spamVal.textContent = `${spam_prob}%`;
    hamVal.textContent  = `${ham_prob}%`;

    // Animate bars (reset first)
    spamBar.style.width = '0';
    hamBar.style.width  = '0';

    panel.classList.remove('visible');
    void panel.offsetWidth;  // force reflow
    panel.classList.add('visible');

    requestAnimationFrame(() => {
      setTimeout(() => {
        spamBar.style.width = `${spam_prob}%`;
        hamBar.style.width  = `${ham_prob}%`;
      }, 80);
    });

    panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  // ── Clear ───────────────────────────────────────────
  function clearAll() {
    input.value = '';
    counter.textContent = '0 / 1000';
    document.getElementById('result-panel').classList.remove('visible');
    input.focus();
  }

  // ── Load examples ───────────────────────────────────
  async function loadExamples() {
    try {
      const res     = await fetch('/examples');
      const samples = await res.json();
      const grid    = document.getElementById('examples-grid');
      grid.innerHTML = '';

      samples.forEach(({ text, expected }) => {
        const chip = document.createElement('button');
        chip.className = 'example-chip';
        chip.innerHTML = `
          <div class="chip-label ${expected}">${expected}</div>
          <div class="chip-text">${text}</div>
        `;
        chip.onclick = () => {
          input.value = text;
          counter.textContent = `${text.length} / 1000`;
          scan();
        };
        grid.appendChild(chip);
      });
    } catch (_) { /* silently ignore if server not ready */ }
  }

  // ── Enter key shortcut ──────────────────────────────
  input.addEventListener('keydown', e => {
    if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) scan();
  });

  // Init
  loadExamples();
</script>
</body>
</html>
