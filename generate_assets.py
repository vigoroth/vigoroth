from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math
import html
import zipfile

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / 'assets'
ASSETS.mkdir(parents=True, exist_ok=True)
W, H = 1200, 360
BG = '#0b1020'
WHITE = '#edf2ff'
MUTED = '#9baecb'
CYAN = '#67e8f9'
VIOLET = '#a78bfa'
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
MONO = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'

def font(size, style=FONT):
    return ImageFont.truetype(style, size)

base = Image.new('RGB', (W,H), BG)
d = ImageDraw.Draw(base)
for y in range(H):
    d.line((0,y,W,y), fill=(11+int(y/H*3),16+int(y/H*4),32+int(y/H*6)))
for x in range(24,W,26):
    for y in range(24,H,26):
        if x > 720:
            d.point((x,y),fill='#233047')
d.rounded_rectangle((1,1,W-2,H-2),radius=20,outline='#28354e',width=2)
d.rounded_rectangle((42,35,268,65),radius=15,fill='#19273c')
d.ellipse((55,46,63,54),fill=CYAN)
d.text((73,40),'NICK / @VIGOROTH',font=font(14,MONO),fill=CYAN)
d.text((42,92),'Nick Kantiotis',font=font(57,BOLD),fill=WHITE)
d.text((45,169),'Data Scientist',font=font(27),fill=WHITE)
d.text((45,214),'AI AGENTS  /  MACHINE LEARNING  /  COMPUTER VISION',font=font(15,MONO),fill=MUTED)
d.line((45,282,687,282),fill='#2b3852',width=1)
d.text((45,302),'STATISTICS + COMPUTER SCIENCE',font=font(12,MONO),fill=MUTED)
d.text((496,302),'ATHENS, GREECE',font=font(12,MONO),fill=MUTED)

layers = [[(807,103),(807,177),(807,251)],[(918,76),(918,144),(918,212),(918,280)],[(1033,111),(1033,245)],[(1132,178)]]
edges = [(a,b) for left,right in zip(layers,layers[1:]) for a in left for b in right]
for a,b in edges:
    d.line((*a,*b),fill='#2b3a55',width=1)
d.text((795,315),'BUILD  /  EVALUATE  /  ITERATE',font=font(12,MONO),fill=MUTED)
frames=[]
N=84
for k in range(N):
    im=base.copy()
    draw=ImageDraw.Draw(im)
    phase=k/N
    for j,(a,b) in enumerate(edges):
        t=(phase*2+j*0.137)%1
        x=a[0]+(b[0]-a[0])*t
        y=a[1]+(b[1]-a[1])*t
        color=CYAN if j%2 else VIOLET
        draw.line((x-(b[0]-a[0])*0.075,y-(b[1]-a[1])*0.075,x,y),fill=color,width=2)
        draw.ellipse((x-2,y-2,x+2,y+2),fill='#f3fbff')
    for li,layer in enumerate(layers):
        for ni,(x,y) in enumerate(layer):
            r=6+2*math.sin(2*math.pi*(phase*2+li/5+ni/8))
            draw.ellipse((x-r-5,y-r-5,x+r+5,y+r+5),fill='#16263b',outline='#344665')
            draw.ellipse((x-r,y-r,x+r,y+r),fill=CYAN if li%2 else VIOLET)
            draw.ellipse((x-2,y-2,x+2,y+2),fill=WHITE)
    frames.append(im)
frames[20].save(ASSETS/'header-static.png',optimize=True)
palette=frames[20].quantize(colors=112)
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
    svg+='<rect x="1" y="1" width="618" height="216" rx="16" fill="#0e1626" stroke="#2b3852"/>'
    svg+=f'<rect x="23" y="26" width="38" height="30" rx="8" fill="#1c2940"/>'
    svg+=text(31,47,num,15,accent,'700')+text(77,47,kicker,15,MUTED)
    svg+=text(24,93,title,27,WHITE,'700')
    svg+=text(24,130,desc,18,MUTED)
    svg+=f'<line x1="24" y1="155" x2="596" y2="155" stroke="#27344d"/>'
    svg+=text(24,187,stack,15,accent)+text(511,187,'Explore →',14,accent)
    svg+='</svg>'
    (ASSETS/f'{slug}.svg').write_text(svg)

skills=[('Python','#ffd166'),('SQL','#67e8f9'),('PyTorch','#ff9a76'),('OpenCV','#98e5a1'),('LangGraph','#a78bfa'),('FastAPI','#67e8d0'),('DuckDB','#ffd166'),('Docker','#7cb9ff'),('Git','#ff9a76'),('Evaluation','#a78bfa')]
svg=svg_start(1200,120)
for i,(label,color) in enumerate(skills):
    row,col=divmod(i,5)
    x,y=col*240,row*60
    svg+=f'<rect x="{x+2}" y="{y+3}" width="226" height="46" rx="9" fill="#111c2e" stroke="#2b3852"/>'
    svg+=f'<circle cx="{x+20}" cy="{y+26}" r="4" fill="{color}"/>'
    svg+=text(x+35,y+33,label,20,WHITE)
svg+='</svg>'
(ASSETS/'stack.svg').write_text(svg)

