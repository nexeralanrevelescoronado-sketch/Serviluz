(function(){
'use strict';
var $=function(s,c){return(c||document).querySelector(s)},$$=function(s,c){return[].slice.call((c||document).querySelectorAll(s))};
var mobile=window.matchMedia('(max-width:768px),(orientation:portrait)').matches;
var reduce=window.matchMedia('(prefers-reduced-motion:reduce)').matches;
var lite=(navigator.hardwareConcurrency&&navigator.hardwareConcurrency<=2)||(navigator.deviceMemory&&navigator.deviceMemory<=2);
var hasIO='IntersectionObserver' in window;

/* header */
var hdr=$('.hdr');
function hs(){hdr.classList.toggle('solid',window.scrollY>40)}hs();
window.addEventListener('scroll',hs,{passive:true});
var b=$('.burger'),n=$('.nav');
function menu(open){n.classList.toggle('open',open);b.setAttribute('aria-expanded',open);b.setAttribute('aria-label',open?'Cerrar menú':'Abrir menú')}
if(b){
 b.addEventListener('click',function(){menu(!n.classList.contains('open'))});
 $$('.nav a').forEach(function(a){a.addEventListener('click',function(){menu(false)})});
 document.addEventListener('keydown',function(e){if(e.key==='Escape')menu(false)});
}

/* aparecer al bajar (solo opacity/transform) */
if(hasIO){
 var D=[0,60,110,150,180];
 var io=new IntersectionObserver(function(es){var k=0;es.forEach(function(e){if(!e.isIntersecting)return;var el=e.target;io.unobserve(el);
  if(!reduce){el.style.transitionDelay=D[Math.min(k++,4)]+'ms';el.addEventListener('transitionend',function f(ev){if(ev.propertyName!=='transform')return;el.style.transitionDelay='';el.classList.add('done');el.removeEventListener('transitionend',f)})}else el.classList.add('done');
  el.classList.add('in')})},{threshold:.12});
 $$('.rv').forEach(function(el){io.observe(el)});
}else{$$('.rv').forEach(function(el){el.classList.add('in')})}

/* videos: version cel o escritorio */
$$('video[data-src]:not([data-scrub])').forEach(function(v){
 v.src=mobile&&v.dataset.srcM?v.dataset.srcM:v.dataset.src;
 if(mobile&&v.dataset.posterM)v.poster=v.dataset.posterM;
});

/* autoplay solo cuando se ve; sin movimiento -> cuadro fijo */
$$('video[data-auto]').forEach(function(v){
 if(reduce||lite){v.removeAttribute('autoplay');v.pause();return}
 if(!hasIO){var p0=v.play();if(p0&&p0.catch)p0.catch(function(){});return}
 new IntersectionObserver(function(es){es.forEach(function(e){
  if(e.isIntersecting){var p=v.play();if(p&&p.catch)p.catch(function(){})}else v.pause();
 })},{threshold:.35}).observe(v);
});

/* scroll-scrub */
var sc=$('.scrub');if(!sc)return;
var v=$('video',sc),bar=$('.bar',sc),hint=$('.scroll-hint',sc),stages=$$('.stage',sc),pic=$('.posterimg',sc);
var st=(sc.dataset.stops||'.3,.68').split(',').map(Number);
var target=0,cur=0,dur=0,ready=false,visible=true,raf=0,lastStage=-1;

var lastHint=-1,lastP=-1,span=0;
function measure(){span=sc.offsetHeight-window.innerHeight}measure();
window.addEventListener('resize',measure,{passive:true});
function setStage(p){
 var i=p<st[0]?0:p<st[1]?1:2;
 if(i!==lastStage){stages.forEach(function(s,k){s.classList.toggle('on',k===i)});lastStage=i}
 var hv=p>.04?0:1;if(hint&&hv!==lastHint){hint.style.opacity=hv;lastHint=hv}
 if(bar&&Math.abs(p-lastP)>.001){bar.style.transform='scaleX('+p+')';lastP=p}
}
function prog(){var t=sc.getBoundingClientRect().top;return span>0?Math.min(1,Math.max(0,-t/span)):0}

/* plan B: sin movimiento o equipo lento -> cuadro final fijo, textos por scroll */
if(reduce||lite){
 var img=$('img',pic);
 if(img&&img.dataset.end){var s0=$('source',pic);if(s0)s0.parentNode.removeChild(s0);img.src=mobile&&img.dataset.endM?img.dataset.endM:img.dataset.end}
 if(v&&v.parentNode)v.parentNode.removeChild(v);
 var loop=function(){setStage(prog())};
 window.addEventListener('scroll',loop,{passive:true});loop();
 return;
}

function tick(){
 raf=0;if(!visible)return;
 var p=prog();setStage(p);
 if(ready){
  target=p*(dur-.05);cur+=(target-cur)*.18;
  if(Math.abs(cur-v.currentTime)>.012){try{v.currentTime=cur}catch(e){}}
  /* ya llego al cuadro: se duerme hasta el siguiente scroll */
  if(Math.abs(target-cur)<.004)return;
 }
 raf=requestAnimationFrame(tick);
}
function start(){if(!raf&&visible)raf=requestAnimationFrame(tick)}
window.addEventListener('scroll',start,{passive:true});
function init(){dur=v.duration||0;ready=dur>0;start()}

/* corre solo mientras el hero esta en pantalla */
if(hasIO){
 new IntersectionObserver(function(es){visible=es[0].isIntersecting;if(visible)start()},{rootMargin:'200px 0px'}).observe(sc);
}

if(mobile&&v.dataset.posterM)v.poster=v.dataset.posterM;
v.src=mobile?v.dataset.srcM:v.dataset.src;
v.muted=true;v.playsInline=true;v.setAttribute('playsinline','');v.preload='auto';
v.addEventListener('loadedmetadata',init);
/* si el video falla, queda el cuadro fijo y los textos siguen funcionando */
v.addEventListener('error',function(){ready=false;start()});
/* iOS: despertar el decodificador con el primer toque o scroll */
var wake=function(){var p=v.play();if(p&&p.then)p.then(function(){v.pause()}).catch(function(){});window.removeEventListener('touchstart',wake);window.removeEventListener('scroll',wake)};
window.addEventListener('touchstart',wake,{passive:true,once:true});
window.addEventListener('scroll',wake,{passive:true,once:true});
v.load();
setStage(0);start();
})();
