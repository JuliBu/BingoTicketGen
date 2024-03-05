# Bingo Ticket Generator
This Python script generates random Bingo tickets. 

Each ticket consists of a 3x9 matrix where the numbers are arranged to adhere to the rules of the Bingo game (1-90).

## Example Output
You can see a 500 ticket example output in BingoCardGen/example_output/500_tickets.pdf

## Usage
Make sure you have Python installed on your system. You also need reportlab (pip package) for generating pdfs.
Clone or copy the script and run it.
You can adjust the number of tickets to generate by modifying the num_tickets_to_generate variable.
## Functions
- generate_bingo_ticket(already_used_rows):
Generates a single Bingo ticket. Used rows are stored in already_used_rows to avoid duplicates.

- generate_multiple_tickets(num_tickets):
Generates a list of Bingo tickets without duplicate rows.

- print_bingo_ticket(ticket):
Prints a single Bingo ticket to the console.

- print_multiple_tickets(tickets):
Prints all generated Bingo tickets to the console.

- save_bingo_tickets_to_pdf(tickets, filename):
Saves generated tickets to a pdf file.

# Happy Bingo playing! 🎉