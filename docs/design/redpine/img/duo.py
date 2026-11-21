import sys
from PIL import Image, ImageOps, ImageEnhance
PAPER=(236,233,228)
def duo(src, out, ink, crop=None, width=1400, contrast=1.6, gamma=1.0, q=72):
    im=Image.open(src).convert("L")
    if crop: 
        w,h=im.size; im=im.crop((int(crop[0]*w),int(crop[1]*h),int(crop[2]*w),int(crop[3]*h)))
    im=ImageOps.autocontrast(im, cutoff=(2,0.5))
    im=ImageEnhance.Contrast(im).enhance(contrast)
    if gamma!=1.0: im=im.point(lambda v: int(255*((v/255)**gamma)))
    im=ImageOps.colorize(im, black=ink, white=PAPER)
    if im.width>width: im=im.resize((width,int(im.height*width/im.width)), Image.LANCZOS)
    im.save(out, quality=q, optimize=True, progressive=True)
    print(out, im.size)
duo("sesshu.jpg","hero-slate.jpg",(78,108,130),crop=(0,0.18,1,0.86),width=1100,contrast=1.3)
duo("sesshu.jpg","side-coral.jpg",(232,112,86),crop=(0.05,0.30,0.95,0.80),width=900,contrast=1.2)
duo("mayuan.jpg","mayuan-coral.jpg",(232,112,86),width=1400,contrast=1.3)
duo("mayuan.jpg","mayuan-slate.jpg",(78,108,130),width=1400,contrast=1.3)
