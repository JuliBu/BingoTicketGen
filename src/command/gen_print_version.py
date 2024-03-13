from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from bingo_ticket.gen_ticket import generate_multiple_tickets


def save_bingo_tickets_to_pdf(tickets, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica", 25)

    top_y = 730
    for i, ticket in enumerate(tickets, start=1):
        start_y = top_y - ((i-1) % 5) * 140
        c.drawString(100, start_y + 5, f" B I N G O - Ticket {i}:")
        c.setLineWidth(3)
        y = start_y - 20
        for row in ticket:
            x = 95
            for num in row:
                c.drawString(x, y-5, f"{num:2}" if num else "  ")
                x += 45
            y -= 30
        for j in range(4):
            line_width = 3 if (j == 0 or j == 3) else 1
            c.setLineWidth(line_width)
            c.line(90 - 5, start_y - j * 30, 90 + 9 * 45 - 5, start_y - j * 30)
        for j in range(10):
            line_width = 3 if (j == 0 or j == 9) else 1
            c.setLineWidth(line_width)
            c.line(90 + j * 45 - 5, start_y, 90 + j * 45 - 5, start_y - 3 * 30)
        if i % 5 == 0:
            c.showPage()
    c.save()

if __name__ == '__main__':
    save_bingo_tickets_to_pdf(generate_multiple_tickets(500), "../../example_output/500_tickets.pdf")
