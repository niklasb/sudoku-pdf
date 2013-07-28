N = 9
w = 595.0
h = 842.0
rows = 3
cols = 2
padding = 20.0
margin = 30.0

import cairo
import math
import sys

output = sys.argv[1]
inp = sys.stdin.read().split()
grids = []
for i in xrange(len(inp)/9):
  grids.append([map(int,l) for l in inp[i*9:(i+1)*9]])
surface = cairo.PDFSurface(output, w, h)

# background
def get_ctx():
  return cairo.Context(surface)
ctx = get_ctx()
ctx.set_source_rgb(1,1,1)
ctx.rectangle(0,0,w,h)
ctx.fill()

def line(x1,y1,x2,y2):
  ctx.move_to(x1,y1)
  ctx.line_to(x2,y2)

def draw(x1,y1,sz,grid):
  ctx.set_line_width(2)
  ctx.set_source_rgb(0, 0, 0)
  ctx.rectangle(x1, y1, sz, sz)
  ctx.stroke()

  ctx.set_line_width(0.1)
  ctx.set_source_rgb(0, 0, 0)
  for i in xrange(1,N):
    line(x1 + i*sz/N, y1, x1 + i*sz/N, y1 + sz)
    line(x1, y1 + i*sz/N, x1 + sz, y1 + i*sz/N)
  ctx.stroke()

  ctx.set_line_width(1.5)
  ctx.set_source_rgb(0, 0, 0)
  n = int(N**0.5)
  for i in xrange(n):
    for j in xrange(n):
      ctx.rectangle(x1 + i * sz/n, y1 + j * sz/n, sz/n, sz/n)
  ctx.stroke()

  ctx.set_font_size(sz/(N+4))
  for i in xrange(N):
    for j in xrange(N):
      if not grid[i][j]: continue
      txt = str(grid[i][j])
      ext = ctx.text_extents(txt)
      tw, th = ext[2], ext[3]
      ctx.move_to(x1 + j*sz/N + (sz/N-tw)/2 - 1, y1 + (i+1)*sz/N - (sz/N - th)/2)
      ctx.show_text(txt)

#
sz = min((w - (cols-1)*padding - 2*margin)/cols,
         (h - (rows-1)*padding - 2*margin)/rows)
xpad = (w - cols*sz - 2*margin)/(cols - 1)
ypad = (h - rows*sz - 2*margin)/(rows - 1)
y = margin
gi = 0
for i in xrange(rows):
  x = margin
  for j in xrange(cols):
    draw(x,y,sz,grids[gi])
    x += sz + xpad
    gi += 1
  y += sz + ypad

ctx.show_page()
