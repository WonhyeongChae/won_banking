from pathlib import Path
import json
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import simpleSplit
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
pdfmetrics.registerFont(TTFont('Malgun','C:/Windows/Fonts/malgun.ttf'))
pdfmetrics.registerFont(TTFont('MalgunBold','C:/Windows/Fonts/malgunbd.ttf'))
data=json.loads((ROOT/'slides/content.json').read_text(encoding='utf-8'))
assert len(data['pages'])==5, 'Exactly five pages required'
out=ROOT/'output/pdf/proposal_skeleton.pdf'
out.parent.mkdir(parents=True,exist_ok=True)
W,H=841.89,595.28
c=canvas.Canvas(str(out),pagesize=(W,H))
c.setTitle('WON 플러스원 | 예선 제안서 작성용 뼈대')
def text(x,y,t,size=12,color='#10264D',bold=False,width=None):
    font='MalgunBold' if bold else 'Malgun'
    lines=simpleSplit(t,font,size,width) if width else [t]
    c.setFont(font,size);c.setFillColor(HexColor(color))
    for line in lines: c.drawString(x,y,line);y-=size*1.6
    return y
for i,p in enumerate(data['pages']):
    c.setFillColor(HexColor('#F3F8FE'));c.rect(0,0,W,H,fill=1,stroke=0)
    c.setFillColor(HexColor('#0067D8'));c.rect(0,H-10,W,10,fill=1,stroke=0)
    text(36,H-48,p['kicker'],10,'#0067D8',True)
    text(36,H-94,p['title'],25,bold=True)
    text(36,H-128,p['subtitle'],12,'#53657D')
    if i==0:
        c.drawImage(str(ROOT/'assets/originals/team_logo.png'),530,140,width=270,height=270,mask='auto')
        cw=460
    else: cw=W-72
    for j,(title,body) in enumerate(p['cards']):
        y=H-185-j*102
        c.setFillColor(HexColor('#FFFFFF'));c.roundRect(36,y-78,cw,90,12,fill=1,stroke=0)
        text(54,y-10,title,15,'#0067D8',True)
        last=text(54,y-37,body,12,width=cw-36)
        assert last>=y-78, 'Card text overflow: shorten content'
    text(36,61,'출처: 제공 공모전 포스터 / 본문 근거는 작성 후 추가',9,'#53657D')
    text(36,36,data['team']+'  |  '+data['status'],9,'#53657D')
    text(W-65,36,f'{i+1} / 5',9,'#53657D')
    c.showPage()
c.save()
r=PdfReader(str(out));assert len(r.pages)==5
assert all(p.extract_text() for p in r.pages)
print(f'Created {out} | 5 pages | text verified')
