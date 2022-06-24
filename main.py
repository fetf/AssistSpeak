import os
from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
import requests
import json
import time
from twilio.rest import Client

app = Flask(__name__)



def wolframRequest(text):
  finalText = ""
  r = requests.get('https://api.wolframalpha.com/v2/query?appid=' + os.environ['appID'] + '&output=json&input=' + text)
  jsonDict = r.json()
  finalText = "Input: " + jsonDict["queryresult"]["pods"][0]["subpods"][0]["plaintext"] + "\n\n"
  i = 0
  for item in jsonDict["queryresult"]["pods"]:
    if not item["subpods"][0]["plaintext"] == "":
      i+=1
  i-=1;
  if(i > 3): 
    i = 3
  elif (i <0):
    i=0
  
  finalText += "Top Results:\n"
  j = 0
  for z in range(i):
    
    k = j+1
    while jsonDict["queryresult"]["pods"][k]["subpods"][0]["plaintext"] == "":
      k+=1
      j+=1
    finalText += jsonDict["queryresult"]["pods"][k]["title"] + ":\n"
    finalText += jsonDict["queryresult"]["pods"][k]["subpods"][0]["plaintext"] + "\n\n"

    j+=1

  print(finalText)
  return finalText



  






@app.route("/record", methods=['GET', 'POST'])
def record():
    """Returns TwiML which prompts the caller to record a message"""
    response = VoiceResponse()

    response.say('Please say your query.')

    response.record()
    response.hangup()

    
    try:
      url = request.form["RecordingUrl"]
      endpoint = "https://api.assemblyai.com/v2/transcript"

      json = {
        "audio_url": url
      }
      token = os.environ['token']
      headers = {
          "authorization": token,

          "content-type": "application/json"
      }

      r = requests.post(endpoint, json=json, headers=headers)

      status = r.json()["status"]
      requestID = r.json()["id"]


      endpoint = "https://api.assemblyai.com/v2/transcript/" + requestID
      headers = {
          "authorization": token
      }
      
      while status != "completed" and status != "error":
        time.sleep(2)
        r=requests.get(endpoint, headers=headers)
        status = r.json()["status"]

        
      

      words = r.json()["text"]
      print(words)
      textBody = wolframRequest(words)

      account_sid = os.environ['twilioSID']
      auth_token = os.environ['twilioToken']
      client = Client(account_sid, auth_token)

      
      message = client.messages.create(
                                      body=textBody,
                                      from_='+14325294628',
                                      to=os.environ["phoneNum2"]
                                  )
 
    except Exception as e: 
      print(e)
    return str(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
    