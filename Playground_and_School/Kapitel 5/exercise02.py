from deep_translator import GoogleTranslator

# deep_translator (von Google Translate)
def translation(text):
    return GoogleTranslator(source='auto', target='en').translate(text=text)

#Aufruf (Ende mit "Stop")
text = str(input ("Bitte Text eingeben:"))

while text.strip().lower() != "stop": # Mit strip werden leerzeichen gelöscht und mit lower in Kleinbuchstaben umgewandelt (Würde auch ohne das gehen)
    print(translation(text))
    text  = str(input ("Bitte Text eingeben:"))
print ("Programmende ... Bye")



