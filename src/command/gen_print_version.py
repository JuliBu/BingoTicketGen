from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import fonts

from bingo_ticket.gen_ticket import generate_multiple_tickets


def save_bingo_tickets_to_pdf(tickets, filename):
    c = canvas.Canvas(filename, pagesize=letter)

    top_y = 730
    for i, ticket in enumerate(tickets, start=1):
        c.setFont("Helvetica", 35)
        start_y = top_y - ((i-1) % 5) * 140
        # c.drawString(100, start_y + 5, f" B I N G O - Ticket {i}:")
        c.setLineWidth(3)
        y = start_y - 20
        start_x = 70
        cell_width = 55
        x_shift = 8
        cell_height = 35
        y_shift = 3
        for row in ticket:
            x = start_x
            for num in row:
                c.drawString(x, y-10, f"{num:2}" if num else "  ")
                x += cell_width
            y -= cell_height
        for j in range(4):
            line_width = 3 if (j == 0 or j == 3) else 1
            c.setLineWidth(line_width)
            c.line(start_x - x_shift, start_y - j * cell_height, start_x + 9 * cell_width - x_shift, start_y - j * cell_height)
        for j in range(10):
            line_width = 3 if (j == 0 or j == 9) else 1
            c.setLineWidth(line_width)
            c.line(start_x + j * cell_width - x_shift, start_y, start_x + j * cell_width - x_shift, start_y - 3 * cell_height)
        if i % 5 == 0:
            c.showPage()
    c.save()

if __name__ == '__main__':
    save_bingo_tickets_to_pdf(generate_multiple_tickets(500), "../../example_output/500_tickets.pdf")
