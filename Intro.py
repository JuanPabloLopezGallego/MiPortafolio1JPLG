components.html("""
<script>
(function () {
    function setup() {
        const win = window.parent;
        const doc = win.document;

        const probe = doc.getElementById('scroll-bar');
        if (!probe) { setTimeout(setup, 400); return; }
        if (probe.dataset.jsReady === 'true') return;
        probe.dataset.jsReady = 'true';

        // ── 1. Scroll progress bar ──────────────────────────
        function updateProgress() {
            const scrollTop = win.scrollY || doc.documentElement.scrollTop;
            const docHeight = doc.documentElement.scrollHeight - win.innerHeight;
            const pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
            probe.style.width = pct + '%';
        }
        win.addEventListener('scroll', updateProgress, { passive: true });
        doc.addEventListener('scroll', updateProgress, { passive: true });
        updateProgress();

        // ── 2. Side nav: click + IntersectionObserver ──────
        const sectionIds = ['inicio', 'llms', 'tactil', 'iot', 'final'];
        const navLinks = doc.querySelectorAll('.side-nav-dot-wrap');

        function setActive(id) {
            navLinks.forEach(link => {
                link.classList.toggle('is-active', link.dataset.sec === id);
            });
        }

        // Click handlers con feedback inmediato
        navLinks.forEach(link => {
            if (link.dataset.clickBound === 'true') return;
            link.dataset.clickBound = 'true';
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const id = link.dataset.sec;
                setActive(id);
                const target = doc.getElementById(id);
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });

        // IntersectionObserver del realm del padre (funciona con el scroll container de Streamlit)
        if (!window.__navObserverSetup) {
            window.__navObserverSetup = true;
            const IO = win.IntersectionObserver || IntersectionObserver;
            const observer = new IO((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) setActive(entry.target.id);
                });
            }, { rootMargin: '-35% 0px -60% 0px', threshold: 0 });

            sectionIds.forEach(id => {
                const el = doc.getElementById(id);
                if (el) observer.observe(el);
            });
        }

        // ── 3. Carruseles ──────────────────────────────────
        doc.querySelectorAll('.carousel-wrap').forEach(wrap => {
            if (wrap.dataset.carouselBound === 'true') return;
            wrap.dataset.carouselBound = 'true';

            const track = wrap.querySelector('.carousel-track');
            if (!track) return;
            const prev = wrap.querySelector('.carousel-arrow-left');
            const next = wrap.querySelector('.carousel-arrow-right');
            const dots = wrap.querySelectorAll('.carousel-dot');
            const slides = track.querySelectorAll('.carousel-slide');
            const counter = wrap.querySelector('.carousel-counter');

            const step = () => {
                const s = slides[0];
                return s ? s.offsetWidth + 28 : 400;
            };

            if (prev) prev.addEventListener('click', () =>
                track.scrollBy({ left: -step(), behavior: 'smooth' }));
            if (next) next.addEventListener('click', () =>
                track.scrollBy({ left: step(), behavior: 'smooth' }));

            const updateDots = () => {
                const sl = track.scrollLeft;
                let closest = 0, minDist = Infinity;
                slides.forEach((s, i) => {
                    const d = Math.abs(s.offsetLeft - track.offsetLeft - sl);
                    if (d < minDist) { minDist = d; closest = i; }
                });
                dots.forEach((d, i) => d.classList.toggle('is-active', i === closest));
                if (counter) {
                    counter.textContent =
                        String(closest + 1).padStart(2, '0') + ' / ' +
                        String(slides.length).padStart(2, '0');
                }
            };
            track.addEventListener('scroll', updateDots, { passive: true });
            dots.forEach((d, i) => d.addEventListener('click', () => {
                const s = slides[i];
                if (s) track.scrollTo({
                    left: s.offsetLeft - track.offsetLeft,
                    behavior: 'smooth'
                });
            }));
            updateDots();
        });

        // ── 4. Mouse glow + parallax ───────────────────────
        const glow = doc.getElementById('mouse-glow');
        const orb1 = doc.querySelector('.orb-1');
        const orb2 = doc.querySelector('.orb-2');
        if (glow && !glow.dataset.bound) {
            glow.dataset.bound = 'true';
            win.addEventListener('mousemove', (e) => {
                glow.style.setProperty('--mx', e.clientX + 'px');
                glow.style.setProperty('--my', e.clientY + 'px');
                const x = e.clientX / win.innerWidth - 0.5;
                const y = e.clientY / win.innerHeight - 0.5;
                if (orb1) {
                    orb1.style.setProperty('--px', (x * 70) + 'px');
                    orb1.style.setProperty('--py', (y * 70) + 'px');
                }
                if (orb2) {
                    orb2.style.setProperty('--px', (-x * 70) + 'px');
                    orb2.style.setProperty('--py', (-y * 70) + 'px');
                }
            }, { passive: true });
        }

        // ── 5. Canvas de partículas flotantes ──────────────
        const canvas = doc.getElementById('particle-canvas');
        if (canvas && !canvas.dataset.bound) {
            canvas.dataset.bound = 'true';
            const ctx = canvas.getContext('2d');

            function resize() {
                canvas.width = win.innerWidth;
                canvas.height = win.innerHeight;
            }
            resize();
            win.addEventListener('resize', resize);

            const palette = [
                '192, 132, 252',
                '244, 114, 182',
                '251, 191, 36',
                '255, 255, 255',
            ];
            const count = Math.min(110, Math.max(50,
                Math.floor((win.innerWidth * win.innerHeight) / 16000)));
            const parts = [];
            for (let i = 0; i < count; i++) {
                parts.push({
                    x: Math.random() * canvas.width,
                    y: Math.random() * canvas.height,
                    r: Math.random() * 1.7 + 0.4,
                    vx: (Math.random() - 0.5) * 0.25,
                    vy: -Math.random() * 0.35 - 0.08,
                    color: palette[Math.floor(Math.random() * palette.length)],
                    baseAlpha: Math.random() * 0.45 + 0.15,
                    phase: Math.random() * Math.PI * 2,
                });
            }

            let t = 0;
            function draw() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                t += 0.035;
                for (let i = 0; i < parts.length; i++) {
                    const p = parts[i];
                    p.x += p.vx;
                    p.y += p.vy;
                    if (p.y < -10) { p.y = canvas.height + 10; p.x = Math.random() * canvas.width; }
                    if (p.x < -10) p.x = canvas.width + 10;
                    if (p.x > canvas.width + 10) p.x = -10;

                    const tw = Math.sin(t + p.phase) * 0.35 + 0.65;
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
                    ctx.fillStyle = 'rgba(' + p.color + ', ' + (p.baseAlpha * tw) + ')';
                    ctx.fill();
                }
                requestAnimationFrame(draw);
            }
            draw();
        }
    }

    setTimeout(setup, 300);
    setTimeout(setup, 900);
    setTimeout(setup, 1800);
    setTimeout(setup, 3000);
})();
</script>
""", height=0)
