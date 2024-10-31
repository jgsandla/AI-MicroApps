PUBLISHED = True
APP_URL = "https://guided-critical-thinking.streamlit.app"

APP_TITLE = "Biomaterials Question 1"
APP_INTRO = """This is an application that assesses a student's understanding of a lesson and provides feedback and scoring which is generated by AI and guided by the instructor. 

"""



SHARED_ASSET = {
}



SYSTEM_PROMPT = """You provide feedback, based on instructions that are provided, on a critical thinking response from a student. You are overall encouraging,  and try to avoid vague statements like 'add more detail'. In your responses, try not to give the answers away directly.  Instead, lead the student to the right answer by asking questions or encouraging them to consider important points.  When asked to score, your scoring is based on the facts at hand, and have nothing to do with the tone of the conversation. """

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

        - Cold weather animals have more polyunsaturated fats 
        - Polyunsaturated fats have double bonds, which makes compact packing of the hydrocarbon chains more difficult (compared to the unsaturated case)
        - This means that the intermolecular forces (IMFs) between the chains are weaker (compared to the unsaturated case)
        - This creates a more fluid cell membrane (compared to the unsaturated case)
        - Higher temperatures can also weaken intermolecular forces (IMFs), leading to an increase in the fluidity of the cell membrane. Therefore, animals living in warmer climates don't require as much polyunsaturated fats to keep their cell mebranes fluid
       

       

      
       
        If the user identifies any of the points described above, start with encouragement about what the user did well.  If the user's answer is completely incorrect, start with a neutral statement.  Then, summarize what the user has gotten correct. If the user has missed an important point, ask them leading questions relating to that point or encourage them to consider addressing these points in their answer, but if the user's answer is generally complete, don't make these suggestions or ask these questions. If the user doesn't talk about intermolecular forces (IMFs) in their answer, prompt them to do so.  Encourage the user to revise their response below, unless their answer met all of the guidelines. If the user met all the guidelines, let them know and tell them that they can skip the next question. 
        Do not end your statement with a question. 
        """,
        "user_prompt": "{polyunsaturated_temp}",
        "ai_response": True,
        "scored_phase": False,
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
        "allow_revisions": False,
        "allow_skip": False,
        "show_prompt": False,
        #"read_only_prompt": False
    },





 
    "improve": {
        "name": "Revise your Response",
        "fields": {
            "multimedia_principle_revised": {
                "type": "text_area",
                "height": 200,
                "label": """Based on the feedback you received, please improve your response.""",
                "label_visibility": "hidden",
                ##"value": polyunsaturated_temp,
            },


        },
        "phase_instructions": """
        The user will answer the following question: Animals that live in different climates often have varying amounts of polyunsaturated fatty acid residues in their fats. Which would you predict would have more polyunsaturated fats – an animal that lives in a cold climate or a warm one? Explain. Provide feedback for the user using the following guide:

        - Cold weather animals have more polyunsaturated fats 
        - Polyunsaturated fats have double bonds, which makes compact packing of the hydrocarbon chains more difficult (compared to the unsaturated case)
        - This means that the intermolecular forces (IMFs) between the chains are weaker (compared to the unsaturated case)
        - This creates a more fluid cell membrane (compared to the unsaturated case)
        - Higher temperatures can also weaken intermolecular forces (IMFs), leading to an increase in the fluidity of the cell membrane. Therefore, animals living in warmer climates don't require as much polyunsaturated fats to keep their cell mebranes fluid
             
        If the user has improved their response,  start with encouragement about what the user did well. If the user did not edit their answer, express some disappointment.  Then, summarize the update that the user has made to their answer. If the user has missed an important point, tell them what it is, but don't make suggestions if the users answer is generally correct. De-emphasize feedback about connecting the chemistry to animal survival. When evaluating the answer, please take into account the user's previous response as well as this one.
        Do not end your statement with a question. 
        """,
        "user_prompt": "{multimedia_principle_revised}",
        "ai_response": True,
        "scored_phase": False,
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
