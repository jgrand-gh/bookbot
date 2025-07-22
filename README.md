# BookBot

This project analyzes the contents of a text file (book) and generates a report on word and character frequency.

## Features

- Counts total words in a book
- Counts frequency of each character (case-insensitive)
- Outputs a formatted report to the console

## Requirements

- Python 3.12 or newer

## Getting Started

1. **Clone the repository**
2. **Add your own book files:**  
   Create a `books/` directory and place any `.txt` files you want to analyze inside it.
3. **Run the main program:**
   ```sh
   python main.py books/frankenstein.txt
   ```
   Replace `books/frankenstein.txt` with the path to any book file you want to analyze.

## Project Structure

- `main.py` — Entry point, handles reading files and generating reports
- `stats.py` — Word counting logic
- `books/` — Directory for your book text files (not included in this repository)

## License

This project is for educational purposes as part of a Boot.dev learning module.