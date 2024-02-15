# Flashy

Flashy is a simple flashcard application built using Python's Tkinter library. It helps users learn new words by displaying French words and their English translations on flashcards.

## Features
- **Flashcard Learning:** Users can flip through flashcards displaying French words and their English translations.
- **Interactive Buttons:** Users can mark whether they know a word or not using interactive buttons.

## Requirements
- Python 3.x
- Tkinter library
- pandas library

## Installation
1. Clone or download the repository.
2. Ensure you have Python installed on your system.
3. Install pandas library if not already installed:
    ```
    pip install pandas
    ```
4. Run the application by executing the script.

## Usage
1. Run the script.
2. Click on the flashcard to reveal the English translation.
3. If you know the word, click on the "Right" button. If not, click on the "Wrong" button to move to the next flashcard.

## File Structure
- **data/words_to_learn.csv:** CSV file to store words that the user needs to learn.
- **images/card_front.png:** Front side image of the flashcard.
- **images/card_back.png:** Back side image of the flashcard.
- **images/right.png:** Image for the "Right" button.
- **images/wrong.png:** Image for the "Wrong" button.

## Note
- Ensure that you have the necessary image files in the "images" directory.
- The application saves progress automatically by removing learned words from the list.

## Author
This application is developed by Xavier Avery.

