#!/usr/bin/env python3
"""Generate the full animated Terminal OS × AI Command Center GitHub README artwork.

Pure Python standard library; outputs self-contained SVGs (no JavaScript, fonts,
remote assets or package dependencies). Run from any directory.
"""
from __future__ import annotations

from html import escape
from pathlib import Path
import math

BASE = Path(__file__).resolve().parents[1]
ASSETS = BASE / 'assets'
ASSETS.mkdir(parents=True, exist_ok=True)

BG = '#070d1c'; PANEL = '#0b1729'; INK = '#f3f9ff'; MUTED = '#8da8c2';
TEAL = '#55ffe1'; BLUE = '#76b8ff'; VIOLET = '#b391ff'


def e(text):
    return escape(str(text), quote=True)


def rect(x, y, w, h, fill='none', stroke='none', rx=0, sw=1, extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'


def txt(x, y, value, size=16, fill=INK, weight=400, mono=False, extra=''):
    family = "monospace" if mono else "sans-serif"
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{e(value)}</text>'


def line(x1,y1,x2,y2,stroke='#3a5978',width=1,extra=''):
    return f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{stroke}" stroke-width="{width}" {extra}/>'


def circle(x,y,r,fill,extra=''):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" {extra}/>'


def common(w,h,title):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{e(title)}">
  <title>{e(title)}</title>
  <defs>
    <linearGradient id="base" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#071020"/><stop offset=".55" stop-color="#0b1830"/><stop offset="1" stop-color="#070b1c"/></linearGradient>
    <linearGradient id="bright" x1="0" x2="1"><stop stop-color="#49eadb"/><stop offset=".55" stop-color="#67a6ff"/><stop offset="1" stop-color="#b488ff"/></linearGradient>
    <linearGradient id="tealblue" x1="0" x2="1"><stop stop-color="#54ffe0"/><stop offset="1" stop-color="#79baff"/></linearGradient>
    <radialGradient id="halo"><stop stop-color="#00e4dc" stop-opacity=".22"/><stop offset="1" stop-color="#00c6e8" stop-opacity="0"/></radialGradient>
    <radialGradient id="purplehalo"><stop stop-color="#8155d9" stop-opacity=".20"/><stop offset="1" stop-color="#8155d9" stop-opacity="0"/></radialGradient>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#79b5d9" stroke-width=".6" stroke-opacity=".095"/></pattern>
    <filter id="soft"><feGaussianBlur stdDeviation="7"/></filter>
    <clipPath id="frame"><rect width="{w}" height="{h}" rx="17"/></clipPath>
    <style>
      .mono{{font-family:'SFMono-Regular',Consolas,'Liberation Mono',monospace}}
      .sans{{font-family:Inter,'Segoe UI',Arial,sans-serif}}
      .pulse{{animation:pulse 3.4s ease-in-out infinite}}
      .pulseB{{animation:pulse 3.4s ease-in-out 1.1s infinite}}
      .blink{{animation:blink 1.08s steps(2,start) infinite}}
      .orbit{{transform-origin:910px 219px;animation:orbit 32s linear infinite}}
      .orbitRev{{transform-origin:910px 219px;animation:orbit 39s linear infinite reverse}}
      .dash{{stroke-dasharray:7 17;animation:travel 3.2s linear infinite}}
      .flowSlow{{stroke-dasharray:8 15;animation:travel 7s linear infinite}}
      .float{{animation:float 5s ease-in-out infinite}}
      .floatB{{animation:float 5s ease-in-out 1.6s infinite}}
      .arrive{{animation:arrive 1.15s ease-out both}}
      .arriveB{{animation:arrive 1.2s ease-out .4s both}}
      .arriveC{{animation:arrive 1.2s ease-out .8s both}}
      .sweep{{animation:sweep 9s ease-in-out infinite}}
      .sweepShort{{animation:sweepSmall 6s ease-in-out infinite}}
      .rail{{animation:travel 4s linear infinite;stroke-dasharray:4 19}}
      .bar{{animation:bar 4.2s ease-in-out infinite}}
      .focus{{animation:focus 8s ease-in-out infinite}}
      @keyframes pulse{{0%,100%{{opacity:.95}}50%{{opacity:.3}}}}
      @keyframes blink{{50%{{opacity:0}}}}
      @keyframes orbit{{to{{transform:rotate(360deg)}}}}
      @keyframes travel{{to{{stroke-dashoffset:-240}}}}
      @keyframes float{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-5px)}}}}
      @keyframes arrive{{from{{opacity:0;transform:translateY(11px)}}to{{opacity:1;transform:translateY(0)}}}}
      @keyframes sweep{{0%,8%{{transform:translateX(-700px);opacity:0}}27%{{opacity:.7}}56%{{opacity:.65}}86%,100%{{transform:translateX(1400px);opacity:0}}}}
      @keyframes sweepSmall{{0%{{transform:translateX(-500px);opacity:0}}50%{{opacity:.7}}100%{{transform:translateX(1250px);opacity:0}}}}
      @keyframes bar{{0%,100%{{opacity:.35}}50%{{opacity:.95}}}}
      @keyframes focus{{0%,100%{{opacity:.28}}50%{{opacity:.8}}}}
      @media (prefers-reduced-motion:reduce){{*,*::before,*::after{{animation:none!important}}}}
    </style>
  </defs>
  <g clip-path="url(#frame)">
    <rect width="{w}" height="{h}" fill="url(#base)"/>
    <rect width="{w}" height="{h}" fill="url(#grid)"/>
    {rect(1,1,w-2,h-2,stroke='#315572',rx=16,sw=1)}
    <g opacity=".8">{line(24,21,72,21,TEAL,2)}{line(w-72,h-22,w-24,h-22,TEAL,2)}{line(24,h-22,24,h-46,TEAL,2)}{line(w-24,21,w-24,45,TEAL,2)}</g>
  '''


def close():
    return '</g></svg>'


def header(w, name, right, bar_y=64):
    s = rect(22,20,w-44,39,'#0a182b','#23445d',8)
    for i,c in enumerate(('#ff6d7d','#ffd16b','#65f0da')):
        s += circle(43+i*20,39,4.5,c)
    s += txt(113,45,name,12,'#c5dfeb',600,True, 'letter-spacing="1.2"')
    s += txt(w-45,45,right,11,'#8da8c2',500,True,'text-anchor="end" letter-spacing=".6"')
    return s


def pill(x,y,w,label, color=TEAL):
    return rect(x,y,w,29,'#0b2236','#2e657b',8) + circle(x+14,y+14.5,3,color) + txt(x+25,y+19,label,12,'#d7eaff',550,True)


def write_asset(name, parts):
    out=ASSETS/name
    out.write_text(''.join(parts),encoding='utf-8')
    print(f'{out.relative_to(BASE)}: {out.stat().st_size:,} bytes')


def make_hero():
    w,h=1200,450
    s=[common(w,h,'Oussama Mahi terminal operating system and AI mission-control animated hero')]
    s += [rect(550,40,650,420,'url(#purplehalo)')]
    s += [header(w,'~/oussama-mahi/profile · terminal-os','BUILD / ENGINEER / EXPLORE')]
    s += [txt(61,102,'ENGINEERING IDENTITY   /   PROFILE BOOT SUCCESSFUL',12,TEAL,600,True,'letter-spacing="1.1"')]
    s += [rect(61,120,5,86,'url(#tealblue)',rx=2)]
    s += [f'<g class="arrive">{txt(79,175,"OUSSAMA MAHI",70,INK,850,False,"letter-spacing=\"-2.5\"")}</g>']
    s += [f'<g class="arriveB">{txt(81,206,"SOFTWARE ENGINEER  /  BACKEND  /  AGENTIC AI",16,"#b9d6e9",600,True)}</g>']
    s += [rect(65,233,575,142,'#071322','#2d6474',12,1.3)]
    s += [txt(86,260,'❯ whoami',16,TEAL,600,True)]
    s += [txt(104,287,'engineering student · ENSIAS × 1337 (42 Network)',14,INK,400,True)]
    s += [txt(86,315,'❯ cat focus.txt',16,TEAL,600,True)]
    s += [txt(104,340,'Backend architecture · reliable systems · applied AI',14,'#c4dcee',400,True)]
    s += [rect(594,324,8,17,TEAL,extra='class="blink"')]
    s += [txt(64,405,'BUILDING RELIABLE SYSTEMS. EXPLORING INTELLIGENT ONES.',14,'#8da8c2',500,True)]
    s += [txt(64,429,'RABAT, MOROCCO     •     ENGINEERING PROFILE / 2026',11,'#5f8dac',500,True)]
    # Orbiting ecosystem
    cx,cy=920,229
    s += [circle(cx,cy,204,'url(#halo)')]
    for r,opacity in [(160,.24),(125,.35),(91,.38)]:
        s += [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#6aa6c6" stroke-opacity="{opacity}" stroke-width="1" stroke-dasharray="{5 if r!=125 else 0} 12"/>']
    s += [f'<g class="orbit"><circle cx="{cx}" cy="{cy}" r="157" fill="none" stroke="#67f7e1" stroke-width="3" stroke-dasharray="68 930"/><circle cx="{cx+157}" cy="{cy}" r="6" fill="{TEAL}"/><circle cx="{cx+157}" cy="{cy}" r="16" fill="{TEAL}" opacity=".12"/></g>']
    s += [f'<g class="orbitRev"><circle cx="{cx}" cy="{cy}" r="125" fill="none" stroke="{VIOLET}" stroke-width="3" stroke-dasharray="42 780"/><circle cx="{cx-125}" cy="{cy}" r="5" fill="{VIOLET}"/></g>']
    s += [circle(cx,cy,74,'#0e2540','stroke="#467d9c" stroke-width="1.3"')]
    s += [circle(cx,cy,62,'none','stroke="#76ffea" stroke-opacity=".7" stroke-dasharray="3 8" class="pulse"')]
    s += [f'<path d="M905 211l-17 18 17 18 M934 211l17 18-17 18 M928 204l-15 50" stroke="{TEAL}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>']
    s += [txt(cx,280,'SYSTEM / ONLINE',11,'#84b9d1',550,True,'text-anchor="middle" letter-spacing="1"')]
    orbit_tags=[(728,101,'BACKEND',117,BLUE),(1010,116,'AI AGENTS',142,VIOLET),(1005,309,'RAG / LLM',140,TEAL),(705,315,'DATA LAYER',148,BLUE),(811,385,'DEVOPS',125,TEAL)]
    for (x,y,name,wide,color) in orbit_tags:
        s += [rect(x,y,wide,31,'#0b1b32',color,7,1),circle(x+13,y+16,3,color),txt(x+26,y+21,name,12,INK,650,True)]
    for x,y,r,c in [(838,108,3,TEAL),(1048,208,4,BLUE),(840,351,4,VIOLET),(960,88,3,TEAL)]:
        s += [circle(x,y,r,c,'class="pulse"')]
    s += [rect(1193,69,3,320,TEAL,extra='class="pulse"')]
    s += [close()]
    write_asset('hero.svg',s)


def make_skills():
    w,h=1200,744
    s=[common(w,h,'Animated Terminal OS engineering technology stack dashboard')]
    s += [header(w,'~/engineering/skills · capabilities.json','readonly // no inflated proficiency claims')]
    s += [txt(52,111,'❯ ./scan-capabilities --group-by-domain',21,TEAL,600,True)]
    s += [txt(52,145,'ENGINEERING STACK',34,INK,750,False,'letter-spacing="-1"')]
    s += [txt(1145,142,'6 MODULES / 01 SYSTEM',12,BLUE,500,True,'text-anchor="end"')]
    s += [line(52,163,1147,163,'#29536a',1)]

    cards=[
      ('01','BACKEND & ARCHITECTURE','core.backend', ['Java  ·  Python  ·  Spring Boot  ·  FastAPI', 'REST APIs  ·  Microservices  ·  DDD', 'OAuth2  ·  JWT  ·  RBAC'],TEAL),
      ('02','AGENTIC AI & RETRIEVAL','intelligence.pipeline',['LLM APIs  ·  Multi-agent workflows  ·  RAG', 'Qdrant  ·  Embeddings  ·  Vector search', 'Gemini  ·  OpenAI  ·  Evaluation'],BLUE),
      ('03','DATA & MESSAGING','persistence.layer',['PostgreSQL  ·  MongoDB  ·  MySQL', 'Redis  ·  SQL  ·  Data modeling', 'Kafka concepts  ·  Idempotency'],VIOLET),
      ('04','FRONTEND ENGINEERING','interface.runtime',['TypeScript  ·  JavaScript  ·  React', 'Next.js  ·  API integration', 'Accessible interfaces  ·  Component design'],TEAL),
      ('05','PLATFORM & DELIVERY','infra.toolchain',['Docker  ·  Git  ·  Linux  ·  CI/CD', 'GitHub Actions  ·  Jenkins', 'Kubernetes  ·  Cloud-native foundations'],BLUE),
      ('06','ENGINEERING PRACTICE','quality.gates',['Testing  ·  Security  ·  Code review', 'SOLID  ·  Design patterns  ·  ADRs', 'Observability  ·  Reliability  ·  Recovery'],VIOLET),
    ]
    for idx,(num,title,mod,lines,accent) in enumerate(cards):
        col=idx%2; row=idx//2; x=52+col*560; y=183+row*167; cw=538; ch=147
        s += [rect(x,y,cw,ch,'#0b1a2e','#284a61',13,1.2)]
        s += [rect(x,y,5,ch,accent,rx=2,extra='class="pulseB"')]
        s += [rect(x+18,y+17,37,23,'#102d42','#255a6c',6),txt(x+28,y+33,num,13,accent,750,True)]
        s += [txt(x+69,y+34,title,16,INK,750,False)]
        s += [txt(x+cw-19,y+33,'● ACTIVE',11,accent,550,True,'text-anchor="end" class="pulse"')]
        s += [txt(x+18,y+64,'$ cat '+mod,12,accent,550,True)]
        for k,t in enumerate(lines):
            s += [txt(x+20,y+86+19*k,t,13,'#c1d7e9',400,True)]
        s += [line(x+18,y+ch-9,x+cw-18,y+ch-9,'#25465c',2)]
        s += [f'<path d="M{x+18} {y+ch-9}H{x+cw-18}" fill="none" stroke="{accent}" stroke-width="2" stroke-dasharray="25 460" class="flowSlow"/>']
    s += [line(52,695,1147,695,'#2f5269',1)]
    s += [txt(55,721,'CAPABILITY MAPPING  //  THE TOOLS SERVE THE ARCHITECTURE — NOT THE OTHER WAY AROUND.',13,'#94b8c9',550,True)]
    s += [rect(1177,179,2,494,TEAL,extra='class="pulse"')]
    s += [close()]
    write_asset('skills-terminal.svg',s)


def make_systems():
    w,h=1200,362
    s=[common(w,h,'Animated reliable systems engineering architecture workflow')]
    s += [header(w,'~/architecture/system-thinking','failure-aware / controlled changes')]
    s += [txt(50,109,'❯ trace request --show-boundaries',20,TEAL,650,True)]
    s += [txt(50,137,'How I reason about a production system',19,INK,620)]
    xs=[56,287,518,749,980]
    titles=['SIGNAL','SERVICE','STATE','INTELLIGENCE','SAFE ACTION']
    subs=[['Requests','Events / logs'],['APIs','Boundaries'],['Persistence','Consistency'],['Retrieval','Context / agents'],['Approval','Audit / recovery']]
    accents=[TEAL,BLUE,VIOLET,BLUE,TEAL]
    for i,x in enumerate(xs):
        y=177
        s += [rect(x,y,173,114,'#0d2037','#31556e',12,1.4)]
        s += [rect(x+17,y+14,9,9,accents[i],rx=2,extra='class="pulse"')]
        s += [txt(x+36,y+25,titles[i],13,INK,700,True)]
        s += [line(x+17,y+39,x+155,y+39,'#355671')]
        for j,v in enumerate(subs[i]):
            s += [txt(x+18,y+67+j*21,v,14,'#9ab9cd',400,True)]
        if i<4:
            xa=x+173; xb=xs[i+1]
            s += [line(xa,235,xb,235,'#3e738e',2)]
            s += [f'<path d="M{xa} 235H{xb}" fill="none" stroke="{accents[i]}" stroke-width="3" class="dash"/>']
            s += [f'<path d="M{xb-9} 230l9 5-9 5" fill="none" stroke="{accents[i]}" stroke-width="2"/>']
    s += [line(52,313,1148,313,'#31546d')]
    s += [txt(60,339,'INVARIANTS  >  LATENCY TRICKS     ·     HUMAN OVERSIGHT  >  BLIND AUTOMATION',14,'#9fc8d2',550,True)]
    s += [close()]
    write_asset('systems-map.svg',s)


def make_projects():
    w,h=1200,528
    s=[common(w,h,'Animated four-project terminal repository showcase')]
    s += [header(w,'~/workspaces/projects · git log --graph','PUBLIC REPOSITORIES // PORTFOLIO')]
    s += [txt(49,110,'❯ ls -la ~/projects/',22,TEAL,650,True)]
    s += [txt(49,148,'SELECTED WORK / EXPLORATION LOG',27,INK,720)]
    cards=[
      ('DEV PILOT AI','AI / SOFTWARE ENGINEERING','FastAPI · Next.js · PostgreSQL','Multi-agent and document intelligence','Design focus: RAG & service boundaries',TEAL),
      ('MAROC AFFILIATE AI','TRUSTED BACKEND','Python · FastAPI · PostgreSQL','AI-assisted marketing workflows','Design focus: validations & approvals',BLUE),
      ('MINI RAG PRO','RETRIEVAL EXPERIMENTS','Python · LLMs · Vector retrieval','RAG concepts and retrieval experiments','Design focus: grounded answers',VIOLET),
      ('TERMINAL PORTFOLIO','INTERFACE EXPERIMENT','Next.js · TypeScript · React','Developer identity as an interface','Design focus: interaction design',TEAL),
    ]
    for i,(title,category,stack,desc,focus,accent) in enumerate(cards):
        x=50+(i%2)*558; y=176+(i//2)*160; cw=540
        s += [rect(x,y,cw,145,'#0b1b30','#294f6c',12,1)]
        s += [circle(x+22,y+23,5,accent,'class="pulse"')]
        s += [txt(x+36,y+29,f'{i+1:02d} / {title}',19,INK,760)]
        s += [txt(x+cw-18,y+28,category,11,accent,500,True,'text-anchor="end"')]
        s += [line(x+20,y+46,x+cw-20,y+46,'#315571',1)]
        s += [txt(x+21,y+74,'$ stack: '+stack,13,accent,450,True)]
        s += [txt(x+21,y+101,desc,14,'#c7dce9',450)]
        s += [txt(x+21,y+124,focus,13,'#8aa9c3',450,True)]
    s += [txt(52,513,'NOTE: PROJECT DESCRIPTIONS DESCRIBE DIRECTION AND PUBLIC WORK; CHECK EACH REPOSITORY FOR CURRENT IMPLEMENTATION.',11,'#839bb9',400,True)]
    s += [close()]
    write_asset('projects-terminal.svg',s)


def make_footer():
    w,h=1200,174
    s=[common(w,h,'Animated command line GitHub profile footer')]
    s += [header(w,'~/profile/session · exit','status: online / always learning')]
    s += [txt(52,111,'❯ echo "Good systems are designed for what happens when things go wrong."',20,TEAL,600,True)]
    s += [txt(60,144,'GOOD SYSTEMS ARE DESIGNED FOR WHAT HAPPENS WHEN THINGS GO WRONG.',15,'#c7d7e9',550,True)]
    s += [rect(941,130,10,17,TEAL,extra='class="blink"')]
    s += [close()]
    write_asset('footer.svg',s)


if __name__=='__main__':
    make_hero()
    make_skills()
    make_systems()
    make_projects()
    make_footer()
    print('Generated 5 GitHub-safe animated SVG files, all editable in this script.')
