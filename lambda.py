# _*_ coding: utf-8 _*_
""" 
This is the code of ``Harish Resume`` Skill for Amazon Alexa.
"""
from __future__ import print_function

def build_speechlet_response(title, output, reprompt_text, should_end_session):
""" This Functions helps build Speechlet Responce Structure """
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech':{
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
""" This Function helps build Responses for all the Intents """

    return{
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

def get_welcome_response():
""" This Function is invoked when the Welcome intent is called """
    session_attributes = {}
    card_title = "Welcome Responce"
    speech_output = "Welcome Response"
    reprompt_text = "Reprompt Text"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))

def handle_session_end_request():
""" This Function handles the Session End Request """
    session_attributes = {}
    card_title = "Session Ended"
    speech_output = "Session End Text"
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, None, should_end_session))


#----------------------------------- Events -----------------------------------------

def on_session_started(session_started_request, session):
""" Called when the session starts """
    print("on_session_started requestId=" + session_started_request['requestId'] + ", sessionId=" + session['sessionId'])

def on_launch(launch_request, session):
""" Called when the user launches the skill without specifying what they want """
    print("on_launch requestId=" + launch_request['requestId'] +", sessionId=" + session['sessionId'])
    return get_welcome_response()

def on_intent(intent_request, session):
""" Called when the user specifies an intent for this skill """
    print("on_intent requestId=" + intent_request['requestId'] +", sessionId=" + session['sessionId'])
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    if intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")

def on_session_ended(session_ended_request, session):
""" Called when the user ends the session """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +", sessionId=" + session['sessionId'])

#----------------------------------- Main Handler -------------------------------------

def lambda_handler(event, context):
""" Route the incoming request based on type (LaunchRequest, IntentRequest, etc.) The JSON body of the request is provided in the event parameter. """
    print("event.session.application.applicationId=" +event['session']['application']['applicationId'])

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']}, event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])



