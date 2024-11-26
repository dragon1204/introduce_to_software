import pygame as pg
import chesspieces as cp
board=cp.makeBoard();
print(board);
pg.init()
pg.display.set_caption("ChessProject1 - Mr.Long")
WIDTH=800
HEIGHT=800
cell_size = 87.5
screen = pg.display.set_mode([WIDTH,HEIGHT])
font = pg.font.Font('freesansbold.ttf',30)
font1 = pg.font.Font('freesansbold.ttf',20)
timer = pg.time.Clock()
fps = 60
#0- white no select, 1- white with select, 2 black no select, 3 black with select
turn_selection=0
run=True
valid_moves = []
mode=None

# các nút game mode
button_pvp_rect = pg.Rect(715, 28, 70, 40)
button_pvp_text = font.render('PvP',True, 'black')
pvp_text_rect = button_pvp_text.get_rect(center=button_pvp_rect.center)

button_pvb_rect = pg.Rect(715, 28 + cell_size, 70, 40)
button_pvb_text = font.render('PvB',True, 'black')
pvb_text_rect = button_pvb_text.get_rect(center=button_pvb_rect.center)

button_bvb_rect = pg.Rect(715, 28 + 2 * cell_size, 70, 40)
button_bvb_text = font.render('BvB',True, 'black')
bvb_text_rect = button_bvb_text.get_rect(center=button_bvb_rect.center)

button_new_rect = pg.Rect(715, 28 + 3 * cell_size, 70, 40)
button_new_text = font.render('New',True, 'black')
new_text_rect = button_new_text.get_rect(center=button_new_rect.center)

# vẽ bàn cờ
def drawboard(pg, screen):
    for row in range(8):
        for column in range(8):
            color = 'dark gray' if (row + column) % 2 == 0 else 'darkolivegreen'
            pg.draw.rect(screen, color, [column * 87.5, row * 87.5, 87.5, 87.5])
    pg.draw.rect(screen, 'light gray',[0,700,700,100])
    pg.draw.rect(screen, 'light gray',[700,0,100,800])
    pg.draw.rect(screen, 'darkslategray',[0,700,704,100],4)
    pg.draw.rect(screen, 'darkslategray',[700,0,100,800],4)
    status_text=['White Select','White Move','Black Select','Black Move']
    screen.blit(font.render(status_text[turn_selection],True,'black'),(240,720))
# vẽ các quân cờ, chỉnh kích thước, chỉnh vị trí các quân cờ   
def loadimage(t):
    # chỉnh đường dẫn linh ảnh
    # D:\GITHUP\Project1\ChessFull\image\Wbishop.png
    image_path = r"D:\GITHUP\Project1\ChessFull\image\\" + t.name + ".png"
    a = pg.image.load(image_path)
    
    if t.name == "Wpawn" or t.name == "Bpawn":
        a = pg.transform.scale(a, (52, 52))
        screen.blit(a, ( (8-t.location[1] ) * 87.5 + 18,(8-t.location[0] ) * 87.5 + 22))
    else:
        a = pg.transform.scale(a, (65, 65))
        screen.blit(a, ((8-t.location[1] ) * 87.5 + 10,(8-t.location[0] ) * 87.5 + 10))
def load_chess():
    for chess in board:
        loadimage(chess)
valid_moves=[]
def draw_game_over():
    text=font.render(f'{winner} won the game', True,'darkslategray')
    text2=font.render(f'press Enter to restart', True,'darkslategray')
    screen.blit(text,(210,210))
    screen.blit(text2,(210,310))
def checking():
    a=0
    b=0
    for p in board:
        if p.name=="WKing":
            a=1
        if p.name=="BKing":
            b=1
    return [a,b]

# vẽ nút
def drawbutton():
    pg.draw.rect(screen, 'olivedrab', button_pvp_rect)
    screen.blit(button_pvp_text, pvp_text_rect)
    pg.draw.rect(screen, 'olivedrab', button_pvb_rect)
    screen.blit(button_pvb_text, pvb_text_rect)
    pg.draw.rect(screen, 'olivedrab', button_bvb_rect)
    screen.blit(button_bvb_text, bvb_text_rect)
    pg.draw.rect(screen, 'olivedrab', button_new_rect)
    screen.blit(button_new_text, new_text_rect)

    textmode=font1.render(f'Game Mode : {mode}',True, 'black')
    screen.blit(textmode,(240,760))
pvp=False
pvb=False
bvb=False
while run:
    timer.tick(fps)
    screen.fill('dark gray')
    drawboard(pg,screen)
    drawbutton()
    load_chess()
    if checking()[0]==0 or checking()[1]==0:
        if(checking()[0]==0):
            winner="Black"
        else:
            winner="White"
        draw_game_over()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if button_pvp_rect.collidepoint(event.pos):
                mode="PVP"
                pvp=True
                pvb=False
                bvb=False
            if button_pvb_rect.collidepoint(event.pos):
                mode="PVB"
                pvp=False
                pvb=True
                bvb=False
            if button_bvb_rect.collidepoint(event.pos):
                mode="BVB"
                pvp=False
                pvb=False
                bvb=True
            if button_new_rect.collidepoint(event.pos):
                mode=None
                pvp=False
                pvb=False
                bvb=False
                board=board=cp.makeBoard()
                turn_selection=0
        if event.type==pg.KEYDOWN and (checking()[0]==0 or checking()[1]==0):
            if event.key==pg.K_RETURN:
                board=board=cp.makeBoard()
                turn_selection=0
#PVP
        if event.type == pg.MOUSEBUTTONDOWN and event.button ==1 and checking()[0]!=0 and checking()[1]!=0 and pvp:
            x_coord=event.pos[0]//87.5
            y_coord=event.pos[1]//87.5
            click_coord=[8-y_coord,8-x_coord]
            if turn_selection==0:
                print(turn_selection)
                for chess in board: 
                    if(chess.location==click_coord and chess.name[0]=="W"):
                        selection = chess
                        turn_selection=1
                        valid_moves=cp.validmoves(selection,board)
                        print(valid_moves)
                        break
                continue
            if turn_selection==1:
                print(selection.name, selection.location)
                print(turn_selection)
                print(valid_moves)
                print(click_coord)
                if click_coord in valid_moves :
                    for chess in board:
                        if(click_coord==chess.location):
                            board.remove(chess)
                    for chess in board:        
                        if(chess.location[0]==selection.location[0] and chess.location[1]==selection.location[1]):
                            chess.location=click_coord
                    turn_selection=2;
                    continue
                if turn_selection==1:
                    turn_selection=0  
                    continue    
            if turn_selection==2:
                print(turn_selection)
                for chess in board: 
                    if(chess.location==click_coord and chess.name[0]=="B"):
                        selection = chess
                        turn_selection=3
                        valid_moves=cp.validmoves(selection,board)
                        print(valid_moves)
                        break
                continue
            if turn_selection==3:
                print(selection.name, selection.location)
                print(turn_selection)
                print(valid_moves)
                print(click_coord)
                if click_coord in valid_moves :
                    for chess in board:
                        if(click_coord==chess.location):
                            board.remove(chess)
                        if(chess.location[0]==selection.location[0] and chess.location[1]==selection.location[1]):
                            chess.location=click_coord
                    turn_selection=0;
                    continue
                if turn_selection==3:
                    turn_selection=2  
                    continue 
#pvb
        if event.type == pg.MOUSEBUTTONDOWN and event.button ==1 and (checking()[0]!=0 or checking()[1]!=0) and pvb:
            x_coord=event.pos[0]//87.5
            y_coord=event.pos[1]//87.5
            click_coord=[8-y_coord,8-x_coord]
            if turn_selection==0:
                #print(turn_selection)
                for chess in board: 
                    if(chess.location==click_coord and chess.name[0]=="W"):
                        selection = chess
                        turn_selection=1
                        valid_moves=cp.validmoves(selection,board)
                        #print(valid_moves)
                        break
                continue
            if turn_selection==1:
                #print(selection.name, selection.location)
                #print(turn_selection)
                #print(valid_moves)
                #print(click_coord)
                print("next")
                if click_coord in valid_moves :
                    for chess in board:
                        if(click_coord==chess.location):
                            board.remove(chess)
                            break
                    for chess in board:
                        if(chess.location[0]==selection.location[0] and chess.location[1]==selection.location[1]):
                            chess.location=click_coord
                            break
                    turn_selection=2
                    screen.fill('dark gray')
                    drawboard(pg,screen)
                    load_chess()
                    continue
                if turn_selection==1:
                    turn_selection=0  
                    continue 
    if turn_selection==2 and (checking()[0]!=0 or checking()[1]!=0) and pvb:
        board=cp.makeMove(board)
        turn_selection=0
        continue     
#bvb
    if turn_selection==0 and (checking()[0]!=0 and checking()[1]!=0) and bvb:
        board=cp.makeMoveW(board)
        turn_selection=2
        continue 
    pg.display.flip()
    if turn_selection==2 and (checking()[0]!=0 and checking()[1]!=0) and bvb:
        board=cp.makeMove(board)
        turn_selection=0
        continue     
            
    pg.display.flip()
pg.quit()