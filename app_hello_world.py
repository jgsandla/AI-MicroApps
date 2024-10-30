PHASES = {
    "phase1": {
        "name": "What is your name?",
        "fields": {
                "name": {
                "type": "text_input",
                "label": "What is your first name?",
            },
            "animal": {
                "type": "text_input",
                "label": "What is one of your favorite animals?"
            }
        },
        "user_prompt": "My name is {name} and I like this animal: {animal}. Write a sonnet about me and my favorite animal.",
    },
}

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())
