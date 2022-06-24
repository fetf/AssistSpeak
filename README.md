# AssistSpeak  
Winner of **Most Creative Use of Twilio** at [Girls Hoo Hack 2021](https://www.gwcuva.com/hack) ([Devpost](https://girls-hoo-hack-2021.devpost.com/))

Project imported from Devpost  
See full project [here](https://devpost.com/software/assistspeak)
## Inspiration
We wanted to build a project that brings the greatness of virtual assistants to any mobile phone!

## What it does
This project allows anyone with a mobile phone (even flip phones) to have their own virtual assistant. Just call its number, ask a question, and the assistant will text you back with the results.

## How we built it
The program was hosted on Google Cloud and made in Python 3 using flask as the backbone of the project. The call made to the assistant is first managed through Twilio, who says a message and records the call. The recording is sent to AssemblyAI to extract the words being said, then those words are processed through WolframAlpha's API and the results from WolframAlpha are texted back to the caller. 

## Challenges we ran into
This was our first time using many of these APIs which was a challenge to learn, and on top of that integrating these APIs together required some careful coding. For example, Wolfram's API returns a massive JSON, and sifting through it for the information we wanted took some time.

## Accomplishments that we're proud of
All the APIs and frameworks mesh together perfectly in our final code despite the rush to complete it and the program worked for all the questions we threw at it.

## What we learned
We learned how to use many of these APIs for the first time such as Twilio and AssemblyAI which was a difficult challenge but an enjoyable one as well.

## What's next for AssistSpeak
We would want to support other assistants in our code and add functionality for landlines to also be able to use AssistSpeak.
