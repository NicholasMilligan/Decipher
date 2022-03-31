from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException
import json

authenticator = IAMAuthenticator('j8cH-7tI_hVxug4cWueK-2-jav8lq8zmYnVZuP2xwGib')
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=authenticator
)

tone_analyzer.set_service_url('https://api.us-south.tone-analyzer.watson.cloud.ibm.com/instances/4e919009-7b5d-4b06-9af9-b036acbcf24c')



try:
    # Parameters:
    # tone(self,
    #     tone_input: Union['ToneInput', str, TextIO],
    #     *,
    #     content_type: str = None, --> [application/json,text/plain,text/html]
    #     sentences: bool = None, --> true/false : option to return analysis of each sentence in addition to full document
    #     tones: List[str] = None, --> *DEPRECATED* [emotion, language, social]
    #     content_language: str = None, -->  [en,fr]
    #     accept_language: str = None, --> [ar,de,en,es,fr,it,ja,ko,pt-br,zh-cn,zh-tw]
    #     **kwargs
    # ) -> DetailedResponse

    text = None
    # text = 'Team, I know that times are tough! Product '\
    # 'sales have been disappointing for the past three '\
    # 'quarters. We have a competitive product, but we '\
    # 'need to do a better job of selling it!'

    tone_analysis = tone_analyzer.tone({'text': text},
                                        content_type='application/json').get_result()
    print(json.dumps(tone_analysis, indent=2))
    # Invoke a method




except ApiException as ex:
    print ("Method failed with status code " + str(ex.code) + ": " + ex.message)

    # Error Codes:
    # 200
    # OK. The request succeeded. If the input is partially correct, the response can include warning or error fields with appropriate messages.

    # 400
    # Bad Request. A required input parameter is null or a specified input parameter or header value is invalid or not supported.

    # 401
    # Unauthorized. Access is denied due to invalid service credentials.

    # 404
    # Not Found. A requested item or parameter does not exist.

    # 429
    # Too Many Requests. The service is throttling your request because your IBM Cloud ID submitted more than 1200 requests per minute.

    # 500
    # Internal Server Error. The service encountered an internal error.
