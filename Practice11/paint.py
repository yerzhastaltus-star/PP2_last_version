import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    clock = pygame.time.Clock()
    canvas = pygame.Surface((1200, 600))
    canvas.fill((255, 255, 255))
    
    radius = 15
    mode = 'blue'
    points = []
    strokes = [] 
    figures = []
    drawing = True
    drawing_mode = 1
    fig_start = 0
    text = "P = Stop/Draw\n" \
           "Z = Rectangle | X = Circle\n" \
           "E = Square | T = Right Triangle\n" \
           "F = Equilateral Triangle | R = Rhombus\n" \
           "L = Line | C = Eraser | A = Clear"
    r = pygame.Rect(30, 150, 30, 30)
    g = pygame.Rect(30, 200, 30, 30)
    b = pygame.Rect(30, 250, 30, 30)
    while True:
        pressed = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_p:
                    drawing = not drawing
            
                # determine if a letter key was pressed
                
                elif event.key == pygame.K_c:
                    mode = 'erase'
                    drawing_mode = 1
                    points = []
                elif event.key == pygame.K_l:
                    drawing_mode = 1
                elif event.key == pygame.K_z:
                    drawing_mode = 2
                elif event.key == pygame.K_x:
                    drawing_mode = 3 
                elif event.key == pygame.K_e:
                    drawing_mode = 4  # square
                elif event.key == pygame.K_t:
                    drawing_mode = 5  # right triangle
                elif event.key == pygame.K_f:
                    drawing_mode = 6  # equilateral triangle
                elif event.key == pygame.K_r:
                    drawing_mode = 7  # rhombus
                elif event.key == pygame.K_a:
                    strokes = []
                    points = [] 
                    canvas.fill((0, 0, 0))
            
                    

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    if drawing_mode in (2,3,4,5,6,7):
                        fig_start = mouse_pos
                    radius = min(200, radius + 1)
                    
                    if drawing_mode == 1:
                        if points and mode != 'erase':
                            strokes.append((points.copy(), mode, radius))
                    points = []   # start a new continuous line
                    
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
                if g.collidepoint(mouse_pos) or r.collidepoint(mouse_pos) or b.collidepoint(mouse_pos):
                    print("Button Clicked!")
                if r.collidepoint(mouse_pos):
                    mode = 'red'
                    if points and mode != 'erase':
                        strokes.append((points.copy(), mode, radius))
                    points = []   # start a new continuous line
                elif g.collidepoint(mouse_pos):
                    mode = 'green'
                    if points and mode != 'erase':
                        strokes.append((points.copy(), mode, radius))
                    points = []   # start a new continuous line
                elif b.collidepoint(mouse_pos):
                    mode = 'blue'
                    if points and mode != 'erase':
                        strokes.append((points.copy(), mode, radius))
                    points = []   # start a new continuous line
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and (points or figures):
                    if drawing_mode == 1:
                        if mode != 'erase':
                            strokes.append((points.copy(), mode, radius))
                        points = []
                    if drawing_mode in (2,3,4,5,6,7):
                        if figures:
                            st, et = figures[0]
                            drawfig(canvas, 0, st, et, radius, mode, drawing_mode)
                        figures = []
                
                    
            
            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0]:   # Left mouse button is held
                    if drawing_mode == 1:
                        position = event.pos
                        points = points + [position]
                        points = points[-256:]
                    if drawing_mode in (2,3,4,5,6,7):
                        figures = [(fig_start, mouse_pos)]
                
                
        screen.fill((255, 255, 255))
        screen.blit(canvas, (0, 0))

        


        # --- Draw the current stroke (if drawing is enabled) ---
        if drawing:
            if drawing_mode == 1 and len(points) > 1:
                # draw only the LAST segment to avoid multiple redraws
                drawLineBetween(canvas, 0, points[-2], points[-1], radius, mode)
            elif drawing_mode in (2,3,4,5,6,7) and figures and mode != 'erase':
                s,e = figures[0]
                # preview figure ONLY on screen (not canvas)
                drawfig(screen, 0, s, e, radius, mode, drawing_mode)
            
        font = pygame.font.SysFont(None, 26)

        # split text into lines and draw each line separately
        lines = text.split("\n")
        y_offset = 5
        for line in lines:
            p_text = font.render(line, True, (0, 0, 0))
            screen.blit(p_text, (10, y_offset))
            y_offset += 20

        pygame.draw.rect(screen, (0, 0, 255), b)
        pygame.draw.rect(screen, (255, 0, 0), r)
        pygame.draw.rect(screen, (0, 255, 0), g)
        pygame.display.flip()
        
        clock.tick(60)

def drawfig(screen, index, start, end, width, color_mode, draw_mode):
    x1, y1 = start
    x2, y2 = end
    r = int(((x2-x1)**2 + (y2-y1)**2) ** 0.5 / 2)
    c1 = max(0, min(255, r - 256))
    c2 = max(0, min(255, r))
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'erase':
        color = (0,0,0)
    
    
    if draw_mode == 2:
        rect = pygame.Rect(min(x1,x2), min(y1,y2), abs(x2-x1), abs(y2-y1))
        pygame.draw.rect(screen, color, rect, width)
    elif draw_mode == 3:
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2
        r = int(((x2-x1)**2 + (y2-y1)**2) ** 0.5 / 2)
        pygame.draw.circle(screen, color, (cx, cy), max(1, r), width)
    elif draw_mode == 4:
        # square
        size = max(abs(x2-x1), abs(y2-y1))
        rect = pygame.Rect(x1, y1, size, size)
        pygame.draw.rect(screen, color, rect, width)

    elif draw_mode == 5:
        # right triangle
        points = [(x1, y1), (x2, y1), (x1, y2)]
        pygame.draw.polygon(screen, color, points, width)

    elif draw_mode == 6:
        # equilateral triangle
        import math
        side = abs(x2 - x1)
        height = int((math.sqrt(3)/2) * side)
        points = [
            (x1, y1),
            (x1 + side, y1),
            (x1 + side//2, y1 - height)
        ]
        pygame.draw.polygon(screen, color, points, width)

    elif draw_mode == 7:
        # rhombus
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2
        dx = abs(x2 - x1) // 2
        dy = abs(y2 - y1) // 2
        points = [
            (cx, cy - dy),
            (cx + dx, cy),
            (cx, cy + dy),
            (cx - dx, cy)
        ]
        pygame.draw.polygon(screen, color, points, width)


def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'erase':
        color = (255, 255, 255)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)
    
        
        
main()