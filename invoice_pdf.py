from fpdf import FPDF


class Invoice(FPDF):
    address = """
    BILLING TO:
    Client Name:
    Street Avenue 0000
    Maimi, FL
    """

    def company_details(self):
        self.add_page()

        self.page_width = self.w

        self.set_margin(0)
        self.set_text_color(255, 253, 252)
        self.set_fill_color(10, 10, 10)
        self.set_font("helvetica", "B", 20)
        self.cell(self.page_width/2, 20,"INVOICE", new_x="LMARGIN", new_y="NEXT", fill=True, align="C")
        self.ln(2)

        self.set_font("helvetica", "B", 11)
        self.set_text_color(10, 10, 10)
        self.set_x(10)
        self.cell(30, 10, "Design Project Name",new_x="LMARGIN", new_y="NEXT" )


        self.set_font("helvetica", "", 11)
        self.set_text_color(10, 10, 10)
        self.set_x(10)
        self.multi_cell(0, 5, self.address,new_x="LMARGIN", new_y="NEXT" )

    def create_table(self, ids, products, prices, qtys, totals, payment=0):

        total_price = 0
        self.set_font("helvetica", "", 11)
        self.set_fill_color(10, 10, 10)
        self.set_text_color(255, 253, 252)

        self.cell(self.page_width * 0.05, 10, "#", fill=True, align="C")
        self.cell(self.page_width * 0.4, 10, "PRODUCT", fill=True)
        self.cell(self.page_width * 0.2, 10, "PRICE", fill=True)
        self.cell(self.page_width * 0.15, 10, "QTY", fill=True)
        self.cell(self.page_width * 0.2, 10, "TOTAL", fill=True, align="C",new_x="LMARGIN", new_y="NEXT")

        self.set_fill_color(255, 253, 252)
        self.set_text_color(10, 10, 10)



        self.set_margin(10)


        for index in range(len(ids)):
            self.cell(self.page_width * 0.05, 10, f"{ids[index]}", fill=True, align="C", border="T")
            self.cell(self.page_width * 0.4, 10, f"{products[index]}", fill=True, border="T")
            self.cell(self.page_width * 0.15, 10,f"{prices[index]}", fill=True, border="T")
            self.cell(self.page_width * 0.1, 10,f"{qtys[index]}", fill=True, border="T")
            self.cell(self.page_width * 0.2, 10, f"{totals[index]}", fill=True, align="C", new_x="LMARGIN", new_y="NEXT", border="T")
            total_price += float(totals[index])



        self.cell(self.page_width * 0.60, 10, "", fill=True, border="T")
        self.cell(self.page_width * 0.1, 10, "Payment", fill=True, align="R", border="T")
        self.cell(self.page_width * 0.2, 10, f"{payment}", fill=True, align="C", border="T", new_x="LMARGIN",
                  new_y="NEXT")

        self.cell(self.page_width * 0.60, 10, "", fill=True)
        self.cell(self.page_width * 0.1, 10, "Total", fill=True, align="R")
        self.cell(self.page_width * 0.2, 10, f"{total_price}", fill=True, align="C", new_x="LMARGIN", new_y="NEXT")

        self.cell(self.page_width * 0.60, 10, "", fill=True)
        self.cell(self.page_width * 0.1, 10, "Change", fill=True, align="R")
        self.cell(self.page_width * 0.2, 10, f"{payment - total_price}", fill=True, align="C", new_x="LMARGIN", new_y="NEXT")








    def create_pdf(self):

        self.set_margin(0)
        self.output("invoice.pdf")


