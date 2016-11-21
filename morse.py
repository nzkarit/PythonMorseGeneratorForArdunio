#!/usr/bin/python3

pathMessages = 'messages.txt'
pathOutput = 'output.txt'

interLetter = "   " #3

morseAlphabet ={
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    " " : "       ", #7
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    "0" : "-----",
    "." : ".-.-.-",
    "," : "--..--",
    ":" : "---...",
    "?" : "..--..",
    "'" : ".----.",
    "-" : "-....-",
    "/" : "-..-.",
    "@" : ".--.-.",
    "=" : "-...-"
}


def start_script():
    f = open(pathMessages, 'r')
    messages = []
    for line in f:
        messages.append(line.strip())
    f.close()
    print(messages)
    morseMessages = []
    for message in messages:
        morseMessage = ""
        for character in message:
            if character != ' ':
                morseMessage += morseAlphabet[character.upper()]
                morseMessage += interLetter
            else:
               morseMessage += morseAlphabet[character.upper()] 
        morseMessages.append(morseMessage)
    print(morseMessages)
    rawMessages = []
    for message in morseMessages:
        rawMessage = ""
        for character in message:
            if character == '.':
                rawMessage += "10"
            elif character == '-':
                rawMessage += "1110"
            else:
                rawMessage += "0"
        rawMessages.append(rawMessage)
    print(rawMessages)
    
    longest = 0
    for message in rawMessages:
        if len(message) > longest:
            longest = len(message)
    print(longest)
    code = """
#define PIN_0      13
#define PIN_1      12
#define PIN_2      11
#define UNIT_LENGTH  250

void setup() {
    pinMode(PIN_0, OUTPUT);
    digitalWrite(PIN_0, LOW);
    pinMode(PIN_1, OUTPUT);
    digitalWrite(PIN_1, LOW);
    pinMode(PIN_2, OUTPUT);
    digitalWrite(PIN_2, LOW);
}

void loop() {
"""
    numMessages = len(rawMessages)
    state = []
    for i in range(0, numMessages):
        state.append(0)
    for i in range(0, longest):
        print('Count = %s' % (i))
        
        for j in range(0, numMessages):
            try:
                print(rawMessages[j][i])
                if int(rawMessages[j][i]) == 1:
                    if state [j] == 0:
                        code += "    digitalWrite( PIN_%s, HIGH );\n" % (j)
                    state [j] = 1
                else:
                    if state [j] == 1:
                        code += "    digitalWrite( PIN_%s, LOW );\n" % (j)
                    state [j] = 0
            except IndexError:
                pass
                #don't write to save memory as should end low
                #code += "    digitalWrite( PIN_%s, LOW );\n" % (j) 
        code += "    delay( UNIT_LENGTH );\n"
    code += """
    delay( UNIT_LENGTH * 20 );
} 
"""
    print(code)
    f = open(pathOutput, 'w')
    f.write(code)
    f.close()
        

if __name__ == '__main__':
    start_script()
