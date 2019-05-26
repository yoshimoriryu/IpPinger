import time
import pygame
import socket

def statusCheck(input):
    if input == "T":
        return "O"
    else:
        return "X"

def statusColor(status):
    if status == "O":
        return green
    else:
        return red

def quitgame():
    pygame.quit()
    quit()
    
#screen size
width, height = 720, 720

#color RGB
black = (0,0,0)
white = (255,255,255)
grey = (125,125,125)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
block_color = (53,115,255)

pygame.init()
#font used
theFont=pygame.font.Font(None,72)
theFont2=pygame.font.Font(None,55)
theFont3=pygame.font.Font(None,35)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
screen.fill(white)

#Faculty lists
statusA = "X"
statusB = "X"
statusC = "X"
statusD = "X"
statusE = "X"
statusF = "X"
statusG = "X"
statusH = "X"
statusI = "X"
statusJ = "X"
statusK = "X"
statusL = "X"
statusM = "X"
statusN = "X"
statusO = "X"
colorA = grey
colorB = grey
colorC = grey
colorD = grey
colorE = grey
colorF = grey
colorG = grey
colorH = grey
colorI = grey
colorJ = grey
colorK = grey
colorL = grey
colorM = grey
colorN = grey
colorO = grey

pygame.display.set_caption('Server Status')

while True:
	for event in pygame.event.get():  #add this to make program not unresponding
		if event.type == pygame.QUIT:
				pygame.quit()
				quit()
	####try and except section in case error happen
	filein = open("result.txt", "r")
	allstatus = filein.readlines()
	filein.close()
	try:
		#read all status from .txt file here
		statusA = statusCheck(allstatus[1][0])
		colorA = statusColor(statusA)
		statusB = statusCheck(allstatus[3][0])
		colorB = statusColor(statusB)
		statusC = statusCheck(allstatus[5][0])
		colorC = statusColor(statusC)
		statusD = statusCheck(allstatus[7][0])
		colorD = statusColor(statusD)
		statusE = statusCheck(allstatus[9][0])
		colorE = statusColor(statusE)
		statusF = statusCheck(allstatus[11][0])
		colorF = statusColor(statusF)
		statusG = statusCheck(allstatus[13][0])
		colorG = statusColor(statusG)
		statusH = statusCheck(allstatus[15][0])
		colorH = statusColor(statusH)
		statusI = statusCheck(allstatus[17][0])
		colorI = statusColor(statusI)
		statusJ = statusCheck(allstatus[19][0])
		colorJ = statusColor(statusJ)
		statusK = statusCheck(allstatus[21][0])
		colorK = statusColor(statusK)
		statusL = statusCheck(allstatus[23][0])
		colorL = statusColor(statusL)
		statusM = statusCheck(allstatus[25][0])
		colorM = statusColor(statusM)
		statusN = statusCheck(allstatus[27][0])
		colorN = statusColor(statusN)
		statusO = statusCheck(allstatus[29][0])
		colorO = statusColor(statusO)
	except:
		time.sleep(10)
	finally:
		filein = open("result.txt", "r")
		allstatus = filein.readlines()
		filein.close()
		#read all status from .txt file here
		statusA = statusCheck(allstatus[1][0])
		colorA = statusColor(statusA)
		statusB = statusCheck(allstatus[3][0])
		colorB = statusColor(statusB)
		statusC = statusCheck(allstatus[5][0])
		colorC = statusColor(statusC)
		statusD = statusCheck(allstatus[7][0])
		colorD = statusColor(statusD)
		statusE = statusCheck(allstatus[9][0])
		colorE = statusColor(statusE)
		statusF = statusCheck(allstatus[11][0])
		colorF = statusColor(statusF)
		statusG = statusCheck(allstatus[13][0])
		colorG = statusColor(statusG)
		statusH = statusCheck(allstatus[15][0])
		colorH = statusColor(statusH)
		statusI = statusCheck(allstatus[17][0])
		colorI = statusColor(statusI)
		statusJ = statusCheck(allstatus[19][0])
		colorJ = statusColor(statusJ)
		statusK = statusCheck(allstatus[21][0])
		colorK = statusColor(statusK)
		statusL = statusCheck(allstatus[23][0])
		colorL = statusColor(statusL)
		statusM = statusCheck(allstatus[25][0])
		colorM = statusColor(statusM)
		statusN = statusCheck(allstatus[27][0])
		colorN = statusColor(statusN)
		statusO = statusCheck(allstatus[29][0])
		colorO = statusColor(statusO)
	####end of try and except


	theTime=time.strftime("%H:%M:%S", time.localtime())
	lastUpdate = allstatus[30]

	##render all things here
	#rendername
	nameA = theFont2.render(allstatus[0][0:(len(allstatus[0])-1)], True, colorA, white)
	nameB = theFont2.render(allstatus[2][0:(len(allstatus[2])-1)], True, colorB, white)
	nameC = theFont2.render(allstatus[4][0:(len(allstatus[4])-1)], True, colorC, white)
	nameD = theFont2.render(allstatus[6][0:(len(allstatus[6])-1)], True, colorD, white)
	nameE = theFont2.render(allstatus[8][0:(len(allstatus[8])-1)], True, colorE, white)
	nameF = theFont2.render(allstatus[10][0:(len(allstatus[10])-1)], True, colorF, white)
	nameG = theFont2.render(allstatus[12][0:(len(allstatus[12])-1)], True, colorG, white)
	nameH = theFont2.render(allstatus[14][0:(len(allstatus[14])-1)], True, colorH, white)
	nameI = theFont2.render(allstatus[16][0:(len(allstatus[16])-1)], True, colorI, white)
	nameJ = theFont2.render(allstatus[18][0:(len(allstatus[18])-1)], True, colorJ, white)
	nameK = theFont2.render(allstatus[20][0:(len(allstatus[20])-1)], True, colorK, white)
	nameL = theFont2.render(allstatus[22][0:(len(allstatus[22])-1)], True, colorL, white)
	nameM = theFont2.render(allstatus[24][0:(len(allstatus[24])-1)], True, colorM, white)
	nameN = theFont2.render(allstatus[26][0:(len(allstatus[26])-1)], True, colorN, white)
	nameO = theFont2.render(allstatus[28][0:(len(allstatus[28])-1)], True, colorO, white)
	#renderstatus
	statusSymA = theFont2.render(": " + statusA, True, colorA,white)
	statusSymB = theFont2.render(": " + statusB, True, colorB, white)
	statusSymC = theFont2.render(": " + statusC, True, colorC, white)
	statusSymD = theFont2.render(": " + statusD, True, colorD, white)
	statusSymE = theFont2.render(": " + statusE, True, colorE, white)
	statusSymF = theFont2.render(": " + statusF, True, colorF,white)
	statusSymG = theFont2.render(": " + statusG, True, colorG, white)
	statusSymH = theFont2.render(": " + statusH, True, colorH, white)
	statusSymI = theFont2.render(": " + statusI, True, colorI, white)
	statusSymJ = theFont2.render(": " + statusJ, True, colorJ, white)
	statusSymK = theFont2.render(": " + statusK, True, colorK,white)
	statusSymL = theFont2.render(": " + statusL, True, colorL, white)
	statusSymM = theFont2.render(": " + statusM, True, colorM, white)
	statusSymN = theFont2.render(": " + statusN, True, colorN, white)
	statusSymO = theFont2.render(": " + statusO, True, colorO, white)
	timeText=theFont.render(str(theTime), True,black,white)
	thisIP = socket.gethostbyname(socket.gethostname())
	lastUpdateText = theFont3.render("Last Update: "+ lastUpdate + " | This machine IP: " +thisIP,True,black,white)

	#print all things to screen
	y = 40
	xName = 50
	base = 120
	xStatus = 600
	screen.blit(nameA, (xName,base))
	screen.blit(nameB, (xName,base + y))
	screen.blit(nameC, (xName,base + 2*y))
	screen.blit(nameD, (xName,base + 3*y))
	screen.blit(nameE, (xName,base + 4*y))
	screen.blit(nameF, (xName,base + 5*y))
	screen.blit(nameG, (xName,base + 6*y))
	screen.blit(nameH, (xName,base + 7*y))
	screen.blit(nameI, (xName,base + 8*y))
	screen.blit(nameJ, (xName,base + 9*y))
	screen.blit(nameK, (xName,base + 10*y))
	screen.blit(nameL, (xName,base + 11*y))
	screen.blit(nameM, (xName,base + 12*y))
	screen.blit(nameN, (xName,base + 13*y))
	screen.blit(nameO, (xName,base + 14*y))
	screen.blit(statusSymA, (xStatus,base))
	screen.blit(statusSymB, (xStatus,base + y))
	screen.blit(statusSymC, (xStatus,base + 2*y))
	screen.blit(statusSymD, (xStatus,base + 3*y))
	screen.blit(statusSymE, (xStatus,base + 4*y))
	screen.blit(statusSymF, (xStatus,base + 5*y))
	screen.blit(statusSymG, (xStatus,base + 6*y))
	screen.blit(statusSymH, (xStatus,base + 7*y))
	screen.blit(statusSymI, (xStatus,base + 8*y))
	screen.blit(statusSymJ, (xStatus,base + 9*y))
	screen.blit(statusSymK, (xStatus,base + 10*y))
	screen.blit(statusSymL, (xStatus,base + 11*y))
	screen.blit(statusSymM, (xStatus,base + 12*y))
	screen.blit(statusSymN, (xStatus,base + 13*y))
	screen.blit(statusSymO, (xStatus,base + 14*y))


	#print time and last update
	screen.blit(timeText, (0,0))
	screen.blit(lastUpdateText, (0,60))

	clock.tick(1)
	pygame.display.update()
    