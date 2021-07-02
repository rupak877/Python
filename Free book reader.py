#Install this File by typing "pip install pyttsx3" then import it.
import pyttsx3

#Install this File by typing "pip install PyPDF2" then import it.
import PyPDF2
#Type your PDF name in defined text in Your pdf name here then run it.
#PDF name
#Download your PDF in the folder where your project is saved.
book = open('Your pdf name here', 'rb')
#Reading
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)
speaker = pyttsx3.init()
#Type the page you want to listen in the "()" Brackets then run it.
page = pdfreader.getPage(7)
#Running the code.
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
#run