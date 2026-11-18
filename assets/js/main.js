(function(){
'use strict';
var $=function(s,c){return(c||document).querySelector(s)},$$=function(s,c){return[].slice.call((c||document).querySelectorAll(s))};
var mobile=window.matchMedia('(max-width:768px),(orientation:portrait)').matches;
var reduce=window.matchMedia('(prefers-reduced-motion:reduce)').matches;
/* header */
var hdr=$('.hdr');function hs(){hdr.classList.toggle('solid',window.scrollY>40)}hs();window.addEventListener('scroll',hs,{passive:true});
var b=$('.burger'),n=$('.nav');
if(b){b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)});$$('.nav a').forEach(function(a){a.addEventListener('click',function(){n.classList.remove('open')})})}
/* reveal */
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12});$$('.rv').forEach(function(el){io.observe(el)})}else{$$('.rv').forEach(function(el){el.classList.add('in')})}
/* videos: elegir version cel o escritorio */
$$('video[data-src]:not([data-scrub])').forEach(function(v){v.src=mobile&&v.dataset.srcM?v.dataset.srcM:v.dataset.src;if(v.dataset.posterM&&mobile)v.poster=v.dataset.posterM});
/* autoplay solo cuando se ve */
$$('video[data-auto]').forEach(function(v){
 if(reduce){v.removeAttribute('autoplay');return}
 if(!('IntersectionObserver' in window)){v.play();return}
 new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){var p=v.play();if(p&&p.catch)p.catch(function(){})}else v.pause()})},{threshold:.35}).observe(v);
});
/* scroll-scrub */
var sc=$('.scrub');if(!sc)return;
var v=$('video',sc),bar=$('.bar',sc),hint=$('.scroll-hint',sc),stages=$$('.stage',sc);
var target=0,cur=0,dur=0,ready=false;
var st=(sc.dataset.stops||'.3,.68').split(',').map(Number);
function setStage(p){var i=p<st[0]?0:p<st[1]?1:2;stages.forEach(function(s,k){s.classList.toggle('on',k===i)});if(hint)hint.style.opacity=p>.04?0:1;if(bar)bar.style.width=(p*100)+'%'}
function prog(){var r=sc.getBoundingClientRect(),h=sc.offsetHeight-window.innerHeight;return Math.min(1,Math.max(0,-r.top/h))}
function init(){dur=v.duration||0;ready=dur>0;if(reduce&&ready){v.currentTime=dur-.05;setStage(1);return}tick()}
function tick(){
 var p=prog();setStage(p);
 if(ready){target=p*(dur-.05);cur+=(target-cur)*.18;if(Math.abs(cur-v.currentTime)>.012){try{v.currentTime=cur}catch(e){}}}
 requestAnimationFrame(tick)
}
if(mobile&&v.dataset.posterM)v.poster=v.dataset.posterM;
v.src=mobile?v.dataset.srcM:v.dataset.src;v.muted=true;v.playsInline=true;v.setAttribute('playsinline','');v.preload='auto';
v.addEventListener('loadedmetadata',init);
/* iOS: despertar el decodificador */
var wake=function(){var p=v.play();if(p&&p.then)p.then(function(){v.pause()}).catch(function(){});window.removeEventListener('touchstart',wake);window.removeEventListener('scroll',wake)};
window.addEventListener('touchstart',wake,{passive:true,once:true});window.addEventListener('scroll',wake,{passive:true,once:true});
v.load();
if(v.readyState>=1)init();
setStage(0);
})();
