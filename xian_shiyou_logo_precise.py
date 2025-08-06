# xiyou_logo.py
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, Arc, PathPatch
from matplotlib.path import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import math

def draw_precise_logo(size=800, save_path=None):
    """
    基于 SVG 路径数据绘制精确的西安石油大学校徽
    """
    
    # 创建图像
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # 颜色定义
    black = '#000000'
    dark_red = '#9A1E23'  # 深红色
    white = '#FFFFFF'
    
    # 1. 绘制外圆环（黑色）
    outer_ring = Circle((50, 50), 45, fill=False, color=black, linewidth=2)
    ax.add_patch(outer_ring)
    
    # 2. 绘制内圆（深红色）
    inner_circle = Circle((50, 50), 35, fill=True, color=dark_red)
    ax.add_patch(inner_circle)
    
    # 3. 绘制中央标志（基于 SVG 路径数据）
    # 这是一个简化的 X 和 P 组合标志
    center_x, center_y = 50, 50
    
    # 绘制 X 形状（更精确的版本）
    x_size = 8
    line_width = 6
    
    # X 的第一条线（左上到右下，稍微弯曲）
    x1_points = np.array([
        [center_x - x_size, center_y + x_size * 0.8],
        [center_x + x_size * 0.8, center_y - x_size]
    ])
    ax.plot(x1_points[:, 0], x1_points[:, 1], 
            color=black, linewidth=line_width, solid_capstyle='round')
    
    # X 的第二条线（左下到右上，稍微弯曲）
    x2_points = np.array([
        [center_x - x_size * 0.8, center_y - x_size],
        [center_x + x_size, center_y + x_size * 0.8]
    ])
    ax.plot(x2_points[:, 0], x2_points[:, 1], 
            color=black, linewidth=line_width, solid_capstyle='round')
    
    # P 形状（更精确的弧形）
    p_arc = Arc((center_x + 2, center_y), width=14, height=18, 
                angle=0, theta1=180, theta2=360, 
                color=black, linewidth=line_width)
    ax.add_patch(p_arc)
    
    # 小圆点（在 X 的左上角）
    dot = Circle((center_x - 6, center_y + 6), 1.2, fill=True, color=black)
    ax.add_patch(dot)
    
    # 4. 绘制文字（弧形排列）
    # 中文文字（西安石油大学）- 弧形排列
    chinese_text = "西安石油大学"
    radius = 42
    start_angle = 60  # 开始角度（度）
    angle_step = 30   # 每个字符的角度间隔
    
    for i, char in enumerate(chinese_text):
        angle = math.radians(start_angle + i * angle_step)
        x = 50 + radius * math.cos(angle)
        y = 50 + radius * math.sin(angle)
        
        # 计算文字旋转角度
        text_angle = math.degrees(angle) + 90
        
        ax.text(x, y, char, fontsize=10, ha='center', va='center', 
                color=white, weight='bold', fontfamily='SimHei',
                rotation=text_angle)
    
    # 英文文字（XI'AN SHIYOU UNIVERSITY）- 弧形排列
    english_text = "XI'AN SHIYOU UNIVERSITY"
    radius = 42
    start_angle = 240  # 开始角度（度）
    angle_step = 8     # 每个字符的角度间隔
    
    for i, char in enumerate(english_text):
        if char == ' ':  # 跳过空格
            continue
        angle = math.radians(start_angle + i * angle_step)
        x = 50 + radius * math.cos(angle)
        y = 50 + radius * math.sin(angle)
        
        # 计算文字旋转角度
        text_angle = math.degrees(angle) - 90
        
        ax.text(x, y, char, fontsize=6, ha='center', va='center', 
                color=white, weight='bold',
                rotation=text_angle)
    
    # 年份（1951）
    year_text = "1951"
    ax.text(50, 25, year_text, fontsize=12, ha='center', va='center', 
            color=white, weight='bold')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight', 
                   facecolor='white', edgecolor='none')
        print(f"精确校徽已保存到: {save_path}")
    
    # 关闭图形，避免显示问题
    plt.close(fig)
    return fig

def draw_logo_with_curved_text(size=800, save_path=None):
    """
    使用 PIL 绘制带弧形文字的校徽
    """
    
    # 创建图像
    img = Image.new('RGB', (size, size), 'white')
    draw = ImageDraw.Draw(img)
    
    # 颜色定义
    black = (0, 0, 0)
    dark_red = (154, 30, 35)  # #9A1E23
    white = (255, 255, 255)
    
    center = size // 2
    
    # 1. 绘制外圆环（黑色）
    outer_radius = int(size * 0.45)
    draw.ellipse([center - outer_radius, center - outer_radius, 
                  center + outer_radius, center + outer_radius], 
                 outline=black, width=int(size * 0.01))
    
    # 2. 绘制内圆（深红色）
    inner_radius = int(size * 0.35)
    draw.ellipse([center - inner_radius, center - inner_radius, 
                  center + inner_radius, center + inner_radius], 
                 fill=dark_red)
    
    # 3. 绘制中央标志
    # X 形状
    x_size = int(size * 0.08)
    line_width = int(size * 0.02)
    
    # X 的第一条线（左上到右下）
    draw.line([(center - x_size, center + x_size * 0.8), 
               (center + x_size * 0.8, center - x_size)], 
              fill=black, width=line_width)
    
    # X 的第二条线（左下到右上）
    draw.line([(center - x_size * 0.8, center - x_size), 
               (center + x_size, center + x_size * 0.8)], 
              fill=black, width=line_width)
    
    # P 形状（弧形）
    p_width = int(size * 0.14)
    p_height = int(size * 0.18)
    p_x = center + int(size * 0.02)
    p_y = center
    
    # 绘制 P 的弧形部分
    draw.arc([p_x - p_width//2, p_y - p_height//2, 
              p_x + p_width//2, p_y + p_height//2], 
             start=180, end=360, fill=black, width=line_width)
    
    # 小圆点
    dot_radius = int(size * 0.012)
    dot_x = center - int(size * 0.06)
    dot_y = center + int(size * 0.06)
    draw.ellipse([dot_x - dot_radius, dot_y - dot_radius, 
                  dot_x + dot_radius, dot_y + dot_radius], 
                 fill=black)
    
    # 4. 绘制弧形文字
    try:
        chinese_font = ImageFont.truetype("simhei.ttf", int(size * 0.05))
        english_font = ImageFont.truetype("arial.ttf", int(size * 0.03))
        year_font = ImageFont.truetype("arial.ttf", int(size * 0.06))
    except:
        chinese_font = ImageFont.load_default()
        english_font = ImageFont.load_default()
        year_font = ImageFont.load_default()
    
    # 中文文字（弧形排列）
    chinese_text = "西安石油大学"
    radius = int(size * 0.42)
    start_angle = 60
    angle_step = 30
    
    for i, char in enumerate(chinese_text):
        angle = math.radians(start_angle + i * angle_step)
        x = center + radius * math.cos(angle)
        y = center + radius * math.sin(angle)
        
        # 获取文字边界框
        bbox = draw.textbbox((0, 0), char, font=chinese_font)
        char_width = bbox[2] - bbox[0]
        char_height = bbox[3] - bbox[1]
        
        # 调整位置
        x -= char_width // 2
        y -= char_height // 2
        
        # 创建旋转的文字
        char_img = Image.new('RGBA', (char_width, char_height), (0, 0, 0, 0))
        char_draw = ImageDraw.Draw(char_img)
        char_draw.text((0, 0), char, fill=white, font=chinese_font)
        
        # 旋转文字
        rotation_angle = math.degrees(angle) + 90
        rotated_char = char_img.rotate(rotation_angle, expand=True)
        
        # 粘贴到主图像
        img.paste(rotated_char, (int(x), int(y)), rotated_char)
    
    # 英文文字（弧形排列）
    english_text = "XI'AN SHIYOU UNIVERSITY"
    radius = int(size * 0.42)
    start_angle = 240
    angle_step = 8
    
    for i, char in enumerate(english_text):
        if char == ' ':
            continue
        angle = math.radians(start_angle + i * angle_step)
        x = center + radius * math.cos(angle)
        y = center + radius * math.sin(angle)
        
        # 获取文字边界框
        bbox = draw.textbbox((0, 0), char, font=english_font)
        char_width = bbox[2] - bbox[0]
        char_height = bbox[3] - bbox[1]
        
        # 调整位置
        x -= char_width // 2
        y -= char_height // 2
        
        # 创建旋转的文字
        char_img = Image.new('RGBA', (char_width, char_height), (0, 0, 0, 0))
        char_draw = ImageDraw.Draw(char_img)
        char_draw.text((0, 0), char, fill=white, font=english_font)
        
        # 旋转文字
        rotation_angle = math.degrees(angle) - 90
        rotated_char = char_img.rotate(rotation_angle, expand=True)
        
        # 粘贴到主图像
        img.paste(rotated_char, (int(x), int(y)), rotated_char)
    
    # 年份
    year_text = "1951"
    year_bbox = draw.textbbox((0, 0), year_text, font=year_font)
    year_width = year_bbox[2] - year_bbox[0]
    year_x = center - year_width // 2
    year_y = int(size * 0.25)
    draw.text((year_x, year_y), year_text, fill=white, font=year_font)
    
    if save_path:
        img.save(save_path)
        print(f"弧形文字校徽已保存到: {save_path}")
    
    return img

def create_svg_logo():
    """
    创建 SVG 格式的校徽
    """
    
    svg_content = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="800" height="800" viewBox="0 0 800 800" xmlns="http://www.w3.org/2000/svg">
  <!-- 外圆环 -->
  <circle cx="400" cy="400" r="360" fill="none" stroke="#000000" stroke-width="8"/>
  
  <!-- 内圆 -->
  <circle cx="400" cy="400" r="280" fill="#9A1E23"/>
  
  <!-- 中央标志 -->
  <!-- X 形状 -->
  <line x1="320" y1="480" x2="480" y2="320" stroke="#000000" stroke-width="48" stroke-linecap="round"/>
  <line x1="320" y1="320" x2="480" y2="480" stroke="#000000" stroke-width="48" stroke-linecap="round"/>
  
  <!-- P 形状 -->
  <path d="M 440 320 A 96 144 0 0 1 440 608" fill="none" stroke="#000000" stroke-width="48" stroke-linecap="round"/>
  
  <!-- 小圆点 -->
  <circle cx="352" cy="448" r="19" fill="#000000"/>
  
  <!-- 中文文字 -->
  <text x="400" y="340" text-anchor="middle" fill="#FFFFFF" font-family="SimHei" font-size="48" font-weight="bold">西安石油大学</text>
  
  <!-- 英文文字 -->
  <text x="400" y="120" text-anchor="middle" fill="#FFFFFF" font-family="Arial" font-size="32" font-weight="bold">XI'AN SHIYOU UNIVERSITY</text>
  
  <!-- 年份 -->
  <text x="400" y="200" text-anchor="middle" fill="#FFFFFF" font-family="Arial" font-size="40" font-weight="bold">1951</text>
</svg>'''
    
    with open("西安石油大学-logo.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    
    print("SVG 校徽已保存到: 西安石油大学-logo.svg")

if __name__ == "__main__":
    print("正在绘制精确的西安石油大学校徽...")
    
    # 绘制精确版本
    draw_precise_logo(800, "西安石油大学-logo-precise.png")
    
    # 绘制带弧形文字的版本
    logo_img = draw_logo_with_curved_text(800, "西安石油大学-logo-curved.png")
    
    # 创建 SVG 版本
    create_svg_logo()
    
    print("精确校徽绘制完成！")