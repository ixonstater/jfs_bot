import random
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import discord


async def try_execute(message):
    if ("make and bake" not in message.clean_content.lower()):
        return
    try:
        senders = try_parse_participants(message.clean_content.lower())
        recievers = shuffle_participants(senders)
        success_message = make_success_message_text(senders, recievers)
        make_pdf(senders, recievers)
        await message.channel.send(success_message, file=discord.File("/tmp/temp.pdf"))
        
    except:
        await send_explanation_message(message)
     
async def send_explanation_message(message):
    await message.channel.send("Hmm I couldn't find a list of participants, try including a list of more than two people in brackets with commas eg. [bobby, hank, boomhauer].")

def make_success_message_text(senders, recievers):
    base_message = "Here are your make and bake assignments this year:\n\n"
    for pair in zip(senders, recievers):
        base_message += pair[0] + " will be making a gift for " + pair[1] + ".\n\n"
    base_message += "Merry Christmas!!"
    
    return base_message

def make_pdf(senders, recievers):
    fileName = '/tmp/temp.pdf'
    documentTitle = 'Make and Bake Assignments'
    subTitle = 'Make and Bake Assignments'
    textLines = map(lambda pair: pair[0] + " "*2 + "-"*12 + " "*2 + pair[1], zip(senders, recievers))
    
    # creating a pdf object
    pdf = canvas.Canvas(fileName)
    
    # setting the title of the document
    pdf.setTitle(documentTitle)
    
    # creating the subtitle by setting it's font, 
    # colour and putting it on the canvas
    pdf.setFillColorRGB(0 / 255, 122 / 255, 12 / 255)
    pdf.setFont("Courier-Bold", 24)
    pdf.drawCentredString(290, 780, subTitle)
    
    # drawing a line
    pdf.line(30, 760, 550, 760)
    
    # creating a multiline text using 
    # textline and for loop
    text = pdf.beginText(40, 680)
    text.setFont("Courier", 18)
    text.setFillColor(colors.red)
    for line in textLines:
        text.textLine(line)
    pdf.drawText(text)
    
    # saving the pdf
    pdf.save()

def shuffle_participants(participants):
    shuffled = participants.copy()
    random.shuffle(shuffled)
    
    for i in range(0, len(participants)):
        if (participants[i] == shuffled[i]):
            if (i < 0):
                temp = shuffled[i]
                shuffled[i] = shuffled[i - 1]
                shuffled[i - 1] = temp
            else:
                temp = shuffled[i]
                shuffled[i] = shuffled[i + 1]
                shuffled[i + 1] = temp
    return shuffled

def try_parse_participants(message: str):
    index = message.find("[")
    if (index == -1 or index >= len(message)):
        raise RuntimeError()
    index = index + 1
    
    people = []
    person = "";
    while (index < len(message)):
        if (message[index] == ","):
            people.append(person.capitalize())
            person = ""
        elif (message[index] == "]"):
            if (len(person) > 0):
                people.append(person.capitalize())
            break
        elif (message[index] == " " or message[index] == "\n"):
            index += 1
            continue
        else:
            person += message[index]
            
        index += 1
            
    if (len(people) < 2):
        raise RuntimeError()
    
    return people
