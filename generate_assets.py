import os
import math
import subprocess
import sys

# Ensure PIL is installed
try:
    from PIL import Image, ImageDraw
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
    from PIL import Image, ImageDraw

os.makedirs('images', exist_ok=True)

# 1. Generate Custom SVG Banner
svg_content = """<svg width="1000" height="250" viewBox="0 0 1000 250" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad" x1="0" y1="0" x2="1000" y2="250" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#FF512F"/>
      <stop offset="100%" stop-color="#DD2476"/>
    </linearGradient>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="1000" height="250" rx="20" fill="url(#grad)"/>
  <rect width="1000" height="250" rx="20" fill="url(#grid)"/>
  <text x="500" y="110" font-family="Arial, Helvetica, sans-serif" font-size="46" font-weight="900" fill="#FFFFFF" text-anchor="middle">Awesome Masked Autoencoders</text>
  <text x="500" y="160" font-family="Arial, Helvetica, sans-serif" font-size="24" font-weight="600" fill="#FFFFFF" opacity="0.9" text-anchor="middle">&amp; Self-Supervised Learning</text>
  
  <!-- Decorative rotating tech nodes -->
  <g transform="translate(150, 125)">
    <circle cx="0" cy="0" r="50" stroke="white" stroke-width="4" stroke-dasharray="15 15" fill="none" opacity="0.6">
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="15s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="0" r="30" fill="white" opacity="0.2"/>
  </g>
  <g transform="translate(850, 125)">
    <circle cx="0" cy="0" r="50" stroke="white" stroke-width="4" stroke-dasharray="15 15" fill="none" opacity="0.6">
      <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="15s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="0" r="30" fill="white" opacity="0.2"/>
  </g>
</svg>"""

with open("images/banner.svg", "w") as f:
    f.write(svg_content)

# 2. Generate Custom Animated GIF (Neural Network Pulsing)
width, height = 1000, 150
frames = []
for i in range(40):
    # Dark modern background
    img = Image.new('RGB', (width, height), color=(13, 17, 23))
    draw = ImageDraw.Draw(img)
    
    # Pulse calculation for animation
    pulse = math.sin(i * math.pi / 20) * 8
    
    # Define network nodes
    nodes = [(150, 75), (350, 35), (350, 115), (650, 35), (650, 115), (850, 75)]
    
    # Draw connection edges
    for n1 in nodes:
        for n2 in nodes:
            if n1 != n2 and abs(n1[0] - n2[0]) <= 300:
                draw.line([n1, n2], fill=(88, 166, 255), width=2)
                
    # Draw pulsing nodes
    for idx, (nx, ny) in enumerate(nodes):
        r = 12 + (pulse if idx % 2 == 0 else -pulse)
        draw.ellipse((nx-r, ny-r, nx+r, ny+r), fill=(221, 36, 118))
        
    frames.append(img)

# Save as GIF
frames[0].save('images/neural_network.gif', save_all=True, append_images=frames[1:], duration=50, loop=0)
print("Banner SVG and Neural Network GIF generated successfully!")
