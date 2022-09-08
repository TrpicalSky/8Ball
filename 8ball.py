import random
responses = ["Yes - definitely", "It is decidedly so.", "Without a doubt.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "My sources say no.", "Outlook not so good", "Very doubtful."]

name = "Timmy"
askerQuestion = "Will Anthony win his golf tournament next week."
randomNum = random.randrange(0,9)
finishedQuestion = f"{name} asks: {askerQuestion}"
EightBallResponse = f"Magic 8-Ball's answer: {responses[randomNum]}"
print(finishedQuestion)
print(EightBallResponse)
