"""
把 04-authenticator-modal.png 的二维码区域遮住,加 'AI潮汐慢学习' 水印
"""
from PIL import Image, ImageDraw, ImageFont

SRC = '/tmp/codex-bypass-login/assets/04-authenticator-modal.png'
DST = SRC  # 覆盖原图

img = Image.open(SRC).convert('RGBA')
w, h = img.size  # 1368 x 1182
print(f'原图: {w}x{h}')

# QR 在图正中(弹窗内居中),覆盖范围 1000x900 绝对足够
qr_w = 1000
qr_h = 900
qr_cx = w // 2
qr_cy = int(h * 0.50)
x1 = qr_cx - qr_w // 2
y1 = qr_cy - qr_h // 2
x2 = x1 + qr_w
y2 = y1 + qr_h
print(f'覆盖区域: ({x1},{y1}) - ({x2},{y2})')

# 完全不透明白色遮罩(255 alpha) + 绿色边框
overlay = Image.new('RGBA', img.size, (255, 255, 255, 0))
od = ImageDraw.Draw(overlay)
od.rounded_rectangle([x1, y1, x2, y2], radius=16,
                     fill=(255, 255, 255, 255),
                     outline=(16, 163, 127, 255), width=4)
img.alpha_composite(overlay)

# 写字
draw = ImageDraw.Draw(img)
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
try:
    f_big = ImageFont.truetype(font_path, 80)
    f_mid = ImageFont.truetype(font_path, 48)
    f_sm = ImageFont.truetype(font_path, 32)
except Exception as e:
    print(f'字体加载失败: {e}')
    f_big = f_mid = f_sm = ImageFont.load_default()

cx = (x1 + x2) // 2
cy = (y1 + y2) // 2

# 锁 emoji + 二维码已隐藏
draw.text((cx, cy - 200), '🔒', fill='#374151', anchor='mm', font_size=120)
draw.text((cx, cy - 60), '二维码已隐藏', fill='#1f2937', anchor='mm', font=f_big)
draw.text((cx, cy + 30), '(为保护账号信息)', fill='#6b7280', anchor='mm', font=f_sm)

# 分隔线
draw.line([(x1 + 100, cy + 100), (x2 - 100, cy + 100)], fill='#e5e7eb', width=3)

# 宣传文字
draw.text((cx, cy + 180), 'AI 潮汐慢学习', fill='#10a37f', anchor='mm', font=f_big)
draw.text((cx, cy + 270), '扫码加微信一起玩', fill='#374151', anchor='mm', font=f_mid)

# 保存
img.convert('RGB').save(DST, 'PNG', optimize=True)
print(f'已保存: {DST}')

covered_pct = (qr_w * qr_h) / (w * h) * 100
print(f'覆盖区域占原图 {covered_pct:.1f}%')
