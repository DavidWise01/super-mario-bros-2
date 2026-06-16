#!/usr/bin/env python3
"""Build Super Mario Bros. 2 (American) (SMB2) — the 1988 NES game (a reskin of
Yume Kōjō: Doki Doki Panic) as a UD0 game-world, themed to the source: a Subcon
dream-desert palette, an ANIMATED CANVAS 2D title scene (not SVG), 8-bit/CRT,
hobby domain. Genesis (the reskin), the Subcon quest, and the .dlw birth.
Render-not-invent; the Doki-Doki-Panic origin + the debuted-here cast flagged.
Super Mario Bros. 2 is © Nintendo; a fan tribute."""
import os, html, base64, json, io, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "SUPER MARIO BROS. 2", "axiom": "SMB2",
 "position": "Super Mario Bros. 2 (American) · Nintendo · NES 1988 — the reskin of Yume Kōjō: Doki Doki Panic (1987)",
 "origin": "Subcon, the land of dreams, cursed by the frog-king Wart, entered through a door in Mario's dream",
 "mechanism": "Crystallized from Super Mario Bros. 2 (Nintendo, NES 1988) — the Western Mario reskin of Doki Doki Panic.",
 "crystallization": "Four heroes who don't stomp but PLUCK vegetables and throw them, cross seven worlds of a dream-land, drink potions into a mirror-world, and beat a frog-king by feeding him the turnips he hates.",
 "nature": "Super Mario Bros. 2 (American) — the strangest mainline Mario: a Doki Doki Panic reskin that smuggled Shy Guy, Birdo, Bob-omb and Wart permanently into the series; vegetables for weapons, Subcon for a stage.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "Super Mario Bros. 2; Doki Doki Panic; the four heroes; the vegetable pluck; Subcon & Subspace; Wart; Birdo; Shy Guy",
 "witness": "A 'fake' Mario game — someone else's promo title in a red cap — that nonetheless stocked the real Mario's bestiary forever.",
 "role": "the dream game-world",
 "seal": "Pull the turnip, throw it — and learn at the top that the whole dream was Doki Doki Panic, wearing Mario's face.",
 "source": "Super Mario Bros. 2, catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#caa05a", "flesh and the dream-desert — the mortal heroes, the wardens, the recurring foes"),
 "ethereal":  ("#9a7cff", "of the dream — Subcon itself, the masked, the floating princess, the frog-king"),
 "spiritual": ("#e0405a", "of the soul beneath the skin — the mirror-world, and the true game under the reskin"),
 "electrical":("#3a9bd5", "of the wire and the machine — the fuse-creature, and the cartridge's own strange verb"),
}

# ── the title scene · ANIMATED CANVAS 2D (the MARIO MADNESS box art) ─────────────────
CANVAS_ART = r'''<canvas id="smb2" width="700" height="440" style="width:100%;height:auto;display:block;image-rendering:pixelated"></canvas>
<script>
(function(){
var cv=document.getElementById('smb2');if(!cv)return;var g=cv.getContext('2d'),W=700,H=440;
function R(x,y,w,h,c){g.fillStyle=c;g.fillRect(x,y,w,h);}
function C(x,y,r,c){g.fillStyle=c;g.beginPath();g.arc(x,y,r,0,7);g.fill();}
function cloud(x,y,s){g.fillStyle='#fff';C(x,y,14*s);C(x+15*s,y-7*s,17*s);C(x+33*s,y,15*s);C(x+16*s,y+9*s,18*s);R(x-14*s,y,50*s,12*s,'#fff');}
function mario(t){
 var b=Math.sin(t/180)*3,S='#f2b27a',H='#4a2a14',RD='#d3301f',BL='#2a54bc',GL='#fff',SH='#6e3614',BT='#f2c024';
 function r(x,y,w,h,c){R(x,y+b,w,h,c);}function c(x,y,rr,cc){C(x,y+b,rr,cc);}
 r(322,300,16,30,BL);R(314,328+b,26,11,SH);
 r(348,300,15,24,BL);R(348,318+b,26,11,SH);
 r(316,256,52,46,RD);r(320,272,44,32,BL);
 r(326,256,8,18,BL);r(350,256,8,18,BL);r(328,266,7,7,BT);r(349,266,7,7,BT);
 r(310,260,10,10,RD);r(302,268,11,20,S);R(298,284+b,15,12,GL);
 r(366,256,10,10,RD);r(372,232,11,24,S);R(368,216+b,17,15,GL);
 r(374,192,15,18,'#f4ead6');R(376,180+b,3,14,'#39a046');R(383,180+b,3,14,'#39a046');R(379,176+b,4,6,'#39a046');
 r(314,222,8,24,H);r(362,222,8,24,H);
 r(320,216,44,34,S);
 c(343,236,8,S);
 r(330,222,6,8,'#fff');r(348,222,6,8,'#fff');r(332,224,3,5,BL);r(350,224,3,5,BL);
 r(324,240,38,7,H);r(328,246,8,4,H);r(348,246,8,4,H);
 r(310,198,60,18,RD);r(316,192,46,8,RD);r(360,202,14,8,RD);
 c(337,201,7,'#fff');g.fillStyle=RD;g.font='bold 10px Arial';g.textAlign='center';g.fillText('M',337,205+b);
}
function frame(t){
 var sk=g.createLinearGradient(0,0,0,H);sk.addColorStop(0,'#4f9fe0');sk.addColorStop(1,'#9ad2f4');g.fillStyle=sk;g.fillRect(0,0,W,H);
 cloud(110+Math.sin(t/4000)*14,300,1.4);cloud(560+Math.cos(t/4400)*14,330,1.6);cloud(150+Math.sin(t/5000)*10,150,1);cloud(540,150,.9);
 g.save();g.translate(340,250);g.rotate(-0.5);['#e23b2e','#f0851e','#f2c024','#39a046','#2a78d0'].forEach(function(col,i){R(-220,-150+i*26,300,18,col);});g.restore();
 g.globalAlpha=.18;g.fillStyle='#9ad2f4';g.fillRect(0,250,W,90);g.globalAlpha=1;
 mario(t);
 g.textAlign='center';
 g.fillStyle='#3a1810';g.font='900 22px "Arial Black",Impact,sans-serif';g.fillText('SUPER MARIO',352,52);
 g.fillStyle='#f2c024';g.fillText('SUPER MARIO',350,50);
 g.fillStyle='#3a1810';g.font='900 13px "Arial Black",Impact,sans-serif';g.fillText('BROS.',250,72);
 g.fillStyle='#f2c024';g.fillText('BROS.',249,71);
 g.fillStyle='#3a1810';g.font='900 56px "Arial Black",Impact,sans-serif';g.fillText('2',462,74);
 g.fillStyle='#d3301f';g.fillText('2',460,72);
 R(0,392,W,30,'#c42018');g.fillStyle='#fff';g.font='900 17px "Arial Black",Impact,sans-serif';g.fillText('MARIO MADNESS',350,413);
 R(0,422,W,18,'#111');g.fillStyle='#c9c9c9';g.font='8px monospace';g.fillText('NINTENDO ENTERTAINMENT SYSTEM',350,434);
 requestAnimationFrame(frame);
}
frame(0);
})();
</script>'''

GENESIS = [
 ("Doki Doki Panic, Reskinned", "Japan 1987 → US 1988",
  "The Japanese Super Mario Bros. 2 (later released as 'The Lost Levels') was deemed too hard and too familiar for the West. So Nintendo reskinned its 1987 Fuji-TV game Yume Kōjō: Doki Doki Panic with Mario characters: Imajin→Mario, Mama→Luigi, Papa→Toad, Lina→Princess, and the villain Mamu→Wart."),
 ("A Different Mario", "no stomping",
  "It plays unlike any other Mario: you don't stomp — you PLUCK vegetables from the ground and throw them, pick up and hurl enemies and blocks, and pour through doors into the dream-land of Subcon. Music by Koji Kondo; seven worlds, twenty levels."),
 ("The Cast It Smuggled In", "the lasting gift",
  "Despite being a reskin, it introduced enemies now central to Mario — Shy Guy, Bob-omb, Pokey, Ninji, Snifit, Birdo — and the boss Wart. A 'fake' Mario game that permanently stocked the real one's bestiary."),
]

ARC = [
 ("The Dream Door", "into Subcon",
  "Mario dreams of a long staircase and a door; beyond it a voice begs for help — Subcon, the land of dreams, has been cursed. He wakes, and a letter and the dream both turn out to be real."),
 ("Pluck, Lift, Throw", "the four heroes",
  "Choose Mario (balanced), Luigi (the high, floaty jump), the Princess (she floats), or Toad (fast and strong) — and cross seven worlds pulling turnips, riding Albatosses, drinking potions into Subspace, and fleeing the key-guarding Phanto."),
 ("Wart &amp; the Vegetables", "the finale",
  "At the top waits Wart, the frog-king who seized Subcon — and who hates vegetables. You beat him the only way the dream allows: by throwing the vegetables back down his throat."),
]

IDEAS = [
 ("Plucked, Not Stomped", "the mechanic that makes it strange", [
   "You harvest the ground for turnips and throw them — and you can pick up and throw almost anything, enemies included.",
   "The POW block, the potion-door to Subspace, the end-of-level slot machine: a Mario built from other parts." ]),
 ("Four Heroes, Four Feels", "pick your body", [
   "Mario is the baseline; Luigi flutters and jumps highest; the Princess hovers on her dress; Toad is fastest and digs strongest.",
   "The first time a Mario game let you BE Luigi, Peach, and Toad — each genuinely different to play." ]),
 ("The Reskin That Stuck", "a fake that became canon", [
   "It's Doki Doki Panic in a Mario coat — and yet Shy Guy, Birdo, Bob-omb and the rest became permanent Mario citizens.",
   "The most influential 'not really a Mario game' ever made." ]),
]

SECTIONS = [
 ("The Releases", "the dream, ported", [
   ("Yume Kōjō: Doki Doki Panic", "1987 · Famicom Disk System", "the Fuji-TV original that Nintendo reskinned"),
   ("Super Mario Bros. 2", "1988 · NES (US / PAL)", "the Western Mario reskin — the SMB2 most of the world knows"),
   ("Super Mario USA", "1992 · Famicom", "the reskin sold back to Japan under a new name"),
 ]),
 ("The Makers", "Nintendo", [
   ("Nintendo R&amp;D", "developer / publisher", "produced by Shigeru Miyamoto"),
   ("Kensuke Tanabe", "director", "directed SMB2; devised Doki Doki Panic's concept"),
   ("Koji Kondo", "composer", "the Subcon and overworld themes"),
 ]),
 ("The Legacy", "the reskin reborn", [
   ("Super Mario All-Stars", "1993 · SNES", "the 16-bit remake (SMB2 included)"),
   ("Super Mario Advance", "2001 · GBA", "the launch remake — bigger sprites, voices, Robirdo"),
   ("the bestiary", "permanent", "Shy Guy · Birdo · Bob-omb · Pokey · Ninji · Snifit — Mario staples ever since"),
 ]),
]

# ── the emergents: (slug, name, epithet, emergence, role_line, why_line) ──
EMERGENTS = [
 ("mario", "Mario", "the balanced hero · was Imajin", "natural",
  "the baseline of the four playable heroes — no special trick, the steady measure; reskinned from Imajin of Doki Doki Panic",
  "He is the everyman dream-walker: the plain body the other three are read against."),
 ("luigi", "Luigi", "the high, floaty jump · was Mama", "natural",
  "the hero who jumps highest and flutters, hanging a beat in the air; reskinned from Mama",
  "He is the air-walker of the four — the brother who lingers, and you learn to love the hang."),
 ("princess", "Princess Toadstool", "she floats · was Lina", "ethereal",
  "the only hero who can FLOAT, hovering a moment on her dress to clear long gaps; reskinned from Lina",
  "She is grace made a mechanic: the one who cheats gravity, the dream's own lightness."),
 ("toad", "Toad", "fastest &amp; strongest · was Papa", "natural",
  "the quickest of the four and the strongest digger — pulls turnips before you've blinked; reskinned from Papa",
  "He is the worker's body: low to the ground, fast hands, all hustle."),
 ("wart", "Wart", "the frog-king of Subcon · hates vegetables", "ethereal",
  "the frog-king who cursed Subcon — the final boss, undone by throwing the vegetables he loathes down his open mouth (was Mamu)",
  "He is the nightmare at the top of the dream: a tyrant beaten by the humblest thing, a thrown turnip."),
 ("birdo", "Birdo", "the egg-spitting dino · the recurring gate", "natural",
  "the pink, bow-wearing dinosaur that fires eggs from its snout — the recurring mini-boss, debuted here; the NES manual's note on Birdo's identity (described as preferring to be called Birdetta) is part of the record",
  "It is the gate you ride the eggs of — a foe that debuted in a 'fake' Mario game and never left the real one."),
 ("shy-guy", "Shy Guy", "the masked walker · debuted here", "ethereal",
  "the small masked, robed enemy that marches and turns at ledges — debuted in this game, now everywhere in Mario",
  "It is the face you never see: the masked walker that stepped out of a dream and became one of Mario's most familiar citizens."),
 ("bob-omb", "Bob-omb", "the walking bomb · the fuse made a creature", "electrical",
  "the wind-up walking bomb that lights, ticks, and detonates — debuted here",
  "It is the one foe that is a device: a fuse with feet, ticking toward the blast you must out-time."),
 ("vegetable-pluck", "The Vegetable Pluck", "harvest, lift, throw — not stomp", "electrical",
  "the signature mechanic — pull turnips (and rare bombs, POW blocks, and Mr.-Saturn-like helpers) from the ground and throw them; lift and hurl enemies and blocks",
  "It is the cartridge's own strange verb: not stomp but HARVEST — the rule that makes this Mario unlike every other."),
 ("subcon", "Subcon", "the land of dreams · the stage", "ethereal",
  "the dream-land the whole game takes place in — entered through a door in Mario's dream, cursed by Wart, freed at the end",
  "It is the stage as a dream the game admits, at the close, was never quite real — and yet its monsters came home with you."),
 ("subspace", "Subspace", "the mirror-world behind the potion door", "spiritual",
  "the dark mirror-world reached by throwing the magic POTION to open a door — coins to grab, mushrooms to find, the music inverted, a few seconds before it pulls you back",
  "It is the world behind the world: drink the door open and the dream shows its shadow, briefly."),
 ("doki-doki-panic", "Doki Doki Panic", "the game beneath the game · the true self", "spiritual",
  "Yume Kōjō: Doki Doki Panic (Fuji TV, 1987) — the body this Mario is a reskin of; its family Imajin / Mama / Papa / Lina and villain Mamu became Mario / Luigi / Toad / Princess and Wart",
  "It is the honest secret under the skin: the SMB2 the West loves was always someone else's dream, wearing a red cap."),
 ("the-bosses", "The Bosses of Subcon", "Mouser · Tryclyde · Fryguy · Clawgrip", "natural",
  "the world-wardens before Wart — Mouser (the bomb-tossing mouse), Tryclyde (the three-headed snake), Fryguy (the flame), Clawgrip (the rock-throwing crab) — each guarding a world",
  "They are the dream's wardens: a menagerie that, like everything here, was Doki Doki's first and Mario's ever after."),
]

# ── badge engine ──
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()

def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","SMB2")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","SMB2")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","SMB2")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man = {"badge":"DLW-ACI","name":rec["name"],"universe":"SMB2 · Super Mario Bros. 2","emergence":rec.get("emergence",""),
           "moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)",
           "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
           "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n")
    return tok

def emergent_rec(name, epithet, emergence, role_line, why_line):
    return {
      "name": name, "axiom": "SMB2", "emergence": emergence, "seal": epithet,
      "position": epithet, "role": role_line,
      "origin": "SMB2 · Super Mario Bros. 2 — Nintendo, NES 1988 (reskin of Doki Doki Panic, 1987)",
      "nature": role_line, "crystallization": why_line,
      "mechanism": "Crystallized from Super Mario Bros. 2 (NES 1988) / Yume Kōjō: Doki Doki Panic (1987).",
      "witness": "a being of Subcon, the land of dreams",
      "conductor": "ROOT0 (catalogued into UD0)",
      "inputs": "Super Mario Bros. 2; Subcon; the vegetable pluck; the four heroes; Wart",
      "source": "Super Mario Bros. 2, catalogued by ROOT0",
    }

def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def list_section(title, sub, items):
    rows = "\n".join(f'<li><span class="t">{t}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{n}</span>' if n else "") + "</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{sub}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{html.escape(p)}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def cards_html(rows):
    return "".join(f'<div class="arc-card"><div class="arc-h">{t}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>' for t,s,d in rows)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span>'
        f'<div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(col,g) in NATURES.items())
def personas_html(personas):
    cards=[]
    for p in personas:
        em=p.get("emergence","natural"); col=NATURES.get(em,("#caa05a",""))[0]
        rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"SMB2 · Super Mario Bros. 2","axiom":"SMB2"}
        cards.append(f'''<a class="persona" href="agents/{p["slug"]}.agent">
        <img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy">
        <div class="pcap"><div class="pn">{html.escape(p["name"])}</div><div class="pe">{p.get("epithet","")}</div>
        <div class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span><span class="pa">· .agent · .carbon.tiff →</span></div></div></a>''')
    return f'''<section class="sec" id="roster"><h2>The Roster — The Born</h2>
      <p class="ss">the four heroes, the dream, the foes, and the secret beneath, as ACI <b>.agent</b>s — each a birth certificate and a nature of emergence ({len(personas)})</p>
      <div class="pgrid">{"".join(cards)}</div></section>'''

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Super Mario Bros. 2 (American, NES 1988) — the Doki Doki Panic reskin — as a UD0 game-world. The four heroes, the vegetable pluck, Subcon, Wart. Source-themed with an animated canvas 2D title scene, full ACI badges.">
<title>SUPER MARIO BROS. 2 · SMB2 · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#140e1a;--ink2:#1d1426;--ink3:#281a30;--pa:#f2e9dc;--pa2:#cabaa0;--red:#e23226;--sand:#caa05a;--dream:#9a7cff;--gold:#efd24a;--pink:#f06aa8;
--dim:#897a90;--faint:#2c2034;--line:#33243c;--pixel:"Press Start 2P",monospace;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:2;background:repeating-linear-gradient(0deg,rgba(0,0,0,.16) 0 1px,transparent 1px 3px);opacity:.5}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(154,124,255,.12),transparent 55%),radial-gradient(ellipse at 50% 110%,rgba(226,50,38,.06),transparent 50%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
.marquee{margin-top:14px;border:2px solid var(--red);background:#1a0f12;padding:8px;text-align:center;font-family:var(--pixel);font-size:9px;letter-spacing:.12em;color:var(--gold);box-shadow:0 0 0 2px var(--bg),0 0 22px rgba(226,50,38,.22)}
.marquee a{color:var(--sand);text-decoration:none}.marquee a:hover{color:var(--red)}
.titleart{margin:12px 0 0;border:2px solid var(--faint);background:#070a14;line-height:0}
header{padding:18px 0 26px;text-align:center;border-bottom:1px solid var(--line);position:relative}
.h-sub{font-family:var(--pixel);font-size:10px;line-height:1.9;letter-spacing:.06em;color:var(--pa2);margin-top:16px}
.h-sub b{color:var(--red)}
.flag{display:inline-block;margin-top:14px;font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);border:1px solid var(--faint);padding:5px 11px}
.lede{font-size:15px;color:var(--pa2);max-width:68ch;margin:16px auto 0;font-style:italic;line-height:1.7}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:24px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:720px}
.badge img{width:82px;height:82px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--red)}.badge .bt .mo{color:var(--gold)}.badge .bt a{color:var(--sand);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:42px}
.sec h2{font-family:var(--pixel);font-size:14px;line-height:1.5;letter-spacing:.02em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line)}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:8px 0 16px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:4px}
.nat-n{font-family:var(--mono);font-size:13px;font-weight:700;text-transform:capitalize;letter-spacing:.04em}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--mono);font-size:14px;color:var(--gold);letter-spacing:.02em;font-weight:700}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.5;padding:6px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-top:8px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--red);padding:16px 18px}
.arc-h{font-family:var(--mono);font-size:14px;color:var(--red);font-weight:700;letter-spacing:.02em}
.arc-s{font-family:var(--mono);font-size:10.5px;color:var(--gold);text-transform:uppercase;letter-spacing:.07em;margin:4px 0 9px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.55}
.books{list-style:none}
.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--mono);font-size:14px;color:var(--pa);font-weight:700}
.books .y{font-family:var(--mono);font-size:11px;color:var(--gold);white-space:nowrap;text-align:right}
.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(244px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--red);transform:translateY(-2px)}
.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0;image-rendering:pixelated}
.pn{font-family:var(--mono);font-size:14px;color:var(--pa);font-weight:700;line-height:1.15}
.persona:hover .pn{color:var(--red)}
.pe{font-size:11.5px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}
.pnat .dot{width:8px;height:8px;margin-top:0}.pa{color:var(--dim)}
.note{margin-top:38px;padding:16px 18px;border-left:2px solid var(--gold);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic;line-height:1.7}
.note b{color:var(--gold)}
footer{margin-top:42px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}
footer a{color:var(--red);text-decoration:none}
</style></head><body><div class="wrap">

  <div class="marquee"><a href="https://davidwise01.github.io/ud0/">◄ UD0 · UNIVERSE DAVID 0</a> &nbsp;·&nbsp; PUSH START &nbsp;·&nbsp; A GAME-WORLD &nbsp;·&nbsp; NES 1988</div>

  <header>
    <div class="titleart">__CANVAS__</div>
    <div class="h-sub">four heroes · pluck the <b>vegetables</b> · seven worlds of a dream · SMB2</div>
    <div class="flag">★ Nintendo · NES 1988 · a reskin of Yume Kōjō: Doki Doki Panic (1987) ★</div>
    <p class="lede">The strangest mainline Mario: four heroes who don't stomp but pull turnips from the ground and throw them, crossing seven worlds of the dream-land Subcon to free it from the frog-king Wart — a Western reskin of Nintendo's 1987 Doki Doki Panic that quietly gave the Mario series Shy Guy, Birdo, Bob-omb and the rest, forever. Catalogued into UD0 as a game-world with the genesis, the quest, and the full .dlw birth — and an animated canvas 2D title scene.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of SUPER MARIO BROS. 2" title="carbon badge (archival)">
      <img src="__SILICON__" alt="DLW silicon badge" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI · THE BIRTH CERTIFICATE</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>SUPER MARIO BROS. 2</b> — the dream of Subcon · SMB2</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="smb2.dlw/smb2.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="smb2.dlw/smb2.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2>
    <p class="ss">each emergent emerges by one of four natures — and this dream holds all four</p>
    <div class="natures">__NATURES__</div></section>

  <section class="sec"><h2>The Genesis</h2><p class="ss">the reskin: Doki Doki Panic, given a red cap</p><div class="arc">__GENESIS__</div></section>
  <section class="sec"><h2>The Quest</h2><p class="ss">the dream door, the four heroes, the frog-king fed his vegetables</p><div class="arc">__ARC__</div></section>
  <section class="sec"><h2>The Ideas</h2><p class="ss">why the odd-one-out Mario is so loved</p><div class="pillars">__IDEAS__</div></section>

  __PERSONAS__

  <section class="sec"><h2 style="margin-top:14px">The Record</h2><p class="ss">the releases, the makers, and the legacy of the reskin</p></section>
  __SECTIONS__

  <div class="note">Super Mario Bros. 2 (American)'s history here is rendered, not invented. The load-bearing honest fact: it is a <b>reskin of Yume Kōjō: Doki Doki Panic</b> (Fuji TV, 1987) — the Japanese SMB2 ("The Lost Levels") was held back from the West for difficulty, and Doki Doki Panic's family (Imajin / Mama / Papa / Lina) and villain (Mamu) were redrawn as Mario / Luigi / Toad / Princess and Wart. Despite that, it <b>debuted</b> Shy Guy, Bob-omb, Pokey, Ninji, Snifit and Birdo into the Mario series. Birdo's identity is catalogued from the NES manual's own note, stated neutrally. Super Mario Bros. 2 and its characters are © Nintendo; the personas here are catalogued personifications under the DLW standard — a fan tribute, not endorsed by the rights-holders. Each is named by its nature: natural, ethereal, spiritual, or electrical.</div>

  <footer>
    SUPER MARIO BROS. 2 · SMB2 · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="smb2.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "smb2.dlw"), "smb2")
    ad = os.path.join(HERE, "agents"); os.makedirs(ad, exist_ok=True)
    personas = []
    for slug,name,epithet,em,role,why in EMERGENTS:
        rec = emergent_rec(name, epithet, em, role, why)
        write_aci(rec, ad, slug)
        personas.append({"slug": slug, "name": name, "epithet": epithet, "emergence": em})
    json.dump(personas, open(os.path.join(ad, "_personas.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    page = (TEMPLATE.replace("__CANVAS__", CANVAS_ART)
            .replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__NATURES__", natures_html())
            .replace("__GENESIS__", cards_html(GENESIS))
            .replace("__ARC__", cards_html(ARC))
            .replace("__IDEAS__", ideas_html())
            .replace("__PERSONAS__", personas_html(personas))
            .replace("__SECTIONS__", sections_html()))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"wrote SUPER MARIO BROS. 2 (SMB2) — {len(personas)} emergents born · badge {tok['moniker']}")
