PUBLISHED = True
APP_URL = "https://guided-critical-thinking.streamlit.app"

APP_TITLE = "Biomaterials Problem 1"
APP_INTRO = """Animals that live in different climates often have varying amounts of polyunsaturated fatty acid residues in their fats. Which would you predict would have more polyunsaturated fats – an animal that lives in a cold climate or a warm one? 

"""

#APP_HOW_IT_WORKS = """
 #Using this app, a student submits a response. The student's response is compared to the key points that the instructor is looking for in the response, and the AI provides feedback on where the student met or fell short of expectations. 
 #The AI may also score a student based on rubrics created by the instructor. AI generally performs better when grading discrete, tangible items (i.e. The student included a personal experience) whereas it is less consistent with judgement calls (e.g. The student's response is high quality). 


 #"""

SHARED_ASSET = {
   
}



SYSTEM_PROMPT = """You provide feedback, based on instructions that are provided, on a critical thinking response from a student. You are overall encouraging, and try to be specific about areas improvement and try to avoid vague statements like 'add more detail'. When asked to score, your scoring is based on the facts at hand, and have nothing to do with the tone of the conversation. """

PHASES = {

 "phase0": {
        "name": "Image",
        "fields": {
            "name": {
                "type": "image",
                "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Polar_bear_with_cub.jpg/1600px-Polar_bear_with_cub.jpg",
                "alt": "A polar bear with its cub",
            }
        }
    },



 
    "summarize": {
        "name": "Summarize the Lesson",
        "fields": {
            "multimedia_principle_text": {
                "type": "markdown",
                "body": """**Explain in your own words the Multimedia Principle on course development. Describe an example of how you might use the multimedia principle in practice.**
                <p style="font-size: .9em; color: #3c3c3c;">Make sure to include a definition of the Multimedia Principle, and describe when to use animations vs static illustrations. Also, do remember to include an example of how you might use the multimedia principle in practice.</p>""",
                "unsafe_allow_html": True,
            },
            "multimedia_principle": {
                "type": "text_area",
                "height": 200,
                "label": """Explain in your own words the Multimedia Principle on course development. Describe an example of how you might use the multimedia principle in practice.""",
                "label_visibility": "hidden",
                "value": "The multimedia principle is the idea that learner's retain information better when viewing app_images that match the audio, rather than audio alone. In my own work, I expect that I might try to use app_images that support the audio instead of purely decorative app_images or \"talking head\" format. ",
            },


        },
        "phase_instructions": """
        The user will define the multimedia principle as it pertains to online education. Provide feedback for the user using the following guide:
        - Make sure the user includes a definition of the multimedia principle
        - Make sure the user describes when to use animation vs static illustration. 
        - Make sure the user includes their own example of how they might use the multimedia principle in practice. 
        Start with encouragement about what the user did well. Then, outline any areas for improvement. If the user met all the guidelines, then offer your own suggestion on how they could improve their response. 
        Do not end your statement with a question. 
        """,
        "user_prompt": "{multimedia_principle}",
        "ai_response": True,
        "scored_phase": True,
        "minimum_score": 0,
        "rubric": """
            1. Definition
                1 points - The user has provided an accurate definition of the multimedia principle in the context of online education. 
                0 points - The user has not provided an accurate definition of the multimedia principle in the context of online education. 
            2. Personal Example
                1 points - The user has provided their own example of how they might use the multimedia principle in practice. 
                0 points - The user has not provided their own example of how they might use the multimedia principle in practice. 
            3. Animation vs Static
                1 points - The user has talked about when the multimedia principle advises when to use animation (primarily to illustrate hands-on procedures or to serve an interpretive function) vs static app_images (most other educational visualizations)
                0 points - The user has not spoken to when multimedia principle advises to use animation vs static app_images. 
        """,
        "allow_revisions": True,
        "allow_skip": False,
        #"show_prompt": True,
        #"read_only_prompt": False
    },

  "improve": {
        "name": "Improve your Response",
        "fields": {
            "multimedia_principle_revised": {
                "type": "text_area",
                "height": 200,
                "label": """Based on the feedback you received, please improve your response.""",
                "label_visibility": "hidden",
                "value": """The multimedia principle is the idea that learner's retain information better when viewing app_images that match the audio, rather than audio alone. This is because making a connection between a pictorial and a verbal representation of an item is proven to be an helpful way to store something in long term memory. You might expect that animated app_images are better than static app_images, but the research does not conclusively indicate that. Animated app_images could be more distracting and therefore less effective than static app_images. The exception is when demonstrating complex manual processes, where animations have shown to be effective. In my own work, I expect that I might try to use app_images that support the audio instead of purely decorative app_images or 'talking head' format. I'm thinking particularly of a lesson about building AI apps, where it would be helpful to show screenshots of important steps instead of just talking or writing about them. """,
            },


        },
        "phase_instructions": """
        The user will define the multimedia principle as it pertains to online education. Provide feedback for the user using the following guide:
        - Make sure the user includes a definition of the multimedia principle
        - Make sure the user describes when to use animation vs static illustration. 
        - Make sure the user includes their own example of how they might use the multimedia principle in practice. 
        If the user has improved their earlier response, then applaud them for doing so. If the user did not change their response, then express some disappointment.
        Do not end your statement with a question. 
        """,
        "user_prompt": "{multimedia_principle_revised}",
        "ai_response": True,
        "scored_phase": True,
        "minimum_score": 2,
        "rubric": """
            1. Definition
                1 points - The user has provided an accurate definition of the multimedia principle in the context of online education. 
                0 points - The user has not provided an accurate definition of the multimedia principle in the context of online education. 
            2. Personal Example
                1 points - The user has provided their own example of how they might use the multimedia principle in practice. 
                0 points - The user has not provided their own example of how they might use the multimedia principle in practice. 
            3. Animation vs Static
                1 points - The user has accurately spoken to when the multimedia principle advises when to use animation (primarily to illustrate hands-on procedures or to serve an interpretive function) vs static app_images (most other educational visualizations)
                0 points - The user has not spoken to when multimedia principle advises to use animation vs static app_images. 
        """,
        #"allow_revisions": True,
        "allow_skip": False,
        #"show_prompt": True,
        #"read_only_prompt": False
    },
}

PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only

PAGE_CONFIG = {
    "page_title": "Guided Critical Thinking John",
    "page_icon": "️💡",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = True

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())
