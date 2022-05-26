from fpdf import FPDF, HTMLMixin
 


class PDFCreator(FPDF,HTMLMixin):
	def header(self):
		pass
	def footer(self):
		pass


pdf = PDFCreator(orientation='P', unit='mm', format='A4')
pdf.add_font('Verdana', '', 'verdana.ttf', uni=True)

pdf.add_page()

# pdf.set_font("Verdana", size=24)
# pdf.cell(200, 10, txt="Архив статей Javarush", ln=1, align="C")

pdf.set_font("Verdana", size=12)
with open('articles/a1.html', 'r', encoding='utf-8') as f:
	content = f.read()
	pdf.write_html(content)







pdf.output("javarush_articles.pdf")