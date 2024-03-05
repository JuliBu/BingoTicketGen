import random


def generate_bingo_ticket(already_used_rows):
    bingo_ticket = [[""] * 9 for _ in range(3)]
    used_numbers_per_column = [set() for _ in range(9)]
    row_idx = 0
    while row_idx < 3:
        row = [""] * 9
        numbers_in_row = set()
        selected_columns = random.sample(range(9), 5)
        for col in selected_columns:
            lower_bound = col * 10
            upper_bound = (col + 1) * 10 - 1
            if col == 0:
                lower_bound = 1
            number = random.randint(lower_bound, upper_bound)
            while number in used_numbers_per_column[col]:
                number = random.randint(lower_bound, upper_bound)
            if isinstance(col, int):
                row[col] = number
                used_numbers_per_column[col].add(number)
                numbers_in_row.add(number)
        if numbers_in_row in already_used_rows:
            continue
        else:
            bingo_ticket[row_idx] = row
            row_idx += 1
            already_used_rows.append(numbers_in_row)
    return bingo_ticket


def generate_multiple_tickets(num_tickets):
    all_tickets = []
    used_rows = []
    for _ in range(num_tickets):
        ticket = generate_bingo_ticket(used_rows)
        all_tickets.append(ticket)
    return all_tickets


def print_bingo_ticket(ticket):
    for row in ticket:
        print(" ".join(f"{num:2}" if num else "  " for num in row))


def print_multiple_tickets(tickets):
    for i, ticket in enumerate(tickets, start=1):
        print(f"Ticket {i}:")
        print_bingo_ticket(ticket)
        print()


if __name__ == "__main__":
    num_tickets_to_generate = 5
    my_bingo_tickets = generate_multiple_tickets(num_tickets_to_generate)
    print_multiple_tickets(my_bingo_tickets)
