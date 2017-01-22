from pygame import*
from random import randint
from time import gmtime, strftime
init()

#Color Stuff
red = (255,0,100)
green = (0,255,100)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
darkBlue = (0,120,122)
pink = (255,200,200)
#setup
screenSize=[400,600]
screenColor=(white)
screen=display.set_mode(screenSize)
font =font.Font(None, 25)
display.set_caption("Piano")
#var
music1=[]
music2=[]
music3=[]
music=music1
lose=0
score=0
s=0
text = font.render("Start", 1, darkBlue)
text1 = font.render("Score: ", 1, green)
text10 = font.render("othe maps 1 ,2 ,3 ", 1, pink)
#-----Musics g------
def mapcreator():
	global music,music1,music2,music3
	for i in range(1000):
		music1.append(randint(0, 3))
		music2.append(randint(0, 3))
		music3.append(randint(0, 3))
mapcreator()
#----Corect-------
def corect(use,machine):
	if use==machine:
		return(1)
	return(0)
#----Loser--------
def loser(x):
	global lose
	
	if x==0:
		lose=1
		mapcreator()
	else:
		lose=0
#------Main-----
screen.fill(white)
while True:
	screen.fill(white)
	while lose==0:
		t1=int(strftime("%S"))
		print(t1)
		textTime = font.render(str(t1), 1, green)
		text = font.render(str(score), 1, green)
		screen.blit(text,(90,5))
		screen.blit(text1,(25,5))
		screen.blit(textTime,(120,5))
		screen.blit(text10,(200,5))
		draw.rect(screen,darkBlue,(0,25,400,10))

		draw.rect(screen, black, (music[0]*100,450,100,150))
		draw.rect(screen, black, (music[1]*100,300,100,150)) 
		draw.rect(screen, black, (music[2]*100,150,100,150))
		draw.rect(screen, black, (music[3]*100,50,100,100)) 
		
		
		
		for e in event.get():
			if e.type==KEYDOWN:
				if e.key==K_q:
					loser(corect(0, music[0]))
					if music[0]==0:
						score+=1
						screen.fill(white)
						music.pop(0)
				if e.key==K_w :
					loser(corect(1, music[0]))

					if music[0]==1:
						score+=1
						screen.fill(white)
						music.pop(0)
				if e.key==K_e :
					loser(corect(2, music[0]))

					if music[0]==2:
						score+=1
						screen.fill(white)
						music.pop(0)
				if e.key==K_r : 
					loser(corect(3, music[0]))

					if  music[0]==3:
						score+=1
						screen.fill(white)
						music.pop(0)
				if e.key==K_1:
					s=0
					music=music1
					screen.fill(white)
					print(music)
				if e.key==K_2:
					s=0
					music=music2
					screen.fill(white)
					print(music)
				if e.key==K_3:
					s=0
					music=music3
					screen.fill(white)
					print(music)
			if e.type==QUIT :
				quit()
			
		display.update()
	#f =font.Font(None, 50)
	text2 = font.render("loser your Score is:", 1, green)
	text3 = font.render(str(score), 1, green)
	text4 = font.render("For refresh the game type char ' x'", 1, white)
	while lose==1:
		score=0
		screen.fill(red)
		screen.blit(text2,(90,200))
		screen.blit(text3,(280,200))
		screen.blit(text4,(10,300))
		for e in event.get():
			if e.type==KEYDOWN:
				if e.key==K_x:
					lose=0
			if e.type==QUIT :
				quit()
				
			
		display.update()
