import time

class CMD:
    """Class that holds the CMD pattern [code] to search for in the input stream
    and the CMD priority. Each Special move has an associated CMD class"""
    def __init__(self, code, priority,name):
       self.code = code
       self.priority = priority
       self.checklistPosition=0
       self.name = name

    def get_code(self):
        return self.code

    def get_priority(self):
        return self.priority

    def get_checklistPosition(self):
        return self.checklistPosition

    def increment_checklistPosition(self):
        self.checklistPosition += 1

    def disable_checklist(self):
        self.checklistPosition = None

    def reset_checklist(self):
        self.checklistPosition = 0
    
    def get_name (self):
        return self.name


class Input_stream:
    """holds the inputs in memory for reading.
    a None value means no input"""

    def __init__(self):
        self.stream = [None]*10
        self.beg = 1
        self.end = 0
    
    def get_stream(self):
        return self.stream
        
    def add_input(self,input):
        """adds an input to the array list and shifts the
        beg and end one index to the right; triggered on user
        input"""

        self.stream[self.beg] = input
        
        #checks if the beg or end needs to wrap back around the array
        if(self.beg == len(self.stream)-1):
            self.beg = 0
            self.end += 1
        elif(self.end == len(self.stream)-1):
            self.beg += 1
            self.end = 0
        else:
            self.beg += 1
            self.end += 1

    def push_stream(self):
        """adds a None and pushes the stream. if all elements
        in the stream are None, does nothing. Will be used to
        time out the stream over a second or so"""

        for input in (self.stream):
            if not (input == None):
                self.add_input(None)
                break
        return


    def get_end(self):
        return self.end

class Stream_reader:
    """handles all reading of the stream for
    cmd codes. takes a (stream object, array of cmds) as init arguments"""

    def __init__(self,stream,cmds):
        self.stream = stream
        self.cmds = cmds
        #Above is an array of CMD objects

    def read_stream(self):
        """ looks for any cmds in the array
        that will match those in the stream. Each correct input in sequence will 
        increment the CMD objects checklist. Once the checklist reaches the end of the 
        code, the CMD has succesfully been read. However, priority of the CMD must
        also be checked once the whole stream is proccessed. All checklists must be reset
        at the end of the read.""" 

        cmdsFound = []

        for inputIndex in range(self.stream.get_end()+1,self.stream.get_end()+11):

            # if the current input needs to wrap to the other side, 
            # sub 10 to get the correct index
            if inputIndex > 9:
                input = self.stream.get_stream()[inputIndex -10]
            else: 
                input = self.stream.get_stream()[inputIndex]


             #Do nothing if input is none
            if input == None:
                    pass
            else:
                for cmd in self.cmds:
                    
                    """DEBUG print("Checking: "+ cmd.get_name())
                    print(cmd.get_checklistPosition())
                    print("target position:" + str(len(cmd.get_code())))"""

                    #Do nothing if the checklist of the CMD is complete (it has been found) or the final input (button) does not match the code.
                    if cmd.get_checklistPosition() == None or not cmd.get_code()[len(cmd.get_code())-1]==self.stream.get_stream()[self.stream.get_end()]:
                        pass
                    #If the current input is the same as the current checklist element in the CMD code
                    #increment the checklist then check if it is complete
                    elif input == cmd.get_code()[cmd.get_checklistPosition()]:
                        cmd.increment_checklistPosition()
                        #DEBUG print(cmd.get_checklistPosition())
                        #if the checklist is complete add it to cmds found and set its checklist ot NOne
                        if cmd.get_checklistPosition() == len(cmd.get_code()):
                            cmdsFound.append(cmd)
                            cmd.disable_checklist()
                            #DEBUG print(cmd.get_name()+ "disabled")
        

        #finds the highest priority then  most recent cmd in the list.
        maxPriority = 0
        cmdOutput = None
        for cmd in cmdsFound:
            if cmd.get_priority() >= maxPriority:
                maxPriority = cmd.get_priority()
                cmdOutput = cmd
                

        #reenable all cmd checklists

        for cmd in self.cmds:
            cmd.reset_checklist()



        #Print result if cmd found

        if not (cmdOutput == None):
            print (cmdOutput.get_name())
            # debug print print(self.stream.get_stream())
              #flush stream to prevent double reads
            for input in self.stream.get_stream():
                self.stream.push_stream() 



if __name__ == "__main__":

    "Testing for adding input to the stream"
    inputStream = Input_stream()
    for x in range(10):
        print(str(inputStream.get_stream()))
        inputStream.add_input(0)
    print(str(inputStream.get_stream()))
    inputStream.add_input(1)
    print(inputStream.get_stream())
    inputStream.push_stream()
    print(inputStream.get_stream())




    