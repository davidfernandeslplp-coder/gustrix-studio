from pathlib import Path
import json,shutil,html,re
P=Path(__file__).resolve().parent.parent; D=P/'dist'
if D.exists():shutil.rmtree(D)
D.mkdir();shutil.copytree(P/'media',D/'media')
S=json.loads((P/'content/site.json').read_text())
e=lambda s:html.escape(str(s or ''),quote=True)
def url(s):
 s=str(s or '');return s if s.startswith(('https://','http://','mailto:')) else '#'
def media(s,base=''):
 s=str(s or '');return e(s) if s.startswith('https://') else base+e(s.lstrip('/'))
def paragraphs(s):return ''.join('<p>'+e(t).replace('\n','<br>')+'</p>' for t in str(s or '').split('\n\n') if t.strip())
def load(folder):
 out=[]
 for f in (P/'content'/folder).glob('*.json'):
  x=json.loads(f.read_text()); assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',x['slug']),f'Endereço inválido: {f}'
  if x.get('published'):out.append(x)
 assert len({x['slug'] for x in out})==len(out),'Endereços duplicados'
 return out
G=sorted(load('games'),key=lambda x:x.get('order',10));N=sorted(load('posts'),key=lambda x:str(x.get('date','')),reverse=True)
def shell(title,body,base='',desc='Jogos independentes de RPG, sobrevivência e estratégia.'):return f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)} · {e(S['title'])}</title><meta name="description" content="{e(desc)}"><meta name="theme-color" content="#101313"><link rel="icon" href="{base}media/logo.png"><link rel="stylesheet" href="{base}style.css"></head><body><a class="skip" href="#main">Pular para o conteúdo</a><header><a class="brand" href="{base}index.html" aria-label="Gustrix Studio — início"><img src="{media(S.get('logo'),base)}" alt=""><span>GUSTRIX<small>STUDIO</small></span></a></header><main id="main">{body}</main><footer><a class="footer-brand" href="{base}index.html">GUSTRIX <small>STUDIO</small></a><span>Independente. Brasileiro.</span><a href="{base}admin.html">Área do estúdio ↗</a></footer><dialog id="lightbox"><button aria-label="Fechar imagem" class="close">×</button><img alt="Captura ampliada do jogo"></dialog><script src="{base}app.js" defer></script></body></html>'''
def gamecard(g,i):return f'''<a class="game-card" href="jogos/{e(g['slug'])}.html"><div class="game-art"><img src="{media(g['cover'])}" alt="{e(g['title'])}" loading="lazy"><span class="status">{e(g['status'])}</span><span class="open-arrow">↗</span></div><div class="game-caption"><span class="number">{i:02}</span><div><h3>{e(g['title'])}</h3><p>{e(g['genre'])} <span>·</span> {e(g['platforms'])}</p></div></div></a>'''
f=next((g for g in G if g.get('featured')),G[0] if G else None)
slides=''.join(f'''<a class="portal-slide" href="jogos/{e(g['slug'])}.html" aria-label="Conhecer {e(g['title'])}" {'hidden' if i else ''}><img src="{media(g['cover'])}" alt="{e(g['title'])}" draggable="false"><div class="portal-caption"><span>EM DESTAQUE / {e(g['status']).upper()}</span><h2>{e(g['title'])}</h2><span class="portal-link">Conheça este mundo <b>↗</b></span></div></a>''' for i,g in enumerate(G))
controls=''.join(f'<button class="story-dot" aria-label="Mostrar {e(g["title"])}" aria-pressed="{str(i==0).lower()}"><span></span></button>' for i,g in enumerate(G)) if len(G)>1 else ''
hero=f'<div class="portal stories" role="region" aria-label="Jogos em destaque" aria-roledescription="carrossel">{slides}<div class="story-controls">{controls}</div>'+('<button class="story-pause" aria-label="Pausar troca automática">Ⅱ</button>' if len(G)>1 else '')+'</div>' if G else ''

news=''.join(f'''<a class="news-row" href="novidades/{e(n['slug'])}.html"><span class="news-date">{e(str(n.get('date',''))[:10])}<small>{e(n.get('category'))}</small></span><h3>{e(n['title'])}</h3><span class="news-arrow">↗</span></a>''' for n in N) or '<p class="muted">As próximas histórias chegam por aqui.</p>'
social=''.join(f'<a href="{e(url(S.get(k)))}" target="_blank" rel="noopener noreferrer">{k.title()} ↗</a>' for k in ['instagram','youtube','discord'] if S.get(k))
body=f'''<section class="hero"><div class="hero-copy"><h1>{e(S['headline']).replace(chr(10),'<br>')}</h1><a class="text-link" href="#jogos">Explore nossos jogos <span>↓</span></a><div class="hero-bottom"><span>CRIADO NO BRASIL</span><span>RPG / SURVIVAL / ESTRATÉGIA</span></div></div>{hero}</section><section class="games section" id="jogos"><div class="section-heading"><p class="eyebrow">01 / NOSSOS MUNDOS</p><h2>Entre. Explore.<br><em>Deixe sua marca.</em></h2></div><div class="game-grid">{''.join(gamecard(g,i+1) for i,g in enumerate(G))}</div></section><section class="section news" id="novidades"><div class="section-top"><p class="eyebrow">02 / DIÁRIO DO ESTÚDIO</p><h2>Do lado de cá.</h2></div>{news}</section><section class="studio section" id="studio"><div class="seal"><img src="{media(S.get('logo'))}" alt="Símbolo da Gustrix"></div><div><p class="eyebrow">03 / GUSTRIX STUDIO</p><h2>Uma nova jornada.</h2>{paragraphs(S.get('about'))}</div></section><section class="contact section" id="contato"><p class="eyebrow">TEM ALGO EM MENTE?</p><a class="contact-title" href="mailto:{e(S['email'])}">Vamos conversar.<span>↗</span></a><div class="contact-bottom"><a href="mailto:{e(S['email'])}">{e(S['email'])}</a><div>{social}</div></div></section>'''
(D/'index.html').write_text(shell('Início',body))
for g in G:
 b='../';buttons=''.join(f'<a class="button" href="{e(url(g.get(k)))}" target="_blank" rel="noopener noreferrer">{label} ↗</a>' for k,label in [('play_url','Google Play'),('web_url','Jogar na web')] if g.get(k))
 gallery=''.join(f'<button class="gallery-image" data-image="{media(x,b)}" aria-label="Ampliar captura {i+1}"><img src="{media(x,b)}" alt="{e(g["title"])} — captura {i+1}" loading="lazy"></button>' for i,x in enumerate(g.get('gallery',[])))
 legal=' · '.join(f'<a href="{e(url(g.get(k)))}">{label}</a>' for k,label in [('privacy_url','Privacidade'),('terms_url','Termos de Serviço')] if g.get(k))
 content=f'''<section class="detail section"><a class="back" href="../index.html#jogos">← Todos os jogos</a><div class="detail-grid"><div><p class="eyebrow">{e(g['genre'])} / {e(g['platforms'])}</p><h1>{e(g['title'])}</h1><span class="pill">{e(g['status'])}</span><h2 class="summary">{e(g['summary'])}</h2>{paragraphs(g['description'])}<div class="buttons">{buttons}</div><div class="legal">{legal}</div></div><img class="detail-cover" src="{media(g['cover'],b)}" alt="{e(g['title'])}"></div><div class="gallery">{gallery}</div></section>'''
 (D/'jogos').mkdir(exist_ok=True);(D/'jogos'/f'{g["slug"]}.html').write_text(shell(g['title'],content,b,g['summary']))
for n in N:
 cover=f'<img class="article-cover" src="{media(n["cover"],"../")}" alt="{e(n["title"])}">' if n.get('cover') else ''
 content=f'''<article class="article section"><a class="back" href="../index.html#novidades">← Novidades</a><p class="eyebrow">{e(n.get('category'))} / {e(n.get('date'))}</p><h1>{e(n['title'])}</h1><p class="intro">{e(n.get('summary'))}</p>{cover}<div class="article-body">{paragraphs(n.get('body'))}</div></article>'''
 (D/'novidades').mkdir(exist_ok=True);(D/'novidades'/f'{n["slug"]}.html').write_text(shell(n['title'],content,'../',n.get('summary')))
(D/'admin.html').write_text(shell('Área do estúdio','''<section class="admin section"><p class="eyebrow">GUSTRIX / ADMINISTRAÇÃO</p><h1>Seu próximo capítulo.</h1><p>Jogos, novidades e imagens. Tudo no mesmo lugar.</p><a class="button" href="https://app.pagescms.org/">Entrar com GitHub ↗</a><p class="muted">Acesso pelo Pages CMS, reservado às contas autorizadas no repositório.</p></section>'''))
(D/'404.html').write_text(shell('Página não encontrada','<section class="section admin"><h1>Este caminho ainda não existe.</h1><a class="button" href="./index.html">Voltar ao início</a></section>'))
for n in ['style.css','app.js']:shutil.copy(P/n,D/n)
(D/'.nojekyll').touch()
print(f'Build: {len(G)} jogos, {len(N)} posts. Saída: {D}')
