from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math
import html
import random

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT/'assets'
ASSETS.mkdir(parents=True,exist_ok=True)
W,H=1200,360
BG='#111111'
WHITE='#f3f4f6'
MUTED='#9ca3af'
CYAN=VIOLET='#34D399'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
MONO='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'

def font(size,style=FONT):
    # Linux defaults; a local .ttf with these names also works on other systems.
    for candidate in [style,Path(style).name,'DejaVuSans.ttf','Arial.ttf','arial.ttf']:
        try:
            return ImageFont.truetype(str(candidate),size)
        except OSError:
            continue
    return ImageFont.load_default(size=size)

base=Image.new('RGB',(W,H),BG)
d=ImageDraw.Draw(base)
d.rounded_rectangle((1,1,W-2,H-2),radius=20,outline='#333333',width=2)
d.rounded_rectangle((42,35,268,65),radius=15,fill='#1b2a22')
d.ellipse((55,46,63,54),fill=CYAN)
d.text((73,40),'NICK / @VIGOROTH',font=font(14,MONO),fill=CYAN)
d.text((42,92),'Nick Kantiotis',font=font(57,BOLD),fill=WHITE)
d.text((45,214),'AI AGENTS  /  MACHINE LEARNING  /  COMPUTER VISION',font=font(15,MONO),fill=MUTED)
d.line((45,282,687,282),fill='#333333',width=1)
d.text((45,302),'STATISTICS + COMPUTER SCIENCE',font=font(12,MONO),fill=MUTED)
d.text((496,302),'ATHENS, GREECE',font=font(12,MONO),fill=MUTED)
d.line((745,48,745,313),fill='#282e2b',width=1)
d.text((790,36),'[ DATA → INTELLIGENCE ]',font=font(13,MONO),fill=CYAN)
d.text((790,307),'BUILD / EVALUATE / ITERATE',font=font(13,MONO),fill=CYAN)
rng=random.Random(42)
chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
grid=[[rng.choice(chars) for row in range(15)] for col in range(22)]
frames=[]
N=84
role='Data Scientist'
for k in range(N):
    im=base.copy()
    draw=ImageDraw.Draw(im)
    phase=k/N
    if k<15:
        count=min(len(role),1+int(k/14*len(role)))
    elif k<75:
        count=len(role)
    else:
        count=max(1,int((84-k)/9*len(role)))
    label=role[:count]
    draw.text((45,169),label,font=font(27),fill=MUTED)
    if k<15 or k>=75 or k%12<6:
        x=45+draw.textlength(label,font=font(27))+5
        draw.rectangle((x,174,x+2,197),fill=CYAN)
    for col in range(22):
        head=(phase*15+col*2.731)%15
        for row in range(15):
            distance=(head-row)%15
            a=max(0,1-distance/7)
            color=tuple(int(17+(v-17)*a*0.73) for v in (52,211,153))
            x=790+col*16
            y=74+row*14
            draw.text((x,y),grid[col][row],font=font(11,MONO),fill=color)
        hy=74+head*14
        draw.text((790+col*16,hy),grid[col][int(head)],font=font(11,MONO),fill='#86efac')
    frames.append(im)
frames[40].save(ASSETS/'header-static.png',optimize=True)
palette=frames[40].quantize(colors=112)
indexed=[frame.quantize(palette=palette,dither=Image.Dither.NONE) for frame in frames]
indexed[0].save(ASSETS/'header.gif',save_all=True,append_images=indexed[1:],duration=[80,80,90]*28,loop=0,optimize=True,disposal=1)

def svg_start(width,height):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">'

def text(x,y,label,size=16,fill=MUTED,weight='400'):
    return f'<text x="{x}" y="{y}" font-family="DejaVu Sans,Arial,sans-serif" font-size="{size}" fill="{fill}" font-weight="{weight}">{html.escape(label)}</text>'

cards=[
 ('argus','01','Argus','An AI agent workspace','Tools, retrieval, memory and observability.','LangGraph / FastAPI / React',VIOLET),
 ('triage','02','Support Ticket Triage','Applied AI, evaluated','Classification and retrieval-grounded drafts.','RAG / Evaluation / Cost tracking',CYAN),
 ('data-agent','03','AI Data Analysis Agent','From questions to analysis','Plan, execute and report on tabular data.','Python / DuckDB / LangGraph',CYAN),
 ('segmentation','04','CT Image Segmentation','A model comparison study','U-Net and DeepLabV3+ on chest CT scans.','PyTorch / Optuna / Segmentation',VIOLET),
]
for slug,num,title,kicker,desc,stack,accent in cards:
    svg=svg_start(620,218)
    svg+='<rect x="1" y="1" width="618" height="216" rx="16" fill="#161616" stroke="#333333"/>'
    svg+=f'<rect x="23" y="26" width="38" height="30" rx="8" fill="#202b25"/>'
    svg+=text(31,47,num,15,accent,'700')+text(77,47,kicker,15,MUTED)
    svg+=text(24,93,title,27,WHITE,'700')
    svg+=text(24,130,desc,18,MUTED)
    svg+=f'<line x1="24" y1="155" x2="596" y2="155" stroke="#303b34"/>'
    svg+=text(24,187,stack,15,accent)+text(511,187,'Explore →',14,accent)
    svg+='</svg>'
    (ASSETS/f'{slug}.svg').write_text(svg)

skills=[(name, '#34D399') for name in ['Python','SQL','PyTorch','OpenCV','LangGraph','FastAPI','DuckDB','Docker','Git','Evaluation']]
svg=svg_start(1200,120)
for i,(label,color) in enumerate(skills):
    row,col=divmod(i,5)
    x,y=col*240,row*60
    svg+=f'<rect x="{x+2}" y="{y+3}" width="226" height="46" rx="9" fill="#191d1b" stroke="#333333"/>'
    svg+=f'<circle cx="{x+20}" cy="{y+26}" r="4" fill="{color}"/>'
    svg+=text(x+35,y+33,label,20,WHITE)
svg+='</svg>'
(ASSETS/'stack.svg').write_text(svg)

