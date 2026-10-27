"""
═══════════════════════════════════════════════════════════════════════════
 PORTAFOLIO · JUAN PABLO · PARTE 2
 Interfaces Multimodales — EAFIT
 Experiencia web interactiva en Streamlit (sin librerías externas!)
═══════════════════════════════════════════════════════════════════════════
"""

import streamlit as st
import base64
import os
import html as html_lib

# ═══════════════════════════════════════════════════════════════════════
# CONFIGURACIÓN
# ═══════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Portafolio · Juan Pablo · Parte 2",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ═══════════════════════════════════════════════════════════════════════
# PALETA — "MIDNIGHT EMBER" (azul noche + ámbar cálido)
# ═══════════════════════════════════════════════════════════════════════
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

:root{
  --bg:#070b14;
  --bg-2:#0b1220;
  --surface:#0f1828;
  --surface-2:#131f33;
  --border:#1e2c44;
  --border-2:#2b3d5c;
  --text:#eef3fb;
  --text-2:#c2cfe3;
  --muted:#8a9ab4;
  --muted-2:#5f6f8a;
  --amber:#f5a524;
  --amber-soft:rgba(245,165,36,.12);
  --cyan:#4cc9e0;
  --cyan-soft:rgba(76,201,224,.12);
  --violet:#9d8df1;
}

html, body, [class*="css"], .stApp, button, input, textarea, select{
  font-family:'Inter',sans-serif !important;
  color:var(--text);
}
h1,h2,h3,h4,h5{font-family:'Instrument Serif',serif !important;}

/* ═══ FONDO ANIMADO ═══ */
.stApp{
  background-color:var(--bg) !important;
  background-image:
    radial-gradient(ellipse 900px 520px at 12% -8%, rgba(245,165,36,.13), transparent 60%),
    radial-gradient(ellipse 800px 500px at 88% 8%, rgba(76,201,224,.11), transparent 60%),
    radial-gradient(ellipse 900px 600px at 50% 108%, rgba(157,141,241,.10), transparent 62%);
  background-attachment:fixed;
}
.stApp::before{
  content:'';position:fixed;inset:0;pointer-events:none;z-index:0;
  background-image:
    radial-gradient(1.4px 1.4px at 12% 22%, rgba(255,255,255,.45), transparent),
    radial-gradient(1.2px 1.2px at 78% 14%, rgba(255,255,255,.35), transparent),
    radial-gradient(1.6px 1.6px at 33% 68%, rgba(245,165,36,.40), transparent),
    radial-gradient(1.2px 1.2px at 66% 52%, rgba(76,201,224,.40), transparent),
    radial-gradient(1.5px 1.5px at 88% 78%, rgba(255,255,255,.30), transparent),
    radial-gradient(1.1px 1.1px at 46% 34%, rgba(255,255,255,.25), transparent);
  animation:drift 26s linear infinite;
}
@keyframes drift{
  0%{transform:translateY(0) translateX(0)}
  50%{transform:translateY(-26px) translateX(12px)}
  100%{transform:translateY(0) translateX(0)}
}
@keyframes floaty{0%,100%{transform:translateY(0)}50%{transform:translateY(-14px)}}
@keyframes pulseGlow{0%,100%{opacity:.55;transform:scale(1)}50%{opacity:1;transform:scale(1.06)}}
@keyframes sweep{0%{transform:translateX(-120%)}100%{transform:translateX(220%)}}
@keyframes fadeUp{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:translateY(0)}}
@keyframes shimmer{0%{background-position:-300px 0}100%{background-position:300px 0}}
@keyframes spinSlow{to{transform:rotate(360deg)}}

#MainMenu{visibility:hidden}
footer{visibility:hidden}
header[data-testid="stHeader"]{background:transparent}
.block-container{
  padding-top:3rem !important;padding-bottom:4rem !important;
  max-width:1260px !important;position:relative;z-index:1;
}

/* ═══ BARRA DE PROGRESO / NAVEGACIÓN ═══ */
.progress-shell{
  position:fixed;top:0;left:0;right:0;height:3px;z-index:9999;
  background:rgba(30,44,68,.6);backdrop-filter:blur(6px);
}
.progress-fill{
  height:100%;width:0%;
  background:linear-gradient(90deg,var(--amber),var(--cyan),var(--violet));
  box-shadow:0 0 14px rgba(245,165,36,.7);
  transition:width .25s ease;
}
.topnav{
  position:sticky;top:0;z-index:900;
  display:flex;align-items:center;justify-content:space-between;gap:1rem;
  padding:.65rem 1.1rem;margin:0 0 1rem 0;
  background:rgba(11,18,32,.78);
  backdrop-filter:blur(16px);
  border:1px solid var(--border);
  border-radius:100px;
  box-shadow:0 10px 34px rgba(0,0,0,.42);
}
.topnav .brand{
  display:flex;align-items:center;gap:.6rem;
  font-family:'JetBrains Mono',monospace;font-size:.72rem;
  letter-spacing:.2em;text-transform:uppercase;color:var(--text-2);
}
.topnav .brand b{color:var(--amber);font-weight:600}
.nav-pills{display:flex;gap:.35rem;flex-wrap:wrap}
.nav-pill{
  font-family:'JetBrains Mono',monospace;font-size:.66rem;letter-spacing:.11em;
  text-transform:uppercase;color:var(--muted);text-decoration:none !important;
  padding:.36rem .72rem;border-radius:100px;border:1px solid transparent;
  transition:all .25s ease;white-space:nowrap;
}
.nav-pill:hover{color:var(--bg);background:var(--amber);border-color:var(--amber);text-decoration:none !important;}
.nav-pill.dim:hover{background:var(--cyan);border-color:var(--cyan);}
.stProgress > div > div > div > div > div{background:transparent !important;}

/* ═══ HERO ═══ */
.hero-grid{display:grid;grid-template-columns:1.05fr .95fr;gap:3rem;align-items:center;}
.kicker{
  display:inline-flex;align-items:center;gap:.7rem;
  font-family:'JetBrains Mono',monospace;font-size:.68rem;
  letter-spacing:.26em;text-transform:uppercase;color:var(--amber);font-weight:500;
}
.kicker::before{content:'';width:30px;height:1px;background:linear-gradient(90deg,transparent,var(--amber));}
.hero-h1{
  font-size:4rem !important;line-height:1.02 !important;margin:.9rem 0 1.2rem 0 !important;
  letter-spacing:-.025em !important;font-weight:400 !important;color:var(--text) !important;
}
.hero-h1 em{font-style:italic;color:var(--amber);}
.hero-h1 .accent2{font-style:italic;color:var(--cyan);}
.hero-desc{font-size:1.02rem;line-height:1.8;color:var(--text-2);font-weight:300;max-width:600px;}
.hero-desc strong{color:var(--text);font-weight:600;}
.part-badge{
  display:inline-flex;align-items:center;gap:.6rem;padding:.35rem .9rem .35rem .4rem;
  background:var(--amber-soft);border:1px solid rgba(245,165,36,.32);border-radius:100px;
  font-family:'JetBrains Mono',monospace;font-size:.66rem;letter-spacing:.18em;
  text-transform:uppercase;color:var(--amber);font-weight:600;margin-bottom:1.1rem;
}
.part-badge .num{
  display:inline-flex;align-items:center;justify-content:center;width:23px;height:23px;
  background:var(--amber);color:#1a1005;border-radius:50%;font-size:.66rem;font-weight:800;
}
.hero-note{
  display:flex;gap:.8rem;padding:1rem 1.1rem;margin:1.4rem 0;
  background:rgba(76,201,224,.07);border-left:2px solid var(--cyan);
  border-radius:0 10px 10px 0;font-size:.9rem;line-height:1.65;color:var(--text-2);
}
.hero-note .icon{color:var(--cyan)}
.hero-note b{color:var(--cyan);font-weight:600}
.chips{display:flex;flex-wrap:wrap;gap:.5rem}
.chip{
  display:inline-flex;align-items:center;gap:.5rem;padding:.36rem .82rem;
  background:rgba(19,31,51,.8);border:1px solid var(--border);border-radius:100px;
  font-size:.8rem;color:var(--text-2);
}
.chip::before{content:'';width:5px;height:5px;border-radius:50%;background:var(--cyan);box-shadow:0 0 8px var(--cyan);}
.chip strong{color:var(--text);font-weight:600}
.chip.amber::before{background:var(--amber);box-shadow:0 0 8px var(--amber)}
.cta-row{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1.6rem}
.btn-cta{
  display:inline-flex;align-items:center;gap:.55rem;padding:.6rem 1.25rem;border-radius:100px;
  font-family:'JetBrains Mono',monospace;font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;
  font-weight:600;text-decoration:none !important;transition:all .28s ease;border:1px solid transparent;
}
.btn-cta.primary{background:var(--amber);color:#160e02}
.btn-cta.primary:hover{transform:translateY(-3px);box-shadow:0 12px 30px rgba(245,165,36,.35);color:#160e02}
.btn-cta.ghost{border-color:var(--border-2);color:var(--text-2)}
.btn-cta.ghost:hover{border-color:var(--cyan);color:var(--cyan);transform:translateY(-3px)}

/* Retrato */
.portrait-frame{
  position:relative;border-radius:26px;overflow:hidden;
  border:1px solid var(--border-2);
  background:linear-gradient(160deg,#0f1828,#0a1120);
  box-shadow:0 30px 80px rgba(0,0,0,.55), 0 0 90px rgba(76,201,224,.10);
  animation:floaty 7s ease-in-out infinite;
}
.portrait-frame img{width:100%;display:block;border-radius:26px;}
.portrait-ring{
  position:absolute;inset:-2px;border-radius:28px;padding:2px;
  background:conic-gradient(from 0deg,var(--amber),transparent 30%,var(--cyan) 55%,transparent 80%,var(--amber));
  -webkit-mask:linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);
  -webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none;
  animation:spinSlow 9s linear infinite;opacity:.65;
}
.portrait-badge{
  position:absolute;left:16px;bottom:16px;display:flex;align-items:center;gap:.55rem;
  padding:.45rem .85rem;border-radius:100px;
  background:rgba(7,11,20,.82);backdrop-filter:blur(10px);
  border:1px solid var(--border-2);
  font-family:'JetBrains Mono',monospace;font-size:.63rem;letter-spacing:.2em;
  text-transform:uppercase;color:var(--text-2);
}
.portrait-badge .dot{width:7px;height:7px;border-radius:50%;background:var(--amber);animation:pulseGlow 2s ease-in-out infinite;}
.portrait-caption{
  text-align:center;margin-top:1.3rem;font-family:'JetBrains Mono',monospace;
  font-size:.66rem;letter-spacing:.24em;text-transform:uppercase;color:var(--muted-2);
}
.portrait-caption .star{color:var(--amber);margin:0 .6rem}

/* ═══ MARCAS / STATS ═══ */
.stat-strip{
  display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;margin:3rem 0 .5rem 0;
}
.stat{
  padding:1.1rem 1.2rem;border:1px solid var(--border);border-radius:16px;
  background:linear-gradient(160deg,rgba(19,31,51,.85),rgba(11,18,32,.6));
  transition:transform .3s ease,border-color .3s ease;
}
.stat:hover{transform:translateY(-4px);border-color:var(--amber)}
.stat .v{font-family:'Instrument Serif',serif;font-size:1.9rem;color:var(--text);line-height:1}
.stat .l{font-family:'JetBrains Mono',monospace;font-size:.62rem;letter-spacing:.18em;text-transform:uppercase;color:var(--muted-2);margin-top:.45rem}

/* ═══ SECCIONES ═══ */
.section-head{
  display:flex;align-items:center;gap:1.1rem;padding-bottom:1.1rem;margin:4.5rem 0 2rem 0;
  border-bottom:1px solid var(--border);animation:fadeUp .6s ease both;
}
.section-num{
  display:inline-flex;align-items:center;justify-content:center;min-width:44px;height:32px;padding:0 .6rem;
  background:var(--amber-soft);border:1px solid rgba(245,165,36,.32);border-radius:9px;
  font-family:'JetBrains Mono',monospace;font-size:.76rem;font-weight:700;color:var(--amber);flex-shrink:0;
}
.section-title{font-size:1.7rem !important;font-weight:400 !important;margin:0 !important;color:var(--text) !important;flex:1;letter-spacing:-.01em !important;}
.section-count{font-family:'JetBrains Mono',monospace;font-size:.66rem;letter-spacing:.18em;text-transform:uppercase;color:var(--muted-2)}
.section-lede{color:var(--muted);font-size:.92rem;margin:-1.1rem 0 1.8rem 0;max-width:640px;line-height:1.7}

/* ═══ TARJETA DE PROYECTO ═══ */
.app-card{
  display:block !important;background:var(--surface);border:1px solid var(--border);
  border-radius:18px;text-decoration:none !important;color:var(--text) !important;
  transition:transform .35s cubic-bezier(.2,.7,.3,1),border-color .35s ease,box-shadow .35s ease;
  height:100%;overflow:hidden;position:relative;isolation:isolate;
  animation:fadeUp .7s ease both;
}
.app-card:hover{
  transform:translateY(-8px) scale(1.012);
  border-color:rgba(245,165,36,.55);
  box-shadow:0 26px 60px rgba(0,0,0,.55), 0 0 0 1px rgba(245,165,36,.18), 0 0 60px rgba(245,165,36,.10);
  text-decoration:none !important;color:var(--text) !important;
}
.app-card::after{
  content:'';position:absolute;inset:0;pointer-events:none;border-radius:18px;
  background:linear-gradient(115deg,transparent 30%,rgba(255,255,255,.09) 46%,transparent 62%);
  transform:translateX(-120%);transition:transform .9s ease;
}
.app-card:hover::after{transform:translateX(120%);}
.app-thumb{
  width:100%;aspect-ratio:16/10;background:linear-gradient(150deg,#0c1424,#111c30);
  border-bottom:1px solid var(--border);position:relative;display:flex;
  align-items:center;justify-content:center;overflow:hidden;
}
.app-thumb img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:top center;z-index:1;transition:transform .5s ease,filter .5s ease;}
.app-card:hover .app-thumb img{transform:scale(1.07);filter:saturate(1.12) contrast(1.03);}
.app-thumb .glyph{
  font-family:'Instrument Serif',serif;font-size:2rem;color:var(--muted-2);opacity:.55;
  transition:all .35s ease;
}
.app-card:hover .app-thumb .glyph{opacity:0;transform:scale(.8);}
.app-index{
  position:absolute;top:10px;left:10px;z-index:3;
  font-family:'JetBrains Mono',monospace;font-size:.6rem;letter-spacing:.16em;
  padding:.28rem .55rem;border-radius:6px;background:rgba(7,11,20,.8);
  border:1px solid var(--border-2);color:var(--amber);backdrop-filter:blur(6px);
}
.app-open{
  position:absolute;top:10px;right:10px;z-index:3;
  font-family:'JetBrains Mono',monospace;font-size:.6rem;letter-spacing:.16em;text-transform:uppercase;
  padding:.28rem .55rem;border-radius:6px;background:var(--amber);color:#160e02;font-weight:700;
  opacity:0;transform:translateY(-6px);transition:all .3s ease;
}
.app-card:hover .app-open{opacity:1;transform:translateY(0);}
.app-body{padding:1.3rem 1.35rem 1.45rem;}
.app-kicker{
  display:inline-block;font-family:'JetBrains Mono',monospace;font-size:.6rem;letter-spacing:.2em;
  text-transform:uppercase;color:var(--cyan);font-weight:500;margin-bottom:.65rem;
  padding:.22rem .55rem;border-radius:5px;background:var(--cyan-soft);
}
.app-title{font-size:1.28rem !important;font-weight:400 !important;line-height:1.28 !important;margin:0 0 .6rem 0 !important;color:var(--text) !important;}
.app-desc{font-size:.86rem;line-height:1.68;color:var(--muted);margin:0 0 1.15rem 0;font-weight:400;}
.app-link{
  display:inline-flex;align-items:center;gap:.5rem;font-family:'JetBrains Mono',monospace;
  font-size:.68rem;letter-spacing:.14em;text-transform:uppercase;color:var(--text-2);font-weight:500;
  transition:gap .25s ease,color .25s ease;
}
.app-card:hover .app-link{gap:.95rem;color:var(--amber);}
.card-warm .app-kicker{color:var(--amber);background:var(--amber-soft);}
.card-warm:hover{border-color:rgba(76,201,224,.55);}
.card-warm:hover .app-link{color:var(--cyan);}
.card-warm:hover .app-open{background:var(--cyan);color:#04161a;}

/* ═══ EXPLORADOR INTERACTIVO ═══ */
.explorer{
  border:1px solid var(--border);border-radius:22px;overflow:hidden;
  background:linear-gradient(160deg,rgba(19,31,51,.9),rgba(11,18,32,.85));
  box-shadow:0 22px 56px rgba(0,0,0,.45);
  animation:fadeUp .7s ease both;
}
.explorer-top{
  display:flex;align-items:center;gap:.6rem;padding:.85rem 1.1rem;
  border-bottom:1px solid var(--border);background:rgba(7,11,20,.5);
}
.explorer-top .dots{display:flex;gap:.35rem}
.explorer-top .dots i{width:10px;height:10px;border-radius:50%;display:block}
.explorer-top .dots i:nth-child(1){background:#ef5b5b}
.explorer-top .dots i:nth-child(2){background:#f5a524}
.explorer-top .dots i:nth-child(3){background:#4cc9e0}
.explorer-top .path{
  font-family:'JetBrains Mono',monospace;font-size:.63rem;letter-spacing:.14em;
  text-transform:uppercase;color:var(--muted-2);margin-left:.4rem;
}
.explorer-body{padding:1.3rem 1.4rem;}
.exp-row{
  display:grid;grid-template-columns:repeat(3,1fr);gap:.9rem;
}
.exp-item{
  border:1px solid var(--border);border-radius:14px;padding:1rem 1.05rem;
  background:rgba(7,11,20,.55);transition:all .3s ease;position:relative;overflow:hidden;
}
.exp-item:hover{border-color:var(--border-2);transform:translateY(-3px);background:rgba(15,24,40,.85)}
.exp-item .bar{height:3px;border-radius:3px;background:var(--border);margin-bottom:.75rem;overflow:hidden}
.exp-item .bar span{display:block;height:100%;background:linear-gradient(90deg,var(--amber),var(--cyan));border-radius:3px}
.exp-item .t{font-family:'Instrument Serif',serif;font-size:1.05rem;color:var(--text);margin-bottom:.35rem}
.exp-item .d{font-size:.78rem;color:var(--muted);line-height:1.55}

/* Timeline */
.timeline{position:relative;padding-left:2rem;margin-top:.5rem}
.timeline::before{
  content:'';position:absolute;left:7px;top:6px;bottom:6px;width:2px;
  background:linear-gradient(180deg,var(--amber),var(--cyan),transparent);
}
.tl-item{position:relative;padding:0 0 1.6rem 0;animation:fadeUp .6s ease both}
.tl-item::before{
  content:'';position:absolute;left:-2rem;top:5px;width:16px;height:16px;border-radius:50%;
  background:var(--bg);border:2px solid var(--amber);box-shadow:0 0 0 4px rgba(245,165,36,.10);
}
.tl-item:last-child::before{border-color:var(--cyan);box-shadow:0 0 0 4px rgba(76,201,224,.10)}
.tl-stage{font-family:'JetBrains Mono',monospace;font-size:.62rem;letter-spacing:.2em;text-transform:uppercase;color:var(--amber);margin-bottom:.3rem}
.tl-title{font-family:'Instrument Serif',serif;font-size:1.1rem;color:var(--text);margin-bottom:.25rem}
.tl-desc{font-size:.83rem;color:var(--muted);line-height:1.6}

/* Filtros */
.filter-bar{
  display:flex;flex-wrap:wrap;gap:.55rem;align-items:center;
  padding:1rem 1.1rem;border:1px solid var(--border);border-radius:16px;
  background:rgba(11,18,32,.7);margin-bottom:1.6rem;
}
.filter-label{font-family:'JetBrains Mono',monospace;font-size:.62rem;letter-spacing:.2em;text-transform:uppercase;color:var(--muted-2);margin-right:.3rem}
.filter-btn{
  font-family:'JetBrains Mono',monospace;font-size:.66rem;letter-spacing:.1em;text-transform:uppercase;
  padding:.42rem .85rem;border-radius:100px;border:1px solid var(--border);
  background:rgba(19,31,51,.7);color:var(--text-2);cursor:pointer;transition:all .25s ease;
}
.filter-btn:hover{border-color:var(--amber);color:var(--amber);transform:translateY(-2px)}
.filter-btn.active{background:var(--amber);color:#160e02;border-color:var(--amber);font-weight:700}

/* ═══ FOOTER ═══ */
.footer{text-align:center;padding:3.5rem 0 1rem 0;margin-top:5rem;border-top:1px solid var(--border)}
.footer-ornament{font-family:'Instrument Serif',serif;font-size:1.4rem;color:var(--amber);margin-bottom:1rem;display:block;letter-spacing:1rem}
.footer-text{font-family:'Instrument Serif',serif;font-size:1.15rem;font-style:italic;color:var(--text);margin:0 0 .45rem 0}
.footer-sub{font-family:'JetBrains Mono',monospace;font-size:.66rem;letter-spacing:.2em;text-transform:uppercase;color:var(--muted-2);margin:0}

/* Utilidades */
.stMarkdown a{text-decoration:none !important;}
::-webkit-scrollbar{width:10px;height:10px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--border-2);border:2px solid var(--bg);border-radius:10px}
::-webkit-scrollbar-thumb:hover{background:var(--amber)}
.glow-text{text-shadow:0 0 26px rgba(245,165,36,.35)}
.stButton > button{
  border-radius:100px !important;border:1px solid var(--border-2) !important;
  background:rgba(19,31,51,.8) !important;color:var(--text-2) !important;
  font-family:'JetBrains Mono',monospace !important;font-size:.7rem !important;
  letter-spacing:.13em !important;text-transform:uppercase;transition:all .28s ease !important;
}
.stButton > button:hover{
  border-color:var(--amber) !important;color:var(--amber) !important;
  transform:translateY(-3px) !important;box-shadow:0 10px 26px rgba(0,0,0,.4) !important;
}
.stButton > button[kind="primary"]{
  background:var(--amber) !important;color:#160e02 !important;border-color:var(--amber) !important;font-weight:700;
}

@media (max-width:980px){
  .hero-grid{grid-template-columns:1fr;gap:2rem}
  .hero-h1{font-size:2.6rem !important}
  .stat-strip{grid-template-columns:repeat(2,1fr)}
  .exp-row{grid-template-columns:1fr}
  .section-title{font-size:1.35rem !important}
  .section-count{display:none}
  .nav-pills{display:none}
}
</style>
"""

st.markdown(CSS, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════════
def get_image_base64(path):
    """Convierte una imagen local a Base64 para inyectarla en HTML."""
    try:
        if os.path.exists(path):
            with open(path, "rb") as f:
                data = base64.b64encode(f.read()).decode("utf-8")
                ext = os.path.splitext(path)[1].lower().lstrip(".") or "png"
                if ext == "jpg":
                    ext = "jpeg"
                return f"data:image/{ext};base64,{data}"
    except Exception:
        pass
    return ""


def esc(text):
    return html_lib.escape(str(text))


def section_header(num, title, count, lede=None):
    st.markdown(f"""
    <div class="section-head">
      <span class="section-num">{esc(num)}</span>
      <h2 class="section-title">{esc(title)}</h2>
      <span class="section-count">{esc(count)}</span>
    </div>
    {f'<p class="section-lede">{esc(lede)}</p>' if lede else ''}
    """, unsafe_allow_html=True)


def app_card(kicker, title, desc, url, image_path, index, variant=""):
    """Tarjeta de proyecto con imagen, etiqueta y efecto hover."""
    b64 = get_image_base64(image_path)
    img_tag = f'<img src="{b64}" alt="{esc(title)}">' if b64 else ''
    glyph = '' if b64 else '<span class="glyph">◇</span>'
    warm = " card-warm" if variant == "warm" else ""
    delay = 0.05 * int(index)
    return f"""
    <a href="{esc(url)}" target="_blank" class="app-card{warm}" style="animation-delay:{delay:.2f}s">
      <div class="app-thumb">
        <span class="app-index">{esc(index)}</span>
        <span class="app-open">Abrir</span>
        {img_tag}
        {glyph}
      </div>
      <div class="app-body">
        <span class="app-kicker">{esc(kicker)}</span>
        <h3 class="app-title">{esc(title)}</h3>
        <p class="app-desc">{esc(desc)}</p>
        <span class="app-link">Abrir aplicación →</span>
      </div>
    </a>
    """


# ═══════════════════════════════════════════════════════════════════════
# DATOS (textos originales preservados)
# ═══════════════════════════════════════════════════════════════════════
SECTIONS = [
    {
        "num": "01",
        "title": "Aplicaciones con LLMs",
        "count": "2 aplicaciones",
        "lede": "Sistemas que entienden y generan lenguaje natural: procesamiento de texto y reconocimiento visual.",
        "items": [
            {
                "kicker": "NLP · Procesamiento",
                "title": "Procesamiento de Lenguaje",
                "desc": "Explora cómo la IA comprende, analiza y genera lenguaje natural en español.",
                "url": "https://procesamientolenguajejplg-dpcdtmrteadz4zxvzn8adh.streamlit.app/",
                "img": "LLM1.PNG",
                "variant": "",
            },
            {
                "kicker": "Computer Vision",
                "title": "Visión artificial",
                "desc": "Modelos de visión por computadora que reconocen imágenes, objetos y patrones.",
                "url": "https://visionapp-8whsafj8pj5hdiuow4yjyb.streamlit.app/",
                "img": "LLM2.PNG",
                "variant": "warm",
            },
        ],
    },
    {
        "num": "02",
        "title": "Interacción con interfaces táctiles",
        "count": "4 aplicaciones",
        "lede": "Tableros que reciben trazos a mano y los convierten en instrucciones para la inteligencia artificial.",
        "items": [
            {
                "kicker": "Visión + GPT",
                "title": "Tablero inteligente",
                "desc": "Dibuja un boceto y deja que la IA lo interprete, lo describa o lo resuelva.",
                "url": "https://tablerotuneado-dqjtotfrqskiyeosh6youa.streamlit.app/",
                "img": "Tablero3.PNG",
                "variant": "warm",
            },
            {
                "kicker": "Matemáticas · GPT",
                "title": "Tablero de matemáticas",
                "desc": "Dibuja una operación o ecuación y la IA la resuelve paso a paso con LaTeX.",
                "url": "https://tablerotuneado-ez8ftd2kuoia7yoh7cpdhe.streamlit.app/",
                "img": "Tablero4.PNG",
                "variant": "",
            },
            {
                "kicker": "OCR · Números",
                "title": "Tablero que lee números",
                "desc": "Escribe un número a mano y la IA lo reconoce e interpreta al instante.",
                "url": "https://tactilnumeros-kdpcwepxhzeer6zvu3cq6x.streamlit.app/",
                "img": "Tablero1.PNG",
                "variant": "",
            },
            {
                "kicker": "Canvas · Personalizable",
                "title": "Tablero para dibujar",
                "desc": "Un lienzo libre con herramientas y colores personalizables para crear.",
                "url": "https://tableropersonalizado-nkqwmc7lntrdxrnqmo7nl6.streamlit.app/",
                "img": "Tablero2.PNG",
                "variant": "warm",
            },
        ],
    },
    {
        "num": "03",
        "title": "Sistemas con internet de las cosas",
        "count": "3 aplicaciones",
        "lede": "Dispositivos simulados, sensores y comandos de voz conectados entre Wokwi y Streamlit.",
        "items": [
            {
                "kicker": "Voz · Control",
                "title": "Control de voz",
                "desc": "Interactúa con la aplicación usando únicamente tu voz, sin tocar el teclado.",
                "url": "https://ctrlvoice-4zw5fqi5pmuizke4vdecw7.streamlit.app/",
                "img": "IOT3.PNG",
                "variant": "",
            },
            {
                "kicker": "Sensor · MQTT",
                "title": "Wokwi a Streamlit",
                "desc": "Un sensor simulado en Wokwi envía datos a Streamlit a través de MQTT.",
                "url": "https://lectormqtt-t59niwifyecackdckk82fx.streamlit.app/",
                "img": "IOT1.PNG",
                "variant": "warm",
            },
            {
                "kicker": "Control · MQTT",
                "title": "Streamlit a Wokwi",
                "desc": "Controla dispositivos simulados en Wokwi desde una interfaz en Streamlit.",
                "url": "https://appawokwicmqtt-spyylhsrmng4sdf5fncrty.streamlit.app/",
                "img": "IOT2.PNG",
                "variant": "",
            },
        ],
    },
]

# ═══════════════════════════════════════════════════════════════════════
# BARRA DE PROGRESO + NAVEGACIÓN
# ═══════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="progress-shell"><div class="progress-fill" id="progressFill"></div></div>
<div class="topnav">
  <div class="brand"><b>✦</b> Juan Pablo · Portafolio 2026</div>
  <nav class="nav-pills">
    <a class="nav-pill" href="#inicio">Inicio</a>
    <a class="nav-pill" href="#s01">01 · LLMs</a>
    <a class="nav-pill" href="#s02">02 · Táctiles</a>
    <a class="nav-pill" href="#s03">03 · IoT</a>
    <a class="nav-pill dim" href="#recorrido">Recorrido</a>
  </nav>
</div>
<script>
(function(){
  var fill = document.getElementById('progressFill');
  function upd(){
    var h = document.documentElement.scrollHeight - window.innerHeight;
    var p = h > 0 ? (window.scrollY / h) * 100 : 0;
    if(fill){ fill.style.width = Math.min(100, Math.max(0, p)) + '%'; }
  }
  window.addEventListener('scroll', upd, {passive:true});
  window.addEventListener('resize', upd);
  upd();
  setTimeout(upd, 400);
})();
</script>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════
# HERO
# ═══════════════════════════════════════════════════════════════════════
st.markdown('<div id="inicio"></div>', unsafe_allow_html=True)

left, right = st.columns([1.12, 0.88], gap="large", vertical_alignment="center")

with left:
    st.markdown("""
    <div class="part-badge"><span class="num">2</span><span>Segunda parte · Portafolio 2026</span></div>
    <div class="kicker">Interfaces Multimodales</div>
    <h1 class="hero-h1">Hola, soy<br><em>Juan Pablo</em></h1>
    <p class="hero-desc">
      Tengo <strong>20 años</strong> y estudio <strong>Diseño Interactivo</strong>
      en <strong>EAFIT</strong>. Esta es la <strong>segunda parte</strong> de mi
      portafolio para la materia de <strong>Interfaces Multimodales</strong>, donde
      reunimos los proyectos más recientes del semestre: desde modelos de lenguaje
      hasta integraciones con hardware y visión por computadora.
    </p>
    <div class="hero-note">
      <span class="icon">✦</span>
      <span>Esta es la <b>segunda parte</b> del portafolio. Reúne las actividades más recientes del curso, incluyendo las integraciones con hardware y los tableros interactivos.</span>
    </div>
    <div class="chips">
      <span class="chip"><strong>EAFIT</strong> Diseño Interactivo</span>
      <span class="chip amber"><strong>20 años</strong> Medellín</span>
      <span class="chip"><strong>2026</strong> Interfaces Multimodales</span>
    </div>
    <div class="cta-row">
      <a class="btn-cta primary" href="#s01">Recorrer proyectos ↓</a>
      <a class="btn-cta ghost" href="#recorrido">Ver el recorrido</a>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("""
    <div class="portrait-frame">
      <div class="portrait-ring"></div>
    </div>
    """, unsafe_allow_html=True)
    try:
        st.image("yo.png", use_container_width=True)
    except Exception:
        st.markdown(
            '<div style="height:420px;display:flex;align-items:center;justify-content:center;font-size:6rem;">'
            '👋</div>',
            unsafe_allow_html=True,
        )
    st.markdown(
        '<div class="portrait-badge"><span class="dot"></span> Disponible para nuevas ideas</div>'
        '<div class="portrait-caption">Juan Pablo<span class="star">✦</span>Parte 2 · 2026</div>',
        unsafe_allow_html=True,
    )

# ═══════════════════════════════════════════════════════════════════════
# STATS
# ═══════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="stat-strip">
  <div class="stat"><div class="v">9</div><div class="l">Aplicaciones</div></div>
  <div class="stat"><div class="v">03</div><div class="l">Categorías</div></div>
  <div class="stat"><div class="v">LLM</div><div class="l">Lenguaje y visión</div></div>
  <div class="stat"><div class="v">IoT</div><div class="l">Hardware conectado</div></div>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════
# FILTRO INTERACTIVO
# ═══════════════════════════════════════════════════════════════════════
st.markdown('<div id="s01"></div>', unsafe_allow_html=True)

FILTERS = ["Todos", "LLMs", "Táctiles", "IoT"]
current = st.session_state.get("filtro_actual", "Todos")

if current not in FILTERS:
    current = "Todos"

# Fila de botones nativos (más fiable que JS puro en Streamlit)
bcols = st.columns([1.4, 1, 1, 1, 4])
with bcols[0]:
    st.markdown(
        '<div class="filter-label" style="display:flex;align-items:center;height:38px;">Filtrar por</div>',
        unsafe_allow_html=True,
    )
for i, f in enumerate(FILTERS, start=1):
    with bcols[i]:
        if st.button(f, key=f"btn_{f}", use_container_width=True):
            st.session_state["filtro_actual"] = f
            st.rerun()

st.markdown("""
<div class="filter-bar" style="pointer-events:none;">
  <span class="filter-label">Explorador</span>
  <span class="filter-btn active">Todos</span>
  <span class="filter-btn">LLMs</span>
  <span class="filter-btn">Táctiles</span>
  <span class="filter-btn">IoT</span>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════
# SECCIONES DE PROYECTOS
# ═══════════════════════════════════════════════════════════════════════
sec_index = 0
for sec in SECTIONS:
    anchor = "s" + sec["num"]
    st.markdown(f'<div id="{anchor}"></div>', unsafe_allow_html=True)
    section_header(sec["num"], sec["title"], sec["count"], sec["lede"])

    items = sec["items"]
    if current != "Todos":
        mapping = {"01": "LLMs", "02": "Táctiles", "03": "IoT"}
        if mapping[sec["num"]] != current:
            continue

    if len(items) == 3:
        cols = st.columns(3, gap="medium")
    elif len(items) == 4:
        top = st.columns(2, gap="medium")
        bottom = st.columns(2, gap="medium")
        cols = list(top) + list(bottom)
    else:
        cols = st.columns(len(items), gap="medium")

    for col, item in zip(cols, items):
        with col:
            sec_index += 1
            st.markdown(
                app_card(
                    item["kicker"],
                    item["title"],
                    item["desc"],
                    item["url"],
                    item["img"],
                    f'{sec["num"]}.{items.index(item) + 1}',
                    item["variant"],
                ),
                unsafe_allow_html=True,
            )

# ═══════════════════════════════════════════════════════════════════════
# RECORRIDO (TIMELINE + EXPLORADOR)
# ═══════════════════════════════════════════════════════════════════════
st.markdown('<div id="recorrido"></div>', unsafe_allow_html=True)
section_header("04", "El recorrido", "3 etapas", "Así se construyó esta segunda parte del portafolio, etapa por etapa.")

st.markdown("""
<div class="explorer">
  <div class="explorer-top">
    <div class="dots"><i></i><i></i><i></i></div>
    <span class="path">interfaces-multimodales / parte-2</span>
  </div>
  <div class="explorer-body">
    <div class="exp-row">
      <div class="exp-item">
        <div class="bar"><span style="width:100%"></span></div>
        <div class="t">Lenguaje</div>
        <div class="d">Modelos que comprenden y generan texto en español, y modelos que miran imágenes.</div>
      </div>
      <div class="exp-item">
        <div class="bar"><span style="width:78%"></span></div>
        <div class="t">Trazo</div>
        <div class="d">Tableros táctiles donde la handwritten input se convierte en instrucciones para la IA.</div>
      </div>
      <div class="exp-item">
        <div class="bar"><span style="width:56%"></span></div>
        <div class="t">Conexión</div>
        <div class="d">Sensores y dispositivos simulados en Wokwi hablando por MQTT con Streamlit.</div>
      </div>
    </div>
    <div class="timeline">
      <div class="tl-item">
        <div class="tl-stage">Etapa 01 · Fundamentos</div>
        <div class="tl-title">Aplicaciones con LLMs</div>
        <div class="tl-desc">Procesamiento de Lenguaje y Visión artificial: los primeros experimentos con modelos que interpretan contenido.</div>
      </div>
      <div class="tl-item">
        <div class="tl-stage">Etapa 02 · Interacción</div>
        <div class="tl-title">Interfaces táctiles</div>
        <div class="tl-desc">Cuatro tableros que reciben bocetos a mano: interpretar, resolver matemáticas, leer números y dibujar libremente.</div>
      </div>
      <div class="tl-item">
        <div class="tl-stage">Etapa 03 · Hardware</div>
        <div class="tl-title">Internet de las cosas</div>
        <div class="tl-desc">Control por voz y puentes de datos en ambos sentidos entre Wokwi y Streamlit mediante MQTT.</div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="footer">
  <span class="footer-ornament">✦ ✦ ✦</span>
  <p class="footer-text">Hecho con curiosidad desde Medellín</p>
  <p class="footer-sub">Juan Pablo · EAFIT · Interfaces Multimodales · Parte 2 · 2026</p>
</div>
""", unsafe_allow_html=True)
