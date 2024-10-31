PUBLISHED = True
APP_URL = "https://guided-critical-thinking.streamlit.app"

APP_TITLE = "Biomaterials Question 1"
APP_INTRO = """This is an application that assesses a student's understanding of a lesson and provides feedback and scoring which is generated by AI and guided by the instructor. 

"""



SHARED_ASSET = {
}



SYSTEM_PROMPT = """You provide feedback, based on instructions that are provided, on a critical thinking response from a student. You are overall encouraging, and try to be specific about areas improvement and try to avoid vague statements like 'add more detail'. When asked to score, your scoring is based on the facts at hand, and have nothing to do with the tone of the conversation. """

PHASES = {






 
    "summarize": {
        "name": "Answer the Question",
        "fields": {
            #"polar_bear_image":{
             #   "type": "image",
              #  "image": "https://upload.wikimedia.org/wikipedia/commons/d/dc/Polar_Bear_imported_from_iNaturalist_photo_35085101_on_1_January_2024.jpg",
               # "alt": "An image of a polar bear",
                #"width": "200px",
                #"caption": "An image of a polar bear."
            #},            
         
            "polyunsaturated_temp_text": {
                "type": "markdown",
                "body": """Animals that live in different climates often have varying amounts of polyunsaturated fatty acid residues in their fats. **Which would you predict would have more polyunsaturated fats – an animal that lives in a cold climate or a warm one? Explain.** """,
                "unsafe_allow_html": True,
            },
            "polyunsaturated_temp": {
                "type": "text_area",
                "height": 200,
                "label": """Animals that live in different climates often have varying amounts of polyunsaturated fatty acid residues in their fats. Which would you predict would have more polyunsaturated fats – an animal that lives in a cold climate or a warm one? Explain.""",
                "label_visibility": "hidden",
               # "value": "The multimedia principle is the idea that learner's retain information better when viewing app_images that match the audio, rather than audio alone. In my own work, I expect that I might try to use app_images that support the audio instead of purely decorative app_images or \"talking head\" format. ",
            },


        },
        "phase_instructions": """
        The user will answer the following question: Animals that live in different climates often have varying amounts of polyunsaturated fatty acid residues in their fats. Which would you predict would have more polyunsaturated fats – an animal that lives in a cold climate or a warm one? Explain. Provide feedback for the user using the following guide:
        - Make sure the user identifies that polyunsaturated fats have double bonds, which makes compact packing of the chains more difficult  
        - Make sure the user identifies that the intermolecular forces (IMFs) between the chains are weaker because the packing is less compact 
        - Make sure the user identifies that this leads to a more fluid cell membrane
        - Make sure that heat can also weaken intermolecular forces (IMFs), leading to an increase in the fluidity of the cell membrane
        - Conclude that a hot-weather animal wouldn't need/want a lot of polyunsaturated fat in their cell membrane because their cell membrane would already be more mobile
        If the user identifies any of the points described above, start with encouragement about what the user did well.  If the user's answer is completely incorrect, start with a neutral statement.  Then, outline any areas for improvement. If the user met all the guidelines, then offer your own suggestion on how they could improve their response. 
        Do not end your statement with a question. 
        """,
        "user_prompt": "{polyunsaturated_temp}",
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
        #"allow_revisions": True,
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
