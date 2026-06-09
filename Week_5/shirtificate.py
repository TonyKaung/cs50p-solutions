from fpdf import FPDF


def main():
    name = input("Name: ")
    create_shirtificate(name)


def create_shirtificate(name):
    # A4 dimensions: 210mm wide x 297mm tall
    pdf = FPDF(orientation="P", unit="mm",format="A4")
    pdf.add_page()
    pdf.set_auto_page_break(auto=False)

    # ── Background ──────────────────────────────────────────────────────────
    pdf.set_fill_color(255, 255, 255)          # white
    pdf.rect(0, 0, 210, 297, style="F")

    # ── Decorative border ───────────────────────────────────────────────────
    pdf.set_draw_color(180, 0, 0)           # CS50 red
    pdf.set_line_width(3)
    pdf.rect(8, 8, 194, 281)               # outer border
    pdf.set_line_width(0.8)
    pdf.rect(11, 11, 188, 275)             # inner border

    # ── Title: "CS50 Shirtificate" ──────────────────────────────────────────
    pdf.set_font("Helvetica", style="B", size=36)
    pdf.set_text_color(0, 0, 0)
    pdf.set_y(25)
    pdf.cell(0, 14, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

    # ── Shirt image, centered horizontally ──────────────────────────────────
    img_w = 170          # mm — wide enough to fill nicely
    img_h = 170 * (190 / 330)   # preserve ~330×190 native ratio → ~97mm tall
    img_x = (210 - img_w) / 2
    img_y = 60

    pdf.image("shirtificate.png", x=img_x, y=img_y, w=img_w)

    # ── Name on top of shirt ────────────────────────────────────────────────
    # Position text roughly centred over the shirt graphic
    pdf.set_font("Helvetica", style="B", size=24)
    pdf.set_text_color(255, 255, 255)

    # Place cursor at the vertical midpoint of the shirt image
    name_y = img_y + img_h * 0.50          # ~50% down from top of shirt
    pdf.set_xy(0, name_y)
    pdf.cell(210, 10, f"{name} took CS50!", align="C")

    # ── Save ─────────────────────────────────────────────────────────────────
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()