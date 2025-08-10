import gradio as gr

# Initial glossary terms and definitions
flashcards = [
    {"term": "Argument (R)", "definition": "Information needed by a function in R in order to run."},
    {"term": "Assignment operator (R)", "definition": "An operator used to assign values to variables and vectors."},
    {"term": "C#", "definition": "An object-oriented programming language used to create games and mobile apps in the .NET open source developer platform."},
    {"term": "C++", "definition": "An extension of the C programming language that is used to create console games, such as those for Xbox."},
    {"term": "Case study", "definition": "A common way for employers to assess job skills and gain insight into how a candidate approaches common data-related challenges."},
    {"term": "dplyr (R)", "definition": "An R package in Tidyverse that offers a consistent set of functions to complete common data-manipulation tasks."},
    {"term": "Factor (R)", "definition": "An object that stores categorical data where the data values are limited and usually based on a finite group, such as country or year."},
    {"term": "Function (R)", "definition": "A body of reusable code for performing specific tasks in R."},
    {"term": "ggplot2 (R)", "definition": "An R package in Tidyverse that creates a variety of data visualizations by applying different visual properties to the data variables in R."},
    {"term": "Library", "definition": "A directory containing all of a data analyst's installed packages."},
    {"term": "Logical operator", "definition": "An operator that returns a logical data type."},
    {"term": "Matrix", "definition": "A two-dimensional collection of data elements with rows and columns."},
    {"term": "Nested", "definition": "Code that performs a particular function and is contained within code that performs a broader function."},
    {"term": "Nested function", "definition": "A function that is completely contained within another function."},
    {"term": "Package (R)", "definition": "A unit of reproducible R code."},
    {"term": "Pipe (R)", "definition": 'A tool in R for expressing a sequence of multiple operations, represented with "%>%".'},
    {"term": "readr (R)", "definition": "An R package in Tidyverse used for importing data."},
    {"term": "tidyr (R)", "definition": "An R package in Tidyverse used for data cleaning to make tidy data."},
    {"term": "Tidyverse (R)", "definition": "A system of packages in R with a common design philosophy for data manipulation, exploration, and visualization."},
    {"term": "Variable (R)", "definition": "A representation of a value in R that can be stored for later use."},
    {"term": "Vector (R)", "definition": "A group of data elements of the same type stored in a one-dimensional sequence in R."},
    {"term": "Vignette (R)", "definition": "Documentation for an R package that describes the problem the package is designed to solve, explains how its functions can be used, and lists any dependencies on other packages."}
]

current_index = 0

def show_card(action):
    global current_index
    if action == "Next":
        current_index = (current_index + 1) % len(flashcards)
    elif action == "Previous":
        current_index = (current_index - 1) % len(flashcards)
    
    card = flashcards[current_index]
    return [
        card["term"],
        card["definition"],
        f"Card {current_index + 1} of {len(flashcards)}"
    ]

def add_card(term, definition):
    if term and definition:
        flashcards.append({"term": term, "definition": definition})
        return "Card added successfully!", "", ""
    return "Please fill in both term and definition!", term, definition

with gr.Blocks(title="R Glossary Flashcards") as demo:
    gr.Markdown("# R Glossary Flashcards")
    
    with gr.Row():
        with gr.Column():
            term_display = gr.Textbox(label="Term", interactive=False)
            definition_display = gr.Textbox(label="Definition", interactive=False)
            card_counter = gr.Textbox(label="Card Count", interactive=False)
    
    with gr.Row():
        prev_btn = gr.Button("Previous")
        next_btn = gr.Button("Next")
    
    gr.Markdown("---")
    gr.Markdown("## Add New Flashcard")
    
    with gr.Row():
        with gr.Column():
            new_term = gr.Textbox(label="New Term")
            new_definition = gr.Textbox(label="New Definition")
            add_btn = gr.Button("Add Card")
            result = gr.Textbox(label="Result")

    # Set up button click events
    prev_btn.click(
        show_card,
        inputs=[gr.Textbox(value="Previous", visible=False)],
        outputs=[term_display, definition_display, card_counter]
    )
    next_btn.click(
        show_card,
        inputs=[gr.Textbox(value="Next", visible=False)],
        outputs=[term_display, definition_display, card_counter]
    )
    add_btn.click(
        add_card,
        inputs=[new_term, new_definition],
        outputs=[result, new_term, new_definition]
    )

    # Show initial card
    demo.load(
        show_card,
        inputs=[gr.Textbox(value="Next", visible=False)],
        outputs=[term_display, definition_display, card_counter]
    )

if __name__ == "__main__":
    demo.launch(share=True)
