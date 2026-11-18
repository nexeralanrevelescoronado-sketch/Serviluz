/* Serie de focos — Serví luz
   Una serie de focos cuelga al inicio de cada sección. Con el scroll se prenden
   uno por uno (y se apagan al regresar). Cada foco prendido alumbra lo que tiene
   abajo; cuando la serie queda completa, la sección "recibe" la luz (.lit).
   Motion (motion.dev): scroll() liga el avance al scroll, animate() prende y apaga.
   Compilar (con motion y esbuild instalados): npx esbuild _src/focos.js --bundle --minify --format=iife --target=es2019 --outfile=assets/js/focos.js */
import { animate } from "motion/mini";
import { scroll } from "motion";

const mq = (q) => window.matchMedia(q).matches;
const reduce = mq("(prefers-reduced-motion:reduce)");
const lite = (navigator.hardwareConcurrency && navigator.hardwareConcurrency <= 2) || (navigator.deviceMemory && navigator.deviceMemory <= 2);
const calm = reduce || lite;
const OUT = [0.23, 1, 0.32, 1];

const BULB =
  '<svg class="fo-b" viewBox="0 0 24 44" width="24" height="44" aria-hidden="true" focusable="false">' +
  '<path d="M12 0v8" stroke="#3a3e47" stroke-width="1.6"/>' +
  '<rect x="8" y="8" width="8" height="8" rx="1.6" fill="#2b2f37"/><path d="M8 11h8M8 13.5h8" stroke="#454a55" stroke-width=".8"/>' +
  '<path class="fo-off" d="M8.5 16C8.5 20 3 23 3 30a9 9 0 0 0 18 0C21 23 15.5 20 15.5 16Z" fill="rgba(255,255,255,.05)" stroke="rgba(255,255,255,.3)" stroke-width="1"/>' +
  '<path class="fo-off" d="M10.5 16 9.5 30l1.5-4 1 4 1-4 1.5 4-1-14" fill="none" stroke="rgba(255,255,255,.28)" stroke-width=".8" stroke-linejoin="round"/>' +
  '<g class="fo-on"><path d="M8.5 16C8.5 20 3 23 3 30a9 9 0 0 0 18 0C21 23 15.5 20 15.5 16Z" fill="url(#fo-grad)"/>' +
  '<path d="M10.5 16 9.5 30l1.5-4 1 4 1-4 1.5 4-1-14" fill="none" stroke="#fffdf2" stroke-width="1" stroke-linejoin="round"/></g></svg>';

function defs() {
  if (document.getElementById("fo-grad")) return;
  const d = document.createElement("div");
  d.setAttribute("aria-hidden", "true");
  d.style.cssText = "position:absolute;width:0;height:0;overflow:hidden";
  d.innerHTML = '<svg width="0" height="0"><defs><radialGradient id="fo-grad" cx="50%" cy="66%" r="60%"><stop offset="0" stop-color="#fffbe6"/><stop offset=".45" stop-color="#ffd257"/><stop offset="1" stop-color="#ff9a1f"/></radialGradient></defs></svg>';
  document.body.appendChild(d);
}

function build(sec, idx) {
  const w = window.innerWidth;
  const n = w < 700 ? 3 : w < 1100 ? 5 : 7;
  const sag = w < 700 ? 40 : 60;
  const h = sag / 2 + 4;
  const el = document.createElement("div");
  el.className = "serie";
  el.setAttribute("aria-hidden", "true");
  let html = '<svg class="serie-w" viewBox="0 0 100 ' + h + '" height="' + h + '" preserveAspectRatio="none"><path d="M0,2 Q50,' + (2 + sag) + ' 100,2" fill="none" stroke="#3a3e47" stroke-width="1.6" vector-effect="non-scaling-stroke"/></svg>';
  for (let i = 0; i < n; i++) {
    const t = (i + 0.5) / n;
    const y = 2 + 2 * t * (1 - t) * sag;
    html += '<span class="fo" style="left:' + (t * 100).toFixed(2) + "%;top:calc(var(--up) + " + y.toFixed(1) + 'px)"><i class="fo-w"></i><i class="fo-g"></i>' + BULB + "</span>";
  }
  el.innerHTML = html;
  sec.appendChild(el);
  const bulbs = [].slice.call(el.querySelectorAll(".fo")).map((f) => ({
    on: f.querySelector(".fo-on"), glow: f.querySelector(".fo-g"), wash: f.querySelector(".fo-w"), lit: false, a: [],
  }));
  /* la corriente baja en zigzag: una serie prende de izquierda a derecha, la siguiente al revés */
  if (idx % 2) bulbs.reverse();
  return { sec, el, bulbs, k: 0 };
}

function set(b, on) {
  if (b.lit === on) return;
  b.lit = on;
  b.a.forEach((x) => { try { x.stop(); } catch (e) {} });
  if (on) {
    b.a = calm
      ? [animate(b.on, { opacity: 1 }, { duration: 0.2 }), animate(b.glow, { opacity: 1 }, { duration: 0.2 }), animate(b.wash, { opacity: 1 }, { duration: 0.3 })]
      : [
          /* arranque de foco incandescente: chispazo, baja y se estabiliza */
          animate(b.on, { opacity: [null, 0.9, 0.3, 1] }, { duration: 0.5, times: [0, 0.2, 0.42, 1], ease: "linear" }),
          animate(b.glow, { opacity: [null, 0.9, 0.25, 1], transform: ["translate(-50%,-50%) scale(.6)", "translate(-50%,-50%) scale(1)"] }, { duration: 0.5, times: [0, 0.2, 0.42, 1], ease: "linear" }),
          animate(b.wash, { opacity: 1, transform: ["translateX(-50%) scale(.72)", "translateX(-50%) scale(1)"] }, { duration: 0.8, ease: OUT }),
        ];
  } else {
    /* apagar es más rápido que prender */
    b.a = [animate(b.on, { opacity: 0 }, { duration: 0.22, ease: OUT }), animate(b.glow, { opacity: 0 }, { duration: 0.22, ease: OUT }), animate(b.wash, { opacity: 0 }, { duration: 0.3, ease: OUT })];
  }
}

function update(s, p) {
  const n = s.bulbs.length;
  const k = Math.max(0, Math.min(n, Math.floor(p * n + 0.001)));
  if (k === s.k) return;
  s.k = k;
  for (let i = 0; i < n; i++) set(s.bulbs[i], i < k);
  s.sec.classList.toggle("lit", k === n);
}

function init() {
  const secs = [].slice.call(document.querySelectorAll("main > section")).filter((s) => !s.matches(".scrub,.sub,[data-moment]") && parseFloat(getComputedStyle(s).paddingTop) >= 60);
  if (!secs.length) return;
  defs();
  const series = secs.map(build);
  document.documentElement.classList.add("has-serie");
  series.forEach((s) => {
    try {
      scroll((p) => update(s, p), { target: s.sec, offset: ["0 0.95", "0 0.42"] });
    } catch (e) {
      update(s, 1);
    }
  });
}

if ("requestIdleCallback" in window) requestIdleCallback(init, { timeout: 1500 });
else setTimeout(init, 300);
