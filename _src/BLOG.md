# Blog de Serví luz: cómo publicar artículos

Sitio estático generado con `python3 _src/gen.py` (escribe en la raíz del repo: index.html, /blog/, sitemap.xml, feed).

## Publicar un artículo
1. Crea `_src/blog/AAAA-MM-DD-slug.md` con este encabezado:
   ```
   ---
   slug: slug-en-minusculas-con-guiones
   title: Título (máx. ~60 caracteres, con la palabra clave al inicio)
   desc: Meta descripción de 140-160 caracteres
   date: AAAA-MM-DD
   cat: Fallas eléctricas | Seguridad | Casas | Restaurantes | Negocios
   img: cap-falla   (una de: cap-falla, cap-tablero, cap-prueba, cap-luz, dev-casa, dev-tablero, foco-poster, tablero-poster; todas tienen versión -m)
   alt: Descripción real de la imagen
   ---
   ```
2. Cuerpo en markdown simple: `## h2`, `### h3`, párrafos, `- ` viñetas, `1. ` numeradas, `**negritas**`, `[texto](/ruta/)`.
3. Termina con `## Preguntas frecuentes` y 2-3 `### Pregunta` + respuesta (genera FAQPage JSON-LD).
4. Mínimo 450 palabras, 2+ enlaces internos (servicios `/restaurantes/`, `/residencias/`, `/industrial/` y otros artículos `/blog/slug/`).
5. `python3 _src/gen.py`, revisar, commit, push y disparar deploy en Render (autoDeploy NO se dispara con el push): servicio `srv-dbuk6k2jnfac73dgjmvg`.

## Reglas de contenido (honestidad y seguridad)
- DOMINIO: el único dominio oficial es https://serviluz.com.mx. NUNCA usar serviluz.onrender.com (desactivado, da 404) en artículos, enlaces ni avisos. URL de cada artículo: https://serviluz.com.mx/blog/<slug>/. Enlaces internos siempre relativos (/blog/slug/).
- Datos reales del negocio: visita $300, 7 años de experiencia, servicio express, tel/WhatsApp 33 2827 2152, Guadalajara, Zapopan, Tonalá, Tlaquepaque y todo Jalisco.
- NO inventar precios de mercado, porcentajes, estadísticas, normas con número o reseñas. Si hay duda, decir "depende" y ofrecer la visita.
- Seguridad primero: nunca instruir a abrir tableros, puentear pastillas ni manipular cables. Ante humo o fuego: 911.
- Tono claro y cercano, español de México. Un tema nuevo por artículo; no repetir los ya publicados.

## Temas pendientes (tomar el siguiente, quitarlo de la lista al publicarlo)
- Centro de carga: qué es, cuándo cambiarlo y señales de que el tuyo ya no da
- Apagones y variaciones de voltaje en temporada de lluvias en Jalisco: cómo proteger tus aparatos
- Iluminación LED para tu negocio: cómo elegir la luz por área
- Contactos que se calientan o chispean: causas y qué hacer
- Extensiones y multicontactos: cuándo sí y cuándo es un riesgo
- Revisión eléctrica antes de comprar o rentar una casa
- Instalación eléctrica para locales comerciales y oficinas
- Cámaras de refrigeración: circuitos y protección eléctrica para no perder mercancía
- Instalación eléctrica en obra nueva y remodelación: qué definir con tu arquitecto
- Mantenimiento preventivo eléctrico en bodegas y talleres
- Cargador de auto eléctrico en casa: qué revisar en tu instalación
- Cómo leer tu recibo de la CFE y detectar consumos anormales
- Focos y lámparas que parpadean: causas y soluciones
- Electricista para Zapopan / Tlaquepaque / Tonalá: guías por zona (una por semana)
