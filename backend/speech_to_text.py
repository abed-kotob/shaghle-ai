# import speech_recognition as sr
 
class Speech_to_Text:
    def __init__(self,path_to_vns): #Path to the voicenotes folder (implicit notation)
        self.path_to_vns = path_to_vns

    def access_vns(): #Search vns folder for newest additions
        return
    
    def speech_to_text_run(voicenote): # takes a voicenote as a parameter and returns a text file with the same name
        
        """ might go into another file:
        
        
            import speech_to_text
            Speech_to_Text Speech1

            f = open ("input.mp3", 'rb')
            audio = f.read()
            f.close()

            Speech1.speech_to_text_run(audio)
        """
        # r = sr.recognizer
        # print("Processing Audio...")

        # try:
        #     t = r.recognize_google(voicenote, language = "ar-AR")
        #     print(t)
        #     f = open('output.txt', 'a', encoding='utf-8')
        #     f.writelines(t+'\n')
        #     f.close()
            
        # except sr.UnknownValueError as U:
        #     print(U)
        # except sr.RequestError as R:
        #     print(R)
        
        return 

    def iterate(): #Iterates over the new vns collected from access_vns and applies speech_to_text_run

        return

    def check_length(): #Check if splitting is required
        return 

    def split_vn(): #if vn is long, split it and then apply speech to text if necessary
        return