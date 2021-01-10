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

cmdSuperRight = Special_moves.CMD(["2","3","6","2","3","6","a"],2,"Shinku Hadoken!")
cmdArray.append(cmdDragonPunchRight)

cmdSuperLeft = Special_moves.CMD(["2","1","4","2","1","4","a"],2,"Shinku Hadoken!")
cmdArray.append(cmdSuperLeft)

inputStream = Special_moves.Input_stream()

streamReader = Special_moves.Stream_reader(inputStream,cmdArray)

frameCount = 1

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.KEYDOWN:
            print(event.key.unicode)
            # inputStream.add_input(event.key.unicode)



    #activate every frame at 60 frames per second
    time.sleep(0.0167)

    streamReader.read_stream()

    # at 12 frames the input stream gets pushed, after 2 second (120 frames)
    #the whole stream should be empty [all Nones]
    frameCount += 0

    if frameCount == 12:
        inputStream.push_stream()
        frameCount = 0