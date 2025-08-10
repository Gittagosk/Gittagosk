# R Flashcards Application Documentation

## Overview
The R Flashcards application is an interactive learning tool built using Gradio that helps users learn R programming concepts through digital flashcards. The application provides a simple and intuitive interface for reviewing R-related terms and definitions, with capabilities to navigate through cards and add new ones.

## Features
1. Interactive flashcard display
2. Navigation between cards (Previous/Next)
3. Card counter showing progress
4. Ability to add new flashcards

## Technical Details

### Dependencies
- **gradio**: Used for creating the web interface
- **Python 3.x**: Base programming language

### Code Structure

#### 1. Data Structure
```python
flashcards = [
    {"term": "...", "definition": "..."},
    # ... more cards
]
```
The flashcards are stored in a list of dictionaries, where each dictionary contains:
- `term`: The R programming concept
- `definition`: The explanation of the concept

#### 2. Core Functions

##### `show_card(action)`
- **Purpose**: Displays the current flashcard and handles navigation
- **Parameters**: 
  - `action`: String ("Next" or "Previous")
- **Returns**: List containing:
  - Current term
  - Current definition
  - Card counter status

##### `add_card(term, definition)`
- **Purpose**: Adds a new flashcard to the collection
- **Parameters**:
  - `term`: The new term to add
  - `definition`: The definition of the new term
- **Returns**: 
  - Success/error message
  - Cleared term field
  - Cleared definition field

### User Interface Components

#### Main Display
- Term display (read-only)
- Definition display (read-only)
- Card counter showing current position

#### Navigation
- Previous button
- Next button

#### Add New Cards Section
- Term input field
- Definition input field
- Add Card button
- Result message display

## Usage Instructions

### Viewing Flashcards
1. The application starts by showing the first flashcard
2. Use "Previous" and "Next" buttons to navigate through cards
3. The card counter shows your current position in the deck

### Adding New Flashcards
1. Scroll to the "Add New Flashcard" section
2. Enter the term in the "New Term" field
3. Enter the definition in the "New Definition" field
4. Click "Add Card"
5. A success message will appear if the card was added successfully

## Technical Implementation Notes

### Gradio Interface
The application uses Gradio's `Blocks` interface for layout control and component organization:
```python
with gr.Blocks(title="R Glossary Flashcards") as demo:
    # ... interface components
```

### State Management
- Global `current_index` variable tracks the current card position
- Card navigation wraps around using modulo operation
- Card state is preserved between navigation actions

### Error Handling
- Input validation for new cards
- Prevents adding cards with empty terms or definitions
- Provides user feedback through the result message

## Running the Application

1. Ensure Python and required packages are installed:
```bash
pip install gradio
```

2. Run the application:
```bash
python flashcards_gradio.py
```

3. Access the interface:
- Local URL: http://127.0.0.1:7860
- The application also provides a temporary public URL for remote access

## Additional Notes
- The application includes a pre-loaded set of R programming terms and definitions
- All data is stored in memory and will reset when the application is restarted
- The interface is responsive and works well on both desktop and mobile browsers

---
Last Updated: August 10, 2025
