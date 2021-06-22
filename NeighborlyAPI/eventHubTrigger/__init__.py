import logging
import json
import azure.functions as func

def main(req: func.HttpRequest, sendGridMessage: func.Out[str]) -> func.HttpResponse:

    value = "Sending message from my Azure Functions HTTP Trigger - Vinay :)"

    message = {
        "personalizations": [ {
          "to": [{
            "email": "vincentayorinde@yahoo.com"
            }]}],
        "subject": "[AZURE FUNCTIONS SENDGRID] email",
        "content": [{
            "type": "text/plain",
            "value": value }]}

    sendGridMessage.set(json.dumps(message))
    return func.HttpResponse("Message successfully sent.")