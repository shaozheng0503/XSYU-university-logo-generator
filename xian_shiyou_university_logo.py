import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, Arc
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import math

def draw_xian_shiyou_logo(size=800, save_path=None):
    """
    绘制西安石油大学校徽
    
    参数:
    size: 图像尺寸（像素）
    save_path: 保存路径（可选）
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
    outer_ring = Circle((50, 50), 45, fill=False, color=black, linewidth=3)
    ax.add_patch(outer_ring)
    
    # 2. 绘制内圆（深红色）
    inner_circle = Circle((50, 50), 35, fill=True, color=dark_red)
    ax.add_patch(inner_circle)
    
    # 3. 绘制中央标志（黑色）
    # 这是一个简化的 X 和 P 组合标志
    center_x, center_y = 50, 50
    
    # 绘制 X 形状
    x_points = np.array([
        [center_x - 8, center_y + 8],   # 左上
        [center_x + 8, center_y - 8],   # 右下
        [center_x - 8, center_y - 8],   # 左下
        [center_x + 8, center_y + 8]    # 右上
    ])
    
    # 绘制 X 的两条线
    ax.plot([x_points[0][0], x_points[1][0]], [x_points[0][1], x_points[1][1]], 
            color=black, linewidth=8, solid_capstyle='round')
    ax.plot([x_points[2][0], x_points[3][0]], [x_points[2][1], x_points[3][1]], 
            color=black, linewidth=8, solid_capstyle='round')
    
    # 绘制 P 形状（简化为一个弧形）
    p_arc = Arc((center_x + 2, center_y), width=12, height=16, 
                angle=0, theta1=180, theta2=360, 
                color=black, linewidth=8)
    ax.add_patch(p_arc)
    
    # 绘制小圆点（在 X 的左上角）
    dot = Circle((center_x - 6, center_y + 6), 1.5, fill=True, color=black)
    ax.add_patch(dot)
    
    # 4. 绘制文字
    # 中文文字（西安石油大学）
    chinese_text = "西安石油大学"
    ax.text(50, 85, chinese_text, fontsize=12, ha='center', va='center', 
            color=white, weight='bold', fontfamily='SimHei')
    
    # 英文文字（XI'AN SHIYOU UNIVERSITY）
    english_text = "XI'AN SHIYOU UNIVERSITY"
    ax.text(50, 15, english_text, fontsize=8, ha='center', va='center', 
            color=white, weight='bold')
    
    # 年份（1951）
    year_text = "1951"
    ax.text(50, 25, year_text, fontsize=10, ha='center', va='center', 
            color=white, weight='bold')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight', 
                   facecolor='white', edgecolor='none')
        print(f"校徽已保存到: {save_path}")
    
    # 关闭图形，避免显示问题
    plt.close(fig)
    return fig

def draw_logo_with_pil(size=800, save_path=None):
    """
    使用 PIL 绘制西安石油大学校徽（更精确的版本）
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
    draw.line([(center - x_size, center + x_size), 
               (center + x_size, center - x_size)], 
              fill=black, width=line_width)
    
    # X 的第二条线（左下到右上）
    draw.line([(center - x_size, center - x_size), 
               (center + x_size, center + x_size)], 
              fill=black, width=line_width)
    
    # P 形状（弧形）
    p_width = int(size * 0.12)
    p_height = int(size * 0.16)
    p_x = center + int(size * 0.02)
    p_y = center
    
    # 绘制 P 的弧形部分
    draw.arc([p_x - p_width//2, p_y - p_height//2, 
              p_x + p_width//2, p_y + p_height//2], 
             start=180, end=360, fill=black, width=line_width)
    
    # 小圆点
    dot_radius = int(size * 0.015)
    dot_x = center - int(size * 0.06)
    dot_y = center + int(size * 0.06)
    draw.ellipse([dot_x - dot_radius, dot_y - dot_radius, 
                  dot_x + dot_radius, dot_y + dot_radius], 
                 fill=black)
    
    # 4. 绘制文字
    try:
        # 尝试使用中文字体
        chinese_font = ImageFont.truetype("simhei.ttf", int(size * 0.06))
        english_font = ImageFont.truetype("arial.ttf", int(size * 0.04))
        year_font = ImageFont.truetype("arial.ttf", int(size * 0.05))
    except:
        # 如果找不到字体，使用默认字体
        chinese_font = ImageFont.load_default()
        english_font = ImageFont.load_default()
        year_font = ImageFont.load_default()
    
    # 中文文字
    chinese_text = "西安石油大学"
    chinese_bbox = draw.textbbox((0, 0), chinese_text, font=chinese_font)
    chinese_width = chinese_bbox[2] - chinese_bbox[0]
    chinese_x = center - chinese_width // 2
    chinese_y = int(size * 0.85)
    draw.text((chinese_x, chinese_y), chinese_text, fill=white, font=chinese_font)
    
    # 英文文字
    english_text = "XI'AN SHIYOU UNIVERSITY"
    english_bbox = draw.textbbox((0, 0), english_text, font=english_font)
    english_width = english_bbox[2] - english_bbox[0]
    english_x = center - english_width // 2
    english_y = int(size * 0.15)
    draw.text((english_x, english_y), english_text, fill=white, font=english_font)
    
    # 年份
    year_text = "1951"
    year_bbox = draw.textbbox((0, 0), year_text, font=year_font)
    year_width = year_bbox[2] - year_bbox[0]
    year_x = center - year_width // 2
    year_y = int(size * 0.25)
    draw.text((year_x, year_y), year_text, fill=white, font=year_font)
    
    if save_path:
        img.save(save_path)
        print(f"校徽已保存到: {save_path}")
    
    return img

def create_logo_variations():
    """
    创建不同尺寸的校徽版本
    """
    
    sizes = [512, 1024, 2048]
    
    for size in sizes:
        filename = f"西安石油大学-logo-{size}px.png"
        draw_logo_with_pil(size, filename)
        print(f"已创建 {size}x{size} 像素的校徽")

if __name__ == "__main__":
    print("正在绘制西安石油大学校徽...")
    
    # 绘制并显示校徽
    draw_xian_shiyou_logo(800, "西安石油大学-logo-matplotlib.png")
    
    # 使用 PIL 创建更精确的版本
    logo_img = draw_logo_with_pil(800, "西安石油大学-logo-pil.png")
    
    # 创建不同尺寸的版本
    create_logo_variations()
    
    print("校徽绘制完成！") 