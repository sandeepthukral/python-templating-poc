from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

TITLE = "PoC for Templating in python"
DATA = "sample data for the template"

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("report-template.html")

template_vars = {
  "title" : TITLE,
  "data": DATA
  }

html_out = template.render(template_vars)

HTML(string=html_out).write_pdf("output.pdf")
