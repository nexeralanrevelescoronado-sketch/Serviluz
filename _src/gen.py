import json, os
OUT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE='https://serviluz.com.mx'
TEL='3328272152'; TELF='33 2827 2152'
WA='https://wa.me/52'+TEL+'?text='
def wa(t): return WA+t.replace(' ','%20')

# ---------- Íconos (estilo Lucide, SVG en línea, sin emojis)
_P={
'phone':'<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
'chat':'<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22z"/>',
'zap':'<path d="M13 2 3 14h9l-1 8 10-12h-9z"/>',
'plug':'<path d="M12 22v-5"/><path d="M9 8V2"/><path d="M15 8V2"/><path d="M18 8v5a4 4 0 0 1-4 4h-4a4 4 0 0 1-4-4V8z"/>',
'house':'<path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .71-1.53l7-6a2 2 0 0 1 2.58 0l7 6A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
'store':'<path d="m2 7 4.4-4.4A2 2 0 0 1 7.8 2h8.4a2 2 0 0 1 1.4.6L22 7"/><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"/><path d="M2 7h20v3a2 2 0 0 1-2 2 3 3 0 0 1-2-.8 3 3 0 0 1-4 0 3 3 0 0 1-4 0 3 3 0 0 1-4 0A3 3 0 0 1 4 12a2 2 0 0 1-2-2z"/>',
'factory':'<path d="M2 20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8l-7 5V8l-7 5V4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2z"/><path d="M17 18h1"/><path d="M12 18h1"/><path d="M7 18h1"/>',
'utensils':'<path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 0 0 2-2V2"/><path d="M7 2v20"/><path d="M21 15V2a5 5 0 0 0-5 5v6c0 1.1.9 2 2 2h3zm0 0v7"/>',
'cable':'<path d="M3 8c5 0 4 8 9 8s4-8 9-8"/><circle cx="3" cy="8" r="1.5"/><circle cx="21" cy="8" r="1.5"/><path d="M3 18h18"/>',
'sliders':'<path d="M4 21v-7M4 10V3M12 21v-9M12 8V3M20 21v-5M20 12V3M2 14h4M10 8h4M18 16h4"/>',
'toggle':'<rect width="20" height="12" x="2" y="6" rx="6"/><circle cx="16" cy="12" r="2.5"/>',
'bulb':'<path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/>',
'wrench':'<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94z"/>',
'ground':'<path d="M12 2v11"/><path d="M5 13h14"/><path d="M8 17h8"/><path d="M10.5 21h3"/>',
'ruler':'<path d="M21.3 15.3a2.4 2.4 0 0 1 0 3.4l-2.6 2.6a2.4 2.4 0 0 1-3.4 0L2.7 8.7a2.4 2.4 0 0 1 0-3.4l2.6-2.6a2.4 2.4 0 0 1 3.4 0z"/><path d="m14.5 12.5 2-2"/><path d="m11.5 9.5 2-2"/><path d="m8.5 6.5 2-2"/><path d="m17.5 15.5 2-2"/>',
'pot':'<path d="M2 12h20"/><path d="M20 12v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2v-8"/><path d="m4 8 16-4"/><path d="m8.9 6.8-.4-1.8a2 2 0 0 1 1.4-2.4l1.9-.5a2 2 0 0 1 2.4 1.5l.5 1.8"/>',
'snow':'<path d="M12 2v20"/><path d="m4.9 7 14.2 10"/><path d="M4.9 17 19.1 7"/><path d="m9 3.5 3 2.5 3-2.5"/><path d="m9 20.5 3-2.5 3 2.5"/>',
'hardhat':'<path d="M10 10V5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v5"/><path d="M14 6a6 6 0 0 1 6 6v3"/><path d="M4 15v-3a6 6 0 0 1 6-6"/><rect x="2" y="15" width="20" height="4" rx="1"/>',
'scale':'<path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1z"/><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1z"/><path d="M7 21h10"/><path d="M12 3v18"/><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"/>',
'menu':'<path d="M4 6h16M4 12h16M4 18h16"/>',
'close':'<path d="M18 6 6 18M6 6l12 12"/>',
}
def I(n,s=20):
    c=' i-close' if n=='close' else (' i-menu' if n=='menu' else '')
    return f'<svg class="i{c}" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{_P[n]}</svg>'
_IG='<svg class="i" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>'
_TT='<svg class="i" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><path d="M16.6 3h-3.2v12.4a2.8 2.8 0 1 1-2.8-2.8c.3 0 .6 0 .8.1V9.4a6 6 0 1 0 5.2 5.9V9a7.6 7.6 0 0 0 4.4 1.4V7.2A4.4 4.4 0 0 1 16.6 3z"/></svg>'
IG_URL='https://www.instagram.com/servi_luz_soluciones?dmpr=b2xkZHRqZTgyNGZh'
TT_URL='https://www.tiktok.com/@mst.conejo?_r=1&amp;_t=ZS-9Bcwegzz9Hh'
def social(cls=''):
    return (f'<div class="soc{cls}"><a class="ig" href="{IG_URL}" target="_blank" rel="noopener me" aria-label="Instagram de Serví luz" title="Instagram">{_IG}<span>Instagram</span></a>'
            f'<a class="tt" href="{TT_URL}" target="_blank" rel="noopener me" aria-label="TikTok de Serví luz" title="TikTok">{_TT}<span>TikTok</span></a></div>')
ZONAS=['Guadalajara','Zapopan','Tonalá','Tlaquepaque']


# ---------- BLOG (articulos en _src/blog/*.md)
import re, html, glob
MESES=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
def fdate(s):
    y,m,d=map(int,s.split('-')); return f'{d} de {MESES[m-1]} de {y}'
def md_inline(t):
    t=html.escape(t,quote=False)
    t=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',t)
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',t)
def md_body(txt):
    out=[]; para=[]; lst=None
    def flush():
        nonlocal para,lst
        if para: out.append('<p>'+md_inline(' '.join(para))+'</p>'); para=[]
        if lst: out.append('</'+lst+'>'); lst=None
    for ln in txt.split('\n'):
        ln=ln.rstrip()
        if not ln.strip(): flush(); continue
        if ln.startswith('## '): flush(); out.append('<h2>'+md_inline(ln[3:])+'</h2>'); continue
        if ln.startswith('### '): flush(); out.append('<h3>'+md_inline(ln[4:])+'</h3>'); continue
        m=re.match(r'^(- |\d+\. )(.*)$',ln)
        if m:
            kind='ul class="checks"' if m.group(1)=='- ' else 'ol'
            tag=kind.split()[0]
            if para: out.append('<p>'+md_inline(' '.join(para))+'</p>'); para=[]
            if lst and lst!=tag: out.append('</'+lst+'>'); lst=None
            if not lst: out.append('<'+kind+'>'); lst=tag
            out.append('<li><span>'+md_inline(m.group(2))+'</span></li>' if tag=='ul' else '<li>'+md_inline(m.group(2))+'</li>'); continue
        if lst: out.append('</'+lst+'>'); lst=None
        para.append(ln.strip())
    flush(); return '\n'.join(out)
def load_posts():
    posts=[]
    for f in sorted(glob.glob(os.path.join(OUT,'_src','blog','*.md'))):
        raw=open(f,encoding='utf-8').read()
        m=re.match(r'^---\n(.*?)\n---\n(.*)$',raw,re.S)
        if not m: raise SystemExit('Sin front matter: '+f)
        meta={}
        for ln in m.group(1).split('\n'):
            if ':' in ln: k,v=ln.split(':',1); meta[k.strip()]=v.strip()
        for k in ('slug','title','desc','date','cat','img','alt'):
            if k not in meta: raise SystemExit(f'Falta {k} en {f}')
        body=m.group(2).strip(); faq=[]
        if '\n## Preguntas frecuentes' in '\n'+body:
            body,_,fq=('\n'+body).partition('\n## Preguntas frecuentes')
            body=body.strip(); q=None
            for ln in fq.strip().split('\n'):
                if ln.startswith('### '): q=[ln[4:].strip(),[]]; faq.append(q)
                elif q and ln.strip(): q[1].append(ln.strip())
            faq=[(a,' '.join(b)) for a,b in faq]
        meta['body']=body; meta['faq']=faq
        meta['words']=len(re.findall(r'\w+',body)); meta['min']=max(2,round(meta['words']/200))
        meta['path']='/blog/'+meta['slug']+'/'
        posts.append(meta)
    posts.sort(key=lambda x:(x['date'],x['slug']),reverse=True)
    return posts
POSTS=load_posts()
def post_card(p):
    return f'<a class="card post rv" href="{p["path"]}"><div><span class="eyebrow">{p["cat"]}</span><h3>{p["title"]}</h3><p>{p["desc"]}</p></div><span class="more">Leer · {p["min"]} min →</span></a>'

# ---------- Galería "Nuestro trabajo" (agregar fotos nuevas a esta lista: archivo en assets/img, ancho y alto)
GALERIA=[('trabajo-tablero-abb','Tablero eléctrico con interruptor termomagnético trifásico y cables ordenados dentro de gabinete metálico',1179,1571,'Tablero con protección trifásica')]
def galeria():
    figs=''.join(f'<figure class="gal-i rv"><img src="/assets/img/{n}.webp" srcset="/assets/img/{n}-m.webp 640w, /assets/img/{n}.webp {w}w" sizes="(max-width:768px) 90vw, 360px" alt="{a}" width="{w}" height="{h}" loading="lazy" decoding="async"><figcaption>{I("zap",14)} {c}</figcaption></figure>' for n,a,w,h,c in GALERIA)
    return f'<section id="trabajo"><div class="wrap"><span class="eyebrow rv">Nuestro trabajo</span><h2 class="rv">Instalaciones reales, hechas con orden</h2><p class="lead rv">Fotos de trabajos de Serví luz. Cada conexión identificada, cada cable en su lugar.</p><div class="gal">{figs}</div></div></section>\n'
def blog_teaser():
    if not POSTS: return ''
    return '<section><div class="wrap"><span class="eyebrow rv">Blog</span><h2 class="rv">Consejos de electricistas para tu casa y tu negocio</h2><div class="grid g3">'+''.join(post_card(p) for p in POSTS[:3])+'</div><p class="rv" style="margin-top:22px"><a class="btn btn-ghost" href="/blog/">Ver todos los artículos</a></p></div></section>\n'

def jsonld(extra=None):
    d={"@context":"https://schema.org","@type":"Electrician","name":"Serví luz","@id":BASE+"/#negocio","url":BASE+"/","telephone":"+52"+TEL,"address":{"@type":"PostalAddress","addressLocality":"Guadalajara","addressRegion":"Jalisco","addressCountry":"MX"},
       "image":BASE+"/assets/img/og.jpg","logo":BASE+"/assets/img/icon-512.png",
       "description":"Servicio express con 7 años de experiencia. Electricistas en Guadalajara, Zapopan, Tonalá, Tlaquepaque y todo Jalisco: instalaciones eléctricas residenciales, comerciales, para restaurantes e industriales.",
       "priceRange":"$$",
       "areaServed":[{"@type":"City","name":z} for z in ZONAS]+[{"@type":"AdministrativeArea","name":"Jalisco"}],
       "knowsAbout":["Instalaciones eléctricas","Diseño eléctrico","Tableros eléctricos","Corto circuito","Iluminación LED","Tierras físicas"],
       "contactPoint":{"@type":"ContactPoint","telephone":"+52"+TEL,"contactType":"customer service","availableLanguage":"es"}}
    d.pop("priceRange")
    out=[d,{"@context":"https://schema.org","@type":"WebSite","name":"Serví luz","url":BASE+"/","inLanguage":"es-MX","publisher":{"@id":BASE+"/#negocio"}}]
    if extra: out+=extra
    return '\n'.join('<script type="application/ld+json">'+json.dumps(x,ensure_ascii=False)+'</script>' for x in out)

NAV=[('index.html','Inicio','/'),('restaurantes.html','Restaurantes','/restaurantes/'),('residencias.html','Casas','/residencias/'),('industrial.html','Industrial','/industrial/'),('blog.html','Blog','/blog/')]
def header(cur):
    items=''.join('<a href="%s"%s>%s</a>'%(p,' aria-current="page"' if cur==h else '',t) for h,t,p in NAV)
    return f'''<a class="skip" href="#contenido">Saltar al contenido</a><header class="hdr"><div class="wrap"><div class="brand"><a class="logo" href="/" aria-label="Serví luz, inicio"><img src="/assets/img/logo.webp" alt="Serví luz" width="185" height="38"></a>{social()}</div>
<nav class="nav" id="nav" aria-label="Principal">{items}<a href="#contacto">Contacto</a><a class="call" href="tel:+52{TEL}">Llamar {TELF}</a></nav>
<button class="burger" aria-label="Abrir menú" aria-expanded="false" aria-controls="nav">{I('menu',22)}{I('close',22)}</button></div></header>'''

def footer():
    return f'''<footer><div class="wrap"><div class="cols"><div><img src="/assets/img/logo.webp" alt="Serví luz" width="204" height="42"><p style="margin-top:14px;max-width:34ch">Electricistas en Guadalajara, Zapopan, Tonalá, Tlaquepaque y todo Jalisco. Casas, restaurantes, negocios e industria.</p></div>
<div><p class="fh">Servicios</p><ul><li><a href="/restaurantes/">Electricista para restaurantes</a></li><li><a href="/residencias/">Casas y residencias</a></li><li><a href="/industrial/">Industrial y negocios</a></li><li><a href="/blog/">Blog de consejos eléctricos</a></li></ul></div>
<div><p class="fh">Contacto</p><ul><li><a href="tel:+52{TEL}">{I('phone')} {TELF}</a></li><li><a href="{wa('Hola Serví luz, necesito un electricista')}" rel="noopener">{I('chat')} WhatsApp</a></li><li>Todo Jalisco</li></ul>{social(' soc-f')}</div></div>
<p class="legal">© <span id="y">2026</span> Serví luz. Servicios eléctricos en Jalisco.</p></div></footer>
<div class="fab"><a class="c" href="tel:+52{TEL}" aria-label="Llamar">{I('phone')}</a><a class="w" href="{wa('Hola Serví luz, necesito un electricista')}" aria-label="WhatsApp" rel="noopener">{I('chat')}</a></div>
<script src="/assets/js/main.js" defer></script>
<script src="/assets/js/focos.js" defer></script>
<script>document.getElementById('y').textContent=new Date().getFullYear()</script>'''


def mo_head(ids):
    if not ids: return ''
    pre=''.join(f'<link rel="modulepreload" href="/assets/moments/{i}/moment.js">' for i in ids)
    return ('<meta name="site-kind" content="other"><meta name="page-type" content="service">'
     '<script>document.documentElement.classList.add(\'mo-js\');setTimeout(function(){document.documentElement.classList.add(\'mo-safe\')},2500)</script>'
     '<link rel="modulepreload" href="/assets/moments/moments.js"><link rel="modulepreload" href="/assets/moments/lib.js">'+pre)
MO_TAIL='<script type="module" src="/assets/moments/moments.js"></script>\n</body></html>'
def pic(n,alt,w=1280,h=720,mw=720):
    return f'<img src="/assets/img/{n}.webp" srcset="/assets/img/{n}-m.webp {mw}w, /assets/img/{n}.webp {w}w" sizes="(max-width:768px) 100vw, 1180px" alt="{alt}" width="{w}" height="{h}" loading="lazy" decoding="async">'
CAPS=[('cap-falla','Se fue la luz','Se botaron las pastillas o algo huele a quemado. Nos escribes y salimos de inmediato.','Manos con guantes revisando una caja de conexiones en una cocina a oscuras'),
('cap-tablero','Encontramos el origen','Revisamos el tablero circuito por circuito hasta dar con la falla, sin adivinar.','Manos con guantes revisando las pastillas de un tablero eléctrico'),
('cap-prueba','Probamos todo','Antes de irnos medimos y probamos cada circuito. Luz verde o no nos vamos.','Tablero eléctrico terminado con el indicador en verde'),
('cap-luz','La luz regresa','Tu casa o tu negocio funcionando otra vez, seguro y sin sustos.','Cocina de restaurante iluminada después de la reparación eléctrica')]
HISTORIA='<section data-moment="photo-chapters" aria-labelledby="hist-h"><div class="wrap mo-ph"><div class="mo-ph__head"><span class="eyebrow">Así se vive</span><h2 id="hist-h">De la falla <span class="amber">a la luz</span></h2><p>Lo que pasa desde que nos escribes hasta que todo vuelve a prender.</p></div><ol class="mo-ph__list">'+''.join(f'<li class="mo-ph__ch"><figure class="mo-ph__pic">{pic(n,alt)}</figure><h3>{t}</h3><p>{d}</p></li>' for n,t,d,alt in CAPS)+'</ol></div></section>'
def develop(eyebrow,h2,p,n,alt,msg):
    return f'<section class="nofo"><div class="wrap split"><div><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2><p>{p}</p><div class="btns"><a class="btn btn-primary" href="{wa(msg)}" rel="noopener">{I('chat')} Escríbenos</a></div></div><figure class="develop" data-moment="picture-develops">{pic(n,alt,1440,810,800)}</figure></div></section>\n'

def head(title,desc,path,extra_ld=None,og='/assets/img/og.jpg',pre='',mo=()):
    return f'''<!doctype html>
<html lang="es-MX"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}{path}">
<meta name="theme-color" content="#0a0b0d">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="icon" href="/assets/img/favicon-48.png" type="image/png" sizes="48x48"><link rel="icon" href="/assets/img/icon-192.png" type="image/png" sizes="192x192"><link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<meta property="og:type" content="website"><meta property="og:locale" content="es_MX"><meta property="og:site_name" content="Serví luz">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{BASE}{path}"><meta property="og:image" content="{BASE}{og}">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Serví luz, electricistas en Guadalajara y todo Jalisco">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="{BASE}{og}">
<link rel="alternate" hreflang="es-MX" href="{BASE}{path}"><meta name="format-detection" content="telephone=yes">
{pre}<link rel="stylesheet" href="/assets/css/styles.css">
{mo_head(mo)}
{jsonld(extra_ld)}
</head><body>
'''

FACTS='''<section style="padding:46px 0"><div class="wrap"><div class="facts"><div class="fact rv"><b>7 años</b><span>de experiencia en instalaciones eléctricas</span></div><div class="fact rv"><b>Express</b><span>Te atendemos de inmediato, sin tiempo de espera</span></div><div class="fact rv"><b>$300</b><span>costo de la visita</span></div></div></div></section>'''
def cta(msg):
    return f'''<section id="contacto"><div class="wrap"><div class="cta rv"><span class="eyebrow">Contacto</span><h2>¿Tienes una falla o un proyecto eléctrico?</h2><p>Servicio express: te atendemos de inmediato. Escríbenos por WhatsApp o llámanos, cuéntanos qué necesitas y mándanos fotos si puedes. La visita cuesta $300. Atendemos Guadalajara, Zapopan, Tonalá, Tlaquepaque y todo Jalisco.</p>
<div class="btns"><a class="btn btn-wa" href="{wa(msg)}" rel="noopener">{I('chat')} WhatsApp {TELF}</a><a class="btn btn-primary" href="tel:+52{TEL}">{I('phone')} Llamar ahora</a></div></div></div></section>'''

SERV=[(I('plug'),'Electricista a domicilio','Revisamos y resolvemos fallas eléctricas en tu casa o negocio.'),
(I('house'),'Instalaciones residenciales','Casas, departamentos y residencias: instalación nueva o renovación completa.'),
(I('store'),'Instalaciones comerciales','Locales, oficinas, consultorios y plazas con la carga bien repartida.'),
(I('factory'),'Instalaciones industriales','Naves, bodegas y talleres: potencia, tableros y alimentación de maquinaria.'),
(I('utensils'),'Diseño eléctrico para restaurantes','Cálculo de cargas y distribución para cocina, refrigeración y comedor.'),
(I('zap'),'Corto circuito y fallas','Pastillas que se botan, olor a quemado, luz que parpadea: lo diagnosticamos.'),
(I('cable'),'Cableado y centros de carga','Cambio de cableado viejo y centros de carga nuevos y seguros.'),
(I('sliders'),'Tableros eléctricos','Armado, ampliación y orden de tableros y pastillas.'),
(I('toggle'),'Contactos y apagadores','Instalación, cambio y reubicación de contactos, apagadores y salidas.'),
(I('bulb'),'Iluminación LED','Luz funcional y decorativa para interiores, fachadas y áreas de trabajo.'),
(I('wrench'),'Mantenimiento preventivo','Detectamos sobrecargas y puntos calientes antes de que paren tu operación.'),
(I('ground'),'Tierras físicas y protección','Sistemas de tierra y protección contra descargas.')]
def serv_grid():
    return '<div class="grid g4">'+''.join(f'<div class="card rv"><div class="ic">{i}</div><h3>{t}</h3><p>{d}</p></div>' for i,t,d in SERV)+'</div>'

ZB={'Guadalajara':'Casas, restaurantes, comercios y oficinas de toda la ciudad, de colonias nuevas a construcciones con décadas de instalación.',
'Zapopan':'Fraccionamientos, torres, corporativos y plazas: instalaciones calculadas para zonas que crecen rápido.',
'Tonalá':'Talleres, bodegas, comercios y casas: instalaciones que aguantan el trabajo diario.',
'Tlaquepaque':'Fincas, galerías, restaurantes y negocios turísticos: renovación de cableado viejo y diseño eléctrico.'}
def zonas():
    return '<div class="grid g4">'+''.join(f'<a class="card zone rv" href="{wa("Hola Serví luz, necesito electricista en "+z)}" rel="noopener"><h3>{z}</h3><p>{ZB[z]}</p></a>' for z in ZONAS)+'</div><p class="rv" style="margin-top:22px">¿Estás en otro municipio? También vamos: <strong>cubrimos todo Jalisco</strong>.</p>'

FAQ=[('¿Atienden fuera de Guadalajara?','Sí. Nuestra base fuerte es Guadalajara, Zapopan, Tonalá y Tlaquepaque, pero damos servicio en todo Jalisco. Escríbenos tu municipio por WhatsApp.'),
('¿Cuánto cuesta un electricista?','La visita tiene un costo de $300. El trabajo se cotiza según la falla o el proyecto; mándanos fotos y una descripción por WhatsApp y te orientamos.'),
('¿Qué tan rápido atienden?','Damos servicio express: te atendemos de inmediato, sin tiempo de espera. Escríbenos o llámanos al 33 2827 2152.'),
('¿Hacen instalaciones para restaurantes y negocios?','Sí. Hacemos diseño y distribución eléctrica para cocinas, refrigeración, comedor, locales, oficinas, bodegas e industria.'),
('¿Qué hago si se botan las pastillas o huele a quemado?','Desconecta lo que tengas prendido, evita seguir usando ese circuito y llámanos o escríbenos. Revisamos el origen del corto circuito.'),
('¿Reparan cableado viejo?','Sí. Cambiamos cableado antiguo o dañado, centros de carga y tableros para que la instalación quede segura.')]
def faq():
    return ''.join(f'<details class="rv"><summary>{q}</summary><p>{a}</p></details>' for q,a in FAQ)
def faq_ld():
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]}

# ---------- HOME
home=head('Electricista en Guadalajara, Zapopan y Tlaquepaque | Serví luz',
 'Electricistas en Guadalajara y todo Jalisco con 7 años de experiencia. Servicio express para casas, restaurantes y negocios. WhatsApp 33 2827 2152.','/',[faq_ld()],mo=('photo-chapters',),pre='<link rel="preload" as="image" href="/assets/img/foco-poster.webp" media="(min-width:769px) and (orientation:landscape)" fetchpriority="high"><link rel="preload" as="image" href="/assets/img/foco-poster-m.webp" media="(max-width:768px),(orientation:portrait)" fetchpriority="high">')
home+=header('index.html')+f'''<main id="contenido">
<section class="scrub" aria-label="Serví luz, electricistas en Jalisco"><div class="stick">
<picture class="posterimg"><source media="(max-width:768px),(orientation:portrait)" srcset="/assets/img/foco-poster-m.webp"><img src="/assets/img/foco-poster.webp" data-end="/assets/img/foco-end.webp" data-end-m="/assets/img/foco-end-m.webp" alt="" width="1280" height="720" fetchpriority="high" decoding="async"></picture>
<video data-src="/assets/video/foco-scroll.mp4" data-src-m="/assets/video/foco-scroll-m.mp4" data-poster-m="/assets/img/foco-poster-m.webp" data-scrub muted playsinline preload="auto" aria-hidden="true"></video>
<div class="shade"></div><div class="bar"></div>
<div class="stage s1 on"><div class="wrap"><span class="eyebrow">Electricistas en Jalisco</span><h1>Cuando la luz falla, <span class="amber">nosotros la prendemos.</span></h1><p>Servicio express: te atendemos de inmediato. Electricistas en Guadalajara, Zapopan, Tonalá, Tlaquepaque y todo Jalisco.</p>
<div class="btns"><a class="btn btn-primary" href="{wa('Hola Serví luz, necesito un electricista')}" rel="noopener">{I('chat')} Cotiza por WhatsApp</a><a class="btn btn-ghost" href="tel:+52{TEL}">{I('phone')} {TELF}</a></div></div></div>
<div class="stage"><div class="wrap"><span class="eyebrow">01 · Conexión bien hecha</span><h2>Cada empalme, <span class="amber">como debe ser.</span></h2><p>Cableado, empalmes y cajas de conexión con orden y seguridad. Nada de parches.</p></div></div>
<div class="stage"><div class="wrap"><span class="eyebrow">02 · Resultado</span><h2>Luz estable. <span class="amber">Tranquilidad total.</span></h2><p>Instalaciones eléctricas para tu casa, tu restaurante o tu industria.</p>
<div class="btns"><a class="btn btn-primary" href="#especialidades">Ver especialidades</a><a class="btn btn-wa" href="{wa('Hola Serví luz, necesito un electricista')}" rel="noopener">{I('chat')} WhatsApp</a></div></div></div>
<div class="scroll-hint"><span>Desliza</span><i></i></div>
</div></section>
<div class="strip" aria-hidden="true"><div class="row">{''.join('<span><b>'+I('zap',14)+'</b>'+t+'</span>' for t in (['Guadalajara','Zapopan','Tonalá','Tlaquepaque','Todo Jalisco']*4))}</div></div>

{FACTS}
<section id="especialidades"><div class="wrap"><span class="eyebrow rv">Especialidades</span><h2 class="rv">Una solución eléctrica para cada tipo de lugar</h2>
<div class="grid g3">
<a class="card big rv" href="/restaurantes/"><div><div class="ic">{I('utensils')}</div><h3>Restaurantes</h3><p>Diseño eléctrico y distribución de cargas para cocinas, refrigeración y comedor.</p></div><span class="more">Ver más →</span></a>
<a class="card big rv" href="/residencias/"><div><div class="ic">{I('house')}</div><h3>Casas y residencias</h3><p>Fallas, cableado viejo, centros de carga, contactos y obra nueva.</p></div><span class="more">Ver más →</span></a>
<a class="card big rv" href="/industrial/"><div><div class="ic">{I('factory')}</div><h3>Industrial y negocios</h3><p>Bodegas, naves, talleres y oficinas: tableros, potencia y mantenimiento.</p></div><span class="more">Ver más →</span></a>
</div></div></section>

<section style="background:var(--panel)"><div class="wrap split">
<div class="rv"><span class="eyebrow">Así trabajamos</span><h2>Tablero ordenado, <span class="amber">luz verde.</span></h2><p>Un tablero eléctrico bien armado se nota: cables identificados, pastillas en su lugar y carga repartida. Así dejamos cada instalación.</p>
<ul class="checks"><li>Cables ordenados e identificados</li><li>Pastillas y centros de carga correctos</li><li>Cálculo de cargas antes de conectar</li><li>Revisión final antes de entregar</li></ul>
<div class="btns"><a class="btn btn-primary" href="{wa('Hola Serví luz, quiero cotizar una instalación')}" rel="noopener">Cotizar mi instalación</a></div></div>
<div class="vid rv"><video data-src="/assets/video/tablero.mp4" data-src-m="/assets/video/tablero-m.mp4" data-poster-m="/assets/img/tablero-poster-m.webp" poster="/assets/img/tablero-poster.webp" data-auto autoplay muted loop playsinline preload="metadata" aria-label="Electricista armando un tablero eléctrico"></video><span class="live">EN OBRA</span></div>
</div></section>

<section><div class="wrap"><span class="eyebrow rv">Servicios</span><h2 class="rv">Todo lo eléctrico, en un solo lugar</h2>{serv_grid()}</div></section>

{HISTORIA}

<section style="background:var(--panel)"><div class="wrap"><span class="eyebrow rv">Zonas de servicio</span><h2 class="rv">Guadalajara, Zapopan, Tonalá, Tlaquepaque <span class="amber">y todo Jalisco</span></h2>{zonas()}</div></section>

<section><div class="wrap"><span class="eyebrow rv">Cómo funciona</span><h2 class="rv">Tres pasos y listo</h2>
<div class="grid g3 steps"><div class="step rv"><h3>Escríbenos</h3><p>Cuéntanos qué pasa por WhatsApp o llamada. Fotos ayudan mucho.</p></div><div class="step rv"><h3>Revisamos y cotizamos</h3><p>Diagnosticamos la falla o el proyecto y te damos una cotización clara.</p></div><div class="step rv"><h3>Resolvemos</h3><p>Hacemos el trabajo con orden y lo dejamos funcionando seguro.</p></div></div></div></section>

{galeria()}{blog_teaser()}<section style="background:var(--panel)"><div class="wrap" style="max-width:820px"><span class="eyebrow rv">Preguntas frecuentes</span><h2 class="rv">Lo que más nos preguntan</h2>{faq()}</div></section>
{cta('Hola Serví luz, necesito un electricista')}
</main>'''+footer()+'</body></html>'
home=home.replace('</body></html>',MO_TAIL)
open(OUT+'/index.html','w').write(home)

# ---------- SUBPAGES
def sub(fn,path,title,desc,h1,lead,img,crumb,items,body,extra_title,msg,video=False,scrub='',vid='',extra='',dev=''):
    bc={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Inicio","item":BASE+"/"},{"@type":"ListItem","position":2,"name":crumb,"item":BASE+path}]}
    s=head(title,desc,path,[bc],mo=('picture-develops',) if dev else (),pre='<link rel="preload" as="image" href="'+img+'" fetchpriority="high">')+header(fn)
    s+=f'''<main id="contenido"><section class="sub" style="--img:url({img})"><div class="wrap"><p class="crumb"><a href="/">Inicio</a> › {crumb}</p><span class="eyebrow">{extra_title}</span><h1>{h1}</h1><p class="lead">{lead}</p>
<div class="btns"><a class="btn btn-primary" href="{wa(msg)}" rel="noopener">{I('chat')} Cotiza por WhatsApp</a><a class="btn btn-ghost" href="tel:+52{TEL}">{I('phone')} {TELF}</a></div></div></section>
{scrub}<section><div class="wrap split"><div class="prose rv">{body}</div>
<div class="vid rv">{vid if vid else ('<video data-src="/assets/video/tablero.mp4" data-src-m="/assets/video/tablero-m.mp4" data-poster-m="/assets/img/tablero-poster-m.webp" poster="/assets/img/tablero-poster.webp" data-auto autoplay muted loop playsinline preload="metadata" aria-label="Instalación de tablero eléctrico"></video><span class="live">EN OBRA</span>') if video else ('<img src="/assets/img/foco-poster.webp" alt="Instalación eléctrica con foco encendido" loading="lazy" width="1280" height="720">')}</div></div></section>
{dev}{extra}<section style="background:var(--panel)"><div class="wrap"><span class="eyebrow rv">Qué hacemos</span><h2 class="rv">{extra_title}: servicios</h2><div class="grid g3">'''
    s+=''.join(f'<div class="card rv"><div class="ic">{i}</div><h3>{t}</h3><p>{d}</p></div>' for i,t,d in items)
    s+=f'''</div></div></section>
<section><div class="wrap"><span class="eyebrow rv">Zonas</span><h2 class="rv">Atendemos {', '.join(ZONAS[:-1])} y {ZONAS[-1]}, además de todo Jalisco</h2>{zonas()}</div></section>
{FACTS}
{cta(msg)}</main>'''+footer()+'</body></html>'
    if dev: s=s.replace('</body></html>',MO_TAIL)
    d=OUT+'/'+fn[:-5]; os.makedirs(d,exist_ok=True); open(d+'/index.html','w').write(s)

WA_REST=wa('Hola Serví luz, tengo un restaurante y necesito electricista')
def antes(h2,lead):
    return '''<section><div class="wrap split"><div class="rv"><span class="eyebrow">Antes y después</span><h2>'''+h2+'''</h2><p>'''+lead+'''</p><ul class="checks"><li>Cables fuera de lugar, ordenados y protegidos</li><li>Canaleta y ducto en todo el recorrido</li><li>Tablero con cubierta y circuitos identificados</li><li>Instalación terminada y probada con luz</li></ul><div class="btns"><a class="btn btn-primary" href="'''+WA_REST+'''" rel="noopener">Quiero mi instalación así</a></div></div>
<div class="vid tall rv"><video data-src="/assets/video/antes-despues.mp4" poster="/assets/img/antes-despues-poster.webp" data-auto autoplay muted loop playsinline preload="metadata" aria-label="Antes y después de una instalación eléctrica: de cables expuestos a instalación ordenada en canaleta"></video><span class="live">ANTES → DESPUÉS</span></div></div></section>'''
SCRUB_REST='''<section class="scrub tall" data-stops=".4,.7" aria-label="Instalación eléctrica en cocina de restaurante"><div class="stick">
<picture class="posterimg"><source media="(max-width:768px),(orientation:portrait)" srcset="/assets/img/restaurante-scroll-poster-m.webp"><img src="/assets/img/restaurante-scroll-poster.webp" data-end="/assets/img/restaurante-end.webp" data-end-m="/assets/img/restaurante-end-m.webp" alt="" width="960" height="540" loading="lazy" decoding="async"></picture>
<video data-src="/assets/video/restaurante-scroll.mp4" data-src-m="/assets/video/restaurante-scroll-m.mp4" data-scrub muted playsinline preload="metadata" aria-hidden="true"></video>
<div class="shade"></div><div class="bar"></div>
<div class="stage on"><div class="wrap"><span class="eyebrow">01 · Conexiones seguras</span><h2>Cada empalme, <span class="amber">bien hecho.</span></h2><p>En tu cocina no hay lugar para improvisar: conexiones firmes y cubiertas.</p></div></div>
<div class="stage"><div class="wrap"><span class="eyebrow">02 · Tablero ordenado</span><h2>Cables <span class="amber">ordenados y cinchados.</span></h2><p>Cada circuito identificado y cada cable en su lugar.</p></div></div>
<div class="stage"><div class="wrap"><span class="eyebrow">03 · Todo en verde</span><h2>Tu cocina, <span class="amber">lista para servir.</span></h2><p>Instalación terminada y probada antes de entregarla.</p>
<div class="btns"><a class="btn btn-wa" href="'''+WA_REST+'''" rel="noopener">'''+I('chat')+''' Cotiza por WhatsApp</a></div></div></div>
<div class="scroll-hint"><span>Desliza</span><i></i></div></div></section>'''
VID_CANALETA='''<video data-src="/assets/video/canaleta.mp4" data-src-m="/assets/video/canaleta-m.mp4" data-poster-m="/assets/img/canaleta-poster-m.webp" poster="/assets/img/canaleta-poster.webp" data-auto autoplay muted loop playsinline preload="metadata" aria-label="Electricista instalando canaleta de plástico para cubrir los cables"></video><span class="live">CERO CABLES EXPUESTOS</span>'''
sub('restaurantes.html','/restaurantes/','Electricista para Restaurantes en Guadalajara y Jalisco | Serví luz',
 'Diseño eléctrico y distribución de cargas para restaurantes, cafeterías, bares y cocinas industriales en Guadalajara, Zapopan, Tlaquepaque, Tonalá y Jalisco.',
 'Electricista para <span class="amber">restaurantes</span> en Guadalajara','Diseño eléctrico y distribución de cargas para que tu cocina no pare en pleno servicio.','/assets/img/restaurante-hero.webp','Restaurantes',
 [(I('ruler'),'Diseño eléctrico de cocina','Cálculo de cargas y distribución de circuitos desde cero o corrección de lo existente.'),(I('pot'),'Equipo de alto consumo','Circuitos para estufas, freidoras, hornos, campanas y máquinas de hielo.'),(I('snow'),'Refrigeración','Circuitos independientes para cámaras de refrigeración y congeladores.'),(I('sliders'),'Tableros y centros de carga','Instalación y ampliación para soportar tu operación completa.'),(I('bulb'),'Iluminación LED','Comedor, barra, fachada y cocina con la luz que cada área necesita.'),(I('wrench'),'Mantenimiento preventivo','Revisión periódica para evitar paros por fallas eléctricas.')],
 '''<h2>Un restaurante vive de que no se le vaya la luz</h2><p>Si se botan las pastillas en plena hora pico, pierdes ventas y clientes. En Serví luz hacemos el <strong>diseño eléctrico de tu cocina</strong> desde cero o corregimos la instalación que ya tienes: cálculo de cargas, distribución de circuitos, tableros, centros de carga y tierras físicas, pensados para equipo pesado como estufas, freidoras, hornos, campanas y cámaras de refrigeración.</p><p><strong>Instalación limpia, sin cables expuestos:</strong> dejamos el cableado ordenado, cinchado y protegido dentro de canaleta o ducto, con las cubiertas cerradas, para que tu cocina se vea profesional y segura.</p><ul class="checks"><li>Cables ordenados y cinchados</li><li>Canaleta de plástico y ducto en todo el recorrido</li><li>Tableros con cubierta y circuitos identificados</li><li>Trabajo con orden y limpieza, respetando tus horarios</li></ul><p style="margin-top:18px">Atendemos restaurantes, cafeterías, bares, taquerías y cocinas industriales en Guadalajara, Zapopan, Tlaquepaque, Tonalá y todo Jalisco.</p>''',
 'Restaurantes','Hola Serví luz, tengo un restaurante y necesito electricista',True,scrub=SCRUB_REST,vid=VID_CANALETA,extra=antes('De cables regados a una cocina <span class="amber">ordenada y segura</span>','Así transformamos la instalación de un restaurante: sin cables expuestos, con todo cinchado, en canaleta y con el tablero cerrado.'))

CASA_VIDEOS='''<section><div class="wrap"><span class="eyebrow rv">Iluminación en casa</span><h2 class="rv">Cuando la luz está bien instalada, <span class="amber">el hogar se siente distinto</span></h2><p class="rv" style="max-width:62ch">Lámparas, arbotantes y luz indirecta que prenden como deben. Si quieres algo así en tu sala, comedor o recámara, platícanos tu idea por WhatsApp.</p>
<div class="pair"><div class="vid land rv"><video data-src="/assets/video/casa-sala.mp4" poster="/assets/img/casa-sala-poster.webp" data-auto autoplay muted loop playsinline preload="metadata" aria-label="Sala y comedor de una casa que pasa de la oscuridad a estar iluminada con lámpara de techo, arbotantes y luz en el librero"></video><span class="live">SALA</span></div>
<div class="vid tall rv"><video data-src="/assets/video/casa-comedor.mp4" poster="/assets/img/casa-comedor-poster.webp" data-auto autoplay muted loop playsinline preload="metadata" aria-label="Comedor de doble altura que se ilumina con lámpara de techo, colgante, arbotantes y luz en el librero"></video><span class="live">COMEDOR</span></div></div>
<p class="rv" style="font-size:.85rem;opacity:.7;margin-top:14px">Videos ilustrativos de ambientes iluminados.</p></div></section>'''
sub('residencias.html','/residencias/','Electricista para Casas y Residencias en Guadalajara | Serví luz',
 'Electricista para casas, departamentos y residencias en Guadalajara, Zapopan, Tlaquepaque y Tonalá: corto circuito, cableado, centros de carga, contactos y LED.',
 'Electricista para <span class="amber">casas y residencias</span>','Desde la falla chiquita hasta la instalación completa de tu hogar, bien hecha y segura.','/assets/img/foco-poster.webp','Casas y residencias',
 [(I('zap'),'Corto circuito y fallas','Pastillas que se botan, olor a quemado, contactos que calientan, luz que parpadea.'),(I('cable'),'Cambio de cableado','Renovamos cableado viejo o peligroso en casas antiguas.'),(I('sliders'),'Centro de carga y pastillas','Instalación y cambio de centros de carga y pastillas.'),(I('toggle'),'Contactos y apagadores','Nuevos, cambiados o reubicados en cualquier parte de tu casa.'),(I('bulb'),'Lámparas, LED y ventiladores','Instalación de iluminación, ventiladores y minisplits.'),(I('hardhat'),'Obra nueva y remodelación','Cableado para construcción y remodelaciones, con constructoras y arquitectos.')],
 '''<h2>La luz de tu casa tiene que ser segura</h2><p>Se botan las pastillas, huele a quemado, hay corto circuito o los contactos calientan: no lo dejes para después. Revisamos, encontramos el origen del problema y lo arreglamos bien, <strong>no a medias</strong>.</p><p>Si tu casa es antigua, tiene muchos años con la misma instalación o le agregaste aparatos nuevos como minisplits, vale la pena una revisión eléctrica antes de que haya un susto. También trabajamos con constructoras, arquitectos y dueños que están levantando o remodelando su casa.</p><p>Servicio de electricista a domicilio en Guadalajara, Zapopan, Tlaquepaque, Tonalá y todo Jalisco.</p>''',
 'Casas y residencias','Hola Serví luz, necesito electricista para mi casa',extra=CASA_VIDEOS,dev=develop('Tu casa, tranquila','Prendes el switch <span class="amber">y todo funciona.</span>','Sin chispazos, sin olor a quemado, sin pastillas que se botan a media noche. Esa tranquilidad es lo que dejamos en cada casa.','dev-casa','Foco encendido sobre una pared de ladrillo con la conexión cubierta y terminada','Hola Serví luz, necesito electricista para mi casa'))

sub('industrial.html','/industrial/','Electricista Industrial y para Negocios en Jalisco | Serví luz',
 'Instalaciones y mantenimiento eléctrico industrial y comercial para bodegas, naves, talleres y oficinas en Guadalajara, Zapopan, Tlaquepaque, Tonalá y Jalisco.',
 'Electricista <span class="amber">industrial y para negocios</span>','Tableros, potencia y mantenimiento para que tu operación no se detenga.','/assets/img/tablero-poster.webp','Industrial y negocios',
 [(I('sliders'),'Tableros y centros de control','Armado, ampliación y ordenamiento de tableros eléctricos.'),(I('factory'),'Alimentación de maquinaria','Cableado de potencia y canalización para equipo industrial.'),(I('bulb'),'Iluminación industrial y LED','Naves, bodegas, talleres y oficinas bien iluminadas.'),(I('ground'),'Tierras físicas y protección','Sistemas de tierra y protección contra descargas.'),(I('scale'),'Balanceo de cargas','Repartimos la carga para evitar sobrecargas y disparos.'),(I('wrench'),'Mantenimiento preventivo y correctivo','Detectamos puntos calientes y falsos contactos a tiempo.')],
 '''<h2>En un negocio, una falla eléctrica es producción detenida</h2><p>Hacemos instalaciones y mantenimiento eléctrico industrial y comercial con orden, seguridad y buen acabado: <strong>tableros, canalización, cableado de potencia, alimentación de maquinaria, iluminación y tierras físicas</strong>.</p><p>Atendemos bodegas y naves industriales, talleres y fábricas, locales comerciales y plazas, oficinas, consultorios, escuelas y clínicas, además de obras nuevas y ampliaciones. Trabajamos por proyecto o por servicio, respetando tus tiempos.</p><p>Si necesitas diseño eléctrico, ampliar tu carga, instalar maquinaria nueva o corregir una instalación que ya no da abasto, platícanos tu caso.</p>''',
 'Industrial y negocios','Hola Serví luz, necesito servicio eléctrico industrial para mi negocio',True,dev=develop('Tu operación, en verde','Tablero en orden, <span class="amber">producción sin parar.</span>','Cada circuito identificado, cada carga en su lugar y todo probado antes de entregar. Para que tu negocio no se detenga por una falla eléctrica.','dev-tablero','Tablero eléctrico ordenado con todos los circuitos identificados y el indicador en verde','Hola Serví luz, necesito servicio eléctrico industrial para mi negocio'),extra=antes('De cables expuestos a una instalación <span class="amber">limpia y profesional</span>','Ordenamos y protegemos instalaciones de bodegas, talleres y negocios: sin cables regados, con canaleta, tableros cerrados y circuitos identificados.'))


# ---------- BLOG: indice, articulos, feed
RSS_LINK='<link rel="alternate" type="application/rss+xml" title="Blog de Serví luz" href="/blog/feed.xml">'
def blog_pages():
    d=OUT+'/blog'; os.makedirs(d,exist_ok=True)
    bc=lambda *it:{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":BASE+u} for i,(n,u) in enumerate(it)]}
    wam='Hola Serví luz, leí su blog y necesito un electricista'
    # indice
    desc='Consejos de electricistas para casas, restaurantes y negocios en Guadalajara y Jalisco: fallas, cableado, tableros, tierra física y seguridad eléctrica.'
    coll={"@context":"https://schema.org","@type":"Blog","name":"Blog de Serví luz","url":BASE+"/blog/","inLanguage":"es-MX","description":desc,
          "blogPost":[{"@type":"BlogPosting","headline":p['title'],"url":BASE+p['path'],"datePublished":p['date']} for p in POSTS]}
    s=head('Blog de electricistas en Guadalajara: consejos y guías | Serví luz',desc,'/blog/',[bc(('Inicio','/'),('Blog','/blog/')),coll],pre=RSS_LINK)+header('blog.html')
    s+=f'<main id="contenido"><section class="sub" style="--img:url(/assets/img/dev-tablero.webp)"><div class="wrap"><p class="crumb"><a href="/">Inicio</a> › Blog</p><span class="eyebrow">Blog</span><h1>Consejos de <span class="amber">electricistas</span> para tu casa y negocio</h1><p class="lead">Guías claras para entender tu instalación eléctrica, evitar sustos y saber cuándo llamar a un profesional en Guadalajara y todo Jalisco.</p></div></section>'
    s+='<section><div class="wrap"><div class="grid g3">'+''.join(post_card(p) for p in POSTS)+'</div></div></section>'
    s+=cta(wam)+'</main>'+footer()+'</body></html>'
    open(d+'/index.html','w').write(s)
    # articulos
    for i,p in enumerate(POSTS):
        n=p['img']; url=BASE+p['path']
        art={"@context":"https://schema.org","@type":"BlogPosting","headline":p['title'],"description":p['desc'],"image":[BASE+'/assets/img/'+n+'.webp'],
             "datePublished":p['date'],"dateModified":p.get('updated',p['date']),"inLanguage":"es-MX","mainEntityOfPage":url,"wordCount":p['words'],
             "author":{"@type":"Organization","name":"Serví luz","url":BASE+"/"},
             "publisher":{"@type":"Organization","name":"Serví luz","logo":{"@type":"ImageObject","url":BASE+"/assets/img/icon-512.png"}}}
        ld=[bc(('Inicio','/'),('Blog','/blog/'),(p['title'],p['path'])),art]
        if p['faq']: ld.append({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in p['faq']]})
        pre=(f'<link rel="preload" as="image" href="/assets/img/{n}-m.webp" media="(max-width:768px)" fetchpriority="high"><link rel="preload" as="image" href="/assets/img/{n}.webp" media="(min-width:769px)" fetchpriority="high">'
             f'<style>.sub{{--img:url(/assets/img/{n}-m.webp)}}@media(min-width:769px){{.sub{{--img:url(/assets/img/{n}.webp)}}}}</style>'+RSS_LINK)
        h=head(p['title']+(' | Serví luz' if len(p['title'])<=46 else ''),p['desc'],p['path'],ld,pre=pre).replace('og:type" content="website"','og:type" content="article"')
        h=h.replace('<meta name="twitter:card"',f'<meta property="article:published_time" content="{p["date"]}"><meta name="twitter:card"',1)
        s=h+header('blog.html')
        s+=f'<main id="contenido"><section class="sub"><div class="wrap"><p class="crumb"><a href="/">Inicio</a> › <a href="/blog/">Blog</a> › {p["cat"]}</p><span class="eyebrow">{p["cat"]}</span><h1>{p["title"]}</h1><p class="lead">{p["desc"]}</p><p class="meta"><time datetime="{p["date"]}">{fdate(p["date"])}</time> · {p["min"]} min de lectura · Por Serví luz</p></div></section>'
        s+=f'<section class="nofo art"><div class="wrap" style="max-width:780px"><article class="prose">{md_body(p["body"])}'
        if p['faq']: s+='<h2>Preguntas frecuentes</h2>'+''.join(f'<details><summary>{q}</summary><p>{html.escape(a,quote=False)}</p></details>' for q,a in p['faq'])
        s+=f'<p class="btns" style="margin-top:28px"><a class="btn btn-wa" href="{wa(wam)}" rel="noopener">{I('chat')} Escríbenos por WhatsApp</a><a class="btn btn-primary" href="tel:+52{TEL}">{I('phone')} {TELF}</a></p></article></div></section>'
        rel=[q for q in POSTS if q['slug']!=p['slug']]
        rel.sort(key=lambda q:(q['cat']!=p['cat'],q['date']),reverse=False)
        rel=sorted([q for q in POSTS if q['slug']!=p['slug']],key=lambda q:(q['cat']!=p['cat'],-int(q['date'].replace('-',''))))[:3]
        if rel: s+='<section><div class="wrap"><span class="eyebrow rv">Sigue leyendo</span><h2 class="rv">Te puede interesar</h2><div class="grid g3">'+''.join(post_card(q) for q in rel)+'</div></div></section>'
        s+=cta(wam)+'</main>'+footer()+'</body></html>'
        od=d+'/'+p['slug']; os.makedirs(od,exist_ok=True); open(od+'/index.html','w').write(s)
    # feed
    items=''.join(f'<item><title>{html.escape(p["title"])}</title><link>{BASE}{p["path"]}</link><guid>{BASE}{p["path"]}</guid><pubDate>{datetime.date(*map(int,p["date"].split("-"))).strftime("%a, %d %b %Y")} 12:00:00 -0600</pubDate><description>{html.escape(p["desc"])}</description></item>' for p in POSTS)
    open(d+'/feed.xml','w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel><title>Blog de Serví luz</title><link>{BASE}/blog/</link><description>Consejos de electricistas en Guadalajara y Jalisco</description><language>es-mx</language>{items}</channel></rss>\n')
import datetime
blog_pages()

# 404, robots, sitemap, render.yaml
open(OUT+'/404.html','w').write(head('Página no encontrada | Serví luz','Página no encontrada','/404.html').replace('index,follow','noindex')+header('')+f'<main id="contenido"><section class="sub"><div class="wrap"><h1>Se fue la luz en esta página <span class="amber">{I('zap')}</span></h1><p class="lead">No encontramos lo que buscas, pero el servicio sigue prendido.</p><div class="btns"><a class="btn btn-primary" href="/">Ir al inicio</a><a class="btn btn-wa" href="{wa("Hola Serví luz")}">{I('chat')} WhatsApp</a></div></div></section></main>'+footer()+'</body></html>')
open(OUT+'/robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n')
open(OUT+'/sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{BASE}{p}</loc><lastmod>{datetime.date.today().isoformat()}</lastmod><changefreq>monthly</changefreq><priority>{pr}</priority></url>\n' for p,pr in [('/','1.0'),('/restaurantes/','0.9'),('/residencias/','0.9'),('/industrial/','0.9'),('/blog/','0.8')])+''.join(f'<url><loc>{BASE}{q["path"]}</loc><lastmod>{q.get("updated",q["date"])}</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>\n' for q in POSTS)+'</urlset>\n')
open(OUT+'/render.yaml','w').write('''services:
  - type: web
    name: serviluz
    runtime: static
    buildCommand: echo "static"
    staticPublishPath: .
    pullRequestPreviewsEnabled: false
    headers:
      - path: /assets/*
        name: Cache-Control
        value: public, max-age=31536000, immutable
      - path: /*
        name: X-Content-Type-Options
        value: nosniff
''')
print('ok')
