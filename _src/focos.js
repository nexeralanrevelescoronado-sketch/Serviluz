/* Serie de focos — Serví luz
   Un cable baja por el lado izquierdo de cada sección con focos colgados.
   Lo que queda a la derecha está en penumbra hasta que su foco prende: con el
   scroll se prenden uno por uno y la oscuridad se va recorriendo hacia abajo;
   al regresar se apagan y la penumbra vuelve a subir.
   Motion (motion.dev): scroll() avisa en cada avance del scroll, animate() prende,
   apaga y mueve la penumbra (solo opacity y transform).
   Compilar (con motion y esbuild instalados):
   npx esbuild _src/focos.js --bundle --minify --format=iife --target=es2019 --outfile=assets/js/focos.js */
import { animate } from "motion/mini";
import { scroll } from "motion";

const mq = (q) => window.matchMedia(q).matches;
const reduce = mq("(prefers-reduced-motion:reduce)");
const lite = (navigator.hardwareConcurrency && navigator.hardwareConcurrency <= 2) || (navigator.deviceMemory && navigator.deviceMemory <= 2);
const calm = reduce || lite;
const OUT = [0.23, 1, 0.32, 1];
const SEL = 'main > section:not(.scrub):not(.sub):not(.nofo):not([data-moment]):not([style*="padding:46px"])';
const F = 150;      /* alto del degradado entre luz y penumbra */
const BASE = 100;   /* alto base del bloque oscuro (se estira con scaleY) */
const LINE = 0.6;   /* un foco prende cuando cruza el 60% de la pantalla */
const HANG = 30;    /* del nudo del cable al centro del foco */

const BULB =
  '<svg class="fo-b" viewBox="0 0 24 44" width="24" height="44" aria-hidden="true" focusable="false">' +
  '<path d="M12 0v8" stroke="#3a3e47" stroke-width="1.6"/>' +
  '<rect x="8" y="8" width="8" height="8" rx="1.6" fill="#2b2f37"/><path d="M8 11h8M8 13.5h8" stroke="#454a55" stroke-width=".8"/>' +
  '<path class="fo-off" d="M8.5 16C8.5 20 3 23 3 30a9 9 0 0 0 18 0C21 23 15.5 20 15.5 16Z" fill="rgba(255,255,255,.05)" stroke="rgba(255,255,255,.34)" stroke-width="1"/>' +
  '<path class="fo-off" d="M10.5 16 9.5 30l1.5-4 1 4 1-4 1.5 4-1-14" fill="none" stroke="rgba(255,255,255,.3)" stroke-width=".8" stroke-linejoin="round"/>' +
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

const stopAll = (list) => list.forEach((x) => { try { x.stop(); } catch (e) {} });

/* dónde cuelga cada foco dentro de una sección de alto H */
function plan(H) {
  const top = 70;
  const usable = H - top - 150;
  const n = Math.max(1, Math.round(usable / 200) + 1);
  const S = n > 1 ? usable / (n - 1) : 0;
  const ys = [];
  for (let i = 0; i < n; i++) ys.push(Math.round(top + i * S));
  return { ys, S: S || 200 };
}

/* hasta dónde llega la luz con k focos prendidos */
function bound(s, k) {
  /* sin focos prendidos: si la sección de arriba sigue a oscuras, la penumbra empieza desde el borde */
  if (k <= 0) return s.soft ? 0 : -F;
  if (k >= s.ys.length) return s.H + 4;
  return Math.round(s.ys[k - 1] + HANG + 0.55 * s.S);
}
const tf = (b) => "translateY(" + b + "px)";
const ts = (s, b) => "scaleY(" + (Math.max(0, s.H - b - F) / BASE).toFixed(4) + ")";

/* arma (o rearma) la serie de una sección; H ya viene medido para no forzar al navegador a recalcular */
function mount(s, H) {
  if (s.el) { stopAll(s.va || []); s.bulbs.forEach((b) => stopAll(b.a)); s.el.remove(); }
  s.H = H;
  const p = plan(H);
  s.ys = p.ys; s.S = p.S;
  const el = (s.el = document.createElement("div"));
  el.className = "serie";
  el.setAttribute("aria-hidden", "true");
  /* cable: baja por la izquierda con una comba entre foco y foco, y un brazo corto a cada foco */
  let d = "M6,0", py = 0;
  s.ys.concat([H]).forEach((y) => { d += " Q0," + (py + y) / 2 + " 6," + y; py = y; });
  s.ys.forEach((y) => { d += " M6," + (y - 9) + " Q22," + (y - 9) + " 22," + y; });
  let html = reduce ? "" : '<div class="serie-v"><i class="ve-f"></i><i class="ve-s"></i></div>';
  const h = Math.ceil(H);
  html += '<svg class="serie-w" width="40" height="' + h + '" viewBox="0 0 40 ' + h + '"><path d="' + d + '" fill="none" stroke="#3a3e47" stroke-width="1.6"/></svg>';
  s.ys.forEach((y) => { html += '<span class="fo" style="top:' + y + 'px"><i class="fo-w"></i><i class="fo-g"></i>' + BULB + "</span>"; });
  el.innerHTML = html;
  s.sec.appendChild(el);
  s.vf = el.querySelector(".ve-f");
  s.vs = el.querySelector(".ve-s");
  s.va = [];
  s.bulbs = [].slice.call(el.querySelectorAll(".fo")).map((f) => ({
    on: f.querySelector(".fo-on"), glow: f.querySelector(".fo-g"), wash: f.querySelector(".fo-w"), lit: false, a: [],
  }));
  s.k = -1;
}

function setBulb(b, on, instant) {
  if (b.lit === on && !instant) return;
  b.lit = on;
  stopAll(b.a);
  b.a = [];
  if (instant) {
    b.on.style.opacity = b.glow.style.opacity = b.wash.style.opacity = on ? "1" : "0";
    return;
  }
  if (on) {
    b.a = calm
      ? [animate(b.on, { opacity: 1 }, { duration: 0.2 }), animate(b.glow, { opacity: 1 }, { duration: 0.2 }), animate(b.wash, { opacity: 1 }, { duration: 0.3 })]
      : [
          /* arranque de foco incandescente: chispazo, baja y se estabiliza */
          animate(b.on, { opacity: [null, 0.9, 0.3, 1] }, { duration: 0.5, times: [0, 0.2, 0.42, 1], ease: "linear" }),
          animate(b.glow, { opacity: [null, 0.9, 0.25, 1], transform: ["translate(-50%,-50%) scale(.6)", "translate(-50%,-50%) scale(1)"] }, { duration: 0.5, times: [0, 0.2, 0.42, 1], ease: "linear" }),
          /* la luz se abre hacia la derecha */
          animate(b.wash, { opacity: 1, transform: ["scaleX(.45)", "scaleX(1)"] }, { duration: 0.8, ease: OUT }),
        ];
  } else {
    /* apagar es más rápido que prender */
    b.a = [animate(b.on, { opacity: 0 }, { duration: 0.22, ease: OUT }), animate(b.glow, { opacity: 0 }, { duration: 0.22, ease: OUT }), animate(b.wash, { opacity: 0 }, { duration: 0.3, ease: OUT })];
  }
}

function apply(s, k, instant) {
  const soft = !s.prev || s.prev.k >= s.prev.bulbs.length;
  if (k === s.k && soft === s.soft && !instant) return;
  const up = k > s.k || (k === s.k && soft);
  s.k = k;
  s.soft = soft;
  const n = s.bulbs.length;
  for (let i = 0; i < n; i++) setBulb(s.bulbs[i], i < k, instant);
  s.sec.classList.toggle("lit", k === n);
  if (!s.vf) return;
  /* la penumbra: un degradado que se recorre y un bloque oscuro que se estira, siempre pegados */
  const b = bound(s, k);
  stopAll(s.va);
  s.va = [];
  if (instant || calm) {
    s.vf.style.transform = tf(b);
    s.vs.style.transform = ts(s, b);
    return;
  }
  const o = { duration: up ? 0.7 : 0.4, ease: OUT };
  s.va = [animate(s.vf, { transform: tf(b) }, o), animate(s.vs, { transform: ts(s, b) }, o)];
}

let series = [], vh = 0, queued = 0;

function tick() {
  const y = window.scrollY;
  for (const s of series) {
    let k = 0;
    while (k < s.trig.length && s.trig[k] <= y) k++;
    apply(s, k, s.fresh);
    s.fresh = false;
  }
}

function measure() {
  queued = 0;
  vh = window.innerHeight;
  const max = Math.max(0, document.documentElement.scrollHeight - vh);
  /* primero todas las lecturas, luego todos los cambios */
  const y0 = window.scrollY;
  const rects = series.map((s) => s.sec.getBoundingClientRect());
  series.forEach((s, i) => {
    const H = rects[i].height;
    if (Math.abs(H - s.H) > 24) { mount(s, H); s.fresh = true; }
    else if (Math.abs(H - s.H) > 0.2) { s.H = H; s.fresh = true; }
    const top = rects[i].top + y0;
    /* si la página se acaba antes de que el foco llegue a la línea, prende al tocar fondo */
    s.trig = s.ys.map((y) => Math.min(top + y + HANG - LINE * vh, max - 4));
  });
  tick();
}
const ask = () => { if (!queued) queued = requestAnimationFrame(measure); };

function init() {
  const secs = [].slice.call(document.querySelectorAll(SEL));
  if (!secs.length) return;
  defs();
  const hs = secs.map((sec) => sec.getBoundingClientRect().height);
  series = secs.map((sec, i) => { const s = { sec, fresh: true, soft: true }; mount(s, hs[i]); return s; });
  /* la serie de la sección pegada arriba, si la hay */
  series.forEach((s, i) => { const a = series[i - 1]; s.prev = a && a.sec.nextElementSibling === s.sec ? a : null; });
  document.documentElement.classList.add("has-serie");
  measure();
  try { scroll(() => tick()); } catch (e) { window.addEventListener("scroll", tick, { passive: true }); }
  window.addEventListener("resize", ask, { passive: true });
  window.addEventListener("load", ask);
  /* si cambia el alto de la página (una pregunta que se abre, una foto que carga), se vuelve a medir */
  if ("ResizeObserver" in window) new ResizeObserver(ask).observe(document.querySelector("main"));
}

if ("requestIdleCallback" in window) requestIdleCallback(init, { timeout: 1500 });
else setTimeout(init, 300);
