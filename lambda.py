# _*_ coding: utf-8 _*_
""" 
This is the code of ``Harish Resume`` Skill for Amazon Alexa.
"""
from __future__ import print_function

def build_speechlet_response(title, speech_output, card_output, reprompt_text, should_end_session):
    """ This Functions helps build Speechlet Responce Structure """
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': speech_output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': card_output
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

#--------------------------------- Response Functions -----------------------------------

def get_welcome_response():
    """ This Function is invoked when the Welcome intent is called """
    session_attributes = {}
    card_title = "Welcome Responce"
    speech_output = "<speak> <audio src='https://s3.amazonaws.com/harish.bot.alexa/Intro_Music.mp3'/>" +\
     "Hi There! I can tell you all about you want to know about Haris Sista. Say \'Help\'" +\
     " to listen to more options. </speak>"
    card_output = " Hi There! I can tell you all about you want to know about Haris Sista." +\
    " Say \'Help\' to listen to more options. "
    reprompt_text = "Say \'Help\' to listen to more options."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, reprompt_text, should_end_session))

def handle_session_end_request():
    """ This Function handles the Session End Request """
    session_attributes = {}
    card_title = "Session Ended"
    speech_output = "<speak> Thanks for visiting, <say-as interpret-as=\"interjection\">cheerio</say-as> </speak>"
    card_output = " Thanks for visiting, cheerio!"
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, card_output, None, should_end_session))

def help_response():
    """ This Function is for handling `HelpIntent` response """
    session_attributes = {}
    card_title = "Help Intent"
    speech_output = "<speak> To know about Harish say \'Who is Harish?\', to know about his skills"+\
    " say \'Tell me about his skill set\', to know more about his projects say "+\
    "\'Tell me about his projects?\' If you want to know more details you can contact him on"+\
    " <say-as interpret-as=\"spell-out\">hsista123@gmail.com</say-as> </speak>"
    card_output = " To know about Harish say \'Who is Harish?\', to know about his skills say "+\
    "\'Tell me about his skill set\', to know more about his projects say \'Tell me about "+\
    "his projects?\'  If you want to know more details you can contact him on \'hsista123@gmail.com\'"
    reprompt_text = "To repeat all the options say \'Help\' again"
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response( card_title, speech_output, card_output, reprompt_text, should_end_session))

def get_intro_response(intent, session):
    """ This Function is for handling `IntroIntent` response """
    session_attributes = {}
    card_title = "Harish Introduction"
    speech_output = "<speak> He is an accomplished technical professional with proven experience,"+\
    " in developing and deploying cutting-edge skills for me, and other AI platforms,"+\
    " I really like him. To know more ask another question or say \'Help\'.</speak>"
    card_output = "He is an accomplished technical professional with proven experience, "+\
    "in developing and deploying cutting-edge skills for me, and other AI platforms, "+\
    "I really like him. To know more ask another question or say \'Help\'."
    reprompt_text = "To know more options say \'Help\' or ask another question."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response( card_title, speech_output, card_output ,reprompt_text, should_end_session))

def get_skill_set_response(intent, session):
    """ This Function is for handling `SkillsIntent` response """
    session_attributes = {}
    card_title = "Skill Sets"
    speech_output = "<speak> He is comfortable with many Programming Languages. Some of "+\
    "his best are Python, Java-Script, Swift and Objective-C </speak>"
    card_output = " He is comfortable with many Programming Languages. Some of his best are "+\
    "Python, Java-Script, Swift and Objective-C "
    reprompt_text = "To know more options say \'Help\' or ask another question."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response( card_title, speech_output, card_output, reprompt_text, should_end_session))

def get_work_response(intent, session):
    """ This Function is for handling `ProjectsIntent` response """
    session_attributes = {}
    card_title = "Projects"
    speech_output = "<speak> Harish keeps upto date knowledge on all the AI-Platforms. "+\
    "Till now he made up 30 Alexa which comprise of News feed skills, Tivia skills and other "+\
    "event based skills. He als worked on lot of IOS APllications and I-Message Applications. </speak>"
    card_output = "Harish keeps upto date knowledge on all the AI-Platforms. Till now he made "+\
    "up to 30 Alexa which comprise of News feed skills, Tivia skills and other event based skills."+\
    " He als worked on lot of IOS APllications and I-Message Applications."
    reprompt_text = "To know more options say \'Help\' or ask another question."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response( card_title, speech_output, card_output, reprompt_text, should_end_session))



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
        return help_response()
    elif intent_name == "IntroIntent":
        return get_intro_response(intent, session)
    elif intent_name == "SkillsIntent":
        return get_skill_set_response(intent, session)
    elif intent_name == "ProjectsIntent":
        return get_work_response(intent, session)
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
