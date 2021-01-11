import Special_moves
import time
import pygame


cmdArray = []

#load special moves into an array
cmdFireballRight = Special_moves.CMD(["2","3","6","a"],0,"Fire ball!")
cmdArray.append(cmdFireballRight)

cmdFireballLeft = Special_moves.CMD(["2","1","4","a"],0, "Fire ball!")
cmdArray.append(cmdFireballLeft)

cmdDragonPunchRight = Special_moves.CMD(["6","3","2","3","a"],1,"Dragon Punch!")
cmdArray.append(cmdDragonPunchRight)

cmdDragonPunchLeft = Special_moves.CMD(["4","1","2","1","a"],1,"Dragon Punch!")
cmdArray.append(cmdDragonPunchLeft)

cmdSuperRight = Special_moves.CMD(["2","3","6","2","3","6","a"],2,"Super!")
cmdArray.append(cmdSuperRight)

cmdSuperLeft = Special_moves.CMD(["2","1","4","2","1","4","a"],2,"Super!")
cmdArray.append(cmdSuperLeft)

inputStream = Special_moves.Input_stream()

streamReader = Special_moves.Stream_reader(inputStream,cmdArray)

frameCount = 1

pygame.init()
win =pygame.display.set_mode((600,600))
pygame.display.set_caption("Input System")

running = True
while running:
    for event in pygame.event.get(): 

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN :
            
            print ("keydown")
            # inputStream.add_input(event.key.unicode)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_KP1 ]:
            inputStream.add_input("1")

        if keys[pygame.K_KP2 ]:
            inputStream.add_input("2")

        if keys[pygame.K_KP3 ]:
            inputStream.add_input("3")

        if keys[pygame.K_KP4 ]:
            inputStream.add_input("4")

        if keys[pygame.K_KP6 ]:
            inputStream.add_input("6")

        if keys[pygame.K_KP7]:
            inputStream.add_input("7")

        if keys[pygame.K_KP8 ]:
            inputStream.add_input("8")

        if keys[pygame.K_KP9 ]:
            inputStream.add_input("9")

        if keys[pygame.K_a]:
            inputStream.add_input("a")



    #activate every frame at 60 frames per second
    time.sleep(0.0167)

    streamReader.read_stream()

    # at 12 frames the input stream gets pushed, after 2 second (120 frames)
    #the whole stream should be empty [all Nones]
    frameCount += 1

    if frameCount == 12:
        inputStream.push_stream()
        frameCount = 0

    # print(str(inputStream.get_stream()))

pygame.quit()